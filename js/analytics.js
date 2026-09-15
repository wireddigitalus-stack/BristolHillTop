/**
 * Bristol Hilltop Camping — Telemetry Counter
 * Posts all events to Supabase + localStorage fallback
 */
(function() {
  'use strict';

  // =============================================
  // SUPABASE CONFIG
  // =============================================
  var SUPABASE_URL = 'https://ypawnqzphvwqinofcsod.supabase.co';
  var SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InlwYXducXpwaHZ3cWlub2Zjc29kIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODk0NjAxNTUsImV4cCI6MjEwNTAzNjE1NX0.B_vZ5u5-T6CGnZVyZO7dhdH_Gm1FHXK_iDMUO9R40gk';

  // =============================================
  // SEND HIT → Supabase
  // =============================================
  function sendHit(type, data) {
    var row = {
      type: type,
      page: data.page || null,
      device: data.device || null,
      source: data.source || null,
      label: data.label || null
    };

    // POST to Supabase
    fetch(SUPABASE_URL + '/rest/v1/hits', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'apikey': SUPABASE_KEY,
        'Authorization': 'Bearer ' + SUPABASE_KEY,
        'Prefer': 'return=minimal'
      },
      body: JSON.stringify(row)
    }).catch(function() {});
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
      if (node.href && node.href.startsWith('tel:')) return null;
      if (node.href && node.href.startsWith('sms:')) return null;
      if (node.classList && node.classList.contains('btn--call')) return '📞 Call Button';
      if (node.classList && node.classList.contains('btn--outline')) return '🔗 ' + (node.textContent || '').trim().substring(0, 40);
      if (node.classList && node.classList.contains('nav__link')) return '📍 Nav: ' + (node.textContent || '').trim();
      if (node.classList && node.classList.contains('race-card')) return '📄 Blog: ' + ((node.querySelector('h3') || {}).textContent || '').trim().substring(0, 40);
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

    if (link && link.href && link.href.startsWith('tel:')) {
      sendHit('call', { page: window.location.pathname });
      return;
    }

    if (link && link.href && link.href.startsWith('sms:')) {
      sendHit('text', { page: window.location.pathname });
      return;
    }

    var label = getClickLabel(e.target);
    if (label) {
      sendHit('click', { label: label, page: window.location.pathname });
    }
  }, true);

  // =============================================
  // LEAD FORM → Supabase
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

    // POST lead to Supabase
    fetch(SUPABASE_URL + '/rest/v1/leads', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'apikey': SUPABASE_KEY,
        'Authorization': 'Bearer ' + SUPABASE_KEY,
        'Prefer': 'return=minimal'
      },
      body: JSON.stringify({
        name: name,
        phone: phone,
        email: email || null,
        interest: interest,
        message: message || null
      })
    }).catch(function() {});

    // Also count as a hit
    sendHit('lead', { page: window.location.pathname });

    // Success message
    form.innerHTML = '<div style="text-align:center;padding:2rem;">' +
      '<p style="font-size:1.5rem;margin-bottom:0.5rem;">✅ Thank You!</p>' +
      '<p>We\'ll call you shortly at <strong>' + phone + '</strong></p>' +
      '<p style="margin-top:1rem;"><a href="tel:+14233835373" class="btn btn--call">' +
      '<span class="btn__icon">📞</span> Call Us Now: (423) 383-5373</a></p></div>';
    return false;
  };

})();
