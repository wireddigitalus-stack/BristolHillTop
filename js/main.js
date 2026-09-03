/* ============================================
   Bristol Hilltop Camping — Main JavaScript
   Lightweight, vanilla JS — no dependencies
   ============================================ */

(function () {
  'use strict';

  // --- Mobile Navigation Toggle ---
  const navToggle = document.querySelector('.header__toggle');
  const nav = document.querySelector('.nav');
  const navLinks = document.querySelectorAll('.nav__link');

  if (navToggle && nav) {
    navToggle.addEventListener('click', function () {
      const isOpen = nav.classList.toggle('nav--open');
      navToggle.setAttribute('aria-expanded', isOpen);
      navToggle.innerHTML = isOpen ? '&#10005;' : '&#9776;';
    });

    // Close nav when a link is clicked
    navLinks.forEach(function (link) {
      link.addEventListener('click', function () {
        nav.classList.remove('nav--open');
        navToggle.setAttribute('aria-expanded', 'false');
        navToggle.innerHTML = '&#9776;';
      });
    });
  }

  // --- Header Scroll Effect ---
  const header = document.querySelector('.header');
  if (header) {
    var lastScroll = 0;
    window.addEventListener('scroll', function () {
      var currentScroll = window.scrollY;
      if (currentScroll > 50) {
        header.classList.add('header--scrolled');
      } else {
        header.classList.remove('header--scrolled');
      }
      lastScroll = currentScroll;
    }, { passive: true });
  }

  // --- FAQ Accordion ---
  const faqItems = document.querySelectorAll('.faq__item');
  faqItems.forEach(function (item) {
    const question = item.querySelector('.faq__question');
    if (question) {
      question.addEventListener('click', function () {
        // Close other items
        faqItems.forEach(function (other) {
          if (other !== item) {
            other.classList.remove('faq__item--open');
          }
        });
        // Toggle current
        item.classList.toggle('faq__item--open');
      });
    }
  });

  // --- Race Countdown Timer ---
  function renderTimer(el, diff) {
    var days = Math.floor(diff / (1000 * 60 * 60 * 24));
    var hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    var minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
    var seconds = Math.floor((diff % (1000 * 60)) / 1000);

    el.innerHTML =
      '<div class="countdown__item"><span class="countdown__number">' + days + '</span><span class="countdown__label">Days</span></div>' +
      '<div class="countdown__item"><span class="countdown__number">' + hours + '</span><span class="countdown__label">Hours</span></div>' +
      '<div class="countdown__item"><span class="countdown__number">' + minutes + '</span><span class="countdown__label">Mins</span></div>' +
      '<div class="countdown__item"><span class="countdown__number">' + seconds + '</span><span class="countdown__label">Secs</span></div>';
  }

  function updateCountdown() {
    var now = new Date();

    // Bass Pro Shops Night Race — September 19, 2026 at 7:30 PM ET
    var nightRaceEl = document.getElementById('countdown-nightrace');
    if (nightRaceEl) {
      var nightDate = new Date('2026-09-19T19:30:00-04:00');
      var diffNight = nightDate - now;
      if (diffNight <= 0) {
        nightRaceEl.innerHTML = '<div class="countdown__item"><span class="countdown__number">🏁</span><span class="countdown__label">Race Day!</span></div>';
      } else {
        renderTimer(nightRaceEl, diffNight);
      }
    }

    // Food City 500 — April 11, 2027 at 3:30 PM ET
    var foodCityEl = document.getElementById('countdown-foodcity');
    if (foodCityEl) {
      var foodCityDate = new Date('2027-04-11T15:30:00-04:00');
      var diffFC = foodCityDate - now;
      if (diffFC <= 0) {
        foodCityEl.innerHTML = '<div class="countdown__item"><span class="countdown__number">🏁</span><span class="countdown__label">Race Day!</span></div>';
      } else {
        renderTimer(foodCityEl, diffFC);
      }
    }
  }

  // Run countdown immediately and every second
  updateCountdown();
  setInterval(updateCountdown, 1000);

  // --- Intersection Observer for Fade-In Animations ---
  if ('IntersectionObserver' in window) {
    var fadeEls = document.querySelectorAll('.fade-in');
    var fadeObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('fade-in--visible');
          fadeObserver.unobserve(entry.target);
        }
      });
    }, {
      threshold: 0.1,
      rootMargin: '0px 0px -40px 0px'
    });

    fadeEls.forEach(function (el) {
      fadeObserver.observe(el);
    });
  } else {
    // Fallback: just show everything
    document.querySelectorAll('.fade-in').forEach(function (el) {
      el.classList.add('fade-in--visible');
    });
  }

  // --- Smooth Scroll for anchor links (fallback for browsers without CSS scroll-behavior) ---
  document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
    anchor.addEventListener('click', function (e) {
      var targetId = this.getAttribute('href');
      if (targetId === '#') return;
      var target = document.querySelector(targetId);
      if (target) {
        e.preventDefault();
        var headerOffset = parseInt(getComputedStyle(document.documentElement).getPropertyValue('--header-height')) || 64;
        var targetPosition = target.getBoundingClientRect().top + window.scrollY - headerOffset;
        window.scrollTo({
          top: targetPosition,
          behavior: 'smooth'
        });
      }
    });
  });

  // --- Lazy Load Images ---
  if ('loading' in HTMLImageElement.prototype) {
    // Browser supports native lazy loading — nothing extra needed
    // Images should have loading="lazy" attribute in HTML
  } else if ('IntersectionObserver' in window) {
    // Fallback lazy loading
    var lazyImages = document.querySelectorAll('img[data-src]');
    var imageObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          var img = entry.target;
          img.src = img.dataset.src;
          if (img.dataset.srcset) {
            img.srcset = img.dataset.srcset;
          }
          img.removeAttribute('data-src');
          imageObserver.unobserve(img);
        }
      });
    });

    lazyImages.forEach(function (img) {
      imageObserver.observe(img);
    });
  }

})();
