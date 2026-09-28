# Content Strategy Brief — drhenriqueleal.com.br

Prepared as part of the SEO/CRO improvement pass on the `seo-cro-improvements` branch.
This is a set of recommendations, not new pages — nothing here should be published as
medical/clinical content without Dr. Henrique's review and sign-off, since claims about
procedures, results and durations are regulated (CFM/CFO/CRBM advertising rules).

## 1. What the site already covers well

The site has strong topical coverage of its core procedures, each with a cornerstone
page plus 1-3 supporting blog posts:

- Harmonização facial (+ masculina guide, + mitos e verdades)
- Botox (+ preventivo, + "quanto tempo dura")
- Fios de PDO (+ lifting sem cirurgia, + comparativo com bioestimulador)
- Bioestimuladores de colágeno (+ comparativo Sculptra/Radiesse/Elleva)
- Preenchimento labial (+ natural lips, + cuidados pós-procedimento)
- Estética íntima (+ preenchimento com ácido hialurônico, + rejuvenescimento e autoestima)
- Ozonioterapia (+ benefícios para pele, + uso pós-procedimento)
- Terapia capilar (+ queda de cabelo, + microinfusão capilar)
- Rinomodelação (+ "dói?", cuidados e duração)
- Protocolo Bioforce (+ regeneração celular)
- Peptídeos bioativos

This is a genuinely well-built topical cluster — most competitors in Curitiba don't have
this much supporting content per procedure.

## 2. Gaps worth considering

**A. Harmonização facial feminina** — there's a dedicated "masculina" guide, but no
equivalent feminine-focused cornerstone content, even though the main harmonização
facial page presumably serves a mostly female audience already. A short guide framed
around common female concerns (linha da mandíbula suave, olheiras, sulco nasogeniano)
would balance the pair and pick up "harmonização facial feminina curitiba"-style queries.

**B. Corporal / glúteo harmonization** — the homepage schema markup (JSON-LD
`hasOfferCatalog`) references "Harmonização Corporal" as a service area, but there is no
dedicated page for it, and competitors offering bioestimuladores corporais or
"harmonização glútea" content rank for a meaningful slice of local searches. Worth
confirming with Dr. Henrique whether this is actually a service he performs before
building a page — if not, the schema mention should be removed for accuracy.

**C. Pricing transparency page** — none of the FAQ answers give even a price range
("o investimento depende da avaliação"), which is standard and appropriate for medical
advertising, but a page addressing "quanto custa harmonização facial em Curitiba" in
general terms (ranges seen in the market, what affects price, financing/parcelamento
options) captures high-intent searches without quoting a fixed price.

**D. Location/neighborhood content** — the clinic is in Água Verde; there's no content
targeting nearby bairros or cities (Batel, Bigorrilho, São José dos Pinhais, Curitiba
region generally beyond the city-wide keyword). Even one well-built "Harmonização
Facial no Batel/Água Verde" style section on the location page could pick up
near-me-adjacent queries.

**E. Before/after case studies as standalone content** — `resultados.html` is a gallery,
but there are no individual "case study" write-ups (procedure + concern + outcome,
without overpromising) that could rank for long-tail queries and support E-E-A-T
(genuine outcomes described by the practitioner). Would need real patient consent and
photos already covered under existing image usage.

**F. Comparison/"vs" content beyond what exists** — the site already compares
Sculptra/Radiesse/Elleva and Fios de PDO vs bioestimulador, which is good.
A "Botox vs Bioestimulador" or "Preenchimento vs Bioestimulador" style page rounds out
the cluster and captures decision-stage searches people make before booking.

## 3. Lower-priority / longer-term

- FAQPage schema exists per-procedure page and now on the homepage (added in this pass);
  a dedicated `/duvidas` or `/faq` page aggregating all of them (with its own schema)
  could become a strong internal-linking hub.
- Video content: none of the audited pages embed video; even short procedure
  walkthroughs or patient testimonials (with consent) tend to perform well for
  aesthetic-medicine SEO and dwell time.
- Seasonal content: harmonização facial has real seasonal search patterns
  (pre-Carnaval, pre-summer, year-end). A lightweight seasonal landing/blog angle timed
  to those windows could capture demand spikes competitors are likely already targeting.

## 4. Not recommended

- Do not add generic, non-differentiated "what is X procedure" content that just
  restates what's already on the cornerstone pages — the current supporting-post
  structure (guide / comparison / myth-busting / post-care) per procedure is a good
  pattern; new posts should follow one of those angles, not duplicate the pillar page.
- The CRO-PR/CRBM-PR registration-number discrepancy flagged earlier in this review
  has been resolved: the correct numbers are **CRO-PR 31739 (odontologia)** and
  **CRBM-PR 8966 (biomédico)**, confirmed by Dr. Henrique/Nathan and applied site-wide.
  Any new page should use these two numbers.
