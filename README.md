# Aision-s-Blog

一个基于 Hugo 的个人博客，适合部署到 GitHub Pages。

## 本地开发

先安装 Hugo Extended，然后在仓库根目录运行：

```bash
hugo server -D
```

打开 `http://localhost:1313/Aision-s-Blog/` 或终端里显示的本地地址预览。

## 新建文章

```bash
hugo new posts/my-first-post.md
```

生成后把文章头部里的 `draft = true` 改成 `false`，就会出现在页面中。

## 部署到 GitHub Pages

仓库已经包含 GitHub Actions 工作流：

- 推送到 `main` 分支后自动构建
- 自动发布到 GitHub Pages

需要在 GitHub 仓库设置中确认：

- `Settings -> Pages -> Source` 使用 `GitHub Actions`

## 目录说明

- `content/` 存放文章内容
- `layouts/` 存放页面模板
- `static/` 存放静态资源
- `.github/workflows/` 存放自动部署配置
