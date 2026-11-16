# CSP Coaching: 7-page website (Royal Blue + White + Orange/Yellow)

Pages: index, about, courses, faculty, results, gallery, contact (.html). Built with Tailwind CSS (compiled) and vanilla JavaScript. No framework.

## Run
    python3 -m http.server 8000        # open http://localhost:8000
Or upload everything in this folder to any static host (Netlify, Cloudflare Pages, GitHub Pages, cPanel).

## Where to edit
- Phone, email, WhatsApp, Supabase keys: `assets/js/config.js` (WhatsApp number also appears in the HTML links).
- Courses, faculty, results, FAQ: the data lists at the top of `build_common.py` / `build_pages.py`, then run `python3 build_pages.py` (and `python3 brochure.py` to refresh the PDF).
- Styles: Tailwind classes in the pages; colours in `tailwind.config.js`. Rebuild CSS: `npm i && npx tailwindcss -i src/input.css -o assets/css/site.css --minify`.

## Saving enquiries in Supabase (optional)
1. Create a project at supabase.com. In the SQL editor run:

       create table inquiries (id bigint generated always as identity primary key, created_at timestamptz default now(),
         name text, phone text, course text, target_year text, message text, source text);
       create table subscribers (id bigint generated always as identity primary key, created_at timestamptz default now(), email text);
       alter table inquiries enable row level security; alter table subscribers enable row level security;
       create policy "anon can insert" on inquiries for insert to anon with check (true);
       create policy "anon can insert" on subscribers for insert to anon with check (true);

2. Put the Project URL and the `anon` public key in `assets/js/config.js`.
3. Read the leads in the Supabase dashboard (Table editor). Anonymous visitors can only add rows, not read them.
Until the keys are filled in, every form opens WhatsApp with the details ready to send.

## Gallery photos
The gallery currently uses crops of one classroom image. Add your real photos to `assets/img/gallery/` and list them in `GAL` in `build_pages.py`.
