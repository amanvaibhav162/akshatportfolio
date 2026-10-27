/**
 * assets/connect-beacon.js - Clean Gamedev Connect Handler
 */

(function () {
  'use strict';

  function initConnect() {
    const msgInput = document.getElementById('connect-msg');
    const nameInput = document.getElementById('connect-name');
    const emailInput = document.getElementById('connect-email');
    const submitBtn = document.getElementById('connect-submit-btn');
    const toast = document.getElementById('connect-toast');

    function handleSubmit() {
      const name = nameInput?.value.trim() || 'Anonymous Developer';
      const email = emailInput?.value.trim() || 'Not specified';
      const msg = msgInput?.value.trim() || '';

      const subject = `[Connect] Message from ${name}`;
      const body = `Hi Akshat,

FROM: ${name} (${email})

MESSAGE:
${msg || '(No additional message provided)'}

---
Sent from akshatyadav.dev`;

      // Copy to clipboard
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(body).catch(() => {});
      }

      // Show toast
      if (toast) {
        toast.classList.add('is-visible');
        setTimeout(() => {
          toast.classList.remove('is-visible');
        }, 6000);
      }

      // Launch mailto
      const mailtoUrl = `mailto:akshatyadavlko@gmail.com?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
      window.location.href = mailtoUrl;
    }

    if (submitBtn) {
      submitBtn.addEventListener('click', handleSubmit);
    }

    // Keyboard shortcut (Ctrl+Enter / Cmd+Enter)
    [nameInput, emailInput, msgInput].forEach(el => {
      if (el) {
        el.addEventListener('keydown', (e) => {
          if ((e.ctrlKey || e.metaKey) && e.key === 'Enter') {
            e.preventDefault();
            handleSubmit();
          }
        });
      }
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initConnect);
  } else {
    initConnect();
  }
})();
