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

  // 3. ARCHITECTURAL PANZOOM STUDIO (STRICT BOUNDARY CLAMPING & FOCAL POINT)
  const planBox = document.getElementById('plan-interactive-box');
  const planImg = document.getElementById('plan-zoom-img');
  const zoomValDisplay = document.getElementById('plan-zoom-val');
  const zoomInBtn = document.getElementById('plan-zoom-in');
  const zoomOutBtn = document.getElementById('plan-zoom-out');
  const zoomResetBtn = document.getElementById('plan-zoom-reset');

  if (planBox && planImg) {
    let scale = 1;
    let panX = 0;
    let panY = 0;
    let isDragging = false;
    let startX = 0;
    let startY = 0;
    const MIN_SCALE = 1;
    const MAX_SCALE = 4.5;

    // Strict boundary clamping so plan edges never detach or reveal blank/black borders
    function clampPan(targetX, targetY, targetScale) {
      if (targetScale <= 1) return { x: 0, y: 0 };

      const boxRect = planBox.getBoundingClientRect();
      const imgNaturalRatio = (planImg.naturalWidth && planImg.naturalHeight) 
        ? (planImg.naturalWidth / planImg.naturalHeight) 
        : (boxRect.width / boxRect.height);

      let baseW = boxRect.width * 0.92;
      let baseH = baseW / imgNaturalRatio;
      if (baseH > boxRect.height * 0.92) {
        baseH = boxRect.height * 0.92;
        baseW = baseH * imgNaturalRatio;
      }

      const scaledW = baseW * targetScale;
      const scaledH = baseH * targetScale;

      const maxPanX = Math.max(0, (scaledW - boxRect.width) / 2);
      const maxPanY = Math.max(0, (scaledH - boxRect.height) / 2);

      const clampedX = Math.max(-maxPanX, Math.min(maxPanX, targetX));
      const clampedY = Math.max(-maxPanY, Math.min(maxPanY, targetY));

      return { x: clampedX, y: clampedY };
    }

    function updateTransform(animate = false) {
      scale = Math.min(MAX_SCALE, Math.max(MIN_SCALE, scale));
      if (scale === 1) {
        panX = 0;
        panY = 0;
      } else {
        const clamped = clampPan(panX, panY, scale);
        panX = clamped.x;
        panY = clamped.y;
      }

      planImg.style.transition = animate ? 'transform 0.28s cubic-bezier(0.2, 0, 0.2, 1)' : 'none';
      planImg.style.transform = `translate3d(${panX}px, ${panY}px, 0) scale(${scale})`;
      planBox.style.cursor = scale > 1 ? (isDragging ? 'grabbing' : 'grab') : 'zoom-in';

      if (zoomValDisplay) {
        zoomValDisplay.textContent = `${Math.round(scale * 100)}%`;
      }
    }

    function zoomToPoint(deltaFactor, focalX, focalY) {
      const boxRect = planBox.getBoundingClientRect();
      const centerX = (focalX !== undefined) ? (focalX - boxRect.left - boxRect.width / 2) : 0;
      const centerY = (focalY !== undefined) ? (focalY - boxRect.top - boxRect.height / 2) : 0;

      const prevScale = scale;
      const newScale = Math.min(MAX_SCALE, Math.max(MIN_SCALE, scale * deltaFactor));

      if (newScale !== prevScale) {
        const scaleRatio = newScale / prevScale;
        panX = centerX - (centerX - panX) * scaleRatio;
        panY = centerY - (centerY - panY) * scaleRatio;
        scale = newScale;
        updateTransform(true);
      }
    }

    // Wheel event with focal zoom
    planBox.addEventListener('wheel', (e) => {
      e.preventDefault();
      const delta = e.deltaY < 0 ? 1.18 : 0.82;
      zoomToPoint(delta, e.clientX, e.clientY);
    }, { passive: false });

    // Drag to Pan with mouse
    planBox.addEventListener('mousedown', (e) => {
      if (e.target.closest('.plan-toolbar')) return;
      if (scale > 1) {
        isDragging = true;
        startX = e.clientX - panX;
        startY = e.clientY - panY;
        planImg.style.transition = 'none';
        planBox.style.cursor = 'grabbing';
      }
    });

    window.addEventListener('mousemove', (e) => {
      if (!isDragging) return;
      panX = e.clientX - startX;
      panY = e.clientY - startY;
      updateTransform(false);
    });

    window.addEventListener('mouseup', () => {
      if (isDragging) {
        isDragging = false;
        updateTransform(true);
      }
    });

    // Touch events for Mobile (Pinch-to-zoom & 1-finger drag)
    let initialPinchDist = 0;
    let initialPinchScale = 1;
    let pinchCenter = { x: 0, y: 0 };

    planBox.addEventListener('touchstart', (e) => {
      if (e.target.closest('.plan-toolbar')) return;
      if (e.touches.length === 2) {
        initialPinchDist = getDistance(e.touches[0], e.touches[1]);
        initialPinchScale = scale;
        pinchCenter = {
          x: (e.touches[0].clientX + e.touches[1].clientX) / 2,
          y: (e.touches[0].clientY + e.touches[1].clientY) / 2
        };
      } else if (e.touches.length === 1 && scale > 1) {
        isDragging = true;
        startX = e.touches[0].clientX - panX;
        startY = e.touches[0].clientY - panY;
        planImg.style.transition = 'none';
      }
    }, { passive: true });

    planBox.addEventListener('touchmove', (e) => {
      if (e.touches.length === 2 && initialPinchDist > 0) {
        const currentDist = getDistance(e.touches[0], e.touches[1]);
        const factor = currentDist / initialPinchDist;
        const newScale = Math.min(MAX_SCALE, Math.max(MIN_SCALE, initialPinchScale * factor));
        zoomToPoint(newScale / scale, pinchCenter.x, pinchCenter.y);
      } else if (e.touches.length === 1 && isDragging) {
        panX = e.touches[0].clientX - startX;
        panY = e.touches[0].clientY - startY;
        updateTransform(false);
      }
    }, { passive: true });

    planBox.addEventListener('touchend', (e) => {
      if (e.touches.length < 2) initialPinchDist = 0;
      if (e.touches.length === 0) {
        isDragging = false;
        updateTransform(true);
      }
    });

    function getDistance(t1, t2) {
      const dx = t1.clientX - t2.clientX;
      const dy = t1.clientY - t2.clientY;
      return Math.sqrt(dx * dx + dy * dy);
    }

    // Double-click/double-tap to toggle 1x and 2.2x
    let lastClick = 0;
    planBox.addEventListener('click', (e) => {
      if (e.target.closest('.plan-toolbar') || e.target.closest('.plan-footer-bar')) return;
      const now = Date.now();
      if (now - lastClick < 320) {
        if (scale > 1.1) {
          scale = 1;
          panX = 0;
          panY = 0;
          updateTransform(true);
        } else {
          zoomToPoint(2.3, e.clientX, e.clientY);
        }
      }
      lastClick = now;
    });

    // Toolbar button listeners
    if (zoomInBtn) {
      zoomInBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        zoomToPoint(1.35);
      });
    }
    if (zoomOutBtn) {
      zoomOutBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        zoomToPoint(0.75);
      });
    }
    if (zoomResetBtn) {
      zoomResetBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        scale = 1;
        panX = 0;
        panY = 0;
        updateTransform(true);
      });
    }
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
