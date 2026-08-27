/* ==========================================================================
   WARM SOUND SYNTHESIZER (Web Audio API)
   Generates soft, elegant harmonic chimes without external audio dependencies.
   ========================================================================== */

class SoundEngine {
  constructor() {
    this.ctx = null;
    this.enabled = false;
  }

  init() {
    if (!this.ctx) {
      const AudioContext = window.AudioContext || window.webkitAudioContext;
      this.ctx = new AudioContext();
    }
    if (this.ctx.state === 'suspended') {
      this.ctx.resume();
    }
  }

  toggle() {
    this.enabled = !this.enabled;
    if (this.enabled) {
      this.init();
      this.playChime(523.25); // C5
    }
    return this.enabled;
  }

  playChime(freq = 440, type = 'sine') {
    if (!this.enabled) return;
    this.init();

    try {
      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();

      osc.type = type;
      osc.frequency.setValueAtTime(freq, this.ctx.currentTime);
      // Soft exponential decay for warm acoustic feel
      gain.gain.setValueAtTime(0.08, this.ctx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.0001, this.ctx.currentTime + 0.6);

      osc.connect(gain);
      gain.connect(this.ctx.destination);

      osc.start();
      osc.stop(this.ctx.currentTime + 0.6);
    } catch (e) {
      console.warn("Audio feedback error:", e);
    }
  }

  playClick() {
    this.playChime(587.33); // D5
  }

  playSwitch() {
    this.playChime(659.25); // E5
  }

  playSuccess() {
    if (!this.enabled) return;
    this.init();
    setTimeout(() => this.playChime(523.25), 0);
    setTimeout(() => this.playChime(659.25), 100);
    setTimeout(() => this.playChime(783.99), 200);
  }
}

window.soundEngine = new SoundEngine();
