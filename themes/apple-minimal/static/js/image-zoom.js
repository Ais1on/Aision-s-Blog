(() => {
  const container = document.querySelector(".article-content");
  if (!container) return;

  const images = Array.from(
    container.querySelectorAll('img:not([data-no-zoom]):not(.avatar-image)')
  );
  if (!images.length) return;

  const overlay = document.createElement("div");
  overlay.className = "image-lightbox";
  overlay.setAttribute("aria-hidden", "true");
  overlay.innerHTML = `
    <button class="lightbox-close" type="button" aria-label="关闭">×</button>
    <figure><img alt=""></figure>
  `;

  const overlayImage = overlay.querySelector("img");
  const closeButton = overlay.querySelector(".lightbox-close");

  let activeImage = null;

  const closeLightbox = () => {
    if (!overlay.classList.contains("is-open")) return;
    overlay.classList.remove("is-open");
    overlay.setAttribute("aria-hidden", "true");
    document.body.classList.remove("is-image-zoom-open");
    if (activeImage) activeImage.focus();
    activeImage = null;
  };

  const openLightbox = (img) => {
    activeImage = img;
    overlayImage.src = img.currentSrc || img.src;
    overlayImage.alt = img.alt || "";
    overlay.classList.add("is-open");
    overlay.setAttribute("aria-hidden", "false");
    document.body.classList.add("is-image-zoom-open");
  };

  images.forEach((img) => {
    img.classList.add("zoomable-image");
    if (!img.hasAttribute("tabindex")) img.tabIndex = 0;
    img.title = "双击放大";

    img.addEventListener("dblclick", (event) => {
      event.preventDefault();
      openLightbox(img);
    });

    img.addEventListener("keydown", (event) => {
      if (event.key === "Enter") {
        event.preventDefault();
        openLightbox(img);
      }
    });
  });

  overlay.addEventListener("click", (event) => {
    const clickedImage = event.target === overlayImage;
    const clickedFigure = overlayImage.closest("figure")?.contains(event.target);
    if (!clickedImage && !clickedFigure) closeLightbox();
  });

  closeButton.addEventListener("click", closeLightbox);

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") closeLightbox();
  });

  document.body.appendChild(overlay);
})();

