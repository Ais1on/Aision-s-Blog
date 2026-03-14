(() => {
  const sidebar = document.querySelector("[data-toc-sidebar]");
  if (!sidebar) return;

  const tocCard = sidebar.querySelector("[data-toc-card]");
  const tocBody = sidebar.querySelector("[data-toc-body]");
  const toggle = sidebar.querySelector("[data-toc-toggle]");
  const tocLinks = Array.from(sidebar.querySelectorAll('a[href^="#"]'));
  const headings = tocLinks
    .map((link) => {
      const id = decodeURIComponent(link.getAttribute("href").slice(1));
      const heading = document.getElementById(id);
      return heading ? { link, heading } : null;
    })
    .filter(Boolean);

  const syncCollapseState = (collapsed) => {
    tocCard.classList.toggle("is-collapsed", collapsed);
    toggle.setAttribute("aria-expanded", String(!collapsed));
    toggle.textContent = collapsed ? "展开" : "收起";
    if (!collapsed) {
      const maxPanelHeight = Math.max(240, window.innerHeight - 220);
      tocBody.style.maxHeight = `${Math.min(tocBody.scrollHeight, maxPanelHeight)}px`;
    }
  };

  const maybeEnableCollapse = () => {
    tocBody.style.maxHeight = "none";
    const shouldCollapse = window.innerWidth > 900 && tocBody.scrollHeight > 360;
    toggle.hidden = !shouldCollapse;
    syncCollapseState(false);
    if (!shouldCollapse) {
      tocCard.classList.remove("is-collapsed");
      const maxPanelHeight = Math.max(240, window.innerHeight - 220);
      tocBody.style.maxHeight = `${Math.min(tocBody.scrollHeight, maxPanelHeight)}px`;
    }
  };

  toggle?.addEventListener("click", () => {
    const collapsed = !tocCard.classList.contains("is-collapsed");
    syncCollapseState(collapsed);
  });

  if (headings.length) {
    const activateLink = (id) => {
      tocLinks.forEach((link) => {
        const active = decodeURIComponent(link.getAttribute("href").slice(1)) === id;
        link.classList.toggle("is-active", active);
      });
    };

    const observer = new IntersectionObserver(
      (entries) => {
        const visible = entries
          .filter((entry) => entry.isIntersecting)
          .sort((a, b) => a.boundingClientRect.top - b.boundingClientRect.top);
        if (visible.length) {
          activateLink(visible[0].target.id);
        }
      },
      {
        rootMargin: "-18% 0px -70% 0px",
        threshold: [0, 1],
      }
    );

    headings.forEach(({ heading }) => observer.observe(heading));
    activateLink(headings[0].heading.id);
  }

  window.addEventListener("resize", maybeEnableCollapse);
  maybeEnableCollapse();
})();
