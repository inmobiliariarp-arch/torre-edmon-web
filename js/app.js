/* ==========================================================================
   TORRE EDMON - LUXURY ARCHITECTURE APPLICATION ENGINE
   Smooth Mouse & Touch Pinch-to-Zoom Controller
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {
  // 1. THEME TOGGLE (Dark / Light)
  const themeToggleBtn = document.getElementById('theme-toggle');
  const themeIcon = document.getElementById('theme-icon');
  const htmlRoot = document.documentElement;

  const savedTheme = localStorage.getItem('torre_edmon_theme') || 'dark';
  applyTheme(savedTheme);

  if (themeToggleBtn) {
    themeToggleBtn.addEventListener('click', () => {
      const current = htmlRoot.getAttribute('data-theme');
      const next = current === 'dark' ? 'light' : 'dark';
      applyTheme(next);
      localStorage.setItem('torre_edmon_theme', next);
    });
  }

  function applyTheme(theme) {
    htmlRoot.setAttribute('data-theme', theme);
    if (themeIcon) {
      if (theme === 'light') {
        themeIcon.className = 'fas fa-moon';
        themeToggleBtn.setAttribute('title', 'Modo Oscuro');
      } else {
        themeIcon.className = 'fas fa-sun';
        themeToggleBtn.setAttribute('title', 'Modo Claro');
      }
    }
  }

  // 2. NAVBAR SCROLL & MOBILE MENU
  const navbar = document.querySelector('.navbar');
  window.addEventListener('scroll', () => {
    if (window.scrollY > 40) {
      navbar.classList.add('scrolled');
    } else {
      navbar.classList.remove('scrolled');
    }
  });

  const mobileMenuBtn = document.getElementById('mobile-menu-btn');
  const navLinks = document.querySelector('.nav-links');
  if (mobileMenuBtn && navLinks) {
    mobileMenuBtn.addEventListener('click', () => {
      navLinks.classList.toggle('open');
    });
    document.querySelectorAll('.nav-link').forEach(l => {
      l.addEventListener('click', () => navLinks.classList.remove('open'));
    });
  }

  // 3. SMOOTH IN-PLACE ZOOM & PAN FOR FLOOR PLAN (PC Mouse + Mobile Touch Pinch)
  const planBox = document.getElementById('plan-interactive-box');
  const planImg = document.getElementById('plan-zoom-img');

  if (planBox && planImg) {
    let scale = 1;
    let panX = 0;
    let panY = 0;
    let isDragging = false;
    let startX = 0;
    let startY = 0;

    // Mobile Pinch-to-Zoom variables
    let initialDistance = 0;
    let initialScale = 1;

    function applyTransform() {
      scale = Math.min(Math.max(1, scale), 4);
      if (scale === 1) {
        panX = 0;
        panY = 0;
      }
      planImg.style.transform = `translate(${panX}px, ${panY}px) scale(${scale})`;
      planBox.style.cursor = scale > 1 ? (isDragging ? 'grabbing' : 'grab') : 'zoom-in';
    }

    // Mouse wheel zoom
    planBox.addEventListener('wheel', (e) => {
      e.preventDefault();
      const delta = e.deltaY * -0.002;
      scale += delta;
      applyTransform();
    }, { passive: false });

    // Mouse Drag to Pan (when zoomed)
    planBox.addEventListener('mousedown', (e) => {
      if (e.target.closest('.plan-zoom-badge-btn')) return;
      if (scale > 1) {
        isDragging = true;
        startX = e.clientX - panX;
        startY = e.clientY - panY;
        applyTransform();
      }
    });

    window.addEventListener('mousemove', (e) => {
      if (!isDragging) return;
      panX = e.clientX - startX;
      panY = e.clientY - startY;
      applyTransform();
    });

    window.addEventListener('mouseup', () => {
      if (isDragging) {
        isDragging = false;
        applyTransform();
      }
    });

    // Touch events for Mobile (Pinch-to-zoom & 1-finger pan)
    planBox.addEventListener('touchstart', (e) => {
      if (e.touches.length === 2) {
        initialDistance = getDistance(e.touches[0], e.touches[1]);
        initialScale = scale;
      } else if (e.touches.length === 1 && scale > 1) {
        isDragging = true;
        startX = e.touches[0].clientX - panX;
        startY = e.touches[0].clientY - panY;
      }
    }, { passive: true });

    planBox.addEventListener('touchmove', (e) => {
      if (e.touches.length === 2 && initialDistance > 0) {
        const currentDist = getDistance(e.touches[0], e.touches[1]);
        const factor = currentDist / initialDistance;
        scale = initialScale * factor;
        applyTransform();
      } else if (e.touches.length === 1 && isDragging) {
        panX = e.touches[0].clientX - startX;
        panY = e.touches[0].clientY - startY;
        applyTransform();
      }
    }, { passive: true });

    planBox.addEventListener('touchend', (e) => {
      if (e.touches.length < 2) {
        initialDistance = 0;
      }
      if (e.touches.length === 0) {
        isDragging = false;
      }
    });

    function getDistance(t1, t2) {
      const dx = t1.clientX - t2.clientX;
      const dy = t1.clientY - t2.clientY;
      return Math.sqrt(dx * dx + dy * dy);
    }

    // Double-click/double-tap to reset or toggle zoom
    let lastTap = 0;
    planBox.addEventListener('click', (e) => {
      if (e.target.closest('.plan-zoom-badge-btn')) return;
      const now = new Date().getTime();
      const timesince = now - lastTap;
      if (timesince < 300 && timesince > 0) {
        // Double tap: toggle 2x or 1x
        scale = scale > 1 ? 1 : 2.2;
        panX = 0;
        panY = 0;
        applyTransform();
      }
      lastTap = new Date().getTime();
    });
  }

  // 4. LIGHTBOX MODAL
  const lightbox = document.getElementById('lightbox-modal');
  const lightboxImg = document.getElementById('lightbox-img');
  const lightboxCaption = document.getElementById('lightbox-caption');
  const lightboxClose = document.getElementById('lightbox-close');

  function openLightbox(src, caption) {
    if (!lightbox || !lightboxImg) return;
    lightboxImg.src = src;
    if (lightboxCaption) lightboxCaption.textContent = caption || 'Torre Edmon';
    lightbox.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  function closeLightbox() {
    if (lightbox) lightbox.classList.remove('active');
    document.body.style.overflow = '';
  }

  document.querySelectorAll('[data-lightbox]').forEach(el => {
    el.addEventListener('click', () => {
      const src = el.dataset.hires || el.querySelector('img')?.src;
      const caption = el.dataset.caption || el.querySelector('img')?.alt || 'Torre Edmon';
      if (src) openLightbox(src, caption);
    });
  });

  if (lightboxClose) lightboxClose.addEventListener('click', closeLightbox);
  if (lightbox) {
    lightbox.addEventListener('click', (e) => {
      if (e.target === lightbox) closeLightbox();
    });
  }
  window.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') closeLightbox();
  });
});
