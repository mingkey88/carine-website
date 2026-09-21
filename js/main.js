/* Carine Zheng - landing page behaviour.
   One job: reveal sections as they enter view. */

(function () {
  'use strict';

  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)');

  /* --- Section reveal ---------------------------------------------------- */

  function setupReveal() {
    var targets = document.querySelectorAll('.reveal');
    if (!targets.length) return;

    // Reduced motion, or no IntersectionObserver: show everything immediately.
    if (reduceMotion.matches || !('IntersectionObserver' in window)) {
      for (var i = 0; i < targets.length; i++) {
        targets[i].classList.add('is-visible');
      }
      return;
    }

    var observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          entry.target.classList.add('is-visible');
          observer.unobserve(entry.target);
        });
      },
      // threshold 0 rather than a fraction: an element taller than the viewport
      // can never satisfy a fractional threshold and would stay hidden forever.
      // rootMargin does the "wait until it is properly on screen" work instead.
      { rootMargin: '0px 0px -10% 0px', threshold: 0 }
    );

    targets.forEach(function (el) {
      observer.observe(el);
    });
  }

  /* --- Init -------------------------------------------------------------- */

  function init() {
    setupReveal();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
