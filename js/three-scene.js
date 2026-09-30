/* ==========================================================================
   TORRE EDMON - LUXURY ARCHITECTURAL 3D AMBIENT ENGINE
   Atmospheric Gold Dust, Floating Bokeh Orbs & Scroll/Mouse Parallax
   - Procedural glowing particle sprites (high luminous visibility)
   - Dual-tier depth: fine gold stardust + soft ambient bokeh orbs
   - Fluid upward drift with subtle organic oscillation
   - Scroll-linked depth response and smooth mouse inertia
   ========================================================================== */

function initLuxuryAmbientScene() {
  const canvas = document.getElementById('three-canvas');
  if (!canvas) return;
  if (typeof THREE === 'undefined') return;

  try {
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(60, window.innerWidth / window.innerHeight, 1, 1200);
    camera.position.z = 320;

    const renderer = new THREE.WebGLRenderer({
      canvas: canvas,
      alpha: true,
      antialias: true
    });
    renderer.setSize(window.innerWidth, window.innerHeight);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

    // 1. Procedural Glowing Gold Sprite Texture
    function createGlowingParticleTexture() {
      const pCanvas = document.createElement('canvas');
      pCanvas.width = 64;
      pCanvas.height = 64;
      const ctx = pCanvas.getContext('2d');

      const gradient = ctx.createRadialGradient(32, 32, 0, 32, 32, 32);
      gradient.addColorStop(0, 'rgba(255, 248, 220, 1.0)');
      gradient.addColorStop(0.18, 'rgba(235, 200, 130, 0.95)');
      gradient.addColorStop(0.45, 'rgba(197, 160, 89, 0.45)');
      gradient.addColorStop(0.75, 'rgba(197, 160, 89, 0.12)');
      gradient.addColorStop(1, 'rgba(197, 160, 89, 0)');

      ctx.fillStyle = gradient;
      ctx.beginPath();
      ctx.arc(32, 32, 32, 0, Math.PI * 2);
      ctx.fill();

      const texture = new THREE.CanvasTexture(pCanvas);
      texture.needsUpdate = true;
      return texture;
    }

    // 2. Procedural Soft Bokeh Texture for Large Ambient Orbs
    function createBokehTexture() {
      const bCanvas = document.createElement('canvas');
      bCanvas.width = 128;
      bCanvas.height = 128;
      const ctx = bCanvas.getContext('2d');

      const gradient = ctx.createRadialGradient(64, 64, 0, 64, 64, 64);
      gradient.addColorStop(0, 'rgba(228, 194, 122, 0.65)');
      gradient.addColorStop(0.35, 'rgba(197, 160, 89, 0.28)');
      gradient.addColorStop(0.7, 'rgba(140, 107, 45, 0.08)');
      gradient.addColorStop(1, 'rgba(140, 107, 45, 0)');

      ctx.fillStyle = gradient;
      ctx.beginPath();
      ctx.arc(64, 64, 64, 0, Math.PI * 2);
      ctx.fill();

      const texture = new THREE.CanvasTexture(bCanvas);
      texture.needsUpdate = true;
      return texture;
    }

    const particleTexture = createGlowingParticleTexture();
    const bokehTexture = createBokehTexture();

    // --------------------------------------------------------------------------
    // LAYER 1: Fine Luminous Gold Stardust (380 particles)
    // --------------------------------------------------------------------------
    const stardustCount = 380;
    const stardustGeo = new THREE.BufferGeometry();
    const stardustPos = new Float32Array(stardustCount * 3);
    const stardustVel = new Float32Array(stardustCount * 3); // velocities and phase offsets

    for (let i = 0; i < stardustCount; i++) {
      const i3 = i * 3;
      stardustPos[i3] = (Math.random() - 0.5) * 1100;
      stardustPos[i3 + 1] = (Math.random() - 0.5) * 900;
      stardustPos[i3 + 2] = (Math.random() - 0.5) * 600;

      // vy, vx oscillation speed, phase
      stardustVel[i3] = (Math.random() - 0.5) * 0.25;      // vx drift
      stardustVel[i3 + 1] = 0.25 + Math.random() * 0.45;   // upward vy
      stardustVel[i3 + 2] = Math.random() * Math.PI * 2;   // phase
    }

    stardustGeo.setAttribute('position', new THREE.BufferAttribute(stardustPos, 3));

    const stardustMat = new THREE.PointsMaterial({
      size: 6.2,
      map: particleTexture,
      transparent: true,
      opacity: 0.88,
      blending: THREE.AdditiveBlending,
      depthWrite: false,
      color: 0xffffff
    });

    const stardustParticles = new THREE.Points(stardustGeo, stardustMat);
    scene.add(stardustParticles);

    // --------------------------------------------------------------------------
    // LAYER 2: Ambient Glowing Bokeh Light Orbs (45 orbs in the depth)
    // --------------------------------------------------------------------------
    const bokehCount = 45;
    const bokehGeo = new THREE.BufferGeometry();
    const bokehPos = new Float32Array(bokehCount * 3);
    const bokehVel = new Float32Array(bokehCount);

    for (let i = 0; i < bokehCount; i++) {
      const i3 = i * 3;
      bokehPos[i3] = (Math.random() - 0.5) * 1200;
      bokehPos[i3 + 1] = (Math.random() - 0.5) * 1000;
      bokehPos[i3 + 2] = -150 + (Math.random() - 0.5) * 450;
      bokehVel[i] = 0.12 + Math.random() * 0.22;
    }

    bokehGeo.setAttribute('position', new THREE.BufferAttribute(bokehPos, 3));

    const bokehMat = new THREE.PointsMaterial({
      size: 42.0,
      map: bokehTexture,
      transparent: true,
      opacity: 0.55,
      blending: THREE.AdditiveBlending,
      depthWrite: false,
      color: 0xffffff
    });

    const bokehParticles = new THREE.Points(bokehGeo, bokehMat);
    scene.add(bokehParticles);

    // --------------------------------------------------------------------------
    // INTERACTION: Mouse Parallax & Scroll Sync
    // --------------------------------------------------------------------------
    let mouseX = 0;
    let mouseY = 0;
    let targetX = 0;
    let targetY = 0;
    let scrollY = window.scrollY || 0;
    let targetScrollY = scrollY;

    window.addEventListener('mousemove', (e) => {
      targetX = (e.clientX - window.innerWidth / 2) * 0.04;
      targetY = (e.clientY - window.innerHeight / 2) * 0.04;
    }, { passive: true });

    window.addEventListener('scroll', () => {
      targetScrollY = window.scrollY || 0;
    }, { passive: true });

    window.addEventListener('resize', () => {
      camera.aspect = window.innerWidth / window.innerHeight;
      camera.updateProjectionMatrix();
      renderer.setSize(window.innerWidth, window.innerHeight);
    });

    // --------------------------------------------------------------------------
    // ANIMATION LOOP (Butter-Smooth 60FPS)
    // --------------------------------------------------------------------------
    let clock = 0;
    function animate() {
      requestAnimationFrame(animate);
      clock += 0.016;

      // Mouse damping
      mouseX += (targetX - mouseX) * 0.05;
      mouseY += (targetY - mouseY) * 0.05;
      scrollY += (targetScrollY - scrollY) * 0.05;

      // Update Stardust positions
      const sPositions = stardustGeo.attributes.position.array;
      for (let i = 0; i < stardustCount; i++) {
        const i3 = i * 3;
        const phase = stardustVel[i3 + 2] + clock;

        // Upward drift + horizontal gentle floating wave
        sPositions[i3] += Math.sin(phase) * 0.35 + stardustVel[i3];
        sPositions[i3 + 1] += stardustVel[i3 + 1];

        // Wrap around bounds
        if (sPositions[i3 + 1] > 480) {
          sPositions[i3 + 1] = -480;
          sPositions[i3] = (Math.random() - 0.5) * 1100;
        }
        if (sPositions[i3] > 600) sPositions[i3] = -600;
        if (sPositions[i3] < -600) sPositions[i3] = 600;
      }
      stardustGeo.attributes.position.needsUpdate = true;

      // Update Bokeh positions
      const bPositions = bokehGeo.attributes.position.array;
      for (let i = 0; i < bokehCount; i++) {
        const i3 = i * 3;
        bPositions[i3 + 1] += bokehVel[i];
        if (bPositions[i3 + 1] > 520) {
          bPositions[i3 + 1] = -520;
          bPositions[i3] = (Math.random() - 0.5) * 1200;
        }
      }
      bokehGeo.attributes.position.needsUpdate = true;

      // Slow elegant orbital rotations
      stardustParticles.rotation.y = clock * 0.035;
      bokehParticles.rotation.y = clock * 0.018;

      // Parallax camera displacement
      camera.position.x = mouseX * 2.2;
      camera.position.y = -mouseY * 2.2 - (scrollY * 0.08);
      camera.lookAt(scene.position);

      renderer.render(scene, camera);
    }

    animate();
  } catch (e) {
    console.warn("Ambient 3D scene fallback:", e);
  }
}

document.addEventListener('DOMContentLoaded', initLuxuryAmbientScene);
