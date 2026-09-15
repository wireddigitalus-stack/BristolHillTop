/**
 * Bristol Hilltop Camping — Telemetry Counter
 * Simple hit counter that logs all events to localStorage.
 * 
 * ┌─────────────────────────────────────────────┐
 * │  TO HOOK UP A DATABASE LATER:               │
 * │  Replace sendHit() to POST to your API      │
 * │  e.g. fetch('/api/track', { body: hit })    │
 * └─────────────────────────────────────────────┘
 */
(function() {
  'use strict';

  var DB_KEY = 'bhc_telemetry';
  var LEADS_KEY = 'bhc_leads';

  // =============================================
  // DATABASE LAYER — swap this out later
  // =============================================
  function getDB() {
    try { return JSON.parse(localStorage.getItem(DB_KEY)) || freshDB(); }
    catch(e) { return freshDB(); }
  }

  function saveDB(db) {
    try { localStorage.setItem(DB_KEY, JSON.stringify(db)); } catch(e) {}
  }

  function getLeads() {
    try { return JSON.parse(localStorage.getItem(LEADS_KEY)) || []; }
    catch(e) { return []; }
  }

  function saveLeads(leads) {
    try { localStorage.setItem(LEADS_KEY, JSON.stringify(leads)); } catch(e) {}
  }

  function freshDB() {
    return {
      counters: {
        views: 0,
        clicks: 0,
        calls: 0,
        texts: 0,
        leads: 0
      },
      daily: {},        // { '2026-09-15': { views: 5, calls: 1 } }
      hourly: {},       // { '14': 3 }
      pages: {},        // { '/': 10, '/blog/': 5 }
      devices: {},      // { 'Mobile': 8, 'Desktop': 3 }
      sources: {},      // { 'Google Search': 4 }
      clickMap: {},     // { '📞 Phone Call Click': 12 }
      sessions: []      // last 100 visitor sessions
    };
  }

  // =============================================
  // SEND HIT — the one function to swap later
  // =============================================
  //
  // Right now: saves to localStorage
  // Later:     POST to /api/track or Firebase
  //
  function sendHit(type, data) {
    var db = getDB();
    var day = new Date().toISOString().split('T')[0];
    var hour = String(new Date().getHours());

    if (!db.daily[day]) db.daily[day] = { views: 0, calls: 0 };

    switch(type) {

      case 'pageview':
        db.counters.views++;
        db.daily[day].views++;
        db.hourly[hour] = (db.hourly[hour] || 0) + 1;
        db.pages[data.page] = (db.pages[data.page] || 0) + 1;
        db.devices[data.device] = (db.devices[data.device] || 0) + 1;
        db.sources[data.source] = (db.sources[data.source] || 0) + 1;
        // Session log
        db.sessions.unshift({
          page: data.page,
          device: data.device,
          source: data.source,
          time: new Date().toISOString()
        });
        if (db.sessions.length > 100) db.sessions = db.sessions.slice(0, 100);
        break;

      case 'click':
        db.counters.clicks++;
        db.clickMap[data.label] = (db.clickMap[data.label] || 0) + 1;
        break;

      case 'call':
        db.counters.calls++;
        db.counters.clicks++;
        db.daily[day].calls++;
        db.clickMap['📞 Phone Call Click'] = (db.clickMap['📞 Phone Call Click'] || 0) + 1;
        break;

      case 'text':
        db.counters.texts++;
        db.counters.clicks++;
        db.clickMap['💬 Text Message Click'] = (db.clickMap['💬 Text Message Click'] || 0) + 1;
        break;

      case 'lead':
        db.counters.leads++;
        break;
    }

    saveDB(db);

    // ── FUTURE DATABASE HOOK ──
    // fetch('/api/track', {
    //   method: 'POST',
    //   headers: { 'Content-Type': 'application/json' },
    //   body: JSON.stringify({ type: type, data: data, ts: Date.now() })
    // }).catch(function(){});
  }

  // =============================================
  // DETECTORS
  // =============================================
  function getDevice() {
    var w = window.innerWidth;
    if (w < 768) return 'Mobile';
    if (w < 1024) return 'Tablet';
    return 'Desktop';
  }

  function getSource() {
    var ref = document.referrer;
    if (!ref) return 'Organic Search';
    if (ref.includes('google.com/maps') || ref.includes('google.com/local')) return 'Google Business';
    if (ref.includes('google')) return 'Google Search';
    if (ref.includes('bing')) return 'Bing Search';
    if (ref.includes('facebook') || ref.includes('fb.')) return 'Facebook';
    if (ref.includes('vercel')) return 'Organic Search';
    return 'Other Referral';
  }

  function getClickLabel(el) {
    var node = el;
    for (var i = 0; i < 5 && node; i++) {
      if (node.href && node.href.startsWith('tel:')) return null; // handled as 'call'
      if (node.href && node.href.startsWith('sms:')) return null; // handled as 'text'
      if (node.classList && node.classList.contains('btn--call')) return '📞 Call Button';
      if (node.classList && node.classList.contains('btn--outline')) return '🔗 ' + (node.textContent || '').trim().substring(0, 40);
      if (node.classList && node.classList.contains('nav__link')) return '📍 Nav: ' + (node.textContent || '').trim();
      if (node.classList && node.classList.contains('race-card')) return '📄 Blog: ' + (node.querySelector('h3')?.textContent || '').trim().substring(0, 40);
      if (node.classList && node.classList.contains('faq__question')) return '❓ FAQ: ' + (node.textContent || '').trim().substring(0, 40);
      if (node.tagName === 'A' && node.href) return '🔗 Link: ' + (node.textContent || '').trim().substring(0, 40);
      node = node.parentElement;
    }
    return null;
  }

  // =============================================
  // EVENT HANDLERS
  // =============================================

  // Track page view
  sendHit('pageview', {
    page: window.location.pathname || '/',
    device: getDevice(),
    source: getSource()
  });

  // Track clicks
  document.addEventListener('click', function(e) {
    var link = e.target.closest ? e.target.closest('a') : null;

    // Phone call
    if (link && link.href && link.href.startsWith('tel:')) {
      sendHit('call', {});
      return;
    }

    // Text message
    if (link && link.href && link.href.startsWith('sms:')) {
      sendHit('text', {});
      return;
    }

    // General click
    var label = getClickLabel(e.target);
    if (label) {
      sendHit('click', { label: label });
    }
  }, true);

  // =============================================
  // LEAD FORM HANDLER
  // =============================================
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

    // Save lead
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

    // Count it
    sendHit('lead', {});

    // Success message
    form.innerHTML = '<div style="text-align:center;padding:2rem;">' +
      '<p style="font-size:1.5rem;margin-bottom:0.5rem;">✅ Thank You!</p>' +
      '<p>We\'ll call you shortly at <strong>' + phone + '</strong></p>' +
      '<p style="margin-top:1rem;"><a href="tel:+14233835373" class="btn btn--call">' +
      '<span class="btn__icon">📞</span> Call Us Now: (423) 383-5373</a></p></div>';
    return false;
  };

})();
