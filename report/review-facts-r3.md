# Fact and compliance check, review round 3

Reviewed: `report/MAKERS_SANTIAGO_ESPINOSA_CALI.pdf` (15 pages, rendered 03:30) against `report/versions/v1_MAKERS_SANTIAGO_ESPINOSA_CALI.pdf`. I extracted the text of both with pypdf, split it into sentences and diffed it. Then I checked every changed or added number, quote and claim against `report/fact-pack.md`, `report/numbers.md`, `report/prototipo.md`, `report/prototipo-snapshot.html`, `models/business_model.py` (`payer_view`, `SELLING_DAYS_PER_MONTH`) and the research files (`08-confianza-canales-fiado.md`, `09-voz-del-usuario.md`, `12-mecanismos-dia-malo.md`, `12a`, `12b`).

`check.py` rerun: **RESULT: ALL PASS** (15 pages, body 5 pages, ANEXOS at the top of page 6, no dashes in the PDF or the HTML, no denylisted names, body 5.137 words). My own scan found no U+2014, no U+2013 and no spaced hyphen in the new PDF text.

Verdict: **not blocking.** Every new number is correct and traceable. Nothing new invents field evidence, and no reference was lost: every R cited in v1 is still cited, both in the body and overall. The funding sentence is unchanged and neutral. Page 1 still says "Yo no entrevisté vendedores en persona". Four wording issues remain. None is a wrong number, but one of them states as fact something the report says elsewhere it has not measured.

## What changed from v1, and whether it holds

| # | Location | New or changed text | Verified against | Result |
|---|---|---|---|---|
| 1 | p.1 | Cut: 35,6% in 24 cities, Perú 36%, 96,5% / 8,0% | 35,6% still in Annex G; R21, R7, R9 still cited | OK |
| 2 | p.2, Usuario | "3 estaciones del IDEAM con dato al día en Cali (Anexo F)" | 12b line 51: Univalle 0026055120, Base Aérea 0026085170, Farallones 0026055100, alta. Annex F lists the same three | OK |
| 3 | p.3, Tabla 2 | "Cada noche el programa le pregunta al minorista '¿vendedor 3 pagó su tercio?'; con el tercer sí ... 'puente cerrado'" | This is a design statement, consistent with the "Esa noche" row and with `prototipo.md` ("No ... lleva el registro de un minorista real") | OK |
| 4 | p.3, Reglas | Cut: "En los 12 meses medidos no hubo rachas de tres" | Still in Table 1 ("rachas de 1 o 2 días") and Annex F ("ninguna de tres o más") | OK |
| 5 | p.3, Lo que no cubre | "$2.184 para la casa" in two-day runs | Snapshot days 15 and 16: $36.416 paid of the deferred balance, $2.184 left; `prototipo.md` | Number OK, wording see must-fix 2 |
| 6 | p.3 and Annex A | Sixths: "unos $7.800 diarios ... (20% del ingreso de un día)" | 46.820 / 6 = 7.803; 7.803 / 38.600 = 20,2% | OK |
| 7 | Annex A | "entre dos días de lluvia pasan en promedio 11 días de venta (294 entre 26)" | 294 / 26 = 11,3; 26 of 294 in numbers.md, 12, 12b | OK (see should-fix 6) |
| 8 | p.4, point 1 | "Queda para el abogado si una regla pagada por quien fía puede leerse como seguro (Anexo I)" | brief-final line 114 | OK |
| 9 | p.4, point 4 | CREO beneficiary count cut, [R31] kept | | OK |
| 10 | p.4, Tabla 3 row 3 | "$4.000 ... 2,5% de los $161.200 ... ($62.000 de fiado por 26 días por 10% de margen [S]; con fiado de $30.000, 5,1%; cálculo propio)" | 62.000 x 26 x 10% = 161.200 (`payer_view`: fiado x SELLING_DAYS_PER_MONTH x 12 x 10% = 1.934.400 a year); 4.000 / 161.200 = 2,48%; 30.000 x 26 x 10% = 78.000, 4.000 / 78.000 = 5,13%. 10% margin is [S] in numbers.md line 31 | Numbers OK, wording see must-fix 3 |
| 11 | p.5, Para quien paga | "con 12, ... unos $562.000 sin cobrar esa tarde, y una racha de dos días, $1,12 millones (cálculo propio, Anexo A)" | 12 x 46.820 = 561.840; 12 x 93.640 = 1.123.680. 12 vendors per retailer matches Table 3 row 4 | OK |
| 12 | p.5, Descarte 1 | "Tercera, el campo mostró que el vendedor ya tiene crédito diario sin interés" | Collaborator's words, fact-pack C16 ("El minorista no le cobra interés") | Supported as reported; see should-fix 5 |
| 13 | p.5, riesgo capa 1 | "50,7% ... negocio, 28,9% a gasto personal y 20,5% a los dos [R4, C. 21.1]" | 09 line 51 and line 435 ("confirmado", alta), 08 line 60 | OK |
| 14 | p.5, riesgo capa 1 | "el cuadro no separa pagarle al que fía de comprar mercancía" | The table's three categories are negocio, gastos personales and ambos | OK (a fair reading) |
| 15 | p.5, riesgo capa 2 | "si el minorista no tiene esos $562.000 de caja" | Same as row 11 | OK |
| 16 | p.5, riesgos menores | "que llueva en el carrito y no en la estación, que es poco en el piloto y pesa más al crecer" | Annex F: "No he medido la distancia"; p.2: "no sé ... a qué distancia"; fact-pack / 12 R.4 row 10 marks "la estación queda cerca de los carritos" as unsupported | **Unsupported: must-fix 1** |

The rest of the diff is hyphenation and reflow only: page 1 line breaks, and the Annex A table that now splits across pages 6 and 7.

## Must fix

1. **Page 5, "Riesgos menores", last clause: "que llueva en el carrito y no en la estación, que es poco en el piloto y pesa más al crecer."** This claim is unsupported, and the report contradicts it twice: page 2 says "no sé ... a qué distancia la lluvia de la estación deja de ser la del carrito", and Annex F says "No he medido la distancia entre la estación de la Universidad del Valle y los carritos de la estación Universidades del MIO". Research file 12 (R.4, row 10) lists "La estación queda cerca de los carritos" as a claim without support. Correction: "que llueva en el carrito y no en la estación (no medí la distancia), que pesa más al crecer." If one word matters: "que llueva en el carrito y no en la estación; no medí la distancia y pesa más al crecer."

2. **Page 3, "Lo que no cubre": "Su punto débil son las rachas de dos días: los tercios se suman y dos días seguidos le quedan $2.184 para la casa (Anexo A)."** The number is right, but a reader can take "dos días seguidos" to mean the two rain days. On those days the vendor keeps $15.000; the $2.184 falls on the two selling days after the run (days 15 and 16 of the example). Correction: "Su punto débil son las rachas de dos días: los tercios se suman y en los dos días de venta siguientes le quedan $2.184 para la casa (Anexo A)." In the sentence before it, "$15.000 para la casa, no $38.600" dropped the "hasta" from the rule. Suggested: "hasta $15.000 para la casa, no $38.600."

3. **Page 4, Tabla 3 row 3: "($62.000 de fiado por 26 días por 10% de margen [S] ...)".** In this report, "26 días" means the 26 rain days a year almost everywhere else: Descarte 2, Annex F, "294 entre 26". Here it means 26 selling days a month (`SELLING_DAYS_PER_MONTH = 26`). An evaluator who recomputes it can read it as 26 rain days, and $161.200 is also the numbers.md figure for 10% default on a year of deferred fiado (62.000 x 26 rain days x 10%). Correction: "($62.000 de fiado por 26 días de venta al mes por 10% de margen [S]; ...)".

4. **Consistency between the sixths test and the rules (page 3, "Lo que no cubre", and Annex A; versus Table 2 "Puente sin cerrar" and page 5 "Cómo sé si me equivoqué").** Round 3 says the first thing to test with the first retailer is paying in sixths. Table 2 still marks a vendor as not eligible if the bridge has not closed "a los 5 días de venta (3 de tercios y 2 de margen)". The pilot kill metric says "al menos 90% de los puentes se cierra en 5 días de venta". With sixths, no bridge can close in 5 selling days, so the test as written would trip both rules. Correction, in the Annex A sentence (cheaper than the body): add "(con sextos, la ventana para cerrar el puente pasa de 5 a 8 días de venta)". Or in the body after "pagar en sextos": "con ventana de 8 días".

## Should fix (low risk)

5. **Page 5, Descarte 1: "Tercera, el campo mostró que el vendedor ya tiene crédito diario sin interés."** The support is one second-hand oral summary (C16), and fact-pack C16 warns: "no afirmar que es gratis sin preguntar el precio de contado" (WIEGO: the interest can hide in the price). v1 said something similar ("el campo movió la pregunta"), so this is not new risk. "Mostró" is still stronger than the evidence. Suggested: "Tercera, lo que trajo el colaborador: el vendedor ya tiene crédito diario sin interés."
6. **Annex A: "que caben porque entre dos días de lluvia pasan en promedio 11 días de venta (294 entre 26, cálculo propio)".** The average is correct, but rain clusters: October 2025 had 7 days, and there were 3 two-day runs. The two-day run is exactly the case this sentence is about. Suggested: "que caben en promedio (294 entre 26, unos 11 días de venta entre días de lluvia; en octubre, menos)".
7. **Two different 5,1% figures, one page apart:** Table 3 (fee as a share of margin with $30.000 of fiado) and "Para quien paga" (share of vendors whose loss pays for the clause). Both are right. If a word can be spared, write the Table 3 one as "con fiado de $30.000, la tarifa es 5,1% del margen".
8. **Page 5, "unos $7.800 diarios por cada día de lluvia".** In a two-day run, the second day's deferred amount is $62.427, not $46.820, because day 14 also carries day 13's first third (snapshot row 14). The sixth of that is about $10.400. "Unos $7.800" is right for a single rain day, which is what the sentence says. No change is needed unless it comes up in the interview.

## Compliance

- Dashes: none (check.py, plus my own scan of the new PDF text for U+2014, U+2013 and " - ").
- Main body is 5 pages. ANEXOS starts on page 6. `style.css` was not touched in this round, according to the review log. The round 2 size overrides in `informe.html` are unchanged.
- No personal names (check.py). No age stated.
- Funding sentence (Table 3 row 6) is unchanged from v1 and neutral: "los pondría como capital de la SAS, nunca como préstamos del público [R15]; la diferencia hasta $34,5 millones sería capital semilla que hoy no tengo". Santiago still has to confirm the real source.
- Field evidence: no vendor count appears, no in-person interview is claimed, and "Yo no entrevisté vendedores en persona" is still on page 1.
- Own calculations are labelled on every new number: Table 3 row 3, "Para quien paga", sixths, Annex A.
- Side note outside the PDF: `ENTREGA.md` section 6 still lists the six items as pending, and the pitch says "¿vendedor 3 pagó su parte?" where the report says "su tercio". Update both before handing it over.
