/* Carine Zheng - landing page behaviour.
   Two jobs only: reveal sections as they enter view, and mark the nav once the
   page has scrolled so it separates from the content beneath it. */

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

  /* --- Nav separation ---------------------------------------------------- */

  function setupNav() {
    var nav = document.getElementById('nav');
    if (!nav || !('IntersectionObserver' in window)) return;

    // A zero-height sentinel at the top of the page. While it is visible we are
    // at the top; once it leaves, the nav has content behind it.
    var sentinel = document.createElement('div');
    sentinel.setAttribute('aria-hidden', 'true');
    sentinel.style.cssText = 'position:absolute;top:0;left:0;width:1px;height:1px;pointer-events:none;';
    document.body.prepend(sentinel);

    new IntersectionObserver(function (entries) {
      nav.dataset.scrolled = String(!entries[0].isIntersecting);
    }).observe(sentinel);
  }

  /* --- Init -------------------------------------------------------------- */

  function init() {
    setupReveal();
    setupNav();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
