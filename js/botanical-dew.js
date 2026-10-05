/* ==========================================================================
   TORRE EDMON — LIVING BOTANICAL DEW & RAINDROP ENGINE
   Subtropical Biofilic Raindrops, Water Beads & Organic Fluid Dynamics
   - Physically-inspired droplet rendering with 3D specular highlight and refraction
   - Stick-slip gravity sliding behavior across tropical leaf surfaces
   - Micro-condensations & glistening dewdrops
   - Zero-dependency, lightweight, 60fps high-performance Canvas 2D
   ========================================================================== */

(function () {
  'use strict';

  function initBotanicalDew() {
    const canvas = document.getElementById('rain-dew-canvas');
    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    if (!ctx) return;

    let width = 0;
    let height = 0;
    let dpr = 1;
    let isVisible = true;
    let mouseX = -1000;
    let mouseY = -1000;
    let mouseSpeed = 0;
    let lastMouseX = 0;
    let lastMouseY = 0;
    let lastTime = performance.now();

    // -------------------------------------------------------------------------
    // DROPLET & WATER BEAD CLASSES
    // -------------------------------------------------------------------------

    // 1. Static Glistening Dew Drops (Pearls on tropical leaves)
    class StaticDewDrop {
      constructor(w, h) {
        this.reset(w, h);
      }

      reset(w, h) {
        this.x = Math.random() * w;
        this.y = Math.random() * h;
        this.radius = 1.5 + Math.random() * 3.5;
        this.baseAlpha = 0.55 + Math.random() * 0.4;
        this.pulsePhase = Math.random() * Math.PI * 2;
        this.pulseSpeed = 0.02 + Math.random() * 0.03;
        this.aspect = 0.85 + Math.random() * 0.3; // slight oblong shape
      }

      update() {
        this.pulsePhase += this.pulseSpeed;
      }

      draw(c) {
        const shimmer = 0.85 + Math.sin(this.pulsePhase) * 0.15;
        const currentAlpha = Math.min(1, this.baseAlpha * shimmer);

        c.save();
        c.translate(this.x, this.y);

        // Soft drop shadow underneath droplet
        c.beginPath();
        c.ellipse(0, this.radius * 0.28, this.radius * 1.1, this.radius * this.aspect * 0.7, 0, 0, Math.PI * 2);
        c.fillStyle = `rgba(0, 0, 0, ${0.45 * currentAlpha})`;
        c.fill();

        // Droplet body with refraction gradient
        const bodyGrad = c.createRadialGradient(
          -this.radius * 0.2, -this.radius * 0.25, this.radius * 0.1,
          0, 0, this.radius
        );
        bodyGrad.addColorStop(0, `rgba(235, 255, 245, ${0.92 * currentAlpha})`);
        bodyGrad.addColorStop(0.35, `rgba(160, 220, 190, ${0.45 * currentAlpha})`);
        bodyGrad.addColorStop(0.75, `rgba(40, 110, 80, ${0.28 * currentAlpha})`);
        bodyGrad.addColorStop(1, `rgba(15, 45, 30, ${0.65 * currentAlpha})`);

        c.beginPath();
        c.ellipse(0, 0, this.radius, this.radius * this.aspect, 0, 0, Math.PI * 2);
        c.fillStyle = bodyGrad;
        c.fill();

        // High specular highlight (sharp sun/sky reflection bead)
        c.beginPath();
        c.ellipse(-this.radius * 0.32, -this.radius * 0.35 * this.aspect, this.radius * 0.32, this.radius * 0.22, -0.2, 0, Math.PI * 2);
        c.fillStyle = `rgba(255, 255, 255, ${0.95 * currentAlpha})`;
        c.fill();

        // Secondary bottom bounce reflection
        c.beginPath();
        c.ellipse(this.radius * 0.18, this.radius * 0.35 * this.aspect, this.radius * 0.28, this.radius * 0.14, 0.2, 0, Math.PI * 2);
        c.fillStyle = `rgba(190, 245, 215, ${0.4 * currentAlpha})`;
        c.fill();

        c.restore();
      }
    }

    // 2. Sliding Rain Drops (Gravity trickles down tropical leaves)
    class SlidingDrop {
      constructor(w, h) {
        this.trail = [];
        this.reset(w, h, true);
      }

      reset(w, h, initial = false) {
        this.x = Math.random() * w;
        this.y = initial ? Math.random() * h : -20 - Math.random() * 50;
        this.radius = 2.5 + Math.random() * 3.8;
        this.mass = this.radius * 0.8;
        this.speedY = 0.4 + Math.random() * 0.6;
        this.targetSpeedY = this.speedY;
        this.slideFriction = 0.94;
        this.pauseTimer = Math.random() * 120; // stick-slip effect
        this.pauseDuration = 30 + Math.random() * 90;
        this.driftX = (Math.random() - 0.5) * 0.35;
        this.trail = [];
        this.maxTrail = 18;
      }

      update(w, h) {
        // Stick-slip physics: drops stick on leaf veins and then surge
        if (this.pauseTimer > 0) {
          this.pauseTimer--;
          this.speedY *= 0.88;
        } else {
          this.speedY += 0.08 * this.mass;
          if (this.speedY > 4.5) this.speedY = 4.5;
          if (Math.random() < 0.008) {
            this.pauseTimer = this.pauseDuration;
            this.driftX = (Math.random() - 0.5) * 0.5;
          }
        }

        // Mouse proximity push
        const dx = this.x - mouseX;
        const dy = this.y - mouseY;
        const dist = Math.hypot(dx, dy);
        if (dist < 120 && dist > 0) {
          const force = (1 - dist / 120) * 0.8;
          this.x += (dx / dist) * force;
          this.speedY += 0.2;
        }

        this.x += this.driftX;
        this.y += this.speedY;

        // Record trail for wet trace on leaf
        if (this.speedY > 0.8 && Math.random() < 0.6) {
          this.trail.push({
            x: this.x + (Math.random() - 0.5) * 0.8,
            y: this.y - this.radius * 0.5,
            r: Math.max(0.6, this.radius * 0.35 * (0.8 + Math.random() * 0.4)),
            alpha: 0.48
          });
          if (this.trail.length > this.maxTrail) this.trail.shift();
        }

        // Fade trail
        for (let i = 0; i < this.trail.length; i++) {
          this.trail[i].alpha *= 0.975;
        }
        this.trail = this.trail.filter(p => p.alpha > 0.02);

        if (this.y > h + 40 || this.x < -30 || this.x > w + 30) {
          this.reset(w, h);
        }
      }

      draw(c) {
        // Draw trailing wet droplets
        for (let i = 0; i < this.trail.length; i++) {
          const pt = this.trail[i];
          c.beginPath();
          c.arc(pt.x, pt.y, pt.r, 0, Math.PI * 2);
          c.fillStyle = `rgba(200, 240, 220, ${pt.alpha})`;
          c.fill();
        }

        c.save();
        c.translate(this.x, this.y);

        // Teardrop elongation based on speed
        const stretch = Math.min(2.2, 1 + this.speedY * 0.18);

        // Shadow
        c.beginPath();
        c.ellipse(0, this.radius * stretch * 0.3, this.radius * 1.1, this.radius * stretch * 0.7, 0, 0, Math.PI * 2);
        c.fillStyle = 'rgba(0, 0, 0, 0.4)';
        c.fill();

        // Droplet body
        const grad = c.createRadialGradient(
          -this.radius * 0.25, -this.radius * stretch * 0.3, this.radius * 0.1,
          0, 0, this.radius * stretch
        );
        grad.addColorStop(0, 'rgba(240, 255, 250, 0.95)');
        grad.addColorStop(0.3, 'rgba(175, 230, 205, 0.55)');
        grad.addColorStop(0.8, 'rgba(40, 115, 85, 0.3)');
        grad.addColorStop(1, 'rgba(10, 35, 25, 0.7)');

        c.beginPath();
        c.ellipse(0, 0, this.radius, this.radius * stretch, 0, 0, Math.PI * 2);
        c.fillStyle = grad;
        c.fill();

        // Main upper specular gleam
        c.beginPath();
        c.ellipse(
          -this.radius * 0.28,
          -this.radius * stretch * 0.4,
          this.radius * 0.35,
          this.radius * 0.25,
          -0.1, 0, Math.PI * 2
        );
        c.fillStyle = 'rgba(255, 255, 255, 0.95)';
        c.fill();

        // Bottom light catch
        c.beginPath();
        c.ellipse(
          this.radius * 0.2,
          this.radius * stretch * 0.45,
          this.radius * 0.25,
          this.radius * 0.15,
          0.1, 0, Math.PI * 2
        );
        c.fillStyle = 'rgba(200, 255, 230, 0.45)';
        c.fill();

        c.restore();
      }
    }

    // 3. Falling Mist / Ambient Fine Tropical Rain Beads
    class MistDrop {
      constructor(w, h) {
        this.reset(w, h, true);
      }

      reset(w, h, initial = false) {
        this.x = Math.random() * (w + 100) - 50;
        this.y = initial ? Math.random() * h : -40 - Math.random() * 40;
        this.length = 12 + Math.random() * 22;
        this.speedX = -0.6 - Math.random() * 0.8; // subtle wind drift
        this.speedY = 8 + Math.random() * 9;
        this.alpha = 0.12 + Math.random() * 0.22;
        this.width = 0.8 + Math.random() * 0.8;
      }

      update(w, h) {
        this.x += this.speedX;
        this.y += this.speedY;

        if (this.y > h + 30 || this.x < -60) {
          this.reset(w, h);
        }
      }

      draw(c) {
        c.beginPath();
        c.moveTo(this.x, this.y);
        c.lineTo(this.x + this.speedX * (this.length / this.speedY), this.y + this.length);
        c.strokeStyle = `rgba(220, 250, 235, ${this.alpha})`;
        c.lineWidth = this.width;
        c.lineCap = 'round';
        c.stroke();
      }
    }

    // -------------------------------------------------------------------------
    // SYSTEM SETUP & POPULATION
    // -------------------------------------------------------------------------
    let staticDrops = [];
    let slidingDrops = [];
    let mistDrops = [];

    function resize() {
      dpr = Math.min(window.devicePixelRatio || 1, 2);
      width = window.innerWidth;
      height = window.innerHeight;

      canvas.width = Math.floor(width * dpr);
      canvas.height = Math.floor(height * dpr);
      canvas.style.width = width + 'px';
      canvas.style.height = height + 'px';

      ctx.scale(dpr, dpr);

      // Scale particle density to screen resolution
      const area = (width * height) / (1920 * 1080);
      const staticCount = Math.floor(45 * Math.max(0.6, area));
      const slidingCount = Math.floor(18 * Math.max(0.6, area));
      const mistCount = Math.floor(25 * Math.max(0.6, area));

      staticDrops = Array.from({ length: staticCount }, () => new StaticDewDrop(width, height));
      slidingDrops = Array.from({ length: slidingCount }, () => new SlidingDrop(width, height));
      mistDrops = Array.from({ length: mistCount }, () => new MistDrop(width, height));
    }

    window.addEventListener('resize', resize, { passive: true });
    resize();

    // Mouse tracking for organic interactivity
    window.addEventListener('mousemove', (e) => {
      mouseX = e.clientX;
      mouseY = e.clientY;
      const dx = mouseX - lastMouseX;
      const dy = mouseY - lastMouseY;
      mouseSpeed = Math.hypot(dx, dy);
      lastMouseX = mouseX;
      lastMouseY = mouseY;
    }, { passive: true });

    document.addEventListener('visibilitychange', () => {
      isVisible = !document.hidden;
      if (isVisible) {
        lastTime = performance.now();
        requestAnimationFrame(render);
      }
    });

    // -------------------------------------------------------------------------
    // ANIMATION TICK
    // -------------------------------------------------------------------------
    function render(currentTime) {
      if (!isVisible) return;
      requestAnimationFrame(render);

      // Clear with transparent layer
      ctx.clearRect(0, 0, width, height);

      // 1. Draw static glistening dewdrops
      for (let i = 0; i < staticDrops.length; i++) {
        staticDrops[i].update();
        staticDrops[i].draw(ctx);
      }

      // 2. Draw sliding water beads with wet tracks
      for (let i = 0; i < slidingDrops.length; i++) {
        slidingDrops[i].update(width, height);
        slidingDrops[i].draw(ctx);
      }

      // 3. Draw subtle atmospheric mist rain
      for (let i = 0; i < mistDrops.length; i++) {
        mistDrops[i].update(width, height);
        mistDrops[i].draw(ctx);
      }
    }

    requestAnimationFrame(render);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initBotanicalDew);
  } else {
    initBotanicalDew();
  }
})();
