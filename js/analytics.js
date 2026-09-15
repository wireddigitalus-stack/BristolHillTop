/**
 * Bristol Hilltop Camping — Lightweight Analytics & Lead Tracking
 * Stores all data in localStorage for static-site use
 */
(function() {
  'use strict';

  const STORAGE_KEY = 'bhc_analytics';
  const LEADS_KEY = 'bhc_leads';

  // --- Helpers ---
  function getData() {
    try {
      return JSON.parse(localStorage.getItem(STORAGE_KEY)) || createFreshData();
    } catch(e) {
      return createFreshData();
    }
  }

  function saveData(data) {
    try { localStorage.setItem(STORAGE_KEY, JSON.stringify(data)); } catch(e) {}
  }

  function getLeads() {
    try {
      return JSON.parse(localStorage.getItem(LEADS_KEY)) || [];
    } catch(e) { return []; }
  }

  function saveLeads(leads) {
    try { localStorage.setItem(LEADS_KEY, JSON.stringify(leads)); } catch(e) {}
  }

  function createFreshData() {
    return {
      totalViews: 0,
      totalClicks: 0,
      totalCalls: 0,
      totalTexts: 0,
      totalLeads: 0,
      pageViews: {},    // { '/': 45, '/blog/': 12 }
      dailyViews: {},   // { '2026-09-10': 23 }
      dailyCalls: {},
      clickMap: {},     // { 'Call Now CTA': 5, 'Rentals Nav': 3 }
      devices: {},      // { 'mobile': 30, 'desktop': 15 }
      referrers: {},    // { 'google': 10, 'direct': 20 }
      hourlyViews: {},  // { '14': 5, '15': 8 }
      sessions: []      // last 50 sessions
    };
  }

  function today() {
    return new Date().toISOString().split('T')[0];
  }

  function getHour() {
    return String(new Date().getHours());
  }

  function getDeviceType() {
    const w = window.innerWidth;
    if (w < 768) return 'Mobile';
    if (w < 1024) return 'Tablet';
    return 'Desktop';
  }

  function getReferrer() {
    const ref = document.referrer;
    if (!ref) return 'Direct / Typed URL';
    if (ref.includes('google.com/maps') || ref.includes('google.com/local')) return 'Google Business';
    if (ref.includes('google')) return 'Google Search';
    if (ref.includes('bing')) return 'Bing Search';
    if (ref.includes('yahoo')) return 'Yahoo Search';
    if (ref.includes('duckduckgo')) return 'DuckDuckGo';
    if (ref.includes('facebook') || ref.includes('fb.')) return 'Facebook';
    if (ref.includes('instagram')) return 'Instagram';
    if (ref.includes('twitter') || ref.includes('t.co')) return 'Twitter / X';
    if (ref.includes('youtube')) return 'YouTube';
    if (ref.includes('tiktok')) return 'TikTok';
    if (ref.includes('nextdoor')) return 'Nextdoor';
    if (ref.includes('yelp')) return 'Yelp';
    try { return new URL(ref).hostname; } catch(e) { return 'Other Referral'; }
  }

  function getPagePath() {
    return window.location.pathname || '/';
  }

  function getClickLabel(el) {
    // Walk up to find meaningful label
    let node = el;
    for (let i = 0; i < 5 && node; i++) {
      if (node.href && node.href.startsWith('tel:')) return '📞 Phone Call Click';
      if (node.href && node.href.startsWith('sms:')) return '💬 Text Message Click';
      if (node.classList && node.classList.contains('btn--call')) return '📞 Call Button';
      if (node.classList && node.classList.contains('btn--outline')) return '🔗 ' + (node.textContent || '').trim().substring(0, 40);
      if (node.classList && node.classList.contains('btn--primary')) return '🔗 ' + (node.textContent || '').trim().substring(0, 40);
      if (node.classList && node.classList.contains('nav__link')) return '📍 Nav: ' + (node.textContent || '').trim();
      if (node.classList && node.classList.contains('race-card')) return '📄 Blog: ' + (node.querySelector('h3')?.textContent || '').trim().substring(0, 40);
      if (node.classList && node.classList.contains('faq__question')) return '❓ FAQ: ' + (node.textContent || '').trim().substring(0, 40);
      if (node.tagName === 'A' && node.href) return '🔗 Link: ' + (node.textContent || '').trim().substring(0, 40);
      node = node.parentElement;
    }
    return null; // Not a trackable click
  }

  // --- Track Page View ---
  function trackPageView() {
    var data = getData();
    var path = getPagePath();
    var day = today();
    var hour = getHour();
    var device = getDeviceType();
    var referrer = getReferrer();

    data.totalViews++;
    data.pageViews[path] = (data.pageViews[path] || 0) + 1;
    data.dailyViews[day] = (data.dailyViews[day] || 0) + 1;
    data.devices[device] = (data.devices[device] || 0) + 1;
    data.referrers[referrer] = (data.referrers[referrer] || 0) + 1;
    data.hourlyViews[hour] = (data.hourlyViews[hour] || 0) + 1;

    // Session log (keep last 100)
    data.sessions.unshift({
      page: path,
      device: device,
      referrer: referrer,
      time: new Date().toISOString()
    });
    if (data.sessions.length > 100) data.sessions = data.sessions.slice(0, 100);

    saveData(data);
  }

  // --- Track Clicks ---
  function trackClick(e) {
    var label = getClickLabel(e.target);
    if (!label) return;

    var data = getData();
    data.totalClicks++;
    data.clickMap[label] = (data.clickMap[label] || 0) + 1;

    // Track calls and texts specifically
    var el = e.target.closest('a');
    if (el) {
      if (el.href && el.href.startsWith('tel:')) {
        data.totalCalls++;
        var day = today();
        data.dailyCalls[day] = (data.dailyCalls[day] || 0) + 1;
      }
      if (el.href && el.href.startsWith('sms:')) {
        data.totalTexts++;
      }
    }

    saveData(data);
  }

  // --- Lead Form Submission ---
  window.bhcSubmitLead = function(form) {
    var name = form.querySelector('[name="lead_name"]').value.trim();
    var phone = form.querySelector('[name="lead_phone"]').value.trim();
    var email = form.querySelector('[name="lead_email"]').value.trim();
    var interest = form.querySelector('[name="lead_interest"]').value;
    var message = form.querySelector('[name="lead_message"]').value.trim();

    if (!name || !phone) {
      alert('Please enter your name and phone number.');
      return false;
    }

    var leads = getLeads();
    leads.unshift({
      id: Date.now(),
      name: name,
      phone: phone,
      email: email,
      interest: interest,
      message: message,
      time: new Date().toISOString(),
      status: 'new'
    });
    saveLeads(leads);

    // Update analytics
    var data = getData();
    data.totalLeads++;
    saveData(data);

    // Show success
    form.innerHTML = '<div style="text-align:center;padding:2rem;"><p style="font-size:1.5rem;margin-bottom:0.5rem;">✅ Thank You!</p><p>We\'ll call you shortly at <strong>' + phone + '</strong></p><p style="margin-top:1rem;"><a href="tel:+14233835373" class="btn btn--call"><span class="btn__icon">📞</span> Call Us Now: (423) 383-5373</a></p></div>';
    return false;
  };

  // --- Initialize ---
  trackPageView();
  document.addEventListener('click', trackClick, true);

})();
