import json
naics=[("325611","Soap and Other Detergent Manufacturing","Primary"),("325612","Polish and Other Sanitation Good Manufacturing",""),("325998","All Other Miscellaneous Chemical Product and Preparation Manufacturing",""),("424690","Other Chemical and Allied Products Merchant Wholesalers",""),("423850","Service Establishment Equipment and Supplies Merchant Wholesalers",""),("811192","Car Washes",""),("561720","Janitorial Services",""),("561790","Other Services to Buildings and Dwellings",""),("561210","Facilities Support Services",""),("561990","All Other Support Services",""),("541330","Engineering Services",""),("541715","Research and Development in the Physical, Engineering, and Life Sciences (except Nanotechnology and Biotechnology)",""),("541620","Environmental Consulting Services",""),("541690","Other Scientific and Technical Consulting Services",""),("541611","Administrative Management and General Management Consulting Services",""),("541511","Custom Computer Programming Services",""),("541512","Computer Systems Design Services",""),("541513","Computer Facilities Management Services",""),("541519","Other Computer Related Services",""),("513210","Software Publishers",""),("518210","Computing Infrastructure Providers, Data Processing, Web Hosting, and Related Services",""),("334118","Computer Terminal and Other Computer Peripheral Equipment Manufacturing","")]
psc=[("6810","Chemicals"),("6850","Miscellaneous Chemical Specialties"),("7930","Cleaning and Polishing Compounds and Preparations"),("S201","Housekeeping: Custodial Janitorial"),("S299","Housekeeping: Other"),("B544","Special Studies/Analysis: Technology"),("R408","Support, Professional: Program Management/Support"),("R425","Support, Professional: Engineering/Technical"),("R499","Support, Professional: Other")]
rows="\n".join(f'<tr><th scope="row">{c}</th><td>{d}{" <strong>(primary)</strong>" if p else ""}</td></tr>' for c,d,p in naics)
prow="\n".join(f'<tr><th scope="row">{c}</th><td>{d}</td></tr>' for c,d in psc)
URL="https://showroomdrz.com/"
ld={"@context":"https://schema.org","@graph":[
 {"@type":["AutoRepair","LocalBusiness","ProfessionalService"],"@id":URL+"#business","name":"ShowRoom Doctor Z","legalName":"ShowRoom Doctor Z Inc.","url":URL,
  "image":URL+"images/og-image.jpg","logo":URL+"images/showroom-doctor-z-logo.png",
  "description":"Premier auto detailing, ceramic coating, paint correction, and interior restoration in Clovis and Fresno, CA. Also offering solar panel surface care, commercial facility cleaning, and Miracle Spritz pH 4.6 multi-surface cleaner.",
  "telephone":"+1-559-492-6329","email":"drz@showroomdrz.com","priceRange":"Quote on request",
  "address":{"@type":"PostalAddress","streetAddress":"1004 San Jose Ave, Suite 101","addressLocality":"Clovis","addressRegion":"CA","postalCode":"93612","addressCountry":"US"},
  "areaServed":[{"@type":"City","name":"Clovis"},{"@type":"City","name":"Fresno"},{"@type":"AdministrativeArea","name":"Fresno County, California"},{"@type":"AdministrativeArea","name":"California Central Valley"}],
  "foundingDate":"2022-04-27","founder":{"@type":"Person","name":"Jorge R. Zavala","jobTitle":"Founder and Chief Executive"},
  "identifier":[{"@type":"PropertyValue","name":"SAM.gov Unique Entity ID","value":"LA62PCQL63D3"},{"@type":"PropertyValue","name":"CAGE Code","value":"25K02"},{"@type":"PropertyValue","name":"Cal eProcure Bidder ID","value":"BID0135007"},{"@type":"PropertyValue","name":"California DGS Small Business/Micro Business Certification ID","value":"2055537"},{"@type":"PropertyValue","name":"California DBE (CUCP) Firm ID","value":"51112"}],
  "knowsAbout":["Auto detailing","Ceramic coating","Paint correction","Interior detailing","Headlight restoration","Hard water spot removal","Engine bay detailing","Solar panel cleaning","Commercial cleaning","Surface care chemistry"],
  "brand":{"@type":"Brand","name":"Miracle Spritz"},
  "hasOfferCatalog":{"@type":"OfferCatalog","name":"ShowRoom Doctor Z services and products","itemListElement":[
   {"@type":"Offer","itemOffered":{"@type":"Service","name":"Auto detailing, ceramic coating, paint correction and interior restoration","areaServed":"Clovis and Fresno, California"}},
   {"@type":"Offer","itemOffered":{"@type":"Service","name":"Solar panel surface care","areaServed":"California Central Valley"}},
   {"@type":"Offer","itemOffered":{"@type":"Service","name":"Commercial facility cleaning and surface care","areaServed":"Clovis and Fresno, California"}},
   {"@type":"Offer","itemOffered":{"@type":"Product","name":"Miracle Spritz pH 4.6 Multi-Surface Cleaner","brand":{"@type":"Brand","name":"Miracle Spritz"}}}]}},
 {"@type":"WebSite","@id":URL+"#website","url":URL,"name":"ShowRoom Doctor Z","publisher":{"@id":URL+"#business"},"inLanguage":"en-US"},
 {"@type":"WebPage","@id":URL+"#webpage","url":URL,"name":"ShowRoom Doctor Z | Auto Detailing, Ceramic Coating & Paint Correction in Clovis & Fresno, CA","isPartOf":{"@id":URL+"#website"},"about":{"@id":URL+"#business"},"inLanguage":"en-US"},
 {"@type":"FAQPage","mainEntity":[
  {"@type":"Question","name":"Where is ShowRoom Doctor Z located?","acceptedAnswer":{"@type":"Answer","text":"ShowRoom Doctor Z Inc. is at 1004 San Jose Ave, Suite 101, Clovis, California 93612. We serve Clovis, Fresno and the California Central Valley."}},
  {"@type":"Question","name":"Is ShowRoom Doctor Z registered to do business with government agencies?","acceptedAnswer":{"@type":"Answer","text":"Yes. ShowRoom Doctor Z Inc. has an active SAM.gov registration for all awards (UEI LA62PCQL63D3, CAGE 25K02), is a California DGS certified Small Business/Micro Business (ID 2055537), and a California DBE (Firm ID 51112)."}},
  {"@type":"Question","name":"How do I request a quote?","acceptedAnswer":{"@type":"Answer","text":"Call 559-492-6329 or email drz@showroomdrz.com with the service you need, the address and the size of the vehicle, array or space."}}]}]}
ldj=json.dumps(ld,indent=1)
html=f'''<!DOCTYPE html>
<html lang="en-US">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>ShowRoom Doctor Z | Auto Detailing, Ceramic Coating &amp; Paint Correction in Clovis &amp; Fresno, CA</title>
<meta name="description" content="ShowRoom Doctor Z in Clovis &amp; Fresno, CA: hand auto detailing, ceramic coating, paint correction, interior restoration, solar panel care, and Miracle Spritz pH 4.6 surface cleaner. Call 559-492-6329.">
<meta name="keywords" content="auto detailing Clovis CA, car detailing Fresno CA, ceramic coating Clovis, paint correction Fresno, interior car detailing, headlight restoration, engine bay detail, Miracle Spritz">
<link rel="canonical" href="{URL}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="theme-color" content="#111111">
<meta name="geo.region" content="US-CA">
<meta name="geo.placename" content="Clovis">
<meta property="og:type" content="website">
<meta property="og:site_name" content="ShowRoom Doctor Z">
<meta property="og:title" content="ShowRoom Doctor Z | Auto Detailing, Ceramic Coating &amp; Paint Correction in Clovis &amp; Fresno, CA">
<meta property="og:description" content="Hand auto detailing, ceramic coating, paint correction, interior restoration, solar panel care, and Miracle Spritz pH 4.6 cleaner in Clovis and Fresno, CA.">
<meta property="og:url" content="{URL}">
<meta property="og:image" content="{URL}images/og-image.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="ShowRoom Doctor Z logo - Auto detailing, ceramic coating and surface care in Clovis and Fresno, California">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="ShowRoom Doctor Z | Auto Detailing &amp; Ceramic Coating in Clovis &amp; Fresno, CA">
<meta name="twitter:description" content="Hand auto detailing, ceramic coating, paint correction, solar panel care and Miracle Spritz pH 4.6 cleaner.">
<meta name="twitter:image" content="{URL}images/og-image.jpg">
<link rel="icon" href="favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="favicon-32.png">
<link rel="icon" type="image/png" sizes="192x192" href="favicon-192.png">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<link rel="stylesheet" href="styles.css">
<script type="application/ld+json">
{ldj}
</script>
</head>
<body>
<a class="skip" href="#main">Skip to main content</a>
<header class="site-header">
 <div class="wrap bar">
  <a class="brand" href="#top" aria-label="ShowRoom Doctor Z, home"><img src="images/showroom-doctor-z-logo.png" width="300" height="55" alt="ShowRoom Doctor Z"></a>
  <nav aria-label="Main">
   <ul>
    <li><a href="#services">Services</a></li>
    <li><a href="#miracle-spritz">Miracle Spritz</a></li>
    <li><a href="#government">Government</a></li>
    <li><a href="#contact">Contact</a></li>
   </ul>
  </nav>
  <a class="btn btn-call" href="tel:+15594926329"><span class="sr">Call </span>559-492-6329</a>
 </div>
</header>

<main id="main">
<section class="hero" id="top" aria-labelledby="h1">
 <div class="wrap hero-grid">
  <div>
   <p class="eyebrow">Clovis &amp; Fresno, California &middot; Serving Fresno County and the Central Valley</p>
   <h1 id="h1">Auto detailing, ceramic coating and paint correction in Clovis &amp; Fresno, CA</h1>
   <p class="lead">ShowRoom Doctor Z delivers showroom-grade hand auto detailing, ceramic coatings, solar panel care, and commercial facility cleaning—powered by Miracle Spritz, our locally formulated pH 4.6 multi-surface cleaner.</p>
   <p class="cta">
    <a class="btn btn-primary" href="mailto:drz@showroomdrz.com?subject=Quote%20request%20from%20showroomdrz.com">Request a quote</a>
    <a class="btn btn-secondary" href="tel:+15594926329">Call 559-492-6329</a>
   </p>
   <ul class="chips" aria-label="Credentials">
    <li>Showroom Auto Detailing</li><li>Ceramic Coating</li><li>CA Certified Small Business</li><li>Locally Made in Clovis</li>
   </ul>
  </div>
  <figure class="hero-fig">
   <img src="images/showroom-bay.webp" width="680" height="508" alt="A detailed orange sports car on the red-and-yellow floor of the ShowRoom Doctor Z bay in Clovis" fetchpriority="high">
  </figure>
 </div>
</section>

<section id="services" class="section" aria-labelledby="h-services">
 <div class="wrap">
  <h2 id="h-services">What we do</h2>
  <p class="sub">Three specialized divisions, one local team, one phone number.</p>
  <div class="cards">
   <article class="card">
    <h3>Auto detailing, the ShowRoom</h3>
    <p>Hand detailing, ceramic protective coating, paint correction, hard water spot removal, engine bay detail, headlight restoration and full interior restoration at our Clovis shop.</p>
    <p class="meta">NAICS 811192</p>
   </article>
   <article class="card">
    <h3>Solar panel surface care</h3>
    <p>Central Valley panels collect baked-on dust and soot. We clean arrays with Miracle Spritz and methods designed to use less wash water than a conventional rinse-down.</p>
    <p class="meta">Service area: Fresno County and the Central Valley</p>
   </article>
   <article class="card">
    <h3>Commercial facility cleaning</h3>
    <p>Custodial and building surface care, facility support, and recurring service for offices, shops and public buildings in Clovis and Fresno. Tell us the building and schedule for a quote.</p>
    <p class="meta">NAICS 561720, 561790, 561210</p>
   </article>
  </div>

  <h3 class="gallery-h">From the shop</h3>
  <ul class="gallery">
   <li><img loading="lazy" src="images/hand-detail.webp" width="600" height="600" alt="Black classic car after a custom hand detail"><span>Custom hand detail</span></li>
   <li><img loading="lazy" src="images/ceramic-coating.webp" width="600" height="600" alt="Red vintage sedan with a glossy ceramic protective coating"><span>Ceramic protective coating</span></li>
   <li><img loading="lazy" src="images/engine-detail.webp" width="600" height="600" alt="Clean yellow engine cover of a sports car after engine bay detail"><span>Engine bay detail</span></li>
   <li><img loading="lazy" src="images/headlight-restoration.webp" width="600" height="600" alt="Before and after photos of restored foggy headlights"><span>Headlight restoration</span></li>
  </ul>
 </div>
</section>

<section id="miracle-spritz" class="section alt" aria-labelledby="h-ms">
 <div class="wrap two">
  <div>
   <h2 id="h-ms">Miracle Spritz pH 4.6 multi-surface cleaner</h2>
   <p>Miracle Spritz is our own formula, a pH 4.6 multi-surface cleaner made and packaged in Clovis, California. It is an alternative to petroleum-solvent and caustic cleaners for vehicles, maintenance garages, shops, offices and solar panels. U.S. registered trademark No. 6,574,238.</p>
   <ul class="ticks">
    <li>Sizes: 16 oz and 32 oz spray bottles, 1-gallon bottles, 5-gallon carboys and 55-gallon drums</li>
    <li>Used on show cars, fleet vehicles, facility surfaces and solar panels</li>
    <li>Spray on, wipe off</li>
    <li>24 to 48 hour delivery across the Central Valley from our Clovis plant</li>
   </ul>
   <p class="note">Miracle Spritz is a surface cleaner. It is not a disinfectant or a pesticide, and we make no germ-killing claims.</p>
   <p><a class="btn btn-primary" href="mailto:drz@showroomdrz.com?subject=Miracle%20Spritz%20order%20or%20pricing">Ask about Miracle Spritz</a></p>
  </div>
  <figure>
   <img loading="lazy" src="images/miracle-spritz-solar-panel-cleaner.webp" width="900" height="506" alt="Miracle Spritz Solar Panel Cleaner spray bottle next to a solar panel">
  </figure>
 </div>
</section>

<section id="government" class="section" aria-labelledby="h-gov">
 <div class="wrap">
  <h2 id="h-gov">For government and public buyers</h2>
  <p class="sub">ShowRoom Doctor Z Inc. is ready to quote and to be paid through the channels public agencies already use. CalCard and federal micro-purchases under $10,000 are welcome.</p>
  <div class="ids">
   <dl>
    <div><dt>Legal name</dt><dd>ShowRoom Doctor Z Inc.</dd></div>
    <div><dt>SAM.gov</dt><dd>Active, all awards, through October 5, 2027</dd></div>
    <div><dt>Unique Entity ID (UEI)</dt><dd>LA62PCQL63D3</dd></div>
    <div><dt>CAGE code</dt><dd>25K02</dd></div>
    <div><dt>Cal eProcure bidder ID</dt><dd>BID0135007</dd></div>
    <div><dt>California Small Business / Micro Business</dt><dd>DGS Certification ID 2055537 (approved September 30, 2026)</dd></div>
    <div><dt>California DBE (CUCP)</dt><dd>Firm ID 51112</dd></div>
    <div><dt>SAM.gov representations</dt><dd>Self-certified small disadvantaged business; minority-owned; Hispanic American owned</dd></div>
    <div><dt>State of incorporation</dt><dd>California (Secretary of State entity 5027333)</dd></div>
   </dl>
  </div>
  <p class="note">California departments may award up to $249,999.99 to a certified Small Business after obtaining two certified Small Business quotes (Government Code section 14838.5). Please contact us to be included in your quote request.</p>

  <details class="codes">
   <summary>NAICS codes on our SAM.gov registration (22)</summary>
   <table>
    <caption>NAICS codes</caption>
    <thead><tr><th scope="col">Code</th><th scope="col">Industry</th></tr></thead>
    <tbody>
{rows}
    </tbody>
   </table>
  </details>
  <details class="codes">
   <summary>Product and service codes (PSC) on our SAM.gov registration</summary>
   <table>
    <caption>PSC codes</caption>
    <thead><tr><th scope="col">Code</th><th scope="col">Title</th></tr></thead>
    <tbody>
{prow}
    </tbody>
   </table>
  </details>
 </div>
</section>

<section id="faq" class="section alt" aria-labelledby="h-faq">
 <div class="wrap narrow">
  <h2 id="h-faq">Common questions</h2>
  <details><summary>Where are you located?</summary><p>1004 San Jose Ave, Suite 101, Clovis, California 93612. We serve Clovis, Fresno and the California Central Valley.</p></details>
  <details><summary>How do I get a quote?</summary><p>Call 559-492-6329 or email drz@showroomdrz.com with the service you need, the address, and the size of the vehicle, array or space.</p></details>
  <details><summary>Can government agencies buy from you?</summary><p>Yes. We are active in SAM.gov for all awards and are a California certified Small Business and DBE. Our identifiers are listed above.</p></details>
  <details><summary>Is Miracle Spritz a disinfectant?</summary><p>No. Miracle Spritz is a pH 4.6 multi-surface cleaner. It is not a disinfectant or a pesticide, and we make no germ-killing claims.</p></details>
 </div>
</section>

<section id="contact" class="section contact" aria-labelledby="h-contact">
 <div class="wrap two">
  <div>
   <h2 id="h-contact">Contact ShowRoom Doctor Z</h2>
   <address>
    <strong>ShowRoom Doctor Z Inc.</strong><br>
    1004 San Jose Ave, Suite 101<br>
    Clovis, CA 93612<br>
    Phone: <a href="tel:+15594926329">559-492-6329</a><br>
    Email: <a href="mailto:drz@showroomdrz.com">drz@showroomdrz.com</a>
   </address>
   <p>Principal: Jorge R. Zavala, Founder and Chief Executive</p>
   <p>Please call or email to schedule a visit or request a quote.</p>
  </div>
  <div class="cta-box">
   <h3>Tell us what you need</h3>
   <p>Include the service, the address and the size of the job, and we will reply with a quote.</p>
   <p><a class="btn btn-primary" href="mailto:drz@showroomdrz.com?subject=Quote%20request%20from%20showroomdrz.com&amp;body=Service%20needed%3A%0AAddress%3A%0ASize%20of%20vehicle%2C%20array%20or%20space%3A%0APreferred%20date%3A%0AYour%20name%20and%20phone%3A">Email a quote request</a></p>
   <p><a class="btn btn-secondary" href="tel:+15594926329">Call 559-492-6329</a></p>
  </div>
 </div>
</section>
</main>

<footer class="site-footer">
 <div class="wrap">
  <p>&copy; 2026 ShowRoom Doctor Z Inc. All rights reserved. Miracle Spritz is a registered trademark (U.S. Reg. No. 6,574,238).</p>
  <p>1004 San Jose Ave, Suite 101, Clovis, CA 93612 &middot; <a href="tel:+15594926329">559-492-6329</a> &middot; <a href="mailto:drz@showroomdrz.com">drz@showroomdrz.com</a></p>
 </div>
</footer>
</body>
</html>
'''
open('index.html','w').write(html)
