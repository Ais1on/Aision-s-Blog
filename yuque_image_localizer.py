#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import re
import sys
from pathlib import Path
from typing import Iterable
from urllib.error import HTTPError, URLError
from urllib.parse import unquote, urlparse
from urllib.request import Request, urlopen


MARKDOWN_IMAGE_RE = re.compile(r"!\[(?P<alt>[^\]]*)\]\((?P<url>https?://[^\s)]+)\)")
HTML_IMAGE_RE = re.compile(
    r"""<img\s+[^>]*src=(?P<quote>["'])(?P<url>https?://.+?)(?P=quote)[^>]*>""",
    re.IGNORECASE,
)
YUQUE_HOST_KEYWORDS = ("cdn.nlark.com", "yuque.com", "aliyuncs.com")
POSTS_DIR = Path("content/posts")
STATIC_IMAGES_DIR = Path("static/images/posts")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Download external images from exported Yuque Markdown and rewrite links for this Hugo blog."
    )
    parser.add_argument("input", type=Path, help="Source Markdown file or directory")
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        help="Output Markdown file. Defaults to the input file (in-place rewrite).",
    )
    parser.add_argument(
        "--assets-dir",
        type=Path,
        help="Directory for downloaded images. Defaults to static/images/posts/<post-slug>/.",
    )
    parser.add_argument(
        "--all-remote",
        action="store_true",
        help="Download all remote images, not just common Yuque/CDN hosts.",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=20,
        help="Download timeout in seconds. Default: 20",
    )
    parser.add_argument(
        "--include-index",
        action="store_true",
        help="Also process _index.md files when input is a directory.",
    )
    parser.add_argument(
        "--continue-on-error",
        action="store_true",
        help="Continue processing other files if one file fails.",
    )
    return parser.parse_args()


def should_download(url: str, download_all_remote: bool) -> bool:
    if download_all_remote:
        return True
    host = urlparse(url).netloc.lower()
    return any(keyword in host for keyword in YUQUE_HOST_KEYWORDS)


def iter_image_urls(text: str, download_all_remote: bool) -> Iterable[str]:
    seen: set[str] = set()
    for pattern in (MARKDOWN_IMAGE_RE, HTML_IMAGE_RE):
        for match in pattern.finditer(text):
            url = match.group("url")
            if url in seen:
                continue
            if should_download(url, download_all_remote):
                seen.add(url)
                yield url


def build_asset_name(url: str) -> str:
    parsed = urlparse(url)
    original_name = Path(unquote(parsed.path)).name or "image"
    stem = Path(original_name).stem or "image"
    suffix = Path(original_name).suffix or ".bin"
    digest = hashlib.sha1(url.encode("utf-8")).hexdigest()[:10]
    return f"{stem}-{digest}{suffix}"


def slugify_path_part(value: str) -> str:
    slug = re.sub(r"[^\w.-]+", "_", value, flags=re.UNICODE).strip("._")
    return slug or "assets"


def build_post_slug(input_file: Path) -> str:
    return slugify_path_part(input_file.stem)


def build_default_assets_dir(input_file: Path, output_file: Path) -> Path:
    try:
        if input_file.resolve().is_relative_to((Path.cwd() / POSTS_DIR).resolve()):
            return Path.cwd() / STATIC_IMAGES_DIR / build_post_slug(output_file)
    except ValueError:
        pass
    return output_file.parent / f"{build_post_slug(output_file)}_assets"


def build_public_asset_path(target_file: Path) -> str:
    static_root = (Path.cwd() / "static").resolve()
    target_resolved = target_file.resolve()
    try:
        relative = target_resolved.relative_to(static_root)
        return relative.as_posix()
    except ValueError:
        return target_file.as_posix()


def iter_markdown_files(input_path: Path, include_index: bool) -> Iterable[Path]:
    if input_path.is_file():
        yield input_path
        return

    for file_path in sorted(input_path.rglob("*.md")):
        if not include_index and file_path.name == "_index.md":
            continue
        yield file_path


def download_file(url: str, target: Path, timeout: int) -> None:
    request = Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (compatible; yuque-image-localizer/1.0)",
        },
    )
    with urlopen(request, timeout=timeout) as response:
        target.write_bytes(response.read())


def localize_markdown(
    source_file: Path,
    output_file: Path,
    assets_dir: Path,
    download_all_remote: bool,
    timeout: int,
) -> tuple[int, int]:
    text = source_file.read_text(encoding="utf-8")
    assets_dir.mkdir(parents=True, exist_ok=True)

    replacements: dict[str, str] = {}
    downloaded = 0

    for url in iter_image_urls(text, download_all_remote):
        asset_name = build_asset_name(url)
        target_file = assets_dir / asset_name
        if not target_file.exists():
            download_file(url, target_file, timeout)
            downloaded += 1
        replacements[url] = build_public_asset_path(target_file)

    for remote_url, local_path in replacements.items():
        text = text.replace(remote_url, local_path)

    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(text, encoding="utf-8", newline="\n")
    return len(replacements), downloaded


def main() -> int:
    args = parse_args()
    input_path = args.input.resolve()
    if not input_path.exists():
        print(f"Input path not found: {input_path}", file=sys.stderr)
        return 1

    if input_path.is_dir() and args.output:
        print("--output can only be used when input is a single Markdown file.", file=sys.stderr)
        return 1

    files = list(iter_markdown_files(input_path, args.include_index))
    if not files:
        print("No Markdown files found to process.", file=sys.stderr)
        return 1

    total_matched = 0
    total_downloaded = 0
    failures: list[str] = []

    for input_file in files:
        output_file = args.output.resolve() if args.output else input_file
        default_assets_dir = build_default_assets_dir(input_file, output_file)
        assets_dir = args.assets_dir.resolve() if args.assets_dir else default_assets_dir.resolve()

        try:
            matched, downloaded = localize_markdown(
                source_file=input_file,
                output_file=output_file,
                assets_dir=assets_dir,
                download_all_remote=args.all_remote,
                timeout=args.timeout,
            )
        except (HTTPError, URLError, TimeoutError) as exc:
            message = f"Download failed for {input_file}: {exc}"
            print(message, file=sys.stderr)
            failures.append(message)
            if not args.continue_on_error:
                return 2
            continue
        except UnicodeDecodeError:
            message = f"Failed to read Markdown as UTF-8: {input_file}"
            print(message, file=sys.stderr)
            failures.append(message)
            if not args.continue_on_error:
                return 3
            continue

        total_matched += matched
        total_downloaded += downloaded
        print(f"Processed: {input_file}")
        print(f"Output:    {output_file}")
        print(f"Assets:    {assets_dir}")
        print(f"Matched:   {matched}")
        print(f"Downloaded:{downloaded}")

    print(f"Files:     {len(files)}")
    print(f"Matched:   {total_matched}")
    print(f"Downloaded:{total_downloaded}")
    if failures:
        print("Failures:")
        for failure in failures:
            print(failure)
        return 4
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
