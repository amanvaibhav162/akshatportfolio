/**
 * assets/tech-stack.js - Interactive React Bits-Inspired Tech Stack Logic
 * Provides mouse-tracking spotlight radial gradient and interactive chip effects.
 */

(() => {
  function initSpotlightCards() {
    const cards = document.querySelectorAll('.spotlight-card');
    if (!cards.length) return;

    cards.forEach((card) => {
      // Mouse movement updates local coordinate relative to card bounding box
      const handleMouseMove = (e) => {
        const rect = card.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;

        card.style.setProperty('--mouse-x', `${x}px`);
        card.style.setProperty('--mouse-y', `${y}px`);
      };

      const handleMouseLeave = () => {
        card.style.setProperty('--mouse-x', '-500px');
        card.style.setProperty('--mouse-y', '-500px');
      };

      card.addEventListener('mousemove', handleMouseMove, { passive: true });
      card.addEventListener('mouseleave', handleMouseLeave, { passive: true });
    });
  }

  // Interactive chip click micro-interaction (copies chip name or provides haptic feedback)
  function initChipInteractions() {
    const chips = document.querySelectorAll('.bento-chip');
    chips.forEach((chip) => {
      chip.addEventListener('click', () => {
        const text = chip.textContent.trim();
        // Subtle micro-pulse
        chip.style.transform = 'scale(0.94)';
        setTimeout(() => {
          chip.style.transform = '';
        }, 150);
      });
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
      initSpotlightCards();
      initChipInteractions();
    });
  } else {
    initSpotlightCards();
    initChipInteractions();
  }
})();
