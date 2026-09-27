# Compliance and clarity review, round 2

Reviewed: `report/MAKERS_SANTIAGO_ESPINOSA_CALI.pdf` (15 pages, US Letter 612 x 792 pt, rendered 27 sep 2026 03:11), `report/informe.html`, `report/brief-final.md`, `report/review-log.md`. Text extracted with pypdf; all 15 pages rasterized with pypdfium2 and pages 1 to 7, 11 and 14 inspected visually; `check.py` run; `models/business_model.py` re-run; quotes checked against `docs/06`, `docs/07` and `docs/09`.

Verdict: **not blocking.** Every disqualifying rule passes and every round 1 must-fix that did not depend on Santiago was applied. What is left are six small consistency and wording errors (about 60 words of edits in total, none of which should push the body past 5 pages) and the funding-source clause that needs Santiago.

## 1. Hard rules (disqualification checks)

| Check | Result |
|---|---|
| File name exactly `MAKERS_SANTIAGO_ESPINOSA_CALI.pdf` | PASS |
| Main body at most 5 pages | PASS (pages 1 to 5; 5.045 words) |
| "ANEXOS" opens a new page | PASS (top of page 6, right under the running header) |
| Em dash, en dash, figure dash, horizontal bar, entities, spaced hyphen (PDF text, HTML visible text, HTML source) | PASS (`check.py` ALL PASS; the U+2010 characters in the extracted text are Chrome's soft hyphenation, not dashes) |
| Personal names, kinship ("mamá", "madre", "tía", etc.) | PASS (none; PDF metadata has only the title) |
| Field rule (no lender contact, no recordings or photos of vendors) | PASS (stated on p. 1 and in Annex D "Reglas que cumplí") |
| Collaborator described honestly (in my name, 26 sep, oral summary in two voice notes, count unknown, "muchos" cut and the cut disclosed) | PASS |
| Informant described honestly (second hand, no sampling, bias to bad outcomes, hypotheses only) | PASS |
| Third round of informant questions not cited | PASS |
| Every [Rn] cited is in Annex B and every Annex B entry is cited | PASS (R1 to R39, no orphans either way) |
| Printed URLs free of fake hyphens | PASS (round 1 fix holds; breaks fall without a hyphen) |
| Table 3, "¿Cierra?", Annex E.2 and Annex A hoja 2 match `business_model.py` | PASS |
| Brief section 13 "must not appear" list (Decreto 1469, Battaglia, BRAC, Fenalco, El País, "muchos vendedores", "mis entrevistas", "nosotros", fellowship as funder) | PASS (none present) |

## 2. Must-fix (exact location and correction)

1. **Page 5, "Otras seis opciones descartadas, con sus razones, están en el Anexo H." The count is wrong.** Annex H lists 10 rows. Take out A and F (Descartes 1 and 2) and E (it became the clause) and seven remain: B, C, D, Adelanto sobre ventas por QR, Refinanciar la deuda del gota a gota, App de préstamo rápido, Guía de préstamos. An evaluator who counts will see the mismatch. Correction: "Las otras siete opciones que descarté, con sus razones, están en el Anexo H." (or drop the number: "Las demás opciones que descarté...").

2. **Page 1, "Lo leo como la mercancía del día, y es lo primero que confirmo en campo."** In the present tense this can be read as "I already confirmed it in the field", which overstates the evidence. Everywhere else it is marked "por confirmar" (Table 1). Correction: "Lo leo como la mercancía del día, y es lo primero que voy a confirmar en campo."

3. **Table 3 (page 4), row 3 against rows 4 and 5: "inscrito" and "que pagan" are used for the same divisor.** Row 3 says "$2.800 por vendedor inscrito al mes", but row 4 multiplies $2.800 by the vendors who "pagan" (27 of 40 inscritos in month 3: 27 x $2.800 = $75.600) and row 5 divides the fixed cost by $2.800 to get "904 vendedores que pagan". Read literally, 40 inscritos x $2.800 would give $112.000, not $75.600. Correction in row 3: "$2.800 por vendedor que paga al mes (fuera del mes gratis)". Keep "pagan" in rows 4 and 5 and in Annex A hoja 2 as they are.

4. **Page 3, "Lo que no cubre": "pagar en tercios una deuda de $31.000 a $62.000"** (and Annex E.4 last line, "pagar en tercios $31.000 o $62.000"). $31.000 is never explained, and it sits next to the $30.000 low end of the fiado range used everywhere else (E.1, E.3, E.4, "Para el vendedor"), so it reads like a typo. Per `numbers.md` it is half of a $62.000 fiado. Correction on p. 3: "pagar en tercios la mitad o todo un fiado de $62.000 ($31.000 o $62.000) le quita de 27% a 54% del ingreso de cada uno de esos tres días (cálculo propio)." In E.4: "pagar en tercios la mitad o todo el fiado ($31.000 o $62.000) le cuesta...".

5. **Annex D (page 10), last informant bullet: "Percibe los préstamos que se anuncian por WhatsApp como "más tranquilos" que un gota a gota."** The quote does not match the transcript. `docs/07`, finding 9: "me imagino que algo como más tranquilo que un gota a gota". Quotation marks promise exact words. Correction: "Se imagina los préstamos que se anuncian por WhatsApp como algo "más tranquilo que un gota a gota"." (this also keeps her own hedge, "me imagino").

6. **Table 3 row 6 and Annex E.2 note: "¿De dónde saldría?" is still half answered (carried over from round 1, must-fix 4).** The text says the $8,5 millones "los pondría como capital de la SAS" but not whose money it is. Santiago must confirm the source (own savings, family as shareholders, other) and then add one clause, for example "...con ahorro propio [y aportes de mi familia como socios, si lo confirma], nunca como préstamos del público [R15]". Do not invent it. Not blocking: the current wording is honest, just incomplete.

## 3. Should-fix (clarity, Spanish quality, print)

1. **Point the body to Annex J.** Block 2 of the rubric rewards tracing every distinctive feature to a finding, and Annex J does exactly that, but the body never mentions it. Table 1 caption (p. 2): "Tabla 1. Hallazgo, qué lo respalda y qué decidí (la trazabilidad completa está en el Anexo J)". The caption line has room, so this costs no extra line.
2. **Page 4, point 4: "Lo que aprendí y usé."** It is the answer to a required question ("¿Qué aprendiste de ellas?") but it sits unbolded in the middle of the paragraph. Make it bold like the other lead-ins (`<span class="lead">`), or start the sentence with "Lo que aprendí de ellas y usé:".
3. **Page 4, point 1: "Vendo un servicio de información desde una SAS desde el día 1."** The double "desde" is clumsy. Correction: "Desde el día 1 vendo un servicio de información a través de una SAS."
4. **Page 2 to 3: "Tomado literal, en Cali serían unos 50".** Correction: "Leído al pie de la letra, en Cali serían unos 50".
5. **Page 5, "Riesgos menores: que llueva en Meléndez y no en el carrito".** "Meléndez" is only explained in Annex F. Correction: "que llueva en la estación de la Universidad del Valle y no en el carrito (no medí la distancia)".
6. **Annex A, vendor card: "lo de ese día me lo paga en los 3 días siguientes".** The rule is 3 días de venta (a Sunday does not count). Correction: "lo de ese día me lo paga en sus 3 días de venta siguientes, sin recargo." Optional: add "y se queda con lo de la casa" so the card also carries the $15.000 floor.
7. **Page 3, "Empiezo en Cali, donde están mi campo y mi disparador".** "Disparador" is used here before the reader knows it means the IDEAM station. Correction: "donde están mi campo y la estación que dispara la cláusula".
8. **Anglicism "app".** Figure 1 ("sin cédula, RUT ni app"), Table 2 week 1 row ("celular ni app"), Annex J. Fundéu recommends "aplicación". Low priority, because "app" is common in Colombia and the figure box is narrow; change it at least in Table 2 and Annex J.
9. **Numbering collision (carried over).** The list "1. No soy entidad financiera ... 4. El problema ya tiene soluciones" is followed right away by the heading "3. Los números del negocio". A lettered list (a to d) would remove the collision without costing space.
10. **Annex C refers to "A" and "F" before Annex H defines them** ("cambiar de A a la cláusula", "descartar F"). Add "(Anexo H)" after the first "A".
11. **Print density.** Body 9,5 pt with 1,32 line height; page 5 has 1.132 words. It reads fine on screen and is acceptable on paper, but it is at the limit, so do not shrink the type further. The citation tags are 7 pt in the accent blue: on a black and white printer they come out light grey but still legible. The Annex A snapshot is 7,4 pt with 13 columns: tight, but it is an annex. No change needed unless space opens up.
12. **Footer "x / 15".** It is not a compliance problem because ANEXOS is explicit, but an evaluator skimming the footer sees 15 pages. Optional: add under the byline "Cuerpo: páginas 1 a 5; anexos: páginas 6 a 15."

## 4. Coverage of "Lo que debes entregar"

| Part | Question | Where | Status |
|---|---|---|---|
| 1 | Tamaño | p. 1 "Qué tan grande es" | OK |
| 1 | Consecuencias | p. 1 | OK |
| 1 | Por qué falla el formal | p. 1 | OK |
| 1 | Qué hace bien el informal | p. 1 | OK |
| 1 | Necesidades, comportamientos, barreras; habla con personas; datos reales con fuentes | p. 1 to 2, Tabla 1, Annex D | OK (fix must-fix 2) |
| 2 | Usuario exacto | p. 2 "Usuario, cliente y alcance" | OK |
| 2 | Problema específico | p. 2 | OK |
| 2 | Paso a paso | Figura 1, Tabla 2, Reglas | OK |
| 2 | Cómo resuelve el problema | p. 3 "Por qué la lluvia", p. 4 cuatro puntos | OK, with limits stated in "Lo que no cubre" |
| 2 | A cuántas personas podría impactar | p. 2 (468 in month 12; ceiling 17.745; 286.061 in 24 cities) | OK (round 1 gap closed) |
| 2 | Soluciones similares | p. 4 point 4 and "A qué se parece" | OK |
| 2 | Qué aprendí de ellas | p. 4 "Lo que aprendí y usé" | OK (should-fix 2 for visibility) |
| 3 | 1. Inversión inicial | Tabla 3 row 1 | OK |
| 3 | 2. Costos mensuales | Tabla 3 row 2 | OK (minimum wage now sourced, R39) |
| 3 | 3. Cuánto deja cada usuario, con impago | Tabla 3 row 3, "Para quien paga", E.3 | OK (fix must-fix 3) |
| 3 | 4. Usuarios e ingresos meses 3, 6, 12 | Tabla 3 row 4 | OK |
| 3 | 5. Break-even, usuarios y mes | Tabla 3 row 5, "¿Cierra?" | OK |
| 3 | 6. Cuánto para sobrevivir y de dónde | Tabla 3 row 6, E.2 note | Amount OK; source half answered (must-fix 6) |
| 3 | Supuesto detrás de cada número | Tabla 3 column 3, E.1 | OK |
| 4 | Dos alternativas: por qué parecían buenas, qué cambió | p. 5 Descarte 1 and 2 | OK |
| 4 | Riesgo real | p. 5, three layers with mitigation and kill criteria | OK |
| 5 | Prototipo: capturas, qué hace, qué no, tiempo, herramientas, a quién se lo mostré | Annex A | OK, all six items |
| Platform | Cuatro puntos (no entidad financiera; ingreso diario sin ahorro; desconocido de 22 años; ya hay soluciones) | p. 4 "Cómo una sola pieza resuelve los cuatro puntos" | OK |

## 5. Field evidence and privacy

- Informant quotes checked against `docs/06` and `docs/07`: "para pagarle a uno, se meten en otro", "que tengan casa o... alguna propiedad... o un trabajo donde les paguen por nómina", "ni volvió a sacar el negocio", "le prestan a un porcentaje mucho más bajito", "la necesidad o porque van a poner un negocio", "un banco no le presta, entonces les toca meterse con gota a gotas", "Si usted no paga, uno le cobra como sea" all match. The only mismatch is "más tranquilos" (must-fix 5).
- Collaborator quote matches `docs/09`; the cut of "que eso les pasa a muchos de ellos" is marked with [...] and disclosed.
- "Vendedora de arepas" is generalized to "vendedora de comida" everywhere. Neither the kinship, the neighborhood nor the names from `docs/07` appear. The police collector is only in Annex D, framed as explanation.
- Place names (estación Universidades del MIO, galería Santa Elena, Aguablanca, Palmira) come from the field site or from published studies and identify no person.
