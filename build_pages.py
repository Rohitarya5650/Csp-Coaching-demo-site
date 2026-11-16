from build_common import *

def initial(name):
    n = name.replace("Dr. ", "").replace("Mr. ", "").replace("Ms. ", "")
    return "".join(w[0] for w in n.split()[:2])

def course_slide(c):
    fee = f'<p class="font-display font-extrabold text-2xl text-royal-700">{c["fee"]}<span class="text-sm font-semibold text-royal-800/70"> / {c["feeNote"]}</span></p>' if c["fee"] else '<p class="font-display font-bold text-lg text-royal-700">Fees on request</p>'
    return f'''<article class="w-[82%] sm:w-[46%] lg:w-[31.5%] mr-4 card card-hover p-6 flex flex-col relative overflow-hidden">
  <span class="absolute -right-8 -top-8 w-24 h-24 rounded-full bg-sun/40"></span>
  <div class="relative w-14 h-14 rounded-2xl bg-royal-600 text-white grid place-items-center mb-4">{ic(c["icon"],"w-7 h-7")}</div>
  <span class="chip bg-orange-100 text-orange-600 self-start mb-2">{E(c["tag"])}</span>
  <h3 class="text-xl">{E(c["name"])}</h3><p class="text-royal-800/80 mt-1.5 text-[.98rem] flex-1">{E(c["desc"])}</p>
  <div class="mt-4 pt-4 border-t border-royal-100 flex flex-col gap-3">{fee}
    <button class="btn btn-royal btn-sm w-full" type="button" data-lead data-title="Enquire: {E(c['name'])}" data-course="{E(c['name'])}" data-source="home-course-{c['id']}">Enquire {ic("arrow")}</button></div></article>'''

def course_full(c):
    pts = "".join(f'<li class="flex gap-2">{ic("check","text-orange mt-1 w-4 h-4")}<span>{E(p)}</span></li>' for p in c["points"])
    return f'''<article class="card card-hover p-6 sm:p-7 flex flex-col {R()}" data-filter-item data-cat="{c["cat"]}" id="course-{c["id"]}">
  <div class="flex items-start justify-between gap-3"><div class="w-14 h-14 rounded-2xl bg-gradient-to-br from-royal-500 to-royal-700 text-white grid place-items-center">{ic(c["icon"],"w-7 h-7")}</div>
    <span class="chip bg-sun-100 text-ink">{E(c["tag"])}</span></div>
  <h3 class="text-2xl mt-4">{E(c["name"])}</h3><p class="text-royal-800/80 mt-1">{E(c["desc"])}</p>
  <ul class="mt-4 space-y-1.5 text-[.98rem]">{pts}</ul>
  <dl class="mt-5 grid grid-cols-2 gap-3 text-sm"><div class="rounded-2xl bg-royal-50 p-3"><dt class="text-royal-800/70">Mode</dt><dd class="font-display font-bold">Offline</dd></div>
    <div class="rounded-2xl bg-royal-50 p-3"><dt class="text-royal-800/70">Batch timing</dt><dd class="font-display font-bold">{E(c["time"])}</dd></div>
    <div class="rounded-2xl bg-sun-100 p-3 col-span-2"><dt class="text-royal-800/70">Fee range</dt><dd class="font-display font-extrabold text-lg">{E(c["feeRange"])}</dd></div></dl>
  <div class="mt-5 flex gap-3 flex-wrap mt-auto pt-5"><button class="btn btn-orange flex-1" type="button" data-lead data-title="Enquire: {E(c['name'])}" data-course="{E(c['name'])}" data-source="course-{c['id']}">Enquire now</button>
    <a class="btn btn-line-royal" target="_blank" rel="noopener" href="{wa_link('Hello CSP Coaching, I want to know more about ' + c['name'] + '.')}" aria-label="WhatsApp about {E(c['name'])}">{ic("wa")}</a></div></article>'''

def student_chip(s):
    return f'<span class="inline-flex items-center gap-2 px-5 py-2.5 mr-3 rounded-full bg-white border border-royal-100 shadow-card whitespace-nowrap"><b class="font-display text-royal-600">{s[2]} {s[3]}</b><span lang="hi" class="font-semibold">{E(s[0])}</span><span class="text-royal-800/60 text-sm" lang="hi">{E(s[1])}</span></span>'

def story_card(s):
    name, place, kind, n = s
    return f'''<article class="w-[78%] sm:w-[44%] lg:w-[24%] mr-4 card p-6 relative overflow-hidden bg-gradient-to-b from-white to-royal-50">
  <p class="font-display font-extrabold text-6xl text-royal-100 absolute -right-1 top-1 leading-none select-none" aria-hidden="true">{n}</p>
  <div class="relative w-16 h-16 rounded-full bg-gradient-to-br from-orange to-sun text-ink grid place-items-center font-display font-extrabold text-2xl ring-4 ring-white shadow-card" lang="hi" aria-hidden="true">{E(name[0])}</div>
  <p class="relative mt-5 chip bg-royal-600 text-white">{kind} {n}</p>
  <h3 class="relative text-xl mt-3" lang="hi">{E(name)}</h3><p class="relative text-royal-800/70 text-[.95rem]" lang="hi">{E(place) if place else "CSP Coaching student"}</p>
  <p class="relative mt-4 text-sm text-royal-800/80 flex items-center gap-1.5">{ic("trophy","text-orange")} Proud CSP achiever</p></article>'''

FAQ = [
 ("Is there a free demo class?", "Yes. CSP Coaching offers a free demo class before admission, so you can see the teaching for yourself."),
 ("Which exams do you prepare for?", "NDA, Army, Airforce, Navy, ICG, Delhi Police and State Police, SSC (CGL, CHSL, GD) and Railway (NTPC, Group D). We also run 8th–12th classes and tuition."),
 ("What are the class timings?", "Defence 6:00–9:00 AM, Police 9:30 AM–12:30 PM, Railway 1:00–3:00 PM, SSC 5:00–8:00 PM and 8th–12th 4:00–7:00 PM."),
 ("Do you provide a hostel?", "Yes. A safe hostel near the institute is available at ₹5,000 per month with no hidden charges."),
 ("Do you give study material?", "Yes. PDF notes and printed study material are provided, along with weekly tests and mock exams."),
]
def faq():
    return "".join(f'<details class="group card p-0 overflow-hidden"><summary class="flex items-center justify-between gap-4 cursor-pointer list-none px-5 py-4 font-display font-semibold min-h-[56px]">{E(q)}<span class="w-8 h-8 shrink-0 grid place-items-center rounded-full bg-royal-50 text-royal-600 group-open:bg-orange group-open:text-ink group-open:rotate-45 transition">{ic("plus","w-4 h-4")}</span></summary><p class="px-5 pb-5 text-royal-800/85">{E(a)}</p></details>' for q, a in FAQ)

def slider_controls(label):
    return f'<div class="flex gap-2"><button type="button" class="w-12 h-12 grid place-items-center rounded-full border-2 border-royal-200 hover:bg-royal-600 hover:text-white hover:border-royal-600 transition" data-slider-prev aria-label="Previous {label}">{ic("left")}</button><button type="button" class="w-12 h-12 grid place-items-center rounded-full border-2 border-royal-200 hover:bg-royal-600 hover:text-white hover:border-royal-600 transition" data-slider-next aria-label="Next {label}">{ic("right")}</button></div>'

CTA_BAND = f'''<section class="relative overflow-hidden bg-gradient-to-r from-orange to-sun"><div class="absolute -left-10 -bottom-16 w-52 h-52 rounded-full bg-white/25"></div>
  <div class="wrap relative py-12 flex flex-col lg:flex-row gap-6 lg:items-center justify-between"><div><h2 class="text-3xl sm:text-4xl text-ink">Ready to achieve your goals?</h2><p class="text-ink/80 mt-2 max-w-xl">Join CSP Coaching and take the first step towards a successful career. Attend a free demo class first.</p></div>
  <div class="flex gap-3 flex-wrap"><button class="btn bg-royal-900 text-white hover:bg-royal-700" type="button" data-lead data-title="Book a Free Demo Class" data-source="cta-band">Book Free Demo {ic("arrow")}</button><a class="btn bg-white text-ink hover:bg-sun-100" target="_blank" rel="noopener" href="{wa_link("Hello CSP Coaching, I want to book a free demo class.")}">{ic("wa")} WhatsApp us</a></div></div></section>'''

# ---------------- HOME ----------------
def home():
    marq = "".join(student_chip(s) for s in STUDENTS)
    bento = f'''<div class="grid gap-4 lg:grid-cols-4 lg:grid-rows-2">
  <div class="relative lg:col-span-2 lg:row-span-2 rounded-3xl overflow-hidden min-h-[320px] {R()}"><img src="assets/img/gallery/teacher-guidance.webp" alt="Teacher guiding a student in a CSP classroom" width="500" height="468" loading="lazy" class="absolute inset-0 w-full h-full object-cover">
    <div class="absolute inset-0 bg-gradient-to-t from-royal-950 via-royal-950/40 to-transparent"></div><div class="absolute bottom-0 p-6 sm:p-8 text-white"><span class="chip bg-sun text-ink mb-3">Core strength</span><h3 class="text-2xl sm:text-3xl">Exam-oriented teaching with personal guidance</h3><p class="mt-2 text-royal-100 max-w-md">Experienced faculty, whiteboard and smart teaching, and regular doubt clearing in every batch.</p></div></div>
  <div class="card p-5 {R(1)}"><div class="w-12 h-12 rounded-2xl bg-orange text-ink grid place-items-center mb-3">{ic("test","w-6 h-6")}</div><h3 class="text-lg">Weekly tests</h3><p class="text-[.95rem] text-royal-800/80">Mock exams on the real pattern with performance analysis.</p></div>
  <div class="card p-5 bg-royal-600 text-white border-royal-600 {R(2)}"><div class="w-12 h-12 rounded-2xl bg-white/15 grid place-items-center mb-3">{ic("dumbbell","w-6 h-6")}</div><h3 class="text-lg text-white">Physical training</h3><p class="text-[.95rem] text-royal-100">Daily running, push-ups, long jump and height practice for Defence and Police.</p></div>
  <div class="card p-5 {R(1)}"><div class="w-12 h-12 rounded-2xl bg-sun text-ink grid place-items-center mb-3">{ic("book","w-6 h-6")}</div><h3 class="text-lg">Study material</h3><p class="text-[.95rem] text-royal-800/80">PDF notes and printed material, updated for the syllabus.</p></div>
  <div class="card p-5 bg-sun-100 {R(2)}"><div class="w-12 h-12 rounded-2xl bg-royal-600 text-white grid place-items-center mb-3">{ic("bed","w-6 h-6")}</div><h3 class="text-lg">Hostel · ₹5,000/mo</h3><p class="text-[.95rem] text-royal-800/80">Safe, affordable, near the institute. No hidden charges.</p></div></div>'''
    gal = "".join(f'<a href="gallery.html" class="group relative overflow-hidden rounded-3xl {cls} {R()}"><img src="assets/img/gallery/{img}.webp" alt="{alt}" loading="lazy" class="w-full h-full object-cover group-hover:scale-105 transition duration-500"><span class="absolute inset-x-0 bottom-0 p-3 bg-gradient-to-t from-royal-950/80 to-transparent text-white font-display font-semibold text-sm">{alt}</span></a>'
                  for img, alt, cls in [("girl-focus","Focused exam practice","row-span-2 min-h-[260px]"),("classroom-wide","Classroom session","col-span-2 min-h-[160px]"),("back-row","Students at work","min-h-[160px]"),("exam-hall-right","Test day","min-h-[160px]")])
    return f'''
<section class="relative bg-gradient-to-br from-royal-950 via-royal-800 to-royal-600 text-white overflow-hidden diag-bottom pb-28 sm:pb-36 pt-10 sm:pt-16 on-dark">
  <div class="absolute -left-20 top-40 w-72 h-72 rounded-full bg-orange/15"></div><div class="absolute right-[-60px] top-[-60px] w-80 h-80 rounded-full border-[34px] border-sun/20"></div>
  <div class="wrap relative grid lg:grid-cols-[1.05fr_.95fr] gap-12 items-center">
    <div><p class="chip bg-white/10 border border-white/20 text-sun mb-5 animate-fadeup">{ic("bolt","w-4 h-4")} Admissions open · Free demo class</p>
      <h1 class="text-[2.4rem] sm:text-5xl lg:text-[3.7rem] leading-[1.06] animate-fadeup">Your path to <span class="relative text-sun">Defence, Police, SSC &amp; Railway</span> success starts here</h1>
      <p class="mt-6 text-lg sm:text-xl text-royal-100 max-w-xl animate-fadeup">Expert faculty, weekly tests, daily physical training and a hostel near the institute. Sit in a free demo class before you join.</p>
      <p class="mt-2 text-sun font-semibold" lang="hi">सफलता की सही दिशा, कुचामन सिटी</p>
      <div class="mt-8 flex flex-wrap gap-3 animate-fadeup"><a class="btn btn-orange" href="courses.html">Explore Courses {ic("arrow")}</a><button class="btn btn-line" type="button" data-lead data-title="Book a Free Demo Class" data-source="hero-demo">Book Free Demo</button></div></div>
    <div class="relative lg:pl-6"><div class="absolute inset-0 translate-x-4 translate-y-4 sm:translate-x-6 sm:translate-y-6 rounded-[2rem] bg-sun rotate-2"></div>
      <img src="assets/img/hero.webp" width="1362" height="468" fetchpriority="high" alt="A teacher guiding a student during a written test in a CSP Coaching classroom" class="relative rounded-[2rem] w-full aspect-[4/3.3] object-cover object-[28%_20%] -rotate-2 shadow-lift">
      <div class="absolute -left-2 sm:-left-6 top-10 bg-white text-ink rounded-2xl shadow-lift px-4 py-3 flex items-center gap-3 animate-floaty"><span class="w-10 h-10 rounded-xl bg-orange grid place-items-center">{ic("test")}</span><span class="leading-tight"><b class="block font-display">Weekly tests</b><span class="text-sm text-royal-800/70">+ mock exams</span></span></div>
      <div class="absolute -right-1 sm:-right-4 bottom-4 bg-white text-ink rounded-2xl shadow-lift px-4 py-3 flex items-center gap-3 animate-floaty [animation-delay:1.5s]"><span class="w-10 h-10 rounded-xl bg-royal-600 text-white grid place-items-center">{ic("bed")}</span><span class="leading-tight"><b class="block font-display">Hostel ₹5,000/mo</b><span class="text-sm text-royal-800/70">near the institute</span></span></div></div></div></section>

<section class="relative z-10 -mt-20 sm:-mt-24"><div class="wrap"><div class="card grid grid-cols-2 lg:grid-cols-4 overflow-hidden">
  <div class="p-5 sm:p-7 text-center"><b class="block font-display font-extrabold text-4xl sm:text-5xl text-royal-600" data-count="500" data-suffix="+">500+</b><span class="text-royal-800/80">Selections</span></div>
  <div class="p-5 sm:p-7 text-center border-l border-royal-100"><b class="block font-display font-extrabold text-4xl sm:text-5xl text-orange" data-count="10" data-suffix="+">10+</b><span class="text-royal-800/80">Years of experience</span></div>
  <div class="p-5 sm:p-7 text-center border-t lg:border-t-0 lg:border-l border-royal-100"><b class="block font-display font-extrabold text-4xl sm:text-5xl text-royal-600" data-count="4">4</b><span class="text-royal-800/80">Expert faculty</span></div>
  <div class="p-5 sm:p-7 text-center border-t lg:border-t-0 border-l border-royal-100"><b class="block font-display font-extrabold text-4xl sm:text-5xl text-orange" data-count="8">8</b><span class="text-royal-800/80">Courses &amp; programs</span></div></div></div></section>

<section class="pt-12 pb-4" aria-label="Our achievers"><div class="wrap flex items-center gap-3 mb-4"><span class="chip bg-orange text-ink">{ic("trophy","w-4 h-4")} Our achievers</span><a class="text-sm font-display font-semibold text-royal-600 hover:underline" href="results.html">View all results</a></div>
  <div class="marquee overflow-hidden" aria-hidden="false"><div class="marquee-track">{marq}{marq}</div></div></section>

<section class="section" data-slider>
  <div class="wrap"><div class="flex flex-wrap items-end justify-between gap-4 mb-8"><div class="{R()}"><p class="eyebrow">Our courses</p><h2 class="h2 max-w-xl">Programs built for your success</h2></div>{slider_controls("course")}</div></div>
  <div class="wrap"><div class="slider-track pb-8 -mx-1 px-1" data-slider-track>{"".join(course_slide(c) for c in COURSES)}</div></div>
  <div class="wrap mt-6"><a class="btn btn-line-royal" href="courses.html">View all courses &amp; fees {ic("arrow")}</a></div></section>

<section class="section bg-royal-50 relative"><div class="wrap"><div class="max-w-2xl mb-10 {R()}"><p class="eyebrow">Why CSP Coaching</p><h2 class="h2">Everything a serious aspirant needs, in one place</h2></div>{bento}</div></section>

<section class="section bg-sun-100/70 overflow-hidden" data-slider data-autoplay>
  <div class="wrap"><div class="flex flex-wrap items-end justify-between gap-4 mb-8"><div class="{R()}"><p class="eyebrow">Success stories</p><h2 class="h2 max-w-xl">Our students, our pride</h2><p class="mt-2 text-royal-800/80">Real results from CSP Coaching students across Rajasthan.</p></div>{slider_controls("story")}</div></div>
  <div class="wrap"><div class="slider-track pb-8" data-slider-track>{"".join(story_card(s) for s in STUDENTS)}</div></div>
  <div class="wrap mt-5"><a class="btn btn-royal" href="results.html">See all results {ic("arrow")}</a></div></section>

<section class="section"><div class="wrap grid gap-3 sm:grid-cols-3 sm:grid-rows-[auto_auto] mb-10">{gal}</div>
  <div class="wrap text-center"><a class="btn btn-line-royal" href="gallery.html">Open the gallery {ic("arrow")}</a></div></section>

<section class="section bg-royal-50"><div class="wrap grid lg:grid-cols-[.8fr_1.2fr] gap-10"><div class="{R()}"><p class="eyebrow">Quick answers</p><h2 class="h2">Questions parents and students ask</h2><p class="mt-3 text-royal-800/80">Still unsure? Call us or send a WhatsApp message and we will help.</p><a class="btn btn-wa mt-5" target="_blank" rel="noopener" href="{wa_link()}">{ic("wa")} Ask on WhatsApp</a></div><div class="space-y-3">{faq()}</div></div></section>
{CTA_BAND}'''

# ---------------- ABOUT ----------------
STEPS = [
 ("Free demo class", "demo", "Visit CSP Coaching and sit in a free demo class. See the teaching style, meet the faculty and ask your questions before you decide."),
 ("Choose your course", "target", "Pick the right batch for Defence, Police, SSC, Railway or school classes. We guide you on timings and fee plans (6 or 12 months)."),
 ("Daily classes", "room", "Exam-oriented teaching with whiteboard and smart explanation, backed by PDF notes and printed study material."),
 ("Weekly tests & mocks", "test", "Regular tests and mock exams on the real exam pattern keep your preparation honest and on track."),
 ("Analysis & doubt clearing", "chat", "After each test you get performance analysis and improvement guidance, plus regular doubt clearing and personal attention."),
 ("Physical training", "dumbbell", "For Defence and Police aspirants: daily running, push-ups, long jump and height practice with discipline-based training."),
]
def about():
    tabs = "".join(f'<button type="button" role="tab" id="st-{i}" aria-controls="sp-{i}" aria-selected="{"true" if i==0 else "false"}" tabindex="{0 if i==0 else -1}" class="step-tab w-full text-left flex items-center gap-4 px-4 py-3.5 rounded-2xl border-2 border-transparent aria-selected:bg-royal-600 aria-selected:text-white aria-selected:shadow-card hover:bg-royal-50 aria-selected:hover:bg-royal-600 transition min-h-[56px]"><span class="w-9 h-9 shrink-0 grid place-items-center rounded-full bg-orange text-ink font-display font-extrabold">{i+1}</span><span class="font-display font-semibold">{E(t)}</span></button>' for i, (t, _, _) in enumerate(STEPS))
    panels = "".join(f'<div role="tabpanel" id="sp-{i}" aria-labelledby="st-{i}" {"" if i==0 else "hidden"} class="step-panel"><p class="chip bg-orange text-ink mb-3">Step {i+1} of {len(STEPS)}</p><h3 class="text-2xl sm:text-3xl">{E(t)}</h3><p class="mt-3 text-lg text-royal-100">{E(d)}</p></div>' for i, (t, _, d) in enumerate(STEPS))
    values = [("users","Personal attention","Every student gets individual guidance from faculty who know their strengths and gaps.","bg-orange"),
              ("chat","Doubt-clearing structure","Regular doubt clearing sessions so no topic stays unclear.","bg-sun"),
              ("test","Weekly assessment","Weekly tests and mock exams with detailed performance analysis.","bg-royal-500 text-white"),
              ("shield","Discipline & fitness","Discipline-based routine and daily physical training for Defence and Police aspirants.","bg-orange")]
    vals = "".join(f'<div class="card card-hover p-6 {R(i%3)} {"lg:translate-y-6" if i%2 else ""}"><div class="w-14 h-14 rounded-2xl {c} grid place-items-center mb-4 {"text-ink" if "text-white" not in c else ""}">{ic(i_,"w-7 h-7")}</div><h3 class="text-xl">{t}</h3><p class="mt-2 text-royal-800/80">{d}</p></div>' for i, (i_, t, d, c) in enumerate(values))
    return page_header("About CSP Coaching", "About", "A trusted offline coaching centre in Kuchaman City, preparing students for Defence, Police, SSC and Railway exams.") + f'''
<section class="section overflow-x-clip"><div class="wrap grid lg:grid-cols-[1fr_1.1fr] gap-12 items-center">
  <div class="relative {R()}"><img src="assets/img/gallery/classroom-wide.webp" alt="CSP Coaching students writing a test in class" width="1362" height="468" loading="lazy" class="rounded-[2rem] w-full aspect-[4/3.4] object-cover object-[92%_40%] shadow-lift">
    <div class="absolute -bottom-6 -right-2 sm:-right-6 bg-orange text-ink rounded-3xl px-6 py-4 shadow-lift rotate-3"><b class="block font-display font-extrabold text-4xl">10+</b><span class="font-semibold">years of experience</span></div></div>
  <div class="{R(1)}"><p class="eyebrow">Our story</p><h2 class="h2">Building dreams since day one</h2>
    <p class="mt-4">CSP Coaching is a trusted offline coaching centre in Kuchaman City, preparing students for Defence, Police, SSC and Railway exams. We believe in quality education, dedicated faculty and result-oriented learning.</p>
    <p class="mt-3">Our goal is simple: help every student give their best and build a successful career. With weekly tests, doubt clearing, daily physical training and a hostel near the institute, students can focus fully on preparation.</p>
    <div class="mt-6 grid grid-cols-3 gap-3 text-center"><div class="rounded-2xl bg-royal-50 p-4"><b class="block font-display text-3xl text-royal-600" data-count="500" data-suffix="+">500+</b><span class="text-sm">Selections</span></div><div class="rounded-2xl bg-sun-100 p-4"><b class="block font-display text-3xl text-orange-600" data-count="10" data-suffix="+">10+</b><span class="text-sm">Years</span></div><div class="rounded-2xl bg-royal-50 p-4"><b class="block font-display text-3xl text-royal-600" data-count="100" data-suffix="%">100%</b><span class="text-sm">Dedication</span></div></div></div></div></section>

<section class="section bg-royal-50 overflow-hidden"><div class="wrap grid lg:grid-cols-[.75fr_1.25fr] gap-10 items-center">
  <div class="relative mx-auto {R()}"><div class="w-64 h-64 sm:w-80 sm:h-80 rounded-[2.5rem] bg-gradient-to-br from-royal-600 to-royal-900 grid place-items-center rotate-3 shadow-lift"><span class="font-display font-extrabold text-8xl text-sun -rotate-3">RS</span></div>
    <div class="absolute -z-10 -left-4 -bottom-4 w-64 h-64 sm:w-80 sm:h-80 rounded-[2.5rem] bg-orange/70 -rotate-3"></div></div>
  <div class="{R(1)}"><p class="eyebrow">Director&rsquo;s desk</p><h2 class="h2">Mr. Rahul Sharma</h2><p class="font-display font-semibold text-royal-600 mt-1">Director / Main Faculty · M.A., B.Ed. · 10+ years of experience</p>
    <blockquote class="mt-5 relative pl-5 border-l-4 border-orange text-xl sm:text-2xl font-display font-semibold leading-snug">With years of experience in competitive exams, we guide students with the right strategy and motivation.</blockquote>
    <p class="mt-5">Our philosophy is simple: experienced faculty, exam-oriented teaching and daily personal guidance. Start your success preparation today.</p>
    <div class="mt-6 flex gap-3 flex-wrap"><button class="btn btn-orange" type="button" data-lead data-title="Book a Free Demo Class" data-source="about-director">Book Free Demo</button><a class="btn btn-line-royal" href="faculty.html">Meet the faculty</a></div></div></div></section>

<section class="section"><div class="wrap"><div class="max-w-2xl mb-10 {R()}"><p class="eyebrow">Core values</p><h2 class="h2">What makes learning at CSP different</h2></div><div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-5 pb-6">{vals}</div></div></section>

<section class="section bg-gradient-to-br from-royal-900 to-royal-700 text-white on-dark"><div class="wrap"><div class="max-w-2xl mb-10 {R()}"><p class="eyebrow">Your journey</p><h2 class="h2">How a student grows at CSP Coaching</h2><p class="mt-2 text-royal-100">Tap a step to see what happens at each stage.</p></div>
  <div class="grid lg:grid-cols-[.9fr_1.1fr] gap-8 items-start" data-tabs><div role="tablist" aria-label="Student journey" class="space-y-2">{tabs}</div>
  <div class="rounded-3xl bg-white/10 border border-white/15 p-7 sm:p-10 min-h-[260px] relative overflow-hidden"><div class="absolute -right-10 -bottom-10 w-40 h-40 rounded-full bg-orange/30"></div><div class="relative">{panels}</div></div></div></div></section>
{CTA_BAND}'''

# ---------------- COURSES ----------------
def courses():
    chips = "".join(f'<button type="button" class="filter-chip px-5 min-h-[46px] rounded-full font-display font-semibold border-2 border-royal-200 aria-pressed:bg-royal-600 aria-pressed:text-white aria-pressed:border-royal-600 hover:border-royal-500 transition" data-filter="{k}" aria-pressed="{"true" if k=="all" else "false"}">{t}</button>' for k, t in CATS)
    rows = "".join(f'<tr class="border-b border-royal-100"><th scope="row" class="text-left py-3 pr-4 font-display font-semibold">{E(c["name"])}</th><td class="py-3 pr-4">{E(c["time"])}</td><td class="py-3 font-display font-bold text-royal-700 whitespace-nowrap">{E(c["feeRange"])}</td></tr>' for c in COURSES)
    return page_header("Courses &amp; Programs", "Courses", "Defence, Police, SSC, Railway, physical fitness and school classes. Pick a program, check the timing and fee, and enquire in one tap.") + f'''
<section class="section pt-10"><div class="wrap">
  <div class="rounded-3xl bg-gradient-to-r from-royal-700 to-royal-500 text-white p-6 sm:p-8 flex flex-col md:flex-row md:items-center justify-between gap-5 mb-10 {R()}"><div><h2 class="text-2xl sm:text-3xl">Download the course brochure</h2><p class="text-royal-100 mt-1">Courses, class timings, fee plans, facilities and contact details in one PDF.</p></div>
    <a class="btn btn-orange shrink-0" href="assets/docs/CSP-Coaching-Brochure.pdf" download>{ic("download")} Download brochure (PDF)</a></div>
  <div class="flex gap-2 flex-wrap mb-8" data-filters data-target="#course-grid" role="group" aria-label="Filter courses">{chips}</div>
  <div class="grid md:grid-cols-2 xl:grid-cols-3 gap-6" id="course-grid">{"".join(course_full(c) for c in COURSES)}</div></div></section>

<section class="section bg-royal-50"><div class="wrap"><div class="max-w-2xl mb-8 {R()}"><p class="eyebrow">At a glance</p><h2 class="h2">Timings and fees</h2><p class="mt-2 text-royal-800/80">Fee plans are for 6 or 12 months as shown. Contact us for 8th–12th and tuition fees.</p></div>
  <div class="card overflow-x-auto"><table class="w-full min-w-[560px] text-[.98rem] m-0"><thead class="bg-royal-600 text-white"><tr><th scope="col" class="text-left p-3.5 font-display">Course</th><th scope="col" class="text-left p-3.5 font-display">Class time</th><th scope="col" class="text-left p-3.5 font-display">Fee</th></tr></thead><tbody class="[&_tr>*]:px-3.5">{rows}</tbody></table></div>
  <div class="mt-8 rounded-3xl bg-ink text-white p-6 sm:p-8 grid md:grid-cols-[1fr_auto] gap-5 items-center {R()}"><div><span class="chip bg-sun text-ink mb-2">Hostel</span><h3 class="text-2xl">Safe hostel near the institute · ₹5,000 / month</h3><p class="text-royal-200 mt-1">Comfortable beds, 24×7 water and electricity, CCTV security, RO drinking water. No hidden charges.</p></div><a class="btn btn-orange" target="_blank" rel="noopener" href="{wa_link("Hello CSP Coaching, I want to know about hostel admission.")}">{ic("wa")} Ask about hostel</a></div></div></section>
{CTA_BAND}'''

# ---------------- FACULTY ----------------
def faculty():
    cards = ""
    for i, f in enumerate(FACULTY):
        big = i == 0
        cards += f'''<article class="card card-hover p-6 {"sm:col-span-2 lg:col-span-3 bg-gradient-to-br from-royal-700 to-royal-900 text-white border-royal-700" if big else ""} {R(i%3)}">
  <div class="flex {"flex-col sm:flex-row sm:items-center gap-6" if big else "flex-col items-center text-center gap-4"}"><div class="{"w-28 h-28 text-4xl" if big else "w-24 h-24 text-3xl"} shrink-0 rounded-[1.6rem] bg-gradient-to-br {"from-orange to-sun text-ink" if big else "from-royal-500 to-royal-800 text-white"} grid place-items-center font-display font-extrabold rotate-3" aria-hidden="true">{initial(f["name"])}</div>
  <div class="{"" if big else "w-full"}"><h3 class="text-xl {"text-white" if big else ""}">{E(f["name"])}</h3><p class="font-display font-semibold {"text-sun" if big else "text-orange-600"}">{E(f["role"])}</p>
  <ul class="mt-3 space-y-1 text-[.97rem] {"text-royal-100" if big else "text-royal-800/85"}"><li><b>Qualification:</b> {E(f["qual"])}</li><li><b>Experience:</b> {E(f["exp"])}</li></ul>
  <button type="button" class="btn {"btn-orange" if big else "btn-line-royal"} btn-sm mt-4" data-faculty="{f["id"]}">View profile {ic("arrow")}</button></div></div>
  <template id="fac-{f["id"]}"><div class="w-20 h-20 rounded-2xl bg-gradient-to-br from-royal-500 to-royal-800 text-white grid place-items-center font-display font-extrabold text-2xl mb-4">{initial(f["name"])}</div>
    <h2 class="text-2xl pr-10">{E(f["name"])}</h2><p class="font-display font-semibold text-orange-600">{E(f["role"])}</p>
    <dl class="grid grid-cols-2 gap-3 mt-5 text-sm"><div class="rounded-2xl bg-royal-50 p-3"><dt class="text-royal-800/70">Qualification</dt><dd class="font-display font-bold">{E(f["qual"])}</dd></div><div class="rounded-2xl bg-sun-100 p-3"><dt class="text-royal-800/70">Experience</dt><dd class="font-display font-bold">{E(f["exp"])}</dd></div></dl>
    {f'<p class="mt-5 text-lg">{E(f["bio"])}</p>' if f["bio"] else ""}
    <h3 class="text-base mt-6 mb-2">In every CSP class you can expect</h3><ul class="space-y-1.5 text-[.97rem]"><li class="flex gap-2">{ic("check","text-orange mt-1 w-4 h-4")}Exam-oriented teaching</li><li class="flex gap-2">{ic("check","text-orange mt-1 w-4 h-4")}Regular doubt clearing and personal guidance</li><li class="flex gap-2">{ic("check","text-orange mt-1 w-4 h-4")}Weekly tests with performance analysis</li></ul>
    <div class="mt-6 flex gap-3 flex-wrap"><button class="btn btn-orange" type="button" data-lead data-title="Book a Free Demo Class" data-source="faculty-{f["id"]}">Book free demo</button><a class="btn btn-line-royal" target="_blank" rel="noopener" href="{wa_link("Hello CSP Coaching, I want to meet " + f["name"] + ".")}">{ic("wa")} WhatsApp</a></div></template></article>'''
    approach = [("room","Exam-oriented teaching","Experienced faculty, whiteboard and smart teaching."),("chat","Doubt clearing","Regular doubt clearing and personal guidance."),("test","Weekly tests","Mock tests with detailed performance analysis."),("dumbbell","Physical training","Daily training for Defence and Police aspirants.")]
    ap = "".join(f'<div class="card p-5 flex gap-4 {R(i%3)}"><span class="w-12 h-12 shrink-0 rounded-2xl bg-orange text-ink grid place-items-center">{ic(a,"w-6 h-6")}</span><div><h3 class="text-lg">{t}</h3><p class="text-royal-800/80 text-[.96rem]">{d}</p></div></div>' for i, (a, t, d) in enumerate(approach))
    return page_header("Faculty &amp; Expert Mentors", "Faculty", "Experienced teachers who bring the right strategy and motivation to every class.") + f'''
<section class="section pt-10"><div class="wrap"><p class="eyebrow">Meet our mentors</p><h2 class="h2 mb-8 max-w-xl">Teachers who know the exam, and the student</h2>
  <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-5">{cards}</div></div></section>
<section class="section bg-royal-50"><div class="wrap"><div class="max-w-2xl mb-8 {R()}"><p class="eyebrow">Teaching approach</p><h2 class="h2">How our faculty teaches</h2></div><div class="grid sm:grid-cols-2 gap-5">{ap}</div></div></section>
{CTA_BAND}'''

# ---------------- RESULTS ----------------
def results():
    air = sorted([s for s in STUDENTS if s[2] == "AIR"], key=lambda s: s[3])
    rank = sorted([s for s in STUDENTS if s[2] == "Rank"], key=lambda s: s[3])
    top = air[:3]
    def podium(s, i):
        big = i == 0
        return f'''<article class="relative overflow-hidden rounded-3xl p-7 {"bg-gradient-to-br from-orange to-sun text-ink md:row-span-1 md:py-12" if big else "bg-white card"} {R(i)}"><p class="font-display font-extrabold text-[7rem] leading-none absolute -right-2 -bottom-4 {"text-white/40" if big else "text-royal-100"} select-none" aria-hidden="true">{s[3]}</p>
  <span class="chip {"bg-ink text-white" if big else "bg-royal-600 text-white"}">{ic("trophy","w-4 h-4")} {s[2]} {s[3]}</span><h3 class="relative mt-4 text-2xl sm:text-3xl" lang="hi">{E(s[0])}</h3><p class="relative {"text-ink/75" if big else "text-royal-800/70"}" lang="hi">{E(s[1])}</p></article>'''
    pod = "".join(podium(s, i) for i, s in enumerate(top))
    def tile(s, k):
        pad = ["py-5", "py-7", "py-6", "py-9"][k % 4]
        return f'''<article class="break-inside-avoid mb-4 card card-hover px-5 {pad} relative overflow-hidden {"bg-royal-600 text-white border-royal-600" if k%5==2 else ""}" data-filter-item data-cat="{s[2].lower()}">
  <div class="flex items-center gap-4"><div class="w-14 h-14 shrink-0 rounded-full {"bg-white/20 text-white" if k%5==2 else "bg-gradient-to-br from-orange to-sun text-ink"} grid place-items-center font-display font-extrabold text-xl" lang="hi" aria-hidden="true">{E(s[0][0])}</div>
  <div class="min-w-0"><h3 class="text-lg {"text-white" if k%5==2 else ""}" lang="hi">{E(s[0])}</h3><p class="text-sm {"text-royal-100" if k%5==2 else "text-royal-800/70"}" lang="hi">{E(s[1]) if s[1] else "CSP Coaching student"}</p></div>
  <span class="ml-auto chip {"bg-sun text-ink" if k%5==2 else "bg-royal-50 text-royal-700"}">{s[2]} {s[3]}</span></div></article>'''
    rest = [s for s in air[3:]] + rank
    tiles = "".join(tile(s, k) for k, s in enumerate(rest))
    chips = "".join(f'<button type="button" class="filter-chip px-5 min-h-[46px] rounded-full font-display font-semibold border-2 border-royal-200 aria-pressed:bg-royal-600 aria-pressed:text-white aria-pressed:border-royal-600 hover:border-royal-500 transition" data-filter="{k}" aria-pressed="{"true" if k=="all" else "false"}">{t}</button>' for k, t in [("all","All achievers"),("air","AIR"),("rank","Rank")])
    return page_header("Results &amp; Toppers", "Results", "Meet the students who turned hard work and the right guidance into rank. Proud results from CSP Coaching.") + f'''
<section class="section pt-10"><div class="wrap"><p class="eyebrow">Top achievers</p><h2 class="h2 mb-8">Best of the best</h2><div class="grid md:grid-cols-3 gap-4 items-stretch">{pod}</div>
  <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 mt-6 text-center"><div class="rounded-2xl bg-royal-50 p-4"><b class="block font-display text-3xl text-royal-600">{len(STUDENTS)}</b><span class="text-sm">Featured achievers</span></div><div class="rounded-2xl bg-sun-100 p-4"><b class="block font-display text-3xl text-orange-600">AIR {air[0][3]}</b><span class="text-sm">Best AIR listed</span></div><div class="rounded-2xl bg-royal-50 p-4"><b class="block font-display text-3xl text-royal-600">Rank {rank[0][3]}</b><span class="text-sm">Best Rank listed</span></div><div class="rounded-2xl bg-sun-100 p-4"><b class="block font-display text-3xl text-orange-600" data-count="500" data-suffix="+">500+</b><span class="text-sm">Total selections</span></div></div></div></section>
<section class="section bg-royal-50"><div class="wrap"><div class="flex flex-wrap items-end justify-between gap-4 mb-8"><div><p class="eyebrow">More achievers</p><h2 class="h2">Every name is a story of effort</h2></div><div class="flex gap-2 flex-wrap" data-filters data-target="#result-grid" role="group" aria-label="Filter results">{chips}</div></div>
  <div class="columns-1 sm:columns-2 lg:columns-3 gap-4" id="result-grid">{tiles}</div></div></section>
<section class="section"><div class="wrap grid lg:grid-cols-2 gap-6"><div class="rounded-3xl bg-ink text-white p-8 {R()}"><span class="chip bg-sun text-ink mb-3">What drives results</span><h2 class="text-3xl">Weekly tests. Honest analysis. Daily practice.</h2><p class="text-royal-200 mt-3">Students improve through regular mock exams, performance analysis, doubt clearing and, for Defence and Police, daily physical training.</p></div>
  <div class="rounded-3xl bg-gradient-to-br from-orange to-sun p-8 flex flex-col justify-center {R(1)}"><h2 class="text-3xl text-ink">Your name could be next</h2><p class="text-ink/80 mt-2">Attend a free demo class and see how we prepare you.</p><div class="mt-5"><button class="btn bg-royal-900 text-white hover:bg-royal-700" type="button" data-lead data-title="Book a Free Demo Class" data-source="results-cta">Book Free Demo</button></div></div></div></section>'''

# ---------------- GALLERY ----------------
GAL = [("classroom-wide","Classroom session","classroom"),("girl-focus","Focused exam practice","exam"),("teacher-guidance","Teacher guiding a student","classroom"),
       ("exam-hall-right","Test day","exam"),("back-row","Students at work","classroom"),("left-desk","Writing practice","exam")]
FACS = [("lock","CCTV surveillance","Students' safety is monitored."),("bed","Hostel","Safe, affordable hostel near the institute."),("dumbbell","Physical training ground","Running, push-ups, long jump and height practice."),
        ("book","Study material","PDF notes and printed material."),("room","Smart classrooms","Whiteboard and smart teaching."),("check-circle","Clean water & washrooms","Safe drinking water and clean washrooms.")]
def gallery():
    chips = "".join(f'<button type="button" class="filter-chip px-5 min-h-[46px] rounded-full font-display font-semibold border-2 border-royal-200 aria-pressed:bg-royal-600 aria-pressed:text-white aria-pressed:border-royal-600 hover:border-royal-500 transition" data-filter="{k}" aria-pressed="{"true" if k=="all" else "false"}">{t}</button>' for k, t in [("all","All"),("classroom","Classroom"),("exam","Exam practice"),("facilities","Facilities")])
    slides = "".join(f'<div class="w-full" role="group" aria-roledescription="slide"><div class="relative aspect-[16/9] sm:aspect-[21/9] bg-royal-900"><img src="assets/img/gallery/{i}.webp" alt="{c}" class="absolute inset-0 w-full h-full object-cover" {"" if k==0 else "loading=\"lazy\""}><div class="absolute inset-0 bg-gradient-to-t from-royal-950/80 to-transparent"></div><p class="absolute bottom-4 left-5 sm:bottom-6 sm:left-8 text-white font-display font-bold text-xl sm:text-3xl">{c}</p></div></div>' for k, (i, c, _) in enumerate(GAL))
    photos = "".join(f'<button type="button" class="group relative overflow-hidden rounded-3xl text-left {["row-span-2","","","row-span-2","",""][k]} {R(k%3)}" data-filter-item data-cat="{cat}" data-lightbox data-src="assets/img/gallery/{i}.webp" data-caption="{c}"><img src="assets/img/gallery/{i}.webp" alt="{c}" loading="lazy" class="w-full h-full min-h-[200px] object-cover group-hover:scale-105 transition duration-500"><span class="absolute inset-x-0 bottom-0 p-4 bg-gradient-to-t from-royal-950/85 to-transparent text-white font-display font-semibold flex justify-between items-center">{c}{ic("expand","w-5 h-5")}</span></button>' for k, (i, c, cat) in enumerate(GAL))
    facs = "".join(f'<div class="card p-6 bg-gradient-to-br from-white to-sun-100 flex flex-col justify-end min-h-[200px] {R(k%3)}" data-filter-item data-cat="facilities"><span class="w-14 h-14 rounded-2xl bg-royal-600 text-white grid place-items-center mb-auto">{ic(a,"w-7 h-7")}</span><h3 class="text-xl mt-6">{t}</h3><p class="text-royal-800/80 text-[.96rem]">{d}</p></div>' for k, (a, t, d) in enumerate(FACS))
    return page_header("Infrastructure &amp; Gallery", "Gallery", "A look at our classrooms, exam practice and the facilities that keep students focused.") + f'''
<section class="section pt-10"><div class="wrap">
  <div class="relative rounded-[2rem] overflow-hidden shadow-lift" data-slider data-autoplay data-single role="region" aria-roledescription="carousel" aria-label="Featured photos">
    <div class="slider-track" data-slider-track>{slides}</div>
    <button type="button" class="absolute left-3 top-1/2 -translate-y-1/2 w-12 h-12 grid place-items-center rounded-full bg-white/90 text-royal-900 hover:bg-sun" data-slider-prev aria-label="Previous photo">{ic("left")}</button>
    <button type="button" class="absolute right-3 top-1/2 -translate-y-1/2 w-12 h-12 grid place-items-center rounded-full bg-white/90 text-royal-900 hover:bg-sun" data-slider-next aria-label="Next photo">{ic("right")}</button>
    <div class="absolute bottom-4 right-5 flex gap-2" data-dots></div></div></div></section>
<section class="section bg-royal-50 pt-12"><div class="wrap"><div class="flex flex-wrap items-end justify-between gap-4 mb-8"><div><p class="eyebrow">Photo gallery</p><h2 class="h2">Life at CSP Coaching</h2></div><div class="flex gap-2 flex-wrap" data-filters data-target="#gal-grid" role="group" aria-label="Filter gallery">{chips}</div></div>
  <div class="grid grid-cols-2 lg:grid-cols-3 auto-rows-[190px] sm:auto-rows-[230px] gap-3 sm:gap-4" id="gal-grid">{photos}{facs}</div></div></section>
{CTA_BAND}'''

# ---------------- CONTACT ----------------
def contact():
    acts = [("phone","Call us",PHONE_DISPLAY,f"tel:{PHONE_TEL}","bg-royal-600 text-white",""),("wa","WhatsApp","Chat instantly",wa_link("Hello CSP Coaching, I have a question."),"bg-[#168f47] text-white",'target="_blank" rel="noopener"'),
            ("mail","Email",EMAIL,f"mailto:{EMAIL}","bg-orange text-ink",""),("clock","Working hours","Mon – Sat, 10 AM – 6 PM","#form","bg-sun text-ink","")]
    cards = "".join(f'<a href="{h}" {x} class="card card-hover p-5 flex items-center gap-4 {R(i%3)}"><span class="w-14 h-14 shrink-0 rounded-2xl {c} grid place-items-center">{ic(a,"w-6 h-6")}</span><span><b class="block font-display">{t}</b><span class="text-royal-800/80 break-all">{d}</span></span></a>' for i, (a, t, d, h, c, x) in enumerate(acts))
    return page_header("Contact &amp; Admission Inquiry", "Contact", "Visit us in Kuchaman City, call, or send an enquiry. We will help you choose the right course.") + f'''
<section class="section pt-10"><div class="wrap"><div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-4 mb-12">{cards}</div>
  <div class="grid lg:grid-cols-2 gap-8 items-start">
    <div class="card p-6 sm:p-9 scroll-mt-28 {R()}" id="form"><p class="eyebrow">Admission inquiry</p><h2 class="text-3xl mb-1">Send us your details</h2><p class="text-royal-800/80 mb-6">Fill in the form and our team will contact you.</p>{lead_form("contact-form")}</div>
    <div class="{R(1)}"><div class="rounded-3xl overflow-hidden border border-royal-100 shadow-card"><iframe title="CSP Coaching location on Google Maps" src="{MAP}" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen class="w-full h-[360px] sm:h-[440px] border-0 block"></iframe></div>
      <div class="mt-4 card p-5 flex gap-4 items-start">{ic("pin","w-6 h-6 text-orange mt-1")}<div><b class="font-display">CSP Coaching</b><p class="text-royal-800/80">Kuchaman City, Rajasthan, India</p><p class="text-sm text-royal-800/70 mt-1">Monday to Saturday, 10 AM to 6 PM</p></div></div></div></div></div></section>
<section class="section bg-royal-50 pt-12"><div class="wrap grid lg:grid-cols-[.8fr_1.2fr] gap-10"><div><p class="eyebrow">Before you visit</p><h2 class="h2">Quick answers</h2></div><div class="space-y-3">{faq()}</div></div></section>'''

PAGES = {
 "index.html": ("index.html", "CSP Coaching, Kuchaman City | Defence, Police, SSC & Railway Exam Coaching", "CSP Coaching in Kuchaman City: expert faculty, weekly tests, physical training and hostel for Defence, Police, SSC and Railway exams. Book a free demo class.", home),
 "about.html": ("about.html", "About CSP Coaching | Director's Desk & Our Journey", "Know CSP Coaching, Kuchaman City: our story, director's message, core values and how students grow with us.", about),
 "courses.html": ("courses.html", "Courses & Fees | CSP Coaching, Kuchaman City", "NDA, Defence, Police, Railway, SSC, physical fitness and 8th-12th courses with timings and fee plans. Download the brochure.", courses),
 "faculty.html": ("faculty.html", "Faculty & Mentors | CSP Coaching, Kuchaman City", "Meet the experienced faculty of CSP Coaching and learn how they teach.", faculty),
 "results.html": ("results.html", "Results & Toppers | CSP Coaching, Kuchaman City", "AIR and rank achievers of CSP Coaching, Kuchaman City.", results),
 "gallery.html": ("gallery.html", "Gallery & Facilities | CSP Coaching, Kuchaman City", "Photos of CSP Coaching classrooms, exam practice and facilities including hostel, CCTV and physical training.", gallery),
 "contact.html": ("contact.html", "Contact & Admission Inquiry | CSP Coaching, Kuchaman City", "Call, WhatsApp or send an admission enquiry to CSP Coaching, Kuchaman City. Find us on Google Maps.", contact),
}
if __name__ == "__main__":
    for fn, (act, t, d, fnc) in PAGES.items():
        open(fn, "w", encoding="utf-8").write(page(act, t, d, fnc()))
    print("built", len(PAGES), "pages")
