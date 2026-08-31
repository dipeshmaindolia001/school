# -*- coding: utf-8 -*-
import os

def get_head(title, desc):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@500;600;700;800&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css">
</head>
<body>"""

def get_nav(active):
    return f"""
<div class="top-bar">
  <span>📍 Built for Schools &amp; Colleges in <strong>Ramnagar · Kashipur · Haldwani · Rudrapur · Kumaon</strong> | Admissions 2026-27 Surge Campaign Live! <a href="contact.html">Get Free School Audit →</a></span>
</div>
<header id="siteHeader">
  <nav class="wrap">
    <a href="index.html" class="brand">
      <span class="brand-mark">C</span>Chalkframe<span class="brand-tag">Education</span>
    </a>
    <div class="nav-links">
      <a href="index.html" class="{'active' if active=='home' else ''}">Home</a>
      <a href="services.html" class="{'active' if active=='services' else ''}">Services</a>
      <a href="portfolio.html" class="{'active' if active=='portfolio' else ''}">Live Reels &amp; Work</a>
      <a href="pricing.html" class="{'active' if active=='pricing' else ''}">Pricing (₹10k/mo)</a>
      <a href="how-it-works.html" class="{'active' if active=='process' else ''}">How It Works</a>
      <a href="about.html" class="{'active' if active=='about' else ''}">About</a>
      <a href="contact.html" class="{'active' if active=='contact' else ''}">Contact</a>
    </div>
    <div class="nav-right">
      <a href="contact.html" class="btn btn-primary btn-sm">Get Free Audit</a>
      <button class="menu-btn" id="menuBtn" aria-label="Toggle navigation menu" aria-expanded="false">
        <span class="hamburger-icon"></span>
      </button>
    </div>
  </nav>
</header>

<!-- MOBILE NAVIGATION DRAWER (FULL-SCREEN, HIGH-CONTRAST & TOUCH-FRIENDLY) -->
<div class="mobile-drawer" id="mobileMenu" aria-hidden="true">
  <div class="mobile-drawer-header">
    <a href="index.html" class="brand">
      <span class="brand-mark">C</span>Chalkframe
    </a>
    <button class="close-menu-btn" id="closeMenuBtn" aria-label="Close navigation menu">
      ✕ Close
    </button>
  </div>
  <div class="mobile-drawer-content">
    <div class="mobile-drawer-links">
      <a href="index.html" class="mobile-nav-link {'active' if active=='home' else ''}">
        <span class="nav-icon">🏠</span>
        <div class="nav-link-text">
          <div class="nav-link-title">Home</div>
          <div class="nav-link-sub">Overview, before-after &amp; highlights</div>
        </div>
      </a>
      <a href="services.html" class="mobile-nav-link {'active' if active=='services' else ''}">
        <span class="nav-icon">⚡</span>
        <div class="nav-link-text">
          <div class="nav-link-title">All Services</div>
          <div class="nav-link-sub">Social media, reels, graphics &amp; websites</div>
        </div>
      </a>
      <a href="portfolio.html" class="mobile-nav-link {'active' if active=='portfolio' else ''}">
        <span class="nav-icon">🎬</span>
        <div class="nav-link-text">
          <div class="nav-link-title">Live Reels &amp; Work</div>
          <div class="nav-link-sub">Interactive playable video reels &amp; posters</div>
        </div>
      </a>
      <a href="pricing.html" class="mobile-nav-link {'active' if active=='pricing' else ''}">
        <span class="nav-icon">💰</span>
        <div class="nav-link-text">
          <div class="nav-link-title">Pricing Plans</div>
          <div class="nav-link-sub">₹10k Social Media · ₹15k Website · ₹3k Maint.</div>
        </div>
      </a>
      <a href="how-it-works.html" class="mobile-nav-link {'active' if active=='process' else ''}">
        <span class="nav-icon">🔄</span>
        <div class="nav-link-text">
          <div class="nav-link-title">How It Works</div>
          <div class="nav-link-sub">Simple WhatsApp workflow &amp; turnaround SLAs</div>
        </div>
      </a>
      <a href="about.html" class="mobile-nav-link {'active' if active=='about' else ''}">
        <span class="nav-icon">🏫</span>
        <div class="nav-link-text">
          <div class="nav-link-title">About Chalkframe</div>
          <div class="nav-link-sub">Our mission for Kumaon &amp; Indian schools</div>
        </div>
      </a>
      <a href="contact.html" class="mobile-nav-link {'active' if active=='contact' else ''}">
        <span class="nav-icon">📞</span>
        <div class="nav-link-text">
          <div class="nav-link-title">Contact &amp; Free Audit</div>
          <div class="nav-link-sub">Get your 5-point school digital report</div>
        </div>
      </a>
    </div>

    <div class="mobile-drawer-cta">
      <a href="contact.html" class="btn btn-primary btn-lg" style="width: 100%; margin-bottom: 10px;">
        ⚡ Get Free School Audit
      </a>
      <a href="https://wa.me/919876543210?text=Hello%20Chalkframe,%20we%20want%20to%20know%20about%20your%20school%20social%20media%20and%20website%20services." class="btn btn-whatsapp btn-lg" target="_blank" rel="noopener" style="width: 100%;">
        💬 Chat on WhatsApp
      </a>
    </div>
  </div>
</div>
"""

def get_footer():
    return """
<footer>
  <div class="wrap">
    <div class="footer-grid">
      <div class="footer-col">
        <a href="index.html" class="brand" style="margin-bottom: 14px;">
          <span class="brand-mark">C</span>Chalkframe
        </a>
        <p style="font-size: 14px; color: var(--ink-soft); line-height: 1.6; margin-top: 10px;">
          The dedicated remote digital team for schools, colleges, and coaching institutes in Ramnagar, Kashipur, Haldwani, Rudrapur, and across Uttarakhand.
        </p>
        <p style="font-size: 13.5px; font-weight: 700; color: var(--pine); margin-top: 12px;">
          WhatsApp: +91 98765 43210 | info@chalkframe.com
        </p>
      </div>

      <div class="footer-col">
        <h4>Quick Navigation</h4>
        <ul class="footer-links-list">
          <li><a href="index.html">Home</a></li>
          <li><a href="services.html">All Services</a></li>
          <li><a href="portfolio.html">Live Reels &amp; Work</a></li>
          <li><a href="pricing.html">Pricing Plans (₹10k)</a></li>
          <li><a href="how-it-works.html">How It Works</a></li>
          <li><a href="about.html">About Chalkframe</a></li>
          <li><a href="contact.html">Get Free Audit</a></li>
        </ul>
      </div>

      <div class="footer-col">
        <h4>Our Core Services</h4>
        <ul class="footer-links-list">
          <li><a href="services.html#social">Social Media (₹10k/mo)</a></li>
          <li><a href="services.html#reels">Reel &amp; Video Editing</a></li>
          <li><a href="services.html#graphics">Admissions Graphics</a></li>
          <li><a href="services.html#website">Website Building (₹15k)</a></li>
          <li><a href="services.html#maintenance">Website Upkeep (₹3k/mo)</a></li>
        </ul>
      </div>

      <div class="footer-col">
        <h4>Target Region Focus</h4>
        <ul class="footer-links-list">
          <li><span style="font-size: 13.5px; color: var(--ink-soft);">📍 Haldwani &amp; Kathgodam</span></li>
          <li><span style="font-size: 13.5px; color: var(--ink-soft);">📍 Kashipur Industrial Hub</span></li>
          <li><span style="font-size: 13.5px; color: var(--ink-soft);">📍 Ramnagar &amp; Corbett Belt</span></li>
          <li><span style="font-size: 13.5px; color: var(--ink-soft);">📍 Rudrapur &amp; Pantnagar</span></li>
          <li><span style="font-size: 13.5px; color: var(--ink-soft);">📍 Nainital &amp; Bhimtal</span></li>
        </ul>
      </div>
    </div>

    <div class="footer-bottom">
      <div>© 2026 Chalkframe. All rights reserved. Designed for Indian Educational Institutions.</div>
      <div>Zero In-House Hiring. WhatsApp Workflow. 100% Guaranteed Reliability.</div>
    </div>
  </div>
</footer>

<div class="sticky-wa-bar">
  <a href="https://wa.me/919876543210?text=Hello%20Chalkframe,%20we%20want%20to%20know%20about%20your%20school%20social%20media%20and%20website%20services." class="btn btn-whatsapp btn-sm" target="_blank" rel="noopener">
    💬 WhatsApp Enquiry
  </a>
  <a href="contact.html" class="btn btn-primary btn-sm">
    ⚡ Free School Audit
  </a>
</div>

<script src="js/main.js"></script>
</body>
</html>"""

with open("gen_base.py", "w", encoding="utf-8") as f:
    f.write(f'''# Updated base template with full-screen mobile drawer
import os

def get_head(title, desc):
    return """{get_head("{title}", "{desc}")}"""

def get_nav(active):
    pass
''')

print("Generating all 7 pages with high-contrast mobile drawer...")
