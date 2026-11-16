# Shared data + layout for the CSP Coaching multi-page site. Every fact below comes from the original site files.
import html, json, urllib.parse
E = html.escape

PHONE_DISPLAY = "+91 98288 25247"
PHONE_TEL = "+919828825247"
WA = "919828825247"
EMAIL = "cspcoaching@gmail.com"
MAP = "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2657.953474803783!2d74.85057937393171!3d27.153101649721435!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x396b79001c9140a3%3A0xbd70103d4a95ee13!2z4KS44KWA4KSP4KS44KSq4KWAIOCkleCli-CkmuCkv-CkguCklw!5e1!3m2!1shi!2sin!4v1766834222606!5m2!1shi!2sin"

SPRITE = {
 "star": '<path d="M12 2.5l2.9 6.1 6.6.8-4.9 4.6 1.3 6.6L12 17.3 6.1 20.6l1.3-6.6L2.5 9.4l6.6-.8z"/>',
 "shield": '<path d="M12 2.5l8 3v6c0 5-3.4 8.6-8 10-4.6-1.4-8-5-8-10v-6z"/>',
 "badge": '<path d="M12 2.5l8 3v6c0 5-3.4 8.6-8 10-4.6-1.4-8-5-8-10v-6z"/><path d="M8.5 12l2.5 2.5 4.5-5"/>',
 "train": '<rect x="5" y="3" width="14" height="14" rx="3"/><path d="M5 11h14M9 21l2-4M15 21l-2-4"/><circle cx="9" cy="14" r=".6"/><circle cx="15" cy="14" r=".6"/>',
 "clip": '<rect x="5" y="4" width="14" height="17" rx="2"/><path d="M9 4V3h6v1M8.5 11h7M8.5 15h5"/>',
 "dumbbell": '<path d="M6 7v10M3 9.5v5M18 7v10M21 9.5v5M6 12h12"/>',
 "book": '<path d="M2.5 4.5h6.5a3 3 0 013 3v12.5a2 2 0 00-2-2H2.5zM21.5 4.5H15a3 3 0 00-3 3v12.5a2 2 0 012-2h7.5z"/>',
 "cap": '<path d="M2 9l10-5 10 5-10 5zM6 11.5V16c0 1.5 3 3 6 3s6-1.5 6-3v-4.5"/>',
 "users": '<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20c0-3.6 2.9-6 6.5-6s6.5 2.4 6.5 6M16 4.8a3.5 3.5 0 010 6.4M18 14.4c2.2.7 3.5 2.6 3.5 5.6"/>',
 "check-circle": '<circle cx="12" cy="12" r="9"/><path d="M8 12.2l2.7 2.7L16 9.5"/>',
 "home": '<path d="M3 11l9-7.5 9 7.5M5 9.5V21h14V9.5M10 21v-6h4v6"/>',
 "phone": '<path d="M5 4h4l2 5-2.5 1.5a11 11 0 005 5L15 13l5 2v4a2 2 0 01-2 2A16 16 0 013 6a2 2 0 012-2z"/>',
 "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>',
 "pin": '<path d="M12 21s7-6.2 7-11.5A7 7 0 005 9.5C5 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/>',
 "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
 "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
 "left": '<path d="M15 5l-7 7 7 7"/>', "right": '<path d="M9 5l7 7-7 7"/>',
 "menu": '<path d="M4 7h16M4 12h16M4 17h16"/>', "x": '<path d="M6 6l12 12M18 6L6 18"/>',
 "check": '<path d="M5 12.5l4.5 4.5L19 7.5"/>',
 "bed": '<path d="M3 19V6M3 15h18v4M21 15v-3a3 3 0 00-3-3h-7v6"/><circle cx="7" cy="11.5" r="1.7"/>',
 "lock": '<rect x="5" y="11" width="14" height="9" rx="2"/><path d="M8 11V8a4 4 0 018 0v3"/>',
 "laptop": '<rect x="4" y="5" width="16" height="11" rx="2"/><path d="M2 20h20"/>',
 "test": '<path d="M9 3h6M10 3v6L5 19a1.5 1.5 0 001.4 2h11.2A1.5 1.5 0 0019 19l-5-10V3"/><path d="M7.5 15h9"/>',
 "room": '<rect x="3" y="4" width="18" height="12" rx="1.5"/><path d="M8 20h8M12 16v4"/>',
 "download": '<path d="M12 3v12M7 10l5 5 5-5M4 20h16"/>',
 "trophy": '<path d="M7 4h10v5a5 5 0 01-10 0zM7 6H4v1a3 3 0 003 3M17 6h3v1a3 3 0 01-3 3M12 14v4M8 21h8M9.5 18h5"/>',
 "target": '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1.2"/>',
 "chat": '<path d="M4 5h16v11H9l-5 4z"/>',
 "bolt": '<path d="M13 2L4 14h7l-1 8 9-12h-7z"/>',
 "expand": '<path d="M4 9V4h5M20 9V4h-5M4 15v5h5M20 15v5h-5"/>',
 "grid": '<rect x="3" y="3" width="7" height="7" rx="1.5"/><rect x="14" y="3" width="7" height="7" rx="1.5"/><rect x="3" y="14" width="7" height="7" rx="1.5"/><rect x="14" y="14" width="7" height="7" rx="1.5"/>',
 "plus": '<path d="M12 5v14M5 12h14"/>',
}
WA_PATH = '<path d="M12.04 2a9.9 9.9 0 00-8.5 15l-1.4 5 5.1-1.3A9.9 9.9 0 1012.04 2zm5.7 14.1c-.24.67-1.4 1.28-1.93 1.33-.5.05-1.12.07-1.8-.12-.42-.13-.95-.31-1.64-.6-2.9-1.25-4.8-4.17-4.94-4.37-.15-.2-1.18-1.57-1.18-3 0-1.43.75-2.13 1.01-2.42.27-.29.58-.36.78-.36h.56c.18 0 .43-.07.67.51.25.6.84 2.06.92 2.2.07.15.12.32.02.52-.1.2-.15.32-.3.5-.15.17-.31.38-.44.51-.15.15-.3.31-.13.6.17.3.77 1.27 1.65 2.05 1.13 1 2.09 1.31 2.39 1.46.3.15.47.12.65-.07.17-.2.75-.87.95-1.17.2-.3.4-.25.67-.15.27.1 1.73.82 2.03.97.3.15.5.22.57.34.07.12.07.7-.17 1.37z"/>'
SPRITE_HTML = "".join(f'<symbol id="i-{k}" viewBox="0 0 24 24">{v}</symbol>' for k, v in SPRITE.items()) + f'<symbol id="i-wa" viewBox="0 0 24 24">{WA_PATH}</symbol>'

def ic(n, cls=""):
    extra = " icon-fill" if n == "wa" else ""
    return f'<svg class="icon{extra} {cls}" aria-hidden="true"><use href="#i-{n}"/></svg>'

def wa_link(msg=""):
    return f"https://wa.me/{WA}" + (f"?text={urllib.parse.quote(msg)}" if msg else "")

COURSES = [
 dict(id="nda", cat="defence", icon="star", name="NDA Coaching", tag="Written + Physical", exams="NDA I & NDA II",
      desc="Complete written and physical preparation for NDA aspirants.", fee="₹42,000", feeNote="12 months", feeRange="₹42,000 / 12 months",
      time="Ask at the centre", points=["Subjects: Maths, GAT", "Written exam preparation", "Physical preparation"]),
 dict(id="defence", cat="defence", icon="shield", name="Defence Coaching", tag="Army · Air Force · Navy · ICG", exams="Army, Airforce, Navy, ICG",
      desc="Defence exam coaching with daily physical training and written guidance.", fee="₹38,000", feeNote="12 months", feeRange="₹38,000 / 12 months",
      time="Morning, 6:00 – 9:00 AM", points=["Written + physical training", "Daily physical practice", "Discipline-based routine"]),
 dict(id="police", cat="govt", icon="badge", name="Police Coaching", tag="Constable · Head Constable", exams="Delhi Police, State Police",
      desc="Focused coaching with physical fitness practice and regular mock tests.", fee="₹12,000", feeNote="6 months", feeRange="₹12,000 (6 mo) – ₹24,000 (12 mo)",
      time="9:30 AM – 12:30 PM", points=["Posts: Constable, Head Constable", "Physical fitness practice", "Regular mock tests"]),
 dict(id="railway", cat="govt", icon="train", name="Railway Coaching", tag="NTPC · Group D", exams="NTPC, Group D",
      desc="Complete syllabus coverage with previous year question practice.", fee="₹12,000", feeNote="6 months", feeRange="₹12,000 (6 mo) – ₹24,000 (12 mo)",
      time="1:00 – 3:00 PM", points=["Full syllabus coverage", "Previous year question practice", "Weekly tests"]),
 dict(id="ssc", cat="govt", icon="clip", name="SSC Coaching", tag="CGL · CHSL · GD", exams="CGL, CHSL, GD",
      desc="Dedicated SSC preparation with concept clarity for government job aspirants.", fee="₹15,000", feeNote="6 months", feeRange="₹15,000 (6 mo) – ₹30,000 (12 mo)",
      time="Evening, 5:00 – 8:00 PM", points=["Concept clarity", "Exam-pattern practice", "Weekly tests and analysis"]),
 dict(id="fitness", cat="fitness", icon="dumbbell", name="Physical Fitness Training", tag="Defence & Police", exams="For Defence & Police exams",
      desc="Daily physical practice under expert guidance for Defence and Police exams.", fee="₹9,000", feeNote="6 months", feeRange="₹9,000 (6 mo) – ₹18,000 (12 mo)",
      time="Daily practice", points=["Running practice", "Push-ups", "Long jump and height practice"]),
 dict(id="school", cat="school", icon="book", name="8th – 12th Classes", tag="Maths · Science · English", exams="Maths, Science, English",
      desc="Strong foundation building for school students, with personal attention.", fee=None, feeNote="", feeRange="Contact us for fees",
      time="4:00 – 7:00 PM", points=["Subjects: Maths, Science, English", "Full academic year", "Personal attention"]),
 dict(id="tuition", cat="school", icon="cap", name="Tuition / Coaching Classes", tag="School & competitive", exams="School & competitive",
      desc="Personal tuition with focused learning and doubt clearing.", fee=None, feeNote="", feeRange="Contact us for fees",
      time="Flexible", points=["School and competitive", "Duration as per course", "Doubt clearing"]),
]
CATS = [("all", "All"), ("defence", "Defence"), ("govt", "Police · Railway · SSC"), ("fitness", "Physical Fitness"), ("school", "School & Tuition")]

FACULTY = [
 dict(id="rahul", name="Mr. Rahul Sharma", role="Director / Main Faculty", qual="M.A., B.Ed.", exp="10+ Years",
      bio="With years of experience in competitive exams, guides students with the right strategy and motivation."),
 dict(id="bhagit", name="Dr. Bhagit Chaudhary", role="Faculty", qual="Ph.D (Computer Science)", exp="12 Years", bio=""),
 dict(id="neha", name="Ms. Neha Verma", role="Faculty", qual="M.Tech (IT)", exp="8 Years", bio=""),
 dict(id="amit", name="Mr. Amit Kumar", role="Faculty", qual="M.Sc (Mathematics)", exp="10 Years", bio=""),
]

# Name, place, kind, number — pairing from the original student page. Photos intentionally NOT used.
STUDENTS = [
 ("मनीष चौधरी","सुरसुरा (अजमेर)","AIR",95),("हरेंद्र थोरी","पीपलाद (परबतसर)","AIR",176),("अरविंद भाकर","रोल (नागौर)","AIR",196),
 ("शिवराज सिंह","सुथली (मकराना)","AIR",257),("भींवाराम कुमावत","लिचाना","AIR",258),("ओमप्रकाश लादडिया","","AIR",286),
 ("मनोज कुमार","जूसरिया (मकराना)","AIR",303),("कुलदीप आंवला","लोरोली (डीडवाना)","AIR",342),("दीपक माली","सुरसुरा (अजमेर)","AIR",440),
 ("नरेंद्र खोखर","बालरधना (रानीगांव)","AIR",527),
 ("हंसा","छापरी (मौलसर)","Rank",12),("अभयराज सिंह","जालसु कलां (डेगाना)","Rank",17),("राजेश चौधरी","बुहारू (किशनगढ़)","Rank",25),
 ("नंदराम गुर्जर","नया गांव (हरमाडा)","Rank",45),("पुष्पेंद्र सिंह","छपारा (लाडनूं)","Rank",68),("सूरज सिंह","खेतड़ी (अलवर)","Rank",80),
 ("रुचिका बारहट","रेवासा (दलेलपुरा)","Rank",94),("रवींद्र सोहू","पाबूपुरा (धनकोली)","Rank",98),("पवन कुमार","मिठडी (नावा)","Rank",321),
 ("युवराज सिंह राठौड़","ढिगाल (मौलासर)","Rank",548),
]

NAV = [("index.html","Home"),("about.html","About"),("courses.html","Courses"),("faculty.html","Faculty"),("results.html","Results"),("gallery.html","Gallery"),("contact.html","Contact")]

def R(d=0): return f'reveal" data-d="{d}' if d else "reveal"

LOGO = '<svg viewBox="0 0 48 48" aria-hidden="true" class="w-11 h-11 shrink-0"><rect width="48" height="48" rx="14" fill="#1f44b8"/><path d="M24 11L8 18.5l16 7.5 16-7.5z" fill="#fff"/><path d="M14 23.5V30c0 2.6 4.5 5 10 5s10-2.4 10-5v-6.5L24 29z" fill="#ffc21a"/><path d="M40 19v10" stroke="#ff8a1f" stroke-width="2.4" stroke-linecap="round"/></svg>'
def brand(dark=False):
    c1 = "text-white" if dark else "text-royal-900"
    return f'<a class="flex items-center gap-2.5" href="index.html" aria-label="CSP Coaching home">{LOGO}<span class="leading-none"><span class="block font-display font-extrabold text-xl {c1}">CSP Coaching</span><span class="block text-xs font-semibold text-orange mt-1" lang="hi">सफलता की सही दिशा</span></span></a>'

def head(title, desc, extra=""):
    ld = {"@context":"https://schema.org","@type":"EducationalOrganization","name":"CSP Coaching","telephone":PHONE_TEL,"email":EMAIL,
          "address":{"@type":"PostalAddress","addressLocality":"Kuchaman City","addressRegion":"Rajasthan","addressCountry":"IN"}}
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(title)}</title><meta name="description" content="{E(desc)}"><meta name="theme-color" content="#1f44b8">
<meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}"><meta property="og:type" content="website">
<link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,700;12..96,800&family=Mukta:wght@400;600;700&display=swap">
<link rel="stylesheet" href="assets/css/site.css">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
<script>document.documentElement.classList.add("js")</script>{extra}</head>'''

def header(active):
    links = "".join(f'<a class="nav-link" href="{h}"{" aria-current=\"page\"" if h==active else ""}>{t}</a>' for h, t in NAV)
    mlinks = "".join(f'<a class="flex items-center justify-between py-3.5 border-b border-royal-100 font-display font-semibold text-lg {"text-royal-600" if h==active else "text-royal-900"}" href="{h}"{" aria-current=\"page\"" if h==active else ""}>{t}{ic("arrow","text-orange")}</a>' for h, t in NAV)
    return f'''<svg width="0" height="0" class="absolute" aria-hidden="true">{SPRITE_HTML}</svg>
<a href="#main" class="sr-only focus:not-sr-only focus:fixed focus:top-2 focus:left-2 focus:z-[100] focus:bg-ink focus:text-white focus:px-4 focus:py-2 focus:rounded-lg">Skip to content</a>
<header id="site-header" class="sticky top-0 z-50 bg-white/95 backdrop-blur border-b border-transparent transition-shadow">
  <div class="bg-royal-900 text-royal-100 text-[.82rem] hidden sm:block"><div class="wrap flex justify-between items-center py-1.5">
    <p class="flex items-center gap-2"><span class="w-2 h-2 rounded-full bg-orange animate-pulse"></span><b class="text-sun font-semibold">Admissions open</b><span>· Free demo class before admission</span></p>
    <p class="flex gap-5"><a class="hover:text-white inline-flex items-center gap-1.5" href="mailto:{EMAIL}">{ic("mail")} {EMAIL}</a><span class="inline-flex items-center gap-1.5">{ic("pin")} Kuchaman City, Rajasthan</span></p></div></div>
  <div class="wrap flex items-center justify-between gap-3 h-[68px]">
    {brand()}
    <nav class="hidden lg:flex items-center" aria-label="Main">{links}</nav>
    <div class="flex items-center gap-3">
      <a href="tel:{PHONE_TEL}" class="hidden xl:inline-flex items-center gap-2 font-display font-semibold text-royal-800 hover:text-royal-600">{ic("phone","text-orange")}{PHONE_DISPLAY}</a>
      <button type="button" class="btn btn-orange btn-sm hidden sm:inline-flex" data-lead data-title="Book a Free Demo Class" data-source="header-demo">Book Free Demo</button>
      <button type="button" class="lg:hidden w-12 h-12 grid place-items-center rounded-xl border border-royal-200 text-royal-900" id="menu-open" aria-label="Open menu" aria-controls="drawer" aria-expanded="false">{ic("menu","w-6 h-6")}</button>
    </div></div>
</header>
<div class="overlay fixed inset-0 z-[60] bg-royal-950/70" id="overlay"></div>
<aside class="drawer fixed top-0 right-0 bottom-0 z-[70] w-[86%] max-w-[360px] bg-white shadow-lift flex flex-col" id="drawer" aria-label="Menu">
  <div class="flex items-center justify-between px-5 h-[68px] border-b border-royal-100">{brand()}<button type="button" id="menu-close" class="w-11 h-11 grid place-items-center rounded-xl bg-royal-50 text-royal-900" aria-label="Close menu">{ic("x","w-6 h-6")}</button></div>
  <nav class="flex-1 overflow-y-auto px-5 py-2" aria-label="Mobile">{mlinks}</nav>
  <div class="p-5 space-y-3 bg-royal-50">
    <a class="btn btn-royal w-full" href="tel:{PHONE_TEL}">{ic("phone")} {PHONE_DISPLAY}</a>
    <button type="button" class="btn btn-orange w-full" data-lead data-title="Book a Free Demo Class" data-source="drawer-demo">Book Free Demo</button></div>
</aside>'''

def footer():
    quick = "".join(f'<li><a class="hover:text-sun" href="{h}">{t}</a></li>' for h, t in NAV)
    cats = "".join(f'<li><a class="hover:text-sun" href="courses.html#{k}">{t}</a></li>' for k, t in CATS[1:])
    return f'''<footer class="bg-royal-950 text-royal-200 pt-16 relative overflow-hidden">
  <div class="absolute -top-24 -right-24 w-72 h-72 rounded-full bg-orange/10"></div>
  <div class="wrap relative"><div class="grid grid-cols-1 gap-10 sm:grid-cols-2 lg:grid-cols-[1.4fr_.8fr_1fr_1.3fr] [&>*]:min-w-0">
    <div>{brand(True)}<p class="mt-4 text-[.97rem]">CSP Coaching is a trusted offline coaching centre in Kuchaman City for Defence, Police, SSC and Railway exams.</p>
      <ul class="mt-5 space-y-2 text-[.95rem]"><li class="flex gap-2.5">{ic("pin","mt-1 text-sun")}Kuchaman City, Rajasthan</li><li class="flex gap-2.5">{ic("phone","mt-1 text-sun")}<a class="hover:text-sun" href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></li><li class="flex gap-2.5">{ic("wa","mt-1 text-sun")}<a class="hover:text-sun" target="_blank" rel="noopener" href="{wa_link()}">WhatsApp chat</a></li></ul></div>
    <div><h4 class="text-white text-base mb-4">Quick links</h4><ul class="space-y-2">{quick}</ul></div>
    <div><h4 class="text-white text-base mb-4">Course categories</h4><ul class="space-y-2">{cats}</ul></div>
    <div><h4 class="text-white text-base mb-4">Get updates</h4><p class="text-[.95rem] mb-3">New batches and admission news, straight to your inbox.</p>
      <form id="news-form" class="flex gap-2" novalidate><label class="sr-only" for="news-email">Email address</label>
        <input id="news-email" type="email" required placeholder="Your email" class="flex-1 min-w-0 min-h-[48px] px-4 rounded-full bg-white/10 border border-white/20 text-white placeholder:text-royal-200 focus:outline-none focus:border-sun">
        <button class="btn btn-orange btn-sm" type="submit">Subscribe</button></form><p id="news-msg" role="status" class="text-sm mt-2 min-h-[1.25rem]"></p>
      <p class="text-sm mt-3">Email: <a class="text-sun hover:underline" href="mailto:{EMAIL}">{EMAIL}</a></p></div>
  </div>
  <div class="mt-12 border-t border-white/10 py-5 text-sm flex flex-col sm:flex-row gap-2 justify-between"><p>© 2025 CSP Coaching, Kuchaman City. All rights reserved.</p><p>Offline coaching for Defence · Police · SSC · Railway</p></div></div>
</footer>
<button type="button" data-lead data-title="Quick Inquiry" data-source="floating-badge" class="fixed left-3 bottom-4 z-40 inline-flex items-center gap-2 pl-3 pr-4 h-12 rounded-full bg-orange text-ink font-display font-bold text-sm shadow-lift hover:bg-sun transition">{ic("chat","w-5 h-5")}<span>Quick Inquiry</span></button>
<a class="fixed right-3 bottom-4 z-40 w-14 h-14 rounded-full bg-[#168f47] text-white grid place-items-center shadow-lift hover:scale-105 transition" target="_blank" rel="noopener" href="{wa_link()}" aria-label="Chat on WhatsApp">{ic("wa","w-7 h-7")}</a>
{lead_dialog()}{faculty_dialog_shell()}{lightbox_shell()}
<script src="assets/js/config.js"></script><script src="assets/js/main.js" defer></script></body></html>'''

def lead_form(fid, compact=False):
    courses = "".join(f'<option>{E(c["name"])}</option>' for c in COURSES) + "<option>Hostel</option><option>Not sure yet</option>"
    years = "".join(f"<option>{y}</option>" for y in (2027, 2028, 2029)) + "<option>Not sure yet</option>"
    return f'''<form class="lead-form space-y-3.5" id="{fid}" novalidate data-source="">
  <div class="grid sm:grid-cols-2 gap-3.5">
    <div class="field"><label for="{fid}-name">Your name</label><input id="{fid}-name" name="name" autocomplete="name" required><p class="err">Please enter your name.</p></div>
    <div class="field"><label for="{fid}-phone">Phone number</label><input id="{fid}-phone" name="phone" type="tel" inputmode="numeric" autocomplete="tel" placeholder="10-digit mobile" required><p class="err">Enter a valid 10-digit mobile number.</p></div>
  </div>
  <div class="grid sm:grid-cols-2 gap-3.5">
    <div class="field"><label for="{fid}-course">Course</label><select id="{fid}-course" name="course"><option value="">Select a course</option>{courses}</select></div>
    <div class="field"><label for="{fid}-year">Target year</label><select id="{fid}-year" name="target_year"><option value="">Select year</option>{years}</select></div>
  </div>
  <div class="field"><label for="{fid}-msg">Message (optional)</label><textarea id="{fid}-msg" name="message" rows="{2 if compact else 3}"></textarea></div>
  <button class="btn btn-orange w-full" type="submit">Send enquiry {ic("arrow")}</button>
  <p class="text-sm text-royal-800/80 form-status" role="status" aria-live="polite"></p>
</form>'''

def lead_dialog():
    return f'''<dialog id="lead-dlg" aria-labelledby="lead-title"><div class="m-3 w-[min(520px,calc(100vw-24px))] max-h-[calc(100dvh-24px)] overflow-y-auto rounded-3xl bg-white shadow-lift">
  <div class="relative bg-gradient-to-br from-royal-700 to-royal-900 text-white px-6 pt-6 pb-8 rounded-t-3xl"><div class="absolute -right-6 -top-6 w-28 h-28 rounded-full bg-orange/30"></div>
    <button type="button" data-close class="absolute top-3 right-3 w-11 h-11 grid place-items-center rounded-full bg-white/15 hover:bg-white/25" aria-label="Close">{ic("x","w-5 h-5")}</button>
    <p class="chip bg-sun text-ink mb-2">Free demo class available</p><h2 id="lead-title" class="text-2xl pr-10">Quick Inquiry</h2><p class="text-royal-100 text-[.95rem] mt-1">Leave your details. We will get back to you shortly.</p></div>
  <div class="p-6">{lead_form("lead-form", True)}</div></div></dialog>'''

def faculty_dialog_shell():
    return f'''<dialog id="fac-dlg" aria-label="Faculty details"><div class="m-3 w-[min(520px,calc(100vw-24px))] max-h-[calc(100dvh-24px)] overflow-y-auto rounded-3xl bg-white shadow-lift relative p-6 sm:p-8">
  <button type="button" data-close class="absolute top-3 right-3 w-11 h-11 grid place-items-center rounded-full bg-royal-50 text-royal-900" aria-label="Close">{ic("x","w-5 h-5")}</button><div id="fac-body"></div></div></dialog>'''

def lightbox_shell():
    return f'''<dialog id="lb" aria-label="Photo viewer"><div class="fixed inset-0 grid place-items-center p-3">
  <button type="button" data-close class="absolute top-3 right-3 w-12 h-12 grid place-items-center rounded-full bg-white/15 text-white hover:bg-white/25" aria-label="Close">{ic("x","w-6 h-6")}</button>
  <button type="button" id="lb-prev" class="absolute left-2 sm:left-6 top-1/2 -translate-y-1/2 w-12 h-12 grid place-items-center rounded-full bg-white/15 text-white hover:bg-white/25" aria-label="Previous photo">{ic("left","w-6 h-6")}</button>
  <button type="button" id="lb-next" class="absolute right-2 sm:right-6 top-1/2 -translate-y-1/2 w-12 h-12 grid place-items-center rounded-full bg-white/15 text-white hover:bg-white/25" aria-label="Next photo">{ic("right","w-6 h-6")}</button>
  <figure class="max-w-[min(1000px,86vw)] text-center"><img id="lb-img" alt="" class="max-h-[74dvh] w-auto mx-auto rounded-2xl bg-royal-900"><figcaption id="lb-cap" class="text-white font-display font-semibold mt-3"></figcaption></figure></div></dialog>'''

def page_header(title, crumb, lead, active_icon="grid"):
    return f'''<section class="relative bg-gradient-to-br from-royal-800 via-royal-700 to-royal-900 text-white overflow-hidden diag-bottom pb-16 sm:pb-24 pt-12 sm:pt-16 on-dark">
  <div class="absolute -right-16 -top-16 w-64 h-64 rounded-full border-[28px] border-sun/25"></div><div class="absolute right-24 bottom-6 w-24 h-24 rounded-full bg-orange/25"></div>
  <div class="wrap relative"><nav aria-label="Breadcrumb" class="text-sm text-royal-200 mb-4"><a class="hover:text-sun" href="index.html">Home</a> <span class="mx-1">/</span> <span class="text-sun">{crumb}</span></nav>
  <h1 class="text-4xl sm:text-5xl lg:text-6xl max-w-3xl">{title}</h1><p class="mt-4 max-w-2xl text-royal-100 text-lg">{lead}</p></div></section>'''

def page(active, title, desc, body):
    return head(title, desc) + '<body>' + header(active) + f'<main id="main">{body}</main>' + footer()
