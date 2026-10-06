/* ==========================================================================
   TORRE EDMON — ARCHITECTURAL APPLICATION ENGINE
   Smooth Panzoom Controller • Lightbox Modal • Dark Luxury Architecture
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {
  // 1. DEFAULT DARK LUXURY ENFORCEMENT
  document.documentElement.setAttribute('data-theme', 'dark');

  // 2. NAVBAR SCROLL & MOBILE MENU
  const navbar = document.querySelector('.navbar');
  window.addEventListener('scroll', () => {
    if (window.scrollY > 40) {
      navbar?.classList.add('scrolled');
    } else {
      navbar?.classList.remove('scrolled');
    }
  }, { passive: true });

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

  // 3. ARCHITECTURAL PANZOOM STUDIO (TOUCH PINCH & MOUSE WHEEL/DRAG)
  const planBox = document.getElementById('plan-interactive-box');
  const planImg = document.getElementById('plan-zoom-img');

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

      let baseW = boxRect.width * 0.94;
      let baseH = baseW / imgNaturalRatio;
      if (baseH > boxRect.height * 0.94) {
        baseH = boxRect.height * 0.94;
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
      if (scale <= 1.02) {
        scale = 1;
        panX = 0;
        panY = 0;
        planBox.classList.remove('zoomed');
      } else {
        const clamped = clampPan(panX, panY, scale);
        panX = clamped.x;
        panY = clamped.y;
        planBox.classList.add('zoomed');
      }

      planImg.style.transition = animate ? 'transform 0.28s cubic-bezier(0.2, 0, 0.2, 1)' : 'none';
      planImg.style.transform = `translate3d(${panX}px, ${panY}px, 0) scale(${scale})`;
      planBox.style.cursor = scale > 1 ? (isDragging ? 'grabbing' : 'grab') : 'zoom-in';
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

    // Wheel event with focal zoom for PC Mouse
    planBox.addEventListener('wheel', (e) => {
      e.preventDefault();
      const delta = e.deltaY < 0 ? 1.18 : 0.82;
      zoomToPoint(delta, e.clientX, e.clientY);
    }, { passive: false });

    // Drag to Pan with mouse
    planBox.addEventListener('mousedown', (e) => {
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

    // Touch events for Mobile (Pinch to Zoom & Touch Pan)
    let initialPinchDist = 0;
    let initialPinchScale = 1;
    let pinchCenter = { x: 0, y: 0 };

    planBox.addEventListener('touchstart', (e) => {
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

    // Double-click / double-tap to toggle 1x and 2.3x zoom
    let lastClick = 0;
    planBox.addEventListener('click', (e) => {
      if (e.target.closest('.plan-footer-bar')) return;
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

  lightboxClose?.addEventListener('click', closeLightbox);
  lightbox?.addEventListener('click', (e) => {
    if (e.target === lightbox) closeLightbox();
  });
  window.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') closeLightbox();
  });

  // 5. FOOTER DUAL BRANDING INFINITE CAROUSEL
  const carouselContainer = document.querySelector('.footer-carousel-container');
  const slides = document.querySelectorAll('.footer-carousel-slide');
  const dots = document.querySelectorAll('.footer-carousel-dot');

  if (carouselContainer && slides.length > 1) {
    let currentSlide = 0;
    let carouselTimer = null;
    const intervalTime = 3800; // 3.8s per slide

    function goToSlide(index) {
      currentSlide = (index + slides.length) % slides.length;
      slides.forEach((s, idx) => {
        s.classList.toggle('active', idx === currentSlide);
      });
      dots.forEach((d, idx) => {
        d.classList.toggle('active', idx === currentSlide);
      });
    }

    function startCarousel() {
      stopCarousel();
      carouselTimer = setInterval(() => {
        goToSlide(currentSlide + 1);
      }, intervalTime);
    }

    function stopCarousel() {
      if (carouselTimer) {
        clearInterval(carouselTimer);
        carouselTimer = null;
      }
    }

    // Interactive controls
    dots.forEach(dot => {
      dot.addEventListener('click', () => {
        const target = parseInt(dot.dataset.target, 10);
        if (!isNaN(target)) {
          goToSlide(target);
          startCarousel();
        }
      });
    });

    // Pause on hover
    carouselContainer.addEventListener('mouseenter', stopCarousel);
    carouselContainer.addEventListener('mouseleave', startCarousel);

    // Initial start
    startCarousel();
  }

  // 6. GLASS SLIDING PANELS ENGINE (GLASSDOOR INTERACTIVE DRAWERS)
  function initGlassSlidingPanels() {
    const panels = document.querySelectorAll('.glass-sliding-panel');

    panels.forEach(panel => {
      const tabs = panel.querySelectorAll('.glass-tab-btn');
      const cards = panel.querySelectorAll('.glass-slide-card');
      const dots = panel.querySelectorAll('.glass-dot');
      const prevBtn = panel.querySelector('.glass-ctrl-btn.prev');
      const nextBtn = panel.querySelector('.glass-ctrl-btn.next');

      if (!cards.length) return;

      let currentIndex = 0;

      function switchSlide(index) {
        currentIndex = (index + cards.length) % cards.length;

        // Update cards
        cards.forEach((card, idx) => {
          card.classList.toggle('active', idx === currentIndex);
        });

        // Update tabs if present
        tabs.forEach((tab, idx) => {
          const isActive = idx === currentIndex;
          tab.classList.toggle('active', isActive);
          tab.setAttribute('aria-selected', isActive ? 'true' : 'false');
        });

        // Update dots if present
        dots.forEach((dot, idx) => {
          dot.classList.toggle('active', idx === currentIndex);
        });
      }

      // Tab click events
      tabs.forEach((tab, idx) => {
        tab.addEventListener('click', () => switchSlide(idx));
      });

      // Dot click events
      dots.forEach((dot, idx) => {
        dot.addEventListener('click', () => switchSlide(idx));
      });

      // Prev/Next buttons
      prevBtn?.addEventListener('click', () => switchSlide(currentIndex - 1));
      nextBtn?.addEventListener('click', () => switchSlide(currentIndex + 1));

      // Optional Touch swipe inside viewport
      const viewport = panel.querySelector('.glass-slider-viewport');
      if (viewport) {
        let touchStartX = 0;
        let touchEndX = 0;

        viewport.addEventListener('touchstart', (e) => {
          touchStartX = e.changedTouches[0].screenX;
        }, { passive: true });

        viewport.addEventListener('touchend', (e) => {
          touchEndX = e.changedTouches[0].screenX;
          const diff = touchStartX - touchEndX;
          if (Math.abs(diff) > 45) {
            if (diff > 0) {
              switchSlide(currentIndex + 1); // Swipe left -> Next
            } else {
              switchSlide(currentIndex - 1); // Swipe right -> Prev
            }
          }
        }, { passive: true });
      }
    });
  }

  initGlassSlidingPanels();

  // 7. FOOTER CONTACT CHANNELS INTERACTIVE CAROUSEL
  function initContactCarousel() {
    const track = document.getElementById('contact-carousel-track');
    const prevBtn = document.getElementById('contact-carousel-prev');
    const nextBtn = document.getElementById('contact-carousel-next');
    const dots = document.querySelectorAll('#contact-carousel-dots .contact-dot');
    const slides = document.querySelectorAll('.contact-carousel-slide');

    if (!track || !slides.length) return;

    let currentContactIndex = 0;
    const totalSlides = slides.length;

    function goToContactSlide(index) {
      currentContactIndex = (index + totalSlides) % totalSlides;
      track.style.transform = `translateX(-${currentContactIndex * 100}%)`;

      dots.forEach((dot, idx) => {
        dot.classList.toggle('active', idx === currentContactIndex);
      });
    }

    prevBtn?.addEventListener('click', () => goToContactSlide(currentContactIndex - 1));
    nextBtn?.addEventListener('click', () => goToContactSlide(currentContactIndex + 1));

    dots.forEach((dot, idx) => {
      dot.addEventListener('click', () => goToContactSlide(idx));
    });

    // Touch swipe for contact carousel
    let touchStartX = 0;
    let touchEndX = 0;

    track.addEventListener('touchstart', (e) => {
      touchStartX = e.changedTouches[0].screenX;
    }, { passive: true });

    track.addEventListener('touchend', (e) => {
      touchEndX = e.changedTouches[0].screenX;
      const diff = touchStartX - touchEndX;
      if (Math.abs(diff) > 40) {
        if (diff > 0) {
          goToContactSlide(currentContactIndex + 1);
        } else {
          goToContactSlide(currentContactIndex - 1);
        }
      }
    }, { passive: true });
  }

  initContactCarousel();
});
