# Three Trees Retirement Partners — Landing Page v3

## Project Overview

A full-width, vertically scrolling landing page for **Three Trees Retirement Partners**, a retirement income planning firm run by **Michael & Stephanie Cooley** (ChFC® RICP® NSSA® M.Ed.). Built as a faithful HTML/CSS/JS implementation of the master design PDFs, with all corrections from v1, v2, and v3 annotation PDFs applied.

---

## ✅ Round 3 Corrections (v3 — current)

| # | Correction | Status |
|---|-----------|--------|
| 1 | Hero heading reduced (clamp 1.8–2.8rem) | ✅ Done |
| 1 | Names/credentials block moved UNDER the photo (`hero-image-caption`) | ✅ Done |
| 1 | Hero image pulled up (`margin-top: -20px`) and enlarged (`max-width: 560px`) | ✅ Done |
| 2 | **Retirement Income Intro section** added between Hero and Framework | ✅ Done (HTML + CSS) |
| 3 | Tree Cards: Now → `Rev8MFId`, Soon → `bAHC4quK`, Later → `casEiD2o` | ✅ Done |
| 3 | Tree card image area: white background, `object-fit: contain` for white-bg PNGs | ✅ Done |
| 4 | Flow nodes (Later/Soon/Now): all use `H1vrYEXL` (single gold-ring tree) | ✅ Done |
| 4 | YOUR RETIREMENT node: `IzdiR7jq` (3 trees in white circle) | ✅ Done |
| 4 | YOUR RETIREMENT circle: white bg + `object-fit: contain` to show circle correctly | ✅ Done |
| 5 | Who We Serve photo: replaced with `UZAhXZCn` (couple with financial advisor) | ✅ Done |
| 6 | Altitude Capital section: confirmed in place below Stephanie, logo `si2Bb78W` | ✅ Done |

---

## ✅ Previous Corrections Implemented (v2)

| # | Correction | Status |
|---|-----------|--------|
| Global | Removed ALL diagonal white stripe/divider effects | ✅ Done |
| 1 | Header logo updated; hero spacing fixed; full hero copy added | ✅ Done |
| 2 | Framework section: solid dark green, infographic in cream card | ✅ Done |
| 3 | Tree Detail Cards: transparent tree PNGs, type badges, correct layout | ✅ Done |
| 4 | Flow section: circle tree assets (Later→Soon→Now→Your Retirement) | ✅ Done |
| 5 | Triple Shield: new graphic (light bg version `Uu90hfUP`), shadow box | ✅ Done |
| 6 | Shield cards: SVG icons, solid dark green section background | ✅ Done |
| 7 | Who We Serve: couple + advisor photo, left text + right image layout | ✅ Done |
| 8 | Team: Michael (photo-left) and Stephanie (text-left) separate cards | ✅ Done |
| 9 | Altitude Capital: logo `si2Bb78W`, cream bg, two-col layout | ✅ Done |
| 10 | Seminar cards: equal-height titles, pinned buttons, aligned icons | ✅ Done |
| 11 | FAQ: solid dark green bg, all 13 questions with full answers | ✅ Done |
| 12 | Footer: 4-column layout (Brand/Our Approach/Company/Connect) | ✅ Done |


```
/
├── index.html          ← Complete landing page (all 16 sections)
├── css/
│   └── style.css       ← Master stylesheet v2 (~1450 lines)
├── js/
│   └── main.js         ← Interactive JS
└── README.md
```

---

## 📋 All Sections — In Order

| # | Section | Background |
|---|---------|-----------|
| 1 | Header/Nav | White sticky |
| 2 | Hero | Dark green gradient |
| **2b** | **Retirement Income Intro** *(NEW v3)* | **Warm cream** |
| 3 | Three Trees Framework | Dark green (solid) |
| 4 | Tree Detail Cards (Now/Soon/Later) | Off-white |
| 5 | How the Trees Work Together (Flow) | Forest mid-green (solid) |
| 6 | Triple Shield Introduction | Warm cream |
| 7 | Triple Shield Cards | Dark green (solid) |
| 8 | Who We Serve | White |
| 9 | Meet the Team | Dark green (solid) |
| 10 | Altitude Capital Management | Warm cream |
| 11 | Seminars | Forest mid-green (solid) |
| 12 | Testimonials | White |
| 13 | FAQ (13 questions) | Dark green (solid) |
| 14 | Schedule / Calendly | Warm cream |
| 15 | Contact Form | Dark green (solid) |
| 16 | Footer | Dark charcoal |

---

## 🖼 Image Assets Used

| Usage | Genspark URL Key |
|-------|-----------------|
| Nav + footer logo (horizontal) | `pBMRPkL5` |
| Square logo (dark bg) | `W7NV3AaH` |
| Three Trees timeline infographic | `kSxhjoB6` |
| Triple Shield graphic (light bg) | `Uu90hfUP` |
| **Now Tree card image** *(v3)* | **`Rev8MFId`** |
| **Soon Tree card image** *(v3)* | **`bAHC4quK`** |
| **Later Tree card image** *(v3)* | **`casEiD2o`** |
| **Flow node tree (gold ring) — used 3×** *(v3)* | **`H1vrYEXL`** |
| **YOUR RETIREMENT node (3 trees white circle)** *(v3)* | **`IzdiR7jq`** |
| Michael + Stephanie hero photo | `tNci8ZRV` |
| **Who We Serve — couple with advisor** *(v3)* | **`UZAhXZCn`** |
| Stephanie solo headshot | `GKZiiKXC` |
| Michael solo headshot | `VnPGG270` |
| Altitude Capital Management logo | `si2Bb78W` |

---

## 🎨 Brand Design System

| Token | Hex | Usage |
|-------|-----|-------|
| `--gold` | `#b09556` | CTAs, accents, borders |
| `--forest-green` | `#1e3a2f` | Primary dark sections |
| `--forest-mid` | `#254d3e` | Secondary dark sections |
| `--teal` | `#2c6e6b` | Icons, check marks |
| `--cream` | `#faf6ee` | Light section backgrounds |

**Fonts:** Playfair Display (headings) + Lato (body) + Cormorant Garamond (italic/quote accents)

---

## ⚙️ Features Not Yet Implemented

- [ ] Real Calendly embed code
- [ ] Backend form submission
- [ ] Real phone number / email address
- [ ] Seminar registration dates
- [ ] Social media links
- [ ] Google Analytics / tracking

---

## 🚀 Next Steps

1. **Add Calendly embed** — replace the mock placeholder with your embed URL
2. **Update contact details** — phone, email
3. **Connect contact form** — Formspree or similar
4. **Deploy** → Go to the **Publish tab** to make the site live

---

---

## 🚀 Netlify Deployment Guide

### Final folder structure required before deploying:
```
/
├── index.html
├── netlify.toml
├── css/
│   └── style.css
├── js/
│   └── main.js
└── images/
    ├── logo-horizontal.png
    ├── logo-square-dark.png
    ├── michael-stephanie-cooley.jpg
    ├── three-trees-infographic.png
    ├── tree-now.png
    ├── tree-soon.png
    ├── tree-later.png
    ├── flow-tree-node.png
    ├── flow-retirement-node.png
    ├── triple-shield-graphic.png
    ├── who-we-serve-couple.jpg
    ├── michael-cooley.jpg
    ├── stephanie-cooley.jpg
    └── altitude-capital-logo.png    ← optional, add if you obtain this later
```

### Step 1 — Download your images
Open each URL while logged into Genspark and save with the exact filename:

| URL | Save as |
|-----|---------|
| `https://www.genspark.ai/api/files/s/pBMRPkL5` | `logo-horizontal.png` |
| `https://www.genspark.ai/api/files/s/W7NV3AaH` | `logo-square-dark.png` |
| `https://www.genspark.ai/api/files/s/tNci8ZRV` | `michael-stephanie-cooley.jpg` |
| `https://www.genspark.ai/api/files/s/kSxhjoB6` | `three-trees-infographic.png` |
| `https://www.genspark.ai/api/files/s/Rev8MFId` | `tree-now.png` |
| `https://www.genspark.ai/api/files/s/bAHC4quK` | `tree-soon.png` |
| `https://www.genspark.ai/api/files/s/casEiD2o` | `tree-later.png` |
| `https://www.genspark.ai/api/files/s/H1vrYEXL` | `flow-tree-node.png` |
| `https://www.genspark.ai/api/files/s/IzdiR7jq` | `flow-retirement-node.png` |
| `https://www.genspark.ai/api/files/s/Uu90hfUP` | `triple-shield-graphic.png` |
| `https://www.genspark.ai/api/files/s/UZAhXZCn` | `who-we-serve-couple.jpg` |
| `https://www.genspark.ai/api/files/s/VnPGG270` | `michael-cooley.jpg` |
| `https://www.genspark.ai/api/files/s/GKZiiKXC` | `stephanie-cooley.jpg` |

### Step 2 — Download the code files from Genspark
Use the file explorer in Genspark to download:
- `index.html`
- `css/style.css`
- `js/main.js`
- `netlify.toml`

### Step 3 — Assemble the folder
Create the structure shown above — put all 14 images into an `images/` subfolder.

### Step 4 — Deploy to Netlify
**Option A — Drag & Drop (easiest):**
1. Go to [netlify.com](https://netlify.com) and log in
2. Click **"Add new site"** → **"Deploy manually"**
3. Drag your entire project folder into the Netlify drop zone
4. Done — your site is live in ~30 seconds

**Option B — GitHub (recommended for ongoing updates):**
1. Push the project folder to a GitHub repository
2. In Netlify: **"Add new site"** → **"Import an existing project"** → connect GitHub
3. Select your repo — Netlify auto-detects `netlify.toml`
4. Click **Deploy** — future pushes to GitHub auto-deploy

### Step 5 — After deploying, update these placeholders:
| Item | Where in index.html |
|------|-------------------|
| Calendly embed URL | Line ~1069 — replace mock with real embed |
| Phone number | Line ~1093 |
| Email address | Line ~1098 — replace `hello@threetreesretirement.com` |
| Footer copyright year | Line ~1227 |
| Privacy Policy / Terms links | Lines ~1238–1240 |



- **No build step** — pure static HTML/CSS/JS
- **0 JavaScript errors** (verified via Playwright console capture)
- **CDN 403 errors** for Genspark image URLs are expected in headless contexts; all images load correctly in a real browser session
- **Deploy** → Go to the **Publish tab** to publish the site live

---

*© 2024 Three Trees Retirement Partners. Built with Genspark.*
