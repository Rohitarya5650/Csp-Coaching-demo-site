(function () {
  "use strict";
  var C = window.CSP_CONFIG || {};
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  function store(k, v) { try { if (v === undefined) return sessionStorage.getItem(k); sessionStorage.setItem(k, v); } catch (e) {} }

  /* Header shadow */
  var header = $("#site-header");
  function onScroll() { header.classList.toggle("shadow-card", window.scrollY > 8); header.classList.toggle("border-royal-100", window.scrollY > 8); }
  onScroll(); window.addEventListener("scroll", onScroll, { passive: true });

  /* Mobile drawer */
  var drawer = $("#drawer"), overlay = $("#overlay"), openBtn = $("#menu-open");
  function drawerSet(open) {
    drawer.classList.toggle("is-open", open); overlay.classList.toggle("is-open", open);
    openBtn.setAttribute("aria-expanded", open); document.body.style.overflow = open ? "hidden" : "";
    if (open) $("#menu-close").focus(); else if (document.activeElement && drawer.contains(document.activeElement)) openBtn.focus();
  }
  openBtn.addEventListener("click", function () { drawerSet(true); });
  $("#menu-close").addEventListener("click", function () { drawerSet(false); });
  overlay.addEventListener("click", function () { drawerSet(false); });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape") drawerSet(false); });
  window.matchMedia("(min-width:1024px)").addEventListener("change", function (m) { if (m.matches) drawerSet(false); });
  $$("[data-lead]", drawer).forEach(function (b) { b.addEventListener("click", function () { drawerSet(false); }); });

  /* Page transition */
  document.addEventListener("click", function (e) {
    var a = e.target.closest("a[href]");
    if (!a || a.target || a.hasAttribute("download") || e.metaKey || e.ctrlKey || e.shiftKey) return;
    var u = new URL(a.href, location.href);
    if (u.origin !== location.origin || u.pathname === location.pathname || !/\.html$|\/$/.test(u.pathname)) return;
    e.preventDefault(); document.body.classList.add("is-leaving");
    setTimeout(function () { location.href = a.href; }, reduce ? 0 : 170);
  });
  window.addEventListener("pageshow", function () { document.body.classList.remove("is-leaving"); });

  /* Scroll reveal + counters */
  if ("IntersectionObserver" in window) {
    var rv = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add("is-in"); rv.unobserve(e.target); } }); }, { threshold: 0.1, rootMargin: "0px 0px -30px 0px" });
    $$(".reveal").forEach(function (el) { rv.observe(el); });
    var co = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (!e.isIntersecting) return; co.unobserve(e.target); if (reduce) return;
        var el = e.target, end = +el.dataset.count, suf = el.dataset.suffix || "", t0 = performance.now();
        (function tick(t) { var p = Math.min((t - t0) / 1400, 1); el.textContent = Math.round(end * (1 - Math.pow(1 - p, 3))) + suf; if (p < 1) requestAnimationFrame(tick); })(t0);
      });
    }, { threshold: 0.6 });
    $$("[data-count]").forEach(function (el) { co.observe(el); });
  } else { $$(".reveal").forEach(function (el) { el.classList.add("is-in"); }); }

  /* Sliders (scroll-snap tracks with buttons, dots and optional autoplay) */
  $$("[data-slider]").forEach(function (s) {
    var track = $("[data-slider-track]", s), prev = $("[data-slider-prev]", s), next = $("[data-slider-next]", s);
    var single = s.hasAttribute("data-single"), auto = s.hasAttribute("data-autoplay"), dotsBox = $("[data-dots]", s), timer, dots = [];
    function step() { var c = track.children[0]; return c ? c.getBoundingClientRect().width + (single ? 0 : parseFloat(getComputedStyle(c).marginRight) || 0) : 300; }
    function atEnd() { return track.scrollLeft + track.clientWidth >= track.scrollWidth - 4; }
    function go(dir) {
      if (dir > 0 && atEnd()) track.scrollTo({ left: 0 }); else if (dir < 0 && track.scrollLeft <= 2) track.scrollTo({ left: track.scrollWidth }); else track.scrollBy({ left: dir * step() });
    }
    if (prev) prev.addEventListener("click", function () { go(-1); });
    if (next) next.addEventListener("click", function () { go(1); });
    if (dotsBox && single) {
      $$(":scope > *", track).forEach(function (_, i) {
        var d = document.createElement("button"); d.type = "button"; d.setAttribute("aria-label", "Go to photo " + (i + 1));
        d.className = "w-2.5 h-2.5 rounded-full bg-white/60 transition-all"; d.addEventListener("click", function () { track.scrollTo({ left: i * step() }); });
        dotsBox.appendChild(d); dots.push(d);
      });
      var upd = function () { var i = Math.round(track.scrollLeft / step()); dots.forEach(function (d, k) { d.classList.toggle("bg-sun", k === i); d.classList.toggle("w-6", k === i); }); };
      track.addEventListener("scroll", upd, { passive: true }); upd();
    }
    if (auto && !reduce) {
      var start = function () { stop(); timer = setInterval(function () { go(1); }, 4500); }, stop = function () { clearInterval(timer); };
      s.addEventListener("mouseenter", stop); s.addEventListener("mouseleave", start); s.addEventListener("focusin", stop); s.addEventListener("focusout", start);
      document.addEventListener("visibilitychange", function () { document.hidden ? stop() : start(); });
      start();
    }
  });

  /* Filters */
  $$("[data-filters]").forEach(function (box) {
    var target = $(box.dataset.target), chips = $$("[data-filter]", box);
    function apply(k) {
      chips.forEach(function (c) { c.setAttribute("aria-pressed", c.dataset.filter === k); });
      $$("[data-filter-item]", target).forEach(function (it) { it.hidden = !(k === "all" || it.dataset.cat === k); });
    }
    chips.forEach(function (c) { c.addEventListener("click", function () { apply(c.dataset.filter); }); });
    var h = location.hash.slice(1); if (h && chips.some(function (c) { return c.dataset.filter === h; })) apply(h);
  });

  /* Tabs (journey stepper) */
  $$("[data-tabs]").forEach(function (box) {
    var tabs = $$("[role=tab]", box);
    function sel(t) { tabs.forEach(function (x) { var on = x === t; x.setAttribute("aria-selected", on); x.tabIndex = on ? 0 : -1; document.getElementById(x.getAttribute("aria-controls")).hidden = !on; }); }
    tabs.forEach(function (t, i) {
      t.addEventListener("click", function () { sel(t); });
      t.addEventListener("keydown", function (e) {
        var n = e.key === "ArrowDown" || e.key === "ArrowRight" ? 1 : e.key === "ArrowUp" || e.key === "ArrowLeft" ? -1 : 0;
        if (n) { e.preventDefault(); var x = tabs[(i + n + tabs.length) % tabs.length]; sel(x); x.focus(); }
      });
    });
  });

  /* Dialogs */
  function open(d) { if (d.open) return; if (d.showModal) d.showModal(); else d.setAttribute("open", ""); }
  $$("dialog").forEach(function (d) {
    d.addEventListener("click", function (e) { if (e.target === d || e.target.closest("[data-close]") || (e.target.parentElement === d && !e.target.closest("figure,button,img"))) d.close(); });
  });
  var lead = $("#lead-dlg"), leadForm = $("#lead-form"), anyOpen = function () { return $$("dialog").some(function (d) { return d.open; }); };
  function openLead(o) {
    $("#lead-title").textContent = o.title || "Quick Inquiry"; leadForm.dataset.source = o.source || "popup";
    if (o.course) leadForm.elements.course.value = o.course; else leadForm.elements.course.value = "";
    $(".form-status", leadForm).textContent = ""; open(lead);
    setTimeout(function () { leadForm.elements.name.focus(); }, 60);
  }
  document.addEventListener("click", function (e) {
    var b = e.target.closest("[data-lead]"); if (b) { e.preventDefault(); openLead({ title: b.dataset.title, course: b.dataset.course, source: b.dataset.source }); }
  });
  /* Auto popup: after 10 s or on exit intent, once per visit, never on the contact page */
  if (!/contact\.html$/.test(location.pathname)) {
    var fired = function () { return store("csp_popup") === "1"; };
    var pop = function (src) { if (fired() || anyOpen()) return; store("csp_popup", "1"); openLead({ title: "Book a Free Demo Class", source: src }); };
    setTimeout(function () { pop("auto-10s"); }, 10000);
    document.addEventListener("mouseout", function (e) { if (!e.relatedTarget && e.clientY <= 0 && window.innerWidth > 900) pop("exit-intent"); });
  }

  /* Faculty modal */
  var fd = $("#fac-dlg"), fb = $("#fac-body");
  $$("[data-faculty]").forEach(function (b) {
    b.addEventListener("click", function () { fb.innerHTML = ""; fb.appendChild(document.getElementById("fac-" + b.dataset.faculty).content.cloneNode(true)); open(fd); });
  });

  /* Lightbox */
  var lb = $("#lb"), items = [], idx = 0;
  function showLb(i) {
    idx = (i + items.length) % items.length; var it = items[idx];
    $("#lb-img").src = it.dataset.src; $("#lb-img").alt = it.dataset.caption; $("#lb-cap").textContent = it.dataset.caption + "  ·  " + (idx + 1) + " / " + items.length;
  }
  $$("[data-lightbox]").forEach(function (b) {
    b.addEventListener("click", function () { items = $$("[data-lightbox]").filter(function (x) { return !x.hidden; }); showLb(items.indexOf(b)); open(lb); });
  });
  if (lb) {
    $("#lb-prev").addEventListener("click", function () { showLb(idx - 1); });
    $("#lb-next").addEventListener("click", function () { showLb(idx + 1); });
    lb.addEventListener("keydown", function (e) { if (e.key === "ArrowLeft") showLb(idx - 1); if (e.key === "ArrowRight") showLb(idx + 1); });
  }

  /* Forms */
  function cleanPhone(v) { return v.replace(/[\s\-]/g, "").replace(/^(\+91|91|0)/, ""); }
  function sb(table, row) {
    return fetch(C.supabaseUrl.replace(/\/$/, "") + "/rest/v1/" + table, {
      method: "POST", headers: { "Content-Type": "application/json", apikey: C.supabaseAnonKey, Authorization: "Bearer " + C.supabaseAnonKey, Prefer: "return=minimal" }, body: JSON.stringify(row)
    }).then(function (r) { if (!r.ok) throw new Error("HTTP " + r.status); });
  }
  var hasSb = function () { return !!(C.supabaseUrl && C.supabaseAnonKey); };
  function waOpen(text) { window.open("https://wa.me/" + C.whatsapp + "?text=" + encodeURIComponent(text), "_blank", "noopener"); }

  $$(".lead-form").forEach(function (f) {
    var status = $(".form-status", f);
    f.addEventListener("submit", function (e) {
      e.preventDefault();
      var ok = true, name = f.elements.name.value.trim(), phone = cleanPhone(f.elements.phone.value);
      function flag(el, bad) { el.closest(".field").classList.toggle("is-bad", bad); if (bad) ok = false; }
      flag(f.elements.name, name.length < 2); flag(f.elements.phone, !/^[6-9]\d{9}$/.test(phone));
      if (!ok) { status.textContent = "Please fix the highlighted fields."; (f.querySelector(".is-bad input") || {}).focus && f.querySelector(".is-bad input").focus(); return; }
      var row = { name: name, phone: phone, course: f.elements.course.value, target_year: f.elements.target_year.value, message: f.elements.message.value.trim(), source: f.dataset.source || f.id };
      var text = "Hello CSP Coaching,\nName: " + row.name + "\nPhone: " + row.phone + (row.course ? "\nCourse: " + row.course : "") + (row.target_year ? "\nTarget year: " + row.target_year : "") + (row.message ? "\nMessage: " + row.message : "");
      var btn = f.querySelector("[type=submit]"); btn.disabled = true;
      if (hasSb()) {
        status.textContent = "Sending...";
        sb(C.inquiriesTable, row).then(function () { status.textContent = "Thank you, " + name + "! We have received your enquiry and will contact you soon."; f.reset(); setTimeout(function () { if (lead.open) lead.close(); }, 2500); })
          .catch(function () { status.innerHTML = "We could not save your enquiry. Please use WhatsApp instead."; waOpen(text); }).then(function () { btn.disabled = false; });
      } else { waOpen(text); status.textContent = "WhatsApp opened with your details. Tap send there to reach us."; btn.disabled = false; }
    });
    $$("input,select,textarea", f).forEach(function (i) { i.addEventListener("input", function () { i.closest(".field").classList.remove("is-bad"); }); });
  });

  var nf = $("#news-form");
  if (nf) nf.addEventListener("submit", function (e) {
    e.preventDefault(); var em = $("#news-email").value.trim(), msg = $("#news-msg");
    if (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(em)) { msg.textContent = "Please enter a valid email."; return; }
    if (hasSb()) sb(C.subscribersTable, { email: em }).then(function () { msg.textContent = "Subscribed. Thank you!"; nf.reset(); }).catch(function () { msg.textContent = "Could not subscribe right now. Please try again."; });
    else { location.href = "mailto:" + C.email + "?subject=" + encodeURIComponent("Subscribe me to CSP Coaching updates") + "&body=" + encodeURIComponent("Please add " + em + " to your updates list."); msg.textContent = "Your email app opened. Press send to subscribe."; }
  });
})();
