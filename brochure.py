from build_common import *
from playwright.sync_api import sync_playwright
rows="".join(f"<tr><td><b>{E(c['name'])}</b><br><small>{E(c['exams'])}</small></td><td>{E(c['time'])}</td><td>{E(c['feeRange'])}</td></tr>" for c in COURSES)
fac="".join(f"<li>{t}</li>" for t in ["Experienced faculty with exam-oriented teaching","Whiteboard and smart teaching","PDF notes and printed study material","Weekly tests, mock exams and performance analysis","Regular doubt clearing and personal guidance","Daily physical training for Defence and Police exams","CCTV surveillance, safe drinking water, clean washrooms","Free demo class before admission"])
h=f"""<html><head><meta charset=utf-8><style>
body{{font-family:Arial,Helvetica,sans-serif;color:#0b1c50;margin:0}} .hd{{background:#1f44b8;color:#fff;padding:34px 40px;border-bottom:8px solid #ff8a1f}}
h1{{margin:0;font-size:34px}} .hd p{{margin:6px 0 0;color:#ffc21a;font-weight:bold}} .c{{padding:26px 40px}}
h2{{color:#1f44b8;border-left:6px solid #ff8a1f;padding-left:10px;font-size:20px}} table{{width:100%;border-collapse:collapse;font-size:13px}}
th{{background:#0b1c50;color:#fff;text-align:left;padding:9px}} td{{padding:9px;border-bottom:1px solid #dce7ff;vertical-align:top}} small{{color:#555}}
li{{margin:4px 0;font-size:14px}} .box{{background:#fff4d1;border-radius:10px;padding:14px 18px;margin-top:16px;font-size:14px}}
</style></head><body><div class=hd><h1>CSP Coaching</h1><p>Kuchaman City, Rajasthan · Defence · Police · SSC · Railway</p></div><div class=c>
<h2>Courses, timings and fees</h2><table><tr><th>Course</th><th>Class time</th><th>Fee</th></tr>{rows}</table>
<p style="font-size:12px;color:#555">Contact us for 8th-12th and tuition fees.</p>
<h2>Facilities</h2><ul>{fac}</ul>
<div class=box><b>Hostel:</b> safe hostel near the institute, Rs. 5,000 per month, no hidden charges.</div>
<h2>Contact</h2><p style="font-size:14px">Phone / WhatsApp: {PHONE_DISPLAY}<br>Email: {EMAIL}<br>Address: Kuchaman City, Rajasthan<br>Hours: Monday to Saturday, 10 AM to 6 PM</p></div></body></html>"""
open("/tmp/brochure.html","w").write(h)
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(); pg.goto("file:///tmp/brochure.html"); pg.pdf(path="assets/docs/CSP-Coaching-Brochure.pdf",format="A4",print_background=True); b.close()
