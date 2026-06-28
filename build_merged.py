from pathlib import Path
from textwrap import dedent

ROOT = Path('/home/user/threetrees_final')

EXTRA = '''
<style>
  .page-hero {background: linear-gradient(145deg,#162e24 0%,#1e3a2f 55%,#254d3e 100%);padding:150px 0 80px;text-align:center;position:relative;overflow:hidden;}
  .page-hero::before {content:'';position:absolute;inset:0;background:radial-gradient(ellipse 70% 60% at 50% 110%, rgba(176,149,86,0.10) 0%, transparent 70%);pointer-events:none;}
  .page-hero .container {position:relative;z-index:1;}
  .page-hero-eyebrow {font-size:.7rem;font-weight:700;letter-spacing:.28em;text-transform:uppercase;color:#c9ac6a;margin-bottom:18px;display:block;}
  .page-hero-title {font-family:'Playfair Display', Georgia, serif;font-size:clamp(2.2rem,5vw,3.6rem);font-weight:700;color:#fff;line-height:1.15;margin-bottom:20px;}
  .page-hero-sub {font-size:1.1rem;color:rgba(255,255,255,.72);max-width:760px;margin:0 auto 36px;line-height:1.85;}
  .page-hero-ctas {display:flex;justify-content:center;gap:16px;flex-wrap:wrap;}
  .breadcrumb {display:flex;align-items:center;gap:8px;justify-content:center;margin-bottom:22px;font-size:.78rem;color:rgba(255,255,255,.45);}
  .breadcrumb a {color:#c9ac6a;}
  .breadcrumb i {font-size:.6rem;}
  .planning-section,.content-section,.light-section,.legal-content {padding:100px 0;}
  .planning-section {background:var(--cream);}
  .planning-grid,.content-grid,.cta-grid,.legal-grid {display:grid;grid-template-columns:1fr 1fr;gap:70px;align-items:center;}
  .photo-card img,.image-card img {width:100%;border-radius:16px;box-shadow:0 18px 60px rgba(0,0,0,.16);object-fit:cover;}
  .content-section {background:var(--white);}
  .light-section {background:var(--cream);}
  .copy-body {font-size:1.02rem;line-height:1.88;color:var(--body-text);margin-bottom:18px;}
  .copy-body-light {font-size:1.02rem;line-height:1.88;color:rgba(255,255,255,.74);margin-bottom:18px;}
  .mini-cards-3,.mini-cards-4,.mini-cards-5 {display:grid;gap:24px;align-items:stretch;}
  .mini-cards-3 {grid-template-columns:repeat(3,1fr);} .mini-cards-4 {grid-template-columns:repeat(4,1fr);} .mini-cards-5 {grid-template-columns:repeat(5,1fr);} 
  .mini-card {background:#fff;border:1px solid var(--cream-border);border-radius:16px;padding:30px 24px;box-shadow:var(--shadow-card);height:100%;}
  .mini-card h3,.mini-card h4 {font-family:var(--font-serif);color:var(--forest-green);margin-bottom:10px;line-height:1.25;}
  .mini-card p {font-size:.95rem;line-height:1.8;color:var(--body-text);}
  .note-panel {background:rgba(255,255,255,.08);color:#fff;border:1px solid rgba(255,255,255,.12);border-radius:16px;padding:24px 26px;margin-top:30px;}
  .question-stack {display:grid;gap:14px;margin:26px 0 30px;}
  .question-item {background:var(--cream);border:1px solid var(--cream-border);padding:18px 20px;border-radius:12px;font-family:var(--font-serif);font-size:1.08rem;color:var(--forest-green);}
  .cta-strip {background:var(--forest-green);padding:80px 0;text-align:center;}
  .cta-strip p {max-width:680px;margin:0 auto 30px;color:rgba(255,255,255,.72);font-size:1.04rem;line-height:1.8;}
  .policy-panel {background:#fff;border:1px solid var(--cream-border);border-radius:18px;padding:42px;box-shadow:var(--shadow-card);}
  .policy-panel h2 {font-family:var(--font-serif);color:var(--forest-green);font-size:1.6rem;margin:26px 0 14px;}
  .policy-panel h3 {font-family:var(--font-serif);color:var(--forest-green);font-size:1.2rem;margin:22px 0 10px;}
  .policy-panel p,.policy-panel li {font-size:1rem;line-height:1.85;color:var(--body-text);} .policy-panel ul {list-style:disc;padding-left:22px;display:grid;gap:8px;}
  .site-footer .footer-col:nth-child(5) {grid-column:auto;}
  .footer-disclosure-full {margin-top:18px;font-size:.85rem;line-height:1.8;color:rgba(255,255,255,.56);}
  .brand-intro {font-size:1.02rem;line-height:1.8;color:rgba(255,255,255,.72);margin-bottom:18px;}
  .contact-promises {background:var(--cream);border-bottom:1px solid var(--cream-border);} 
  .contact-promises-grid {display:grid;grid-template-columns:repeat(5,1fr);gap:14px;padding:22px 0;} 
  .contact-promise-item {font-size:.88rem;font-weight:700;color:var(--forest-green);display:flex;gap:10px;align-items:center;justify-content:center;} 
  .contact-promise-item i {color:var(--gold);} 
  .calendly-mock {min-height:360px;border-radius:14px;background:linear-gradient(180deg,#fff 0%,#f5efe3 100%);display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:24px;gap:14px;border:1px solid var(--cream-border);} 
  .calendly-logo {width:72px;height:72px;border-radius:50%;object-fit:cover;}
  .legal-hero {background: linear-gradient(145deg,#162e24 0%,#1e3a2f 50%,#254d3e 100%);padding:140px 0 70px;text-align:center;}
  .legal-hero h1 {font-family:var(--font-serif);font-size:clamp(2rem,4vw,3.1rem);color:#fff;margin-bottom:16px;} 
  .legal-hero p {max-width:700px;margin:0 auto;color:rgba(255,255,255,.72);line-height:1.8;font-size:1.03rem;}
  @media (max-width: 1100px){.mini-cards-5{grid-template-columns:repeat(3,1fr);} .contact-promises-grid{grid-template-columns:repeat(2,1fr);} }
  @media (max-width: 900px){.planning-grid,.content-grid,.cta-grid,.legal-grid,.contact-container,.schedule-container,.identity-container,.retirement-intro-container,.hero-container,.team-card-michael,.team-card-stephanie{grid-template-columns:1fr !important;} .mini-cards-3,.mini-cards-4,.mini-cards-5,.tree-cards-grid,.seminars-cards,.footer-grid,.altitude-cards-grid{grid-template-columns:1fr !important;} .contact-promises-grid{grid-template-columns:1fr;} .process-flow{flex-direction:column;gap:20px;} .process-connector{transform:rotate(90deg);} }
</style>
'''

NAV = [
    ('About Us','framework.html','about'),
    ('Tax Strategy','tax-strategy.html','tax'),
    ('Triple Shield','triple-shield.html','triple'),
    ('Seminars','seminars.html','seminars'),
    ('FAQ','faqs.html','faq'),
    ('Contact Us','contact.html','contact'),
]

FOOTER = '''
<footer class="site-footer">
  <div class="container footer-grid">
    <div class="footer-col footer-brand">
      <img src="images/logo-square-dark.png" alt="Three Trees Retirement Partners" class="footer-logo" />
      <p class="footer-tagline">Retirement income planning for the distribution phase. Serving pre-retirees and retirees in Ann Arbor and Washtenaw County, Michigan.</p>
    </div>
    <div class="footer-col">
      <h4 class="footer-col-heading">Navigation</h4>
      <ul class="footer-links">
        <li><a href="index.html">Home</a></li>
        <li><a href="framework.html">About Us</a></li>
        <li><a href="tax-strategy.html">Tax Strategy</a></li>
        <li><a href="triple-shield.html">The Triple Shield</a></li>
        <li><a href="seminars.html">Seminars</a></li>
        <li><a href="faqs.html">FAQ</a></li>
        <li><a href="contact.html">Contact</a></li>
      </ul>
    </div>
    <div class="footer-col">
      <h4 class="footer-col-heading">Risk Assessment</h4>
      <a href="https://app.onpointeriskanalyzer.com/entryform/FD3D33E3-1408-4E26-8DBF-084356C13E58" class="btn btn-gold footer-cta-btn" target="_blank" rel="noopener">GET YOUR RISK SCORE</a>
    </div>
    <div class="footer-col">
      <h4 class="footer-col-heading">Connect</h4>
      <ul class="footer-links">
        <li><a href="contact.html#schedule">Book a Meeting</a></li>
        <li>825 Victors Way, Ann Arbor</li>
        <li><a href="tel:7342122525">(734) 212-2525</a></li>
        <li><a href="mailto:info@3treesrp.com">info@3treesrp.com</a></li>
        <li><a href="privacy.html">Privacy Policy</a></li>
        <li><a href="terms.html">ADV Part 2 / Disclosures</a></li>
      </ul>
    </div>
  </div>
  <div class="footer-divider"></div>
  <div class="footer-legal container">
    <p class="footer-legal-text">© 2026 ThreeTrees Retirement Partners. All rights reserved.</p>
    <p class="footer-disclosure-full">Investment advice offered through ALTITUDE CAPITAL MANAGEMENT LLC, a Securities and Exchange Commission registered investment advisor able to provide investment advice in states where it is registered, exempt, or excluded from registration. Content contained herein should not be construed as an offer or solicitation for investment advice or for the purchase or sale of any security, insurance, or other investment product. Investments involve the risk of loss, including possible loss of principal. Please consult with a qualified financial, tax, accounting, or legal professional before implementing any ideas or strategies discussed here. Content provided is obtained from sources believed to be reliable but cannot be guaranteed as to its accuracy or completeness.</p>
  </div>
</footer>
'''


def header(active=''):
    links=[]
    for label, href, key in NAV:
        cls='active' if key==active else ''
        links.append(f'<li><a href="{href}" class="{cls}">{label}</a></li>')
    links.append('<li><a href="contact.html#schedule" class="nav-cta-btn">Schedule a Consultation</a></li>')
    return f'''
<header id="site-header">
  <nav class="nav-container">
    <a href="index.html" class="nav-logo"><img src="images/logo-horizontal.png" alt="Three Trees Retirement Partners" /></a>
    <button class="nav-toggle" aria-label="Toggle navigation" aria-expanded="false"><span></span><span></span><span></span></button>
    <ul class="nav-links">{''.join(links)}</ul>
  </nav>
</header>
'''


def page(title, active, body, desc=''):
    return dedent(f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <meta name="description" content="{desc}" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500&family=Lato:wght@300;400;700;900&family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;1,300;1,400;1,500&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.4.0/css/all.min.css" />
  <link rel="stylesheet" href="css/style.css" />
  {EXTRA}
</head>
<body>
{header(active)}
{body}
{FOOTER}
<script src="js/main.js"></script>
</body>
</html>
''')

home = '''
<main>
<section class="hero-section">
  <div class="container hero-container">
    <div class="hero-content">
      <p class="hero-eyebrow">Three Trees Retirement Partners</p>
      <h1 class="hero-headline">Plan for the Life You've Worked Hard to Achieve</h1>
      <p class="hero-subtext">Tax-efficient retirement income planning for Ann Arbor-area pre-retirees and retirees with $1M to $3M in savings.</p>
      <div class="hero-ctas">
        <a href="contact.html#schedule" class="btn btn-gold">Schedule a Consultation</a>
        <a href="seminars.html" class="btn btn-outline-light">Attend a Free Seminar</a>
      </div>
    </div>
    <div class="hero-image">
      <div class="hero-photo-wrap"><img src="images/michael-stephanie-cooley.jpg" alt="Michael and Stephanie Cooley — Three Trees Retirement Partners" /></div>
      <div class="hero-image-caption"><span class="cred-name">Michael &amp; Stephanie Cooley</span><span class="cred-badges">CHFC® RICP® NSSA® | M.ED.</span></div>
    </div>
  </div>
</section>
<section class="planning-section">
  <div class="container planning-grid">
    <div class="photo-card"><img src="images/who-we-serve-couple.jpg" alt="Three Trees client conversation" /></div>
    <div>
      <span class="section-label">About Us</span>
      <h2 class="section-heading">Planning Today, Preparing for Tomorrow, Prospering the Future</h2>
      <p class="copy-body">At ThreeTrees Retirement Partners, we believe retirement is about more than just having enough money, it's about living the life you've been working toward for decades.</p>
      <p class="copy-body">We help people transition into and through retirement with both financial confidence and personal clarity. Whether you're five years from retirement or already enjoying it, we guide you through the financial decisions AND the life decisions that make retirement meaningful</p>
      <p class="copy-body">Most of our clients are between 55 and 70, have saved $1-3 million, and want to know their money will last while living purposefully and fully in this next chapter.</p>
    </div>
  </div>
</section>
<section class="methodology-section"><div class="container methodology-container"><div class="methodology-header"><span class="section-label-light">Framework</span><h2 class="section-heading-light">The Three Trees Framework</h2><p class="methodology-subtitle">A structured approach to retirement income — so you always know where your next paycheck is coming from.</p></div><p class="copy-body-light" style="max-width:900px;margin:0 auto 34px;">Most retirement plans treat your savings as a single pile of money to draw from. We organize yours into three distinct time horizons — three trees — each with its own purpose, its own asset type, and its own role in producing reliable income</p><div class="methodology-card"><img src="images/three-trees-infographic.png" alt="The Three Trees — Now, Soon, Later infographic" class="three-trees-infographic" /></div></div></section>
<section class="tree-cards-section"><div class="container"><div class="tree-cards-grid">
<article class="tree-card"><div class="tree-card-image-area tree-card-image-now"><img src="images/tree-now.png" alt="Now Tree" class="tree-img-asset" /></div><div class="tree-card-body"><div class="tree-card-label-row"><span class="tree-number-tag">T R E E &nbsp; O N E</span></div><h3 class="tree-card-name">Now Tree</h3><p class="tree-card-subtitle">Year 1 + Permanent Emergency Fund</p><p class="tree-card-desc">Cash &amp; money market funds. Always liquid, always available, immune to market volatility. This is the year you're living right now.</p></div></article>
<article class="tree-card"><div class="tree-card-image-area tree-card-image-soon"><img src="images/tree-soon.png" alt="Soon Tree" class="tree-img-asset" /></div><div class="tree-card-body"><div class="tree-card-label-row"><span class="tree-number-tag">T R E E &nbsp; T W O</span></div><h3 class="tree-card-name">Soon Tree</h3><p class="tree-card-subtitle">Years 2 – 10</p><p class="tree-card-desc">A laddered foundation built to deliver dependable income for the next decade — designed to participate in market upside while protecting your principal from market downturns. The result: a stable income foundation that doesn't sacrifice long-term growth.</p></div></article>
<article class="tree-card"><div class="tree-card-image-area tree-card-image-later"><img src="images/tree-later.png" alt="Later Tree" class="tree-img-asset" /></div><div class="tree-card-body"><div class="tree-card-label-row"><span class="tree-number-tag">T R E E &nbsp; T H R E E</span></div><h3 class="tree-card-name">Later Tree</h3><p class="tree-card-subtitle">Years 11 – 40+</p><p class="tree-card-desc">Tactical growth investments that have time to weather market cycles. Manages long-term wealth and refills the Soon Tree at favorable market moments.</p></div></article>
</div><div class="tree-synergy-note">This synergy framing is essential. Without it, prospects mentally treat Soon and Later as separate, which misrepresents how the framework works.</div></div></section>
<section class="light-section"><div class="container content-grid"><div><span class="section-label">Credentials</span><h2 class="section-heading">Built for Retirement Income</h2><p class="copy-body">The credentials behind ThreeTrees were chosen specifically for this work. Michael holds three designations from The American College of Financial Services — each focused on the planning challenges that matter once you stop earning a paycheck.</p><p class="copy-body"><strong>ChFC® — Chartered Financial Consultant</strong><br><strong>RICP® — Retirement Income Certified Professional</strong><br><strong>NSSA® — National Social Security Advisor</strong></p><p class="copy-body">This is a different toolkit than the generalist CFP credential. It's purpose-built for the question most retirement advisors don't fully solve: how to turn what you've saved into reliable, tax-efficient income that lasts.</p></div><div class="shield-graphic-box"><img src="images/triple-shield-graphic.png" alt="Triple Shield — Market, Tax, and Spending risk" class="shield-graphic-img" /></div></div></section>
<section class="process-section"><div class="container content-grid"><div><span class="section-label-light">Social Security</span><h2 class="section-heading-light">Get Your Social Security Decision Right</h2><p class="copy-body-light">Social Security is one of the most important financial decisions you'll make in retirement—and most people get it wrong. Filing at the wrong time can cost you tens of thousands of dollars over your lifetime.</p><p class="copy-body-light">But it's not just about the numbers. When you file affects your cash flow, your flexibility, and your peace of mind in those critical early retirement years.</p><p class="copy-body-light">We provide personalized Social Security filing analysis within the context of your complete retirement picture—not just "what maximizes dollars" but "what supports the life you want to live."</p></div><div class="mini-card social-security-card"><span class="section-label">Topics we help you navigate</span><ul class="schedule-list"><li><i class="fas fa-check"></i> When to claim for maximum lifetime benefit</li><li><i class="fas fa-check"></i> How spousal and survivor benefits work</li><li><i class="fas fa-check"></i> Tax implications of Social Security income</li></ul><div style="margin-top:28px;"><a href="seminars.html" class="btn btn-gold">Attend OUR SOCIAL SECURITY Seminar</a></div></div></div></section>
<section class="identity-section"><div class="container identity-container"><div><span class="section-label">Who We Serve</span><h2 class="section-heading">Who We Serve</h2><p class="identity-body">Most of our clients are between 55 and 70, have saved $1 million to $3 million, and want clear answers to three questions:</p><div class="question-stack"><div class="question-item">When can I retire?</div><div class="question-item">Will my money last?</div><div class="question-item">How do I keep more of what I've earned from going to taxes?</div></div></div><div class="identity-image"><img src="images/who-we-serve-couple.jpg" alt="Who We Serve" /></div></div></section>
<section class="light-section"><div class="container content-grid"><div class="image-card"><img src="images/michael-cooley.jpg" alt="Michael Cooley" /></div><div><span class="section-label">Meet Michael Cooley ChFC®, RICP®, NSSA®</span><h2 class="section-heading">Meet Michael Cooley ChFC®, RICP®, NSSA®</h2><p class="copy-body">Michael is the founder and lead advisor at ThreeTrees Retirement Partners. He brings advanced retirement income credentials and a structured framework that helps clients see exactly how their financial life works — both today and over the decades ahead.</p><a href="contact.html#schedule" class="btn btn-gold">Schedule a Meeting</a></div></div></section>
<section class="cta-strip"><div class="container"><span class="section-label-light">Take the First Step</span><h2 class="section-heading-light">Ready to See What Your Retirement Plan Should Look Like?</h2><p>Schedule a complimentary consultation to explore how the Three Trees framework applies to your specific situation. Most first conversations take 30 minutes.</p><a href="contact.html#schedule" class="btn btn-gold">Schedule a Consultation</a></div></section>
</main>
'''

about = '''
<main>
<section class="page-hero about-page-hero">
  <div class="container">
    <div class="breadcrumb"><a href="index.html">Home</a><i class="fas fa-chevron-right"></i><span>About Us</span></div>
    <span class="page-hero-eyebrow">About Us</span>
    <h1 class="page-hero-title">About ThreeTrees Retirement Partners</h1>
    <p class="page-hero-sub">A retirement income planning practice built on a single idea: structure beats prediction.</p>
  </div>
</section>
<section class="content-section about-intro-section">
  <div class="container" style="max-width:900px;">
    <p class="copy-body">ThreeTrees Retirement Partners was founded to solve a specific problem: most retirement plans don't actually have a structure. They have a number — a target balance, a withdrawal rate, an asset allocation — but no system that tells the client exactly where each year's income will come from, how taxes will be managed, and what happens when the market moves.</p>
    <p class="copy-body">We built ThreeTrees around a structured framework — three time-segmented buckets, three layers of protection — so our clients always know how their plan works, not just what it earned last quarter.</p>
    <p class="copy-body">Our clients are typically pre-retirees and retirees in the Ann Arbor area with $1 million to $3 million saved. They've done the hard work of accumulating. Our job is to help them turn what they've saved into reliable, tax-efficient income for the next 20 to 40 years — because the goal of retirement planning isn't to ration what you've built. It's to use it well.</p>
    <p class="copy-body"><strong>Retire longer, not leaner.</strong></p>
  </div>
</section>
<section class="content-section about-detail-section">
  <div class="container content-grid">
    <div class="policy-panel about-policy-panel">
      <span class="section-label">How We Work</span>
      <h2 class="section-heading about-equal-heading">How We Work</h2>
      <p class="copy-body">Every engagement starts with a written income plan. We use professional-grade modeling tools to build a customized strategy that addresses your specific income needs, tax situation, and time horizon.</p>
      <p class="copy-body">The plan itself is built around the Three Trees framework. As the structure produces three protective shields — against market risk, against tax inefficiency, and against the behavioral pressures of a major life transition — it provides a level of resilience most retirement plans don't deliver.</p>
      <a href="triple-shield.html" class="btn btn-gold">Learn more about the Triple Shield→</a>
      <p class="copy-body" style="margin-top:20px;">We then manage the plan year over year — recalibrating tax strategy annually, repositioning the Soon Tree as it depletes, refilling from the Later Tree at favorable market moments, and adjusting Social Security timing decisions as your situation evolves.</p>
    </div>
    <div>
      <span class="section-label">About the Name</span>
      <h2 class="section-heading about-equal-heading">About the Name</h2>
      <p class="copy-body">Our name reflects our framework. Three trees — Now, Soon, and Later — each rooted in a different time horizon, each with its own purpose. Together, they form a structure designed to grow stronger as your retirement unfolds.</p>
      <hr style="border:none;border-top:1px solid var(--cream-border);margin:28px 0;">
      <span class="section-label">Our Approach to This Work</span>
      <h2 class="section-heading about-equal-heading">Our Approach to This Work</h2>
      <p class="copy-body">We believe retirement planning is a stewardship responsibility — for our clients and for ourselves. We approach this work with care for the long-term wellbeing of every household we serve, and we measure our success by the quality of decisions our clients are able to make over decades, not by short-term portfolio performance.</p>
    </div>
  </div>
</section><section class="cta-strip">
  <div class="container">
    <span class="section-label-light">Take the First Step</span>
    <h2 class="section-heading-light">Ready to Get Started?</h2>
    <p>Schedule a complimentary consultation to discuss your retirement situation.</p>
    <a href="contact.html#schedule" class="btn btn-gold">Schedule a Consultation</a>
  </div>
</section>
</main>
'''

team = '''
<main>
<section class="page-hero">
  <div class="container">
    <div class="breadcrumb"><a href="index.html">Home</a><i class="fas fa-chevron-right"></i><span>Meet the Team</span></div>
    <span class="page-hero-eyebrow">Meet the Team</span>
    <h1 class="page-hero-title">Meet the Team</h1>
    <p class="page-hero-sub">ThreeTrees Retirement Partners is led by Michael and Stephanie Cooley — but you’re never relying on just the two of us.</p>
  </div>
</section>
<section class="content-section">
  <div class="container">
    <article class="team-card team-card-michael">
      <div class="team-card-photo"><img src="images/michael-cooley.jpg" alt="Michael Cooley"></div>
      <div class="team-card-info">
        <h2 class="team-card-name">Michael Cooley</h2>
        <div class="team-card-title">Founder &amp; Lead Advisor</div>
        <div class="team-card-credentials"><span class="credential-badge">ChFC®</span><span class="credential-badge">RICP®</span><span class="credential-badge">NSSA®</span></div>
        <p class="team-card-bio">Michael Cooley is the founder of ThreeTrees Retirement Partners and the architect of the Three Trees framework. He holds three retirement-focused designations from The American College of Financial Services — Chartered Financial Consultant® (ChFC®), Retirement Income Certified Professional® (RICP®), and National Social Security Advisor (NSSA®) — credentials chosen specifically for the work of retirement income planning.</p>
        <p class="team-card-bio">Michael leads every client engagement, builds every plan, and manages every household's tax strategy on an ongoing basis. He lives in the Ann Arbor area with his wife Stephanie and serves on the worship team at LifePointe Church.</p>
      </div>
    </article>
    <article class="team-card team-card-stephanie">
      <div class="team-card-info">
        <h2 class="team-card-name">Stephanie Cooley</h2>
        <div class="team-card-title">Co-Owner &amp; Vice President | Retirement Coach</div>
        <div class="team-card-credentials"><span class="credential-badge">M.Ed.</span></div>
        <p class="team-card-bio">Stephanie Cooley is co-owner and Vice President of ThreeTrees Retirement Partners. She holds a Master of Education degree, which informs her work in two complementary areas of the practice.</p>
        <p class="team-card-bio">First, Stephanie leads client relations — she conducts initial conversations with prospective clients, manages communications between meetings, and serves as a primary point of contact for ongoing client relationships. Many ThreeTrees clients have shared that Stephanie's role is what makes the practice feel personal rather than transactional.</p>
        <p class="team-card-bio">Second, Stephanie shapes the educational architecture of our seminar program. Her background in adult learning informs how we structure our Social Security and retirement income workshops, ensuring complex topics are accessible to attendees from any professional background.</p>
        <p class="team-card-bio">For clients who want it, Stephanie also offers retirement coaching — guidance through the personal and behavioral side of the retirement transition. This complements the structural behavioral protections built into every ThreeTrees plan and is available as part of the broader client relationship.</p>
      </div>
      <div class="team-card-photo"><img src="images/stephanie-cooley.jpg" alt="Stephanie Cooley"></div>
    </article>
  </div>
</section>
</main>
'''

team += '''
<section class="altitude-section">
  <div class="container altitude-container">
    <div class="altitude-header">
      <span class="section-label">Support Team at Altitude Capital Management</span>
      <h2 class="section-heading">Support Team at Altitude Capital Management</h2>
      <p class="altitude-intro">As an independent practice operating under Altitude Capital Management, our Registered Investment Advisory firm, we’re backed by a team of experienced professionals who provide compliance oversight, investment research, and portfolio infrastructure. A few of the people working behind the scenes on your behalf:</p>
    </div>
    <div class="altitude-cards-grid">
      <article class="altitude-card">
        <div class="altitude-card-photo"><div class="altitude-photo-label"><i class="fas fa-user"></i><span>Support Team</span></div></div>
        <div class="altitude-card-body"><h3 class="altitude-card-name">Charles Johnson</h3><div class="altitude-card-title">Chief Compliance Officer</div><p class="altitude-card-bio">Charles oversees the compliance and fiduciary framework that governs how every ThreeTrees account is managed. His oversight helps ensure the advice you receive always meets a rigorous, regulated standard.</p></div>
      </article>
      <article class="altitude-card">
        <div class="altitude-card-photo"><div class="altitude-photo-label"><i class="fas fa-user"></i><span>Support Team</span></div></div>
        <div class="altitude-card-body"><h3 class="altitude-card-name">Gene Perez, CFP</h3><div class="altitude-card-title">Chief Investment Officer</div><p class="altitude-card-bio">Gene leads investment research and oversight at the firm level, helping shape the disciplined, risk-aware standards that inform how portfolios across the firm are built and monitored.</p></div>
      </article>
      <article class="altitude-card">
        <div class="altitude-card-photo"><div class="altitude-photo-label"><i class="fas fa-user"></i><span>Support Team</span></div></div>
        <div class="altitude-card-body"><h3 class="altitude-card-name">Aaron Schmidtke</h3><div class="altitude-card-title">Portfolio Allocation Manager</div><p class="altitude-card-bio">Aaron handles portfolio allocation and trading operations, helping translate each client's strategy into properly structured, well-maintained accounts.</p></div>
      </article>
    </div>
  </div>
</section>
<section class="cta-strip">
  <div class="container">
    <span class="section-label-light">Take the First Step</span>
    <h2 class="section-heading-light">Ready to Get Started?</h2>
    <p>Schedule a complimentary consultation to discuss your retirement situation.</p>
    <a href="contact.html#schedule" class="btn btn-gold">Schedule a Consultation</a>
  </div>
</section>
</main>
'''

tax = '''
<main>
<section class="page-hero">
  <div class="container">
    <div class="breadcrumb"><a href="index.html">Home</a><i class="fas fa-chevron-right"></i><span>Tax Strategy</span></div>
    <span class="page-hero-eyebrow">Tax Strategy</span>
    <h1 class="page-hero-title">Tax Strategy for Retirement Income</h1>
    <p class="page-hero-sub">The decisions you make about taxes in your 60s and 70s will shape what's left for you — and what's left to leave behind.</p>
  </div>
</section>
<section class="planning-section">
  <div class="container" style="max-width:900px;">
    <span class="section-label">Why Tax Strategy Matters</span>
    <h2 class="section-heading">Why Tax Strategy Matters</h2>
    <p class="copy-body">Most prospects come to us with the same concern: "I don't want to pay more in taxes than I have to." It's the single most common opening statement in our discovery meetings.</p>
    <p class="copy-body">Here's why: when you're working, your tax picture is relatively simple. Withholding handles most of it. But once you stop earning a paycheck, the rules change. Required Minimum Distributions, Social Security taxation, IRMAA Medicare surcharges, capital gains decisions, and the ongoing balance between pre-tax and Roth accounts all compound over a 20–40 year retirement.</p>
    <p class="copy-body">Done well, these decisions can save a household hundreds of thousands of dollars in lifetime taxes. Done poorly — or not at all — they cost the same.</p>
  </div>
</section>
<section class="content-section">
  <div class="container">
    <span class="section-label">The Tax Decisions We Help You Navigate</span>
    <h2 class="section-heading">The Tax Decisions We Help You Navigate</h2>
    <div class="tax-card-grid">
      <article class="mini-card"><h3>Roth Conversions</h3><p>The right time to convert pre-tax retirement assets to Roth is rarely when the tax software prompts you to. We model the multi-year tax impact of converting in stages — typically during the lower-tax years between retirement and Required Minimum Distribution age — to optimize lifetime taxes rather than just this year's bill.</p></article>
      <article class="mini-card"><h3>RMG Planning</h3><p>Required Minimum Distributions begin at age 73 for most retirees. The accounts you draw from in your 60s heavily influence what's required when you hit RMD age. We coordinate the sequencing of withdrawals across taxable, tax-deferred, and Roth accounts to manage the curve.</p></article>
      <article class="mini-card"><h3>IRMAA Avoidance</h3><p>The Income-Related Monthly Adjustment Amount adds Medicare premium surcharges when household income exceeds specific thresholds. The thresholds are cliffs, not gradients — earning $1 over the line can cost thousands. We model income strategy with IRMAA brackets explicitly in view.</p></article>
      <article class="mini-card"><h3>Social Security Taxation</h3><p>Up to 85% of Social Security benefits become taxable depending on your provisional income. The right combination of withdrawal sources and Roth balances can dramatically reduce the share that's taxed.</p></article>
      <article class="mini-card"><h3>Optimal Traditional/Roth Balance</h3><p>Rather than blanket conversion strategies, we recalibrate your account mix annually based on tax law, your specific situation, and the broader plan. The optimal balance changes over time — and the right answer for one client is rarely the right answer for another.</p></article>
    </div>
  </div>
</section>
<section class="light-section">
  <div class="container" style="max-width:900px;">
    <span class="section-label">Coordination With Your CPA</span>
    <h2 class="section-heading">Coordination With Your CPA</h2>
    <p class="copy-body">Tax strategy is most effective when your retirement advisor and your CPA are working from the same playbook. We coordinate directly with your tax professional to ensure the strategies we model in planning meetings actually translate into the right entries on your return.</p>
    <p class="copy-body">If you don't currently have a tax professional, we can refer you to CPAs in the Ann Arbor area who specialize in retirement-stage tax planning.</p>
  </div>
</section>
<section class="cta-strip">
  <div class="container">
    <span class="section-label-light">Take the First Step</span>
    <h2 class="section-heading-light">Ready to See What Your Tax Picture Could Look Like?</h2>
    <p>Schedule a complimentary consultation. We'll review your current accounts and walk you through the tax decisions that will most affect your retirement.</p>
    <a href="contact.html#schedule" class="btn btn-gold">Schedule a Tax Strategy Consultation</a>
  </div>
</section>
</main>
'''

triple = '''
<main>
<section class="page-hero">
  <div class="container">
    <div class="breadcrumb"><a href="index.html">Home</a><i class="fas fa-chevron-right"></i><span>The Triple Shield</span></div>
    <span class="page-hero-eyebrow">The Triple Shield</span>
    <h1 class="page-hero-title">The Triple Shield</h1>
    <p class="page-hero-sub">Three trees working together produce three layers of protection — against the three risks most likely to derail a retirement.</p>
  </div>
</section>
<section class="light-section">
  <div class="container content-grid">
    <div>
      <span class="section-label">Why the Triple Shield Exists</span>
      <h2 class="section-heading">Why the Triple Shield Exists</h2>
      <p class="copy-body">Most retirement portfolios are built to maximize returns. A retirement income plan has a different job: to keep delivering income across decades, through every kind of market, every kind of tax law, and every kind of life event.</p>
      <p class="copy-body">When the Three Trees framework is structured correctly, it produces more than just an income plan. It produces a system of protection — a triple shield — against the specific risks that catch most retirees off guard.</p>
    </div>
    <div class="shield-graphic-box"><img src="images/triple-shield-graphic.png" alt="The Triple Shield" class="shield-graphic-img"></div>
  </div>
</section>
<section class="process-section">
  <div class="container" style="max-width:980px;">
    <span class="section-label-light">A Note on Bucket Strategies</span>
    <h2 class="section-heading-light">A Note on Bucket Strategies</h2>
    <p class="copy-body-light">If you've researched retirement income strategies, you may have encountered the argument that bucket-based approaches are outdated. The argument has merit — but only when applied to a specific, older version of the bucket strategy.</p>
    <p class="copy-body-light">The classic bucket approach, popularized in the 1980s and 1990s, was largely static. Buckets were established at retirement and refilled on a fixed schedule, regardless of market conditions or changing household circumstances. That approach is outdated. It oversimplifies the complexity of a 30-to-40-year retirement and doesn't respond to the realities a household will encounter along the way.</p>
    <p class="copy-body-light">The Three Trees framework is a different generation of the structure. The bucket organization handles the question of which assets fund which years — a sequencing problem the static approach never fully solved. Layered on top of that structure are the dynamic withdrawal guardrails described in Shield 3, which flex spending up and down each year based on actual portfolio performance. The two work together: the structure provides stability and clarity, the dynamic modeling provides responsiveness.</p>
    <p class="copy-body-light">Modern retirement income research and the leading planning software platforms have converged on this hybrid approach for the same reason we use it: structure alone is too rigid, and dynamic modeling alone lacks the visible architecture clients need to understand their own plan. Together, they produce both.</p>
    <p class="copy-body-light"><strong>Retire longer, not leaner.</strong></p>
  </div>
</section>
<section class="shield-cards-section">
  <div class="container">
    <div class="shield-cards-grid">
      <article class="shield-card"><div class="shield-card-icon-wrap"><i class="fas fa-chart-line shield-svg-icon"></i></div><div class="shield-card-title">SHIELD ONE</div><h3 class="shield-card-name">Market Risk</h3><p class="shield-card-desc">The first risk most retirees fear is the wrong one at the wrong time — a market downturn early in retirement, when withdrawals from a falling portfolio can permanently damage long-term outcomes.</p><p class="shield-card-body">The Three Trees structure addresses this directly. The Now and Soon Trees mean you never have to sell investments in a down market to fund your living expenses — your near-term income comes from sources insulated from market volatility. The Later Tree, in turn, has the time it needs to weather market cycles and refill the Soon Tree at favorable moments.</p></article>
      <article class="shield-card shield-card-featured"><div class="shield-card-icon-wrap"><i class="fas fa-shield-halved shield-svg-icon"></i></div><div class="shield-card-title">SHIELD TWO</div><h3 class="shield-card-name">Tax Risk</h3><p class="shield-card-desc">The second risk is the slow, compounding cost of unmanaged taxes. Required Minimum Distributions, Social Security taxation, IRMAA Medicare surcharges, and the year-over-year balance between pre-tax and Roth accounts all interact in ways that most retirees discover only when the bill arrives.</p><p class="shield-card-body">Shield 2 is the ongoing tax strategy work we do for every client — recalibrated annually — to manage these decisions as a system rather than a series of one-off events.</p><p class="shield-card-body"><a href="tax-strategy.html" style="color:var(--gold-light);font-weight:700;">Learn more on our Learn more on our Tax Strategy page →</a></p></article>
      <article class="shield-card"><div class="shield-card-icon-wrap"><i class="fas fa-arrow-trend-down shield-svg-icon"></i></div><div class="shield-card-title">SHIELD THREE</div><h3 class="shield-card-name">Spending Risk</h3><p class="shield-card-desc">Most retirement advice tells you to cut back. We don't. The real risk in retirement spending isn't excess — it's miscalibration.</p><p class="shield-card-body">Shield 3 is built into the structure of every plan we deliver. Our income strategies use dynamic withdrawal guardrails — a built-in mechanism that flexes spending up when the portfolio outperforms and gently scales back when it underperforms. The goal isn't to spend less. The goal is to spend correctly — calibrated to what the portfolio can actually sustain, year by year, over a long retirement.</p></article>
    </div>
  </div>
</section>
<section class="cta-strip"><div class="container"><span class="section-label-light">Take the First Step</span><h2 class="section-heading-light">Ready to See How the Triple Shield Would Protect Your Retirement?</h2><p>Schedule a complimentary consultation. We'll walk you through how the framework would apply to your specific situation.</p><a href="contact.html#schedule" class="btn btn-gold">Schedule a Consultation</a></div></section>
</main>
'''

seminars = '''
<main>
<section class="page-hero">
  <div class="container">
    <div class="breadcrumb"><a href="index.html">Home</a><i class="fas fa-chevron-right"></i><span>Seminars</span></div>
    <span class="page-hero-eyebrow">Seminars</span>
    <h1 class="page-hero-title">Free Social Security &amp; Retirement Planning Seminar</h1>
    <p class="page-hero-sub">Learn the strategies that could add thousands to your lifetime Social Security benefits.</p>
    <div class="page-hero-ctas"><a href="contact.html#message" class="btn btn-gold">REGISTER FOR SEMINAR</a></div>
  </div>
</section>
<section class="planning-section">
  <div class="container content-grid">
    <div>
      <span class="section-label">What you’ll learn at this Seminar</span>
      <h2 class="section-heading">What you’ll learn at this Seminar</h2>
      <p class="copy-body">Join us for a free educational seminar where you'll learn:</p>
      <ul style="padding-left:20px;display:grid;gap:10px;color:var(--body-text);line-height:1.8;list-style:disc;">
        <li>When to claim Social Security for maximum lifetime benefit</li>
        <li>How spousal and survivor benefits work</li>
        <li>Tax implications of Social Security income</li>
        <li>Strategies for divorced individuals and widows</li>
        <li>How to coordinate Social Security with other retirement income</li>
      </ul>
      <p class="copy-body" style="margin-top:18px;">This is a no-cost educational workshop. No products will be sold.</p>
    </div>
    <div class="seminar-learn-grid">
      <article class="seminar-learn-card"><div class="seminar-learn-tab">Optimal Filing Age</div><div class="seminar-learn-body"><p>Discover when to claim Social Security based on your specific situation—and why waiting isn't always the best answer.</p></div></article>
      <article class="seminar-learn-card"><div class="seminar-learn-tab">Spousal Strategies</div><div class="seminar-learn-body"><p>Learn how married couples can coordinate benefits to maximize household income over both lifetimes.</p></div></article>
      <article class="seminar-learn-card"><div class="seminar-learn-tab">Tax Planning</div><div class="seminar-learn-body"><p>Understand how Social Security income is taxed and strategies to minimize your tax burden in retirement.</p></div></article>
      <article class="seminar-learn-card"><div class="seminar-learn-tab">Common Mistakes</div><div class="seminar-learn-body"><p>Avoid the filing errors that cost retirees tens of thousands of dollars.</p></div></article>
    </div>
  </div>
</section>
<section class="light-section"><div class="container content-grid"><div><span class="section-label">Who Should Attend?</span><h2 class="section-heading">Who Should Attend?</h2><p class="copy-body">This seminar is designed for</p><ul style="padding-left:20px;display:grid;gap:10px;color:var(--body-text);line-height:1.8;list-style:disc;"><li>Adults ages 55-75 planning their Social Security filing decision</li><li>Couples wanting to coordinate spousal benefits</li><li>Divorced individuals unsure about ex-spouse benefits</li><li>Widows and widowers navigating survivor benefits</li><li>Anyone who hasn't filed for Social Security yet</li></ul><p class="copy-body" style="margin-top:18px;">Even if you're already retired, if you haven't filed for Social Security, this seminar can help you make an informed decision.</p></div><div class="photo-card"><img src="images/who-we-serve-couple.jpg" alt="Seminar audience"></div></div></section>
<section class="process-section"><div class="container"><span class="section-label-light">Upcoming Free Seminars</span><h2 class="section-heading-light">Upcoming Free Seminars</h2><p class="copy-body-light" style="text-align:center;max-width:700px;margin:0 auto 28px;">Seating is limited - Register today to secure your spot.</p><div class="mini-cards-3"><article class="mini-card"><h3>Thursday, July 10, 2026 · 6:00 PM</h3><p class="seminar-topic"><strong>The Three Trees Framework: Income That Outlasts Retirement</strong></p><p>📍Washtenaw Community College, Ann Arbor<br>⏱ 90 minutes · Free admission</p><a href="contact.html#message" class="btn btn-gold" style="margin-top:16px;">Reserve your seat</a></article><article class="mini-card"><h3>Tuesday, August 5, 2026 · 6:00 PM</h3><p class="seminar-topic"><strong>Tax-Smart Retirement: RMDs, Roth Conversions &amp; More</strong></p><p>📍Washtenaw Community College, Ann Arbor<br>⏱ 90 minutes · Free admission</p><a href="contact.html#message" class="btn btn-gold" style="margin-top:16px;">Reserve your seat</a></article><article class="mini-card"><h3>Tuesday, SEPT TBA · 6:00 PM</h3><p class="seminar-topic"><strong>Social Security: Maximizing Your Lifetime Benefits</strong></p><p>📍Washtenaw Community College, Ann Arbor<br>⏱ 90 minutes · Free admission</p><a href="contact.html#message" class="btn btn-gold" style="margin-top:16px;">Reserve your seat</a></article></div></div></section>
</main>
'''

faq = '''
<main>
<section class="page-hero"><div class="container"><div class="breadcrumb"><a href="index.html">Home</a><i class="fas fa-chevron-right"></i><span>FAQ</span></div><span class="page-hero-eyebrow">FAQ</span><h1 class="page-hero-title">Frequently Asked Questions</h1><p class="page-hero-sub">Straight answers to the questions we hear most. If yours isn’t here, just ask.</p></div></section>
<section class="process-section"><div class="container" style="max-width:900px;">
'''
for q, a in [
('How old is your firm? / How long have you been around?', 'While ThreeTrees Retirement Partners is a newer firm, it’s built on years of experience helping individuals and families navigate retirement — and it’s supported by an established Registered Investment Advisory firm overseeing approximately $100 million in assets. You get the focus and personal attention of a boutique practice, with the infrastructure and oversight of a much larger one behind it.'),
('Are you a fiduciary? Do you sell products?', 'Yes — as an Investment Adviser Representative, we’re held to a fiduciary standard, which means we’re obligated to act in your best interest. Just as important, we’re planning-first, not product-first. We build the plan around your goals and your timeline, and any recommendation has to earn its place in that plan. You’ll never be sold something that doesn’t fit.'),
('What makes you different from other advisors?', 'Two things. First, structure: we organize your money around when you’ll actually need it — what you need now, what you’ll need soon, and what you’ll need later — so your income today never depends on the market behaving on any given morning. Second, we plan for the whole retirement, not just the money. Stephanie’s work helps clients think through the life side — purpose, time, identity — because the people who retire well plan for more than their portfolio.'),
('Who do you typically work with?', 'Most of our clients are approaching or already in retirement and want a real, durable plan for making their money last. They’ve usually saved diligently over a career and now want clarity and confidence about what comes next. More than any dollar figure, it comes down to fit — so the best way to know is a short, no-obligation conversation.'),
('Do I have to leave my current advisor to work with you?', 'Not necessarily — but here’s how we’d encourage you to think about it. Consider your healthcare over a lifetime. As a child, you saw a pediatrician. As an adult, you settled in with a general practitioner who knew you well and handled most of what came up. But if something serious developed, you wouldn’t ask your GP to treat it alone — you’d want a specialist, someone who has gone deeper into that one challenge than a generalist ever could. Retirement is that kind of transition. The advisor who helped you build your savings over a career did important work. But turning a lifetime of savings into reliable, tax-efficient income that lasts — through market downturns, rising costs, and decades you can’t fully predict — is a different discipline. That’s the specialty ThreeTrees is built around. You’ve spent years with your general practitioner; now you’re entering a phase of life where it pays to see a specialist. For most people, the cleanest and most efficient path is one holistic plan under a single roof, where every piece is coordinated rather than managed in separate silos. That said, if there’s an advisor you value and want to keep, we can work alongside them — it simply takes more coordination to keep both sides aligned. Either way, the goal is the same: the right plan for this season of your life.'),
('When should I claim Social Security?', 'There’s no universal “right” age. The best filing strategy depends on your health, your other income sources, your tax picture, and — for married couples — how the two benefits coordinate over both lifetimes. Claiming early, claiming at full retirement age, and delaying each carry trade-offs, and over a long retirement the gap between a good decision and a poor one can be substantial. We model your specific situation so the timing decision is made with eyes open, not by rule of thumb.'),
('Do you help with tax strategy in retirement?', 'Yes — tax awareness runs through everything we do, because how you draw your income can matter as much as how much you’ve saved. We look at the order you tap different accounts, how required distributions may land down the road, and whether moves like Roth conversions make sense for your situation — recognizing that what’s right for one household can be the wrong move for another. We don’t replace your CPA or prepare your taxes; we coordinate with the tax side so the plan works as a whole, and we revisit it as the rules and your circumstances change.'),
('What’s your investment philosophy?', 'We don’t try to predict the market or chase the hot performer. Instead, we organize your money around when you’ll need it: money for today is kept stable and accessible, while money you won’t touch for years is positioned to grow over time. Each layer is matched to its job and to your comfort with risk. The aim isn’t to win a race in any given quarter — it’s dependable income now and lasting growth later, with fewer sleepless nights along the way.'),
('What do you charge? / How do you get paid?', 'The honest answer is: it depends on your situation — which is exactly why we walk through it together before you ever commit to anything. For the assets we manage on an ongoing basis, our advisory fee is a percentage of those assets, and that percentage steps down as your assets grow, so larger households pay a lower rate. We lay it all out plainly in a planning conversation, with no obligation. You’ll always know exactly what you’re paying, and why, before you decide anything. It’s also worth stepping back from the number itself. Most people are already paying fees — inside a 401(k), a current advisory account, or the funds they own — but those costs are often bundled, hard to see, or simply never explained. The real question isn’t whether there’s a fee; it’s what you receive in return for it. A fair fee paired with a coordinated plan — one that manages risk, keeps an eye on taxes, and is built to produce dependable income — can be worth far more than a “cheaper” arrangement that leaves those things to chance. Our job is to make the value clear and make sure it’s worth every dollar you pay.'),
('Do you meet in person or virtually?', 'Both. Our office is in Ann Arbor, and we welcome clients in for face-to-face planning. For those who prefer it — or who live outside the area — we also meet by secure video, so you can plan from wherever you are.'),
('What happens to my money and my plan if something happens to you?', 'It’s a fair and important question — and the structure is built so that neither your money nor your plan ever depends on any one person. First, your money is never held by ThreeTrees or by me personally. Your accounts are custodied with an independent, third-party custodian, in your name, where you can see them at any time. We’re authorized to advise on and manage those accounts, but the assets themselves sit safely outside our walls — and nothing about that changes if something happens to me. Second, ThreeTrees operates under an established Registered Investment Advisory firm with the oversight and continuity infrastructure to keep your accounts serviced without interruption. And because this is a co-owned practice — Stephanie is co-owner and an active part of the firm — you’re never relying on a single individual to carry things forward. Finally, your plan lives in our records and systems, not in one person’s head. It’s documented, organized, and built to be picked up and carried forward, so the strategy you put in place keeps working for your family no matter what.'),
('What do you stand for?', 'We believe money is a tool, not the point — it exists to fund a life of purpose, security, and generosity. We treat our clients’ savings the way we’d treat our own: carefully, honestly, and with the long view in mind. Our promise is simple — straight talk, no pressure, and a plan built to help you retire longer, not leaner.'),
('What happens at a first meeting? / How do I get started?', 'The first conversation is relaxed and pressure-free — a chance for us to understand where you are, what you’re hoping for, and whether we’re a good fit for each other. There’s no cost and no obligation. When you’re ready, you can schedule directly from our site.')
]:
    faq += f'<details class="faq-item"><summary class="faq-question"><span>{q}</span><i class="fas fa-plus faq-icon"></i></summary><div class="faq-answer"><p>{a}</p></div></details>'
faq += '''</div></section><section class="cta-strip"><div class="container"><span class="section-label-light">Take the First Step</span><h2 class="section-heading-light">Schedule a Conversation</h2><a href="contact.html#schedule" class="btn btn-gold">Schedule a Conversation</a></div></section></main>'''


contact = '''
<main>
<section class="page-hero"><div class="container"><div class="breadcrumb"><a href="index.html">Home</a><i class="fas fa-chevron-right"></i><span>Contact Us</span></div><span class="page-hero-eyebrow">Book Your Call</span><h1 class="page-hero-title">Book Your Call</h1><p class="page-hero-sub">Pick a Time That Works for You</p></div></section>
<section class="schedule-section schedule-call-section" id="schedule"><div class="container schedule-container"><div class="schedule-copy"><span class="section-label">Book Your Call</span><h2 class="section-heading">Schedule a Free 30-Minute Call</h2><p class="schedule-body">There's no pitch, no pressure, and no obligation. We'll spend 30 minutes understanding where you are, where you want to go, and whether the Three Trees Framework is the right fit for your retirement.</p><ul class="schedule-list"><li><i class="fas fa-check"></i>100% Free — no cost, no commitment</li><li><i class="fas fa-check"></i>No products will be sold on this call</li><li><i class="fas fa-check"></i>Honest assessment of your retirement readiness</li><li><i class="fas fa-check"></i>Learn if the Three Trees Framework is right for you</li></ul></div><div class="calendly-placeholder"><div class="calendly-header"><img src="images/logo-square-dark.png" alt="Three Trees Retirement Partners" class="calendly-logo"><h3>Pick a Time That Works for You</h3></div><div class="calendly-embed-wrapper"><div class="calendly-mock"><div class="calendly-mock-text">Calendly scheduling widget</div><div class="calendly-mock-sub">Scheduling placeholder</div><a class="btn btn-gold calendly-btn" href="mailto:info@3treesrp.com?subject=Book%20a%20Meeting">BOOK YOUR FREE CALL</a></div></div></div></div></section>
<section class="contact-section" id="message"><div class="container contact-container"><div><span class="section-label-light">Get in Touch</span><h2 class="section-heading-light">Get in Touch</h2><p class="contact-kicker">Prefer to Reach Out Directly?</p><p class="contact-body">Whether you have a quick question or want to discuss your situation in detail, we're here to help. Send us a message and we'll respond within one business day.</p><div class="contact-details"><div class="contact-detail-item"><i class="fas fa-location-dot"></i><span>825 Victors Way, Ann Arbor</span></div><div class="contact-detail-item"><i class="fas fa-phone"></i><span><a href="tel:7342122525">(734) 212-2525</a></span></div><div class="contact-detail-item"><i class="fas fa-envelope"></i><span><a href="mailto:info@3treesrp.com">info@3treesrp.com</a></span></div></div></div><form id="contact-form" class="contact-form" name="contact" method="POST" data-netlify="true" action="thank-you.html"><input type="hidden" name="form-name" value="contact"><div class="form-card-heading">Send Us a Message</div><p class="form-card-copy">Share a few details below and we'll follow up within one business day.</p><div class="form-row"><div class="form-group"><label for="first-name">First Name</label><input id="first-name" name="first-name" required></div><div class="form-group"><label for="last-name">Last Name</label><input id="last-name" name="last-name" required></div></div><div class="form-row"><div class="form-group"><label for="email">Email</label><input id="email" name="email" type="email" required></div><div class="form-group"><label for="phone">Phone</label><input id="phone" name="phone" type="tel"></div></div><div class="form-row"><div class="form-group"><label for="retirement-timeline">Retirement Timeline</label><select id="retirement-timeline" name="retirement-timeline"><option value="">Select one</option><option>Already retired</option><option>Within 1 year</option><option>1-3 years</option><option>3-5 years</option><option>More than 5 years</option></select></div><div class="form-group"><label for="investable-assets">Approximate Investable Assets</label><select id="investable-assets" name="approximate-investable-assets"><option value="">Select one</option><option>Under $500,000</option><option>$500,000 - $1,000,000</option><option>$1,000,000 - $3,000,000</option><option>$3,000,000+</option></select></div></div><div class="form-group"><label for="message-field">Message</label><textarea id="message-field" name="message" required></textarea></div><button class="btn btn-gold form-submit-btn" type="submit">SEND MESSAGE</button><div class="form-disclaimer">No products will be sold through this form. By reaching out, you're simply starting a conversation.</div><div id="form-success" class="form-success-msg" style="display:none;"><i class="fas fa-check-circle"></i><span>Your message has been sent.</span></div></form></div></section>
</main>
'''

thank_you = '''
<main>
<section class="page-hero"><div class="container"><span class="page-hero-eyebrow">Thank You</span><h1 class="page-hero-title">Thank You</h1><p class="page-hero-sub">We'll respond within one business day.</p><div class="page-hero-ctas"><a href="index.html" class="btn btn-gold">Return Home</a></div></div></section>
</main>
'''

pages = {
    'index.html': page('Three Trees Retirement Partners — Retirement Income Planning', '', home, 'Retirement income planning for Ann Arbor-area pre-retirees and retirees.'),
    'framework.html': page('About Us — Three Trees Retirement Partners', 'about', about, 'About ThreeTrees Retirement Partners.'),
    'team.html': page('Meet the Team — Three Trees Retirement Partners', 'about', team, 'Meet the team at ThreeTrees Retirement Partners.'),
    'tax-strategy.html': page('Tax Strategy — Three Trees Retirement Partners', 'tax', tax, 'Tax strategy for retirement income.'),
    'triple-shield.html': page('The Triple Shield — Three Trees Retirement Partners', 'triple', triple, 'The Triple Shield retirement protection framework.'),
    'seminars.html': page('Seminars — Three Trees Retirement Partners', 'seminars', seminars, 'Free Social Security and retirement planning seminars.'),
    'faqs.html': page('FAQ — Three Trees Retirement Partners', 'faq', faq, 'Frequently asked questions.'),
    'contact.html': page('Contact Us — Three Trees Retirement Partners', 'contact', contact, 'Book your call or send a message.'),
    'thank-you.html': page('Thank You — Three Trees Retirement Partners', 'contact', thank_you, 'Thank you.'),
}
for name, content in pages.items():
    (ROOT / name).write_text(content, encoding='utf-8')
(ROOT / 'netlify.toml').write_text('''[[redirects]]\nfrom = "/about-us"\nto = "/framework.html"\nstatus = 200\n\n[[redirects]]\nfrom = "/tax-strategy"\nto = "/tax-strategy.html"\nstatus = 200\n\n[[redirects]]\nfrom = "/the-triple-shield"\nto = "/triple-shield.html"\nstatus = 200\n\n[[redirects]]\nfrom = "/faq"\nto = "/faqs.html"\nstatus = 200\n\n[[redirects]]\nfrom = "/privacy-policy"\nto = "/privacy.html"\nstatus = 200\n\n[[redirects]]\nfrom = "/terms-and-conditions"\nto = "/terms.html"\nstatus = 200\n\n[[redirects]]\nfrom = "/accessibility-statement"\nto = "/accessibility.html"\nstatus = 200\n''', encoding='utf-8')
print('Generated', len(pages), 'pages')
