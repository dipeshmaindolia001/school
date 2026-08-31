document.addEventListener("DOMContentLoaded", () => {
  // 1. Mobile Menu Toggle & Full-Screen Drawer
  const menuBtn = document.getElementById("menuBtn");
  const closeMenuBtn = document.getElementById("closeMenuBtn");
  const mobileMenu = document.getElementById("mobileMenu");

  const openDrawer = () => {
    if (mobileMenu) {
      mobileMenu.classList.add("open");
      mobileMenu.setAttribute("aria-hidden", "false");
      if (menuBtn) menuBtn.setAttribute("aria-expanded", "true");
      document.body.style.overflow = "hidden";
    }
  };

  const closeDrawer = () => {
    if (mobileMenu) {
      mobileMenu.classList.remove("open");
      mobileMenu.setAttribute("aria-hidden", "true");
      if (menuBtn) menuBtn.setAttribute("aria-expanded", "false");
      document.body.style.overflow = "";
    }
  };

  if (menuBtn) {
    menuBtn.addEventListener("click", (e) => {
      e.stopPropagation();
      if (mobileMenu && mobileMenu.classList.contains("open")) {
        closeDrawer();
      } else {
        openDrawer();
      }
    });
  }

  if (closeMenuBtn) {
    closeMenuBtn.addEventListener("click", (e) => {
      e.stopPropagation();
      closeDrawer();
    });
  }

  if (mobileMenu) {
    mobileMenu.querySelectorAll("a").forEach(link => {
      link.addEventListener("click", () => {
        closeDrawer();
      });
    });
  }

  // 2. Intersection Observer for Smooth Scroll Reveals
  const revealElements = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add("in");
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.05, rootMargin: "0px 0px -20px 0px" });
    revealElements.forEach(el => observer.observe(el));
  } else {
    revealElements.forEach(el => el.classList.add("in"));
  }

  // 3. Mobile & Desktop Reels & Video Player Controls
  const reelCards = document.querySelectorAll(".reel-phone-frame");
  reelCards.forEach(card => {
    const video = card.querySelector("video");
    const centerPlay = card.querySelector(".reel-center-play");
    const soundBtn = card.querySelector(".reel-sound-icon");
    const likeBtn = card.querySelector(".like-btn");
    const likeCount = card.querySelector(".like-count");

    if (video) {
      video.setAttribute("playsinline", "");
      video.setAttribute("webkit-playsinline", "");

      const togglePlay = (e) => {
        if (e) e.stopPropagation();
        if (video.paused) {
          document.querySelectorAll(".reel-phone-frame video").forEach(v => {
            if (v !== video) {
              v.pause();
              const pCard = v.closest(".reel-phone-frame");
              if (pCard) {
                const btn = pCard.querySelector(".reel-center-play");
                if (btn) {
                  btn.style.opacity = "1";
                  btn.innerHTML = `<svg width="22" height="22" viewBox="0 0 24 24" fill="white"><path d="M8 5v14l11-7z"/></svg>`;
                }
              }
            }
          });

          video.play().then(() => {
            if (centerPlay) {
              centerPlay.style.opacity = "0";
              centerPlay.innerHTML = `<svg width="22" height="22" viewBox="0 0 24 24" fill="white"><path d="M6 19h4V5H6v14zm8-14v14h4V5h-4z"/></svg>`;
            }
          }).catch(err => console.log("Playback prevented", err));
        } else {
          video.pause();
          if (centerPlay) {
            centerPlay.style.opacity = "1";
            centerPlay.innerHTML = `<svg width="22" height="22" viewBox="0 0 24 24" fill="white"><path d="M8 5v14l11-7z"/></svg>`;
          }
        }
      };

      if (centerPlay) {
        centerPlay.addEventListener("click", togglePlay);
        centerPlay.addEventListener("touchend", (e) => {
          e.preventDefault();
          togglePlay(e);
        });
      }

      const screen = card.querySelector(".reel-screen");
      if (screen) {
        screen.addEventListener("click", togglePlay);
      }

      if (soundBtn) {
        const toggleSound = (e) => {
          if (e) e.stopPropagation();
          video.muted = !video.muted;
          soundBtn.innerHTML = video.muted
            ? `<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M11 5L6 9H2v6h4l5 4V5z"/><line x1="23" y1="9" x2="17" y2="15"/><line x1="17" y1="9" x2="23" y2="15"/></svg>`
            : `<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07"/></svg>`;
        };
        soundBtn.addEventListener("click", toggleSound);
        soundBtn.addEventListener("touchend", (e) => {
          e.preventDefault();
          toggleSound(e);
        });
      }

      if (likeBtn && likeCount) {
        likeBtn.addEventListener("click", (e) => {
          e.stopPropagation();
          likeBtn.classList.toggle("liked");
          let count = parseInt(likeCount.innerText.replace(/[^0-9]/g, '')) || 480;
          if (likeBtn.classList.contains("liked")) {
            likeBtn.style.color = "#FF3366";
            likeCount.innerText = (count + 1).toLocaleString() + (likeCount.innerText.includes('k') ? 'k' : '');
          } else {
            likeBtn.style.color = "#fff";
            likeCount.innerText = (count - 1).toLocaleString() + (likeCount.innerText.includes('k') ? 'k' : '');
          }
        });
      }
    }
  });

  // 4. Portfolio Filter Buttons
  const filterBtns = document.querySelectorAll(".filter-btn");
  const portfolioItems = document.querySelectorAll("[data-cat]");
  if (filterBtns.length > 0) {
    filterBtns.forEach(btn => {
      btn.addEventListener("click", () => {
        filterBtns.forEach(b => b.classList.remove("active"));
        btn.classList.add("active");
        const filter = btn.dataset.filter;
        portfolioItems.forEach(item => {
          if (filter === "all" || item.dataset.cat === filter || item.dataset.cat.includes(filter)) {
            item.style.display = "";
          } else {
            item.style.display = "none";
          }
        });
      });
    });
  }

  // 5. FAQ Accordions
  const faqItems = document.querySelectorAll(".faq-item");
  faqItems.forEach(item => {
    const questionBtn = item.querySelector(".faq-q");
    const answer = item.querySelector(".faq-a");
    if (questionBtn && answer) {
      questionBtn.addEventListener("click", () => {
        const isOpen = item.classList.contains("open");
        faqItems.forEach(other => {
          other.classList.remove("open");
          const otherAns = other.querySelector(".faq-a");
          if (otherAns) otherAns.style.maxHeight = null;
        });

        if (!isOpen) {
          item.classList.add("open");
          answer.style.maxHeight = answer.scrollHeight + "px";
        }
      });
    }
  });

  // 6. Interactive Service Selection Pills in Form
  const servicePills = document.querySelectorAll(".service-pill");
  servicePills.forEach(pill => {
    pill.addEventListener("click", () => {
      pill.classList.toggle("active");
    });
  });

  // 7. Form Submit Feedback & WhatsApp Redirect Helper
  const auditForms = document.querySelectorAll("form.audit-form");
  auditForms.forEach(form => {
    form.addEventListener("submit", (e) => {
      e.preventDefault();
      const schoolName = form.querySelector("#f-inst, #instName")?.value || "Our School";
      const city = form.querySelector("#f-city, #city")?.value || "Haldwani/Kashipur/Ramnagar";
      const phone = form.querySelector("#f-phone, #phone")?.value || "";
      
      const selectedServices = Array.from(form.querySelectorAll(".service-pill.active"))
        .map(p => p.textContent.trim())
        .join(", ");

      const submitBtn = form.querySelector("button[type=submit]");
      if (submitBtn) {
        submitBtn.disabled = true;
        submitBtn.innerHTML = "Sending Audit Request...";
      }

      setTimeout(() => {
        if (submitBtn) {
          submitBtn.innerHTML = "Audit Request Sent! Opening WhatsApp...";
          submitBtn.style.background = "#25D366";
        }
        
        const waMsg = encodeURIComponent(`Hello Chalkframe Team! I want a Free Digital Audit for *${schoolName}* (${city}). Services of interest: ${selectedServices || 'Social Media, Reels & Website'}. Contact: ${phone}`);
        window.open(`https://wa.me/919876543210?text=${waMsg}`, '_blank');
      }, 800);
    });
  });
});
