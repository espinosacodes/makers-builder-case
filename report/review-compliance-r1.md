# Compliance and clarity review, round 1

Reviewed: `report/MAKERS_SANTIAGO_ESPINOSA_CALI.pdf` (15 pages, US Letter, rendered 27 sep 2026 02:52), `report/informe.html`, `report/brief-final.md`. Text extracted with pypdf; pages 1 to 7 rasterized and inspected visually; `check.py` run; `models/business_model.py` re-run to cross-check every number in Table 3 and Annex E.

Verdict: **not blocking.** Every disqualifying rule passes. The fixes below are cheap and improve source verifiability and clarity.

## 1. Hard rules (disqualification checks)

| Check | Result |
|---|---|
| File name exactly `MAKERS_SANTIAGO_ESPINOSA_CALI.pdf` | PASS |
| Main body at most 5 pages | PASS (pages 1 to 5) |
| "ANEXOS" opens a new page | PASS (top of page 6) |
| Em dash, en dash, figure dash, spaced hyphen as a dash (PDF and HTML) | PASS (none; `check.py` all pass) |
| Personal names or kinship ("mamá", "madre") | PASS (none) |
| Field rule (no lender contact, no recordings) | PASS (stated in body p. 1 and Annex D) |
| Third round of informant questions cited | PASS (not cited) |
| Every [Rn] cited is listed in Annex B and vice versa | PASS (R1 to R37, no orphans) |
| Numbers in Table 3, "¿Cierra?", Annex E match `business_model.py` | PASS |
| Four required parts plus optional prototype present | PASS (sections 1 to 4, Annex A) |

## 2. Must-fix (exact location and correction)

1. **Annex B, printed URLs carry fake hyphens (source verifiability).** `hyphens: auto` on `body` hyphenates link text, so the printed URLs are wrong: R1 and R5 "EMI-CRON" (real: EMICRON), R9 "...8c2-d615122", R13, R14, R15 "gestornorma-tivo" / "gestor-normativo", R23 "de-fault", R34 "ans-wer", R36 "vi-vienda". The links are clickable in the PDF, but a printed copy cannot be typed back. Fix in `informe.html` `<style>`: replace `.bib a { overflow-wrap: anywhere; }` with `.bib a { hyphens: manual; -webkit-hyphens: manual; overflow-wrap: anywhere; word-break: break-all; }`. Re-render and re-check that the body is still 5 pages.
2. **Annex J, row "Casi la mitad no usa celular en el negocio" is factually inverted.** R4 says 48,4% USE a phone, so 51,6% do not. Correct to: "Más de la mitad (51,6%) no usa celular en el negocio; límites legales al contacto de cobro".
3. **Thesis line, page 1 (the most read sentence).** "Le gana la tarde en que un día sin ventas rompe..." reads as "the afternoon beats it". Correct to: "Le gana en la tarde en que un día sin ventas rompe el crédito que el vendedor ya tiene: el fiado diario sin interés de su minorista."
4. **Table 3 row 6 and Annex E.2 note: "¿De dónde saldría?" is only half answered.** The text says the $8,5 millones "entrarían como capital de la SAS" but not from whom. The model itself prints "Funding of the cash needed: PENDING founder confirmation". Santiago must confirm the source, then write it in one clause, for example: "...entrarían como aporte de capital a la SAS con ahorro propio [y de mi familia como socios, si Santiago lo confirma], nunca como préstamos del público [R15]". Do not invent the source.
5. **Section 2, "¿A cuántas personas podría impactar?" has no direct answer in the proposal text.** The pieces are scattered (286.061, 17.745, 904 at equilibrium) and the plan numbers live only in Table 3. Add one sentence at the end of "Usuario, cliente y alcance" (page 3): "Con el plan de la Tabla 3 llegaría a 468 vendedores en el mes 12; el techo en Cali A.M. son 17.745 ambulantes, y no sé cuántos de ellos sacan fiado." Trim a few words elsewhere on page 3 if it pushes the table.
6. **Legal wording of "captación", page 4 point 1 and Annex J.** "así que no hay captación, que es delito" is imprecise: the crime is capturing money from the public massively and habitually without authorization. Correct p. 4 to: "La plata del vendedor nunca pasa por mi cuenta, así que no capto dinero del público, que sin autorización es delito [R14; R15]." Correct Annex J row to: "Captar dinero de más de 20 personas sin autorización es delito [R14; R15]".
7. **Undefined terms in the body.** "puente" appears in Table 2 ("puente cerrado") and in "Cómo sé si me equivoqué" ("90% de los puentes") without definition; "día de disparo" appears in "Reglas" before it is defined; "Cali A.M." and "CV" are never expanded; the letters "C" (p. 2) and "B, C, D" (p. 5) mean nothing to a reader who has not opened Annex H. Fixes:
   - p. 2, first mention of the rule: add "(cada aplazamiento lo llamo un puente)" after "sin recargo".
   - p. 3, Reglas: "Tope de 3 días de disparo seguidos" becomes "Tope de 3 días de lluvia seguidos con la cláusula activa" or define once "día de disparo (5 mm o más)".
   - p. 3: "en Cali A.M." first time becomes "en Cali y su área metropolitana (Cali A.M.)"; "(CV de 8,4%)" becomes "(coeficiente de variación del DANE de 8,4%)".
   - p. 2: "(C, Anexo H)" becomes "(la opción C, cuota diaria de la deuda mensual; Anexo H)". p. 5: "También descarté B, C, D, ..." becomes "También descarté una alcancía con adelanto, convertir la deuda mensual en cuota diaria, el surtido en consignación, refinanciar al gota a gota, una app de préstamo y una guía de préstamos (Anexo H)."
8. **Unsourced figure presented as fact: salario mínimo 2026 ($1.750.905), Table 3 row 2** ("Todo [S] salvo el salario"). Add a reference in Annex B (the official 2026 minimum wage source the research used in frente 07; the brief warns not to cite Decreto 1469 de 2025 as in force) and cite it in the row.

## 3. Should-fix (clarity, Spanish quality, print)

1. **Anglicisms.** p. 4 point 4 "microcrédito con ticket promedio de" becomes "microcrédito con monto promedio de". Annex A "No tiene link público" becomes "No tiene enlace público". Annex A "el script del Anexo E" and "está en el script" become "el programa del Anexo E" / "está en el programa". "Break-even" in Table 3 is the case's own term, keep it, but "5. Punto de equilibrio (break-even)" reads better.
2. **English quote, page 1.** "I take stock on credit every morning then pay back in the evening" (Kenia): add the translation in parentheses or paraphrase: "saco mercancía fiada cada mañana y la pago en la tarde".
3. **Page 4, point 3, awkward phrase.** "La confianza no desaparece: se mueve a la venta a pocos minoristas" becomes "La confianza no desaparece: se traslada a unos pocos minoristas, a los que tengo que venderles la cláusula y que tampoco me conocen".
4. **Page 4, point 4, CREO "que no escaló [R31]" is a judgment without the number.** Add the evidence: "el programa CREO, con meta de un millón de créditos y 15.779 beneficiarios a enero de 2024 [R31]".
5. **Page 4, "A qué se parece": "al plazo que da BEES" has no source.** Either cite R35 (AB InBev 20-F, which covers BEES) or drop "y al plazo que da BEES".
6. **Page 5, "Para el vendedor": "En el prototipo (Anexo A), tres días de lluvia en un mes terminan en 3 préstamos encadenados y $19.866 de interés"** could be read as observed data. Add "En un mes de ejemplo del prototipo (Anexo A, lluvia inventada), ...".
7. **Page 4, the list "1. No soy entidad financiera ... 4. El problema ya tiene soluciones" is followed by the heading "3. Los números del negocio".** Two numbering systems collide. Use "Punto 1", "Punto 2" or a lettered list (a to d), and make "Cómo una sola pieza resuelve los cuatro puntos" an h3 so its lead line does not sit alone at the bottom of page 3.
8. **Byline and running header disagree.** Byline: "Santiago Espinosa · Cali · Builder Case Makers Fellowship"; header: "Santiago Espinosa · Cali, Colombia · Makers Fellowship, Builder Case". Use the header form in both.
9. **Figure 1 relies on color only** (black = mercancía o información, blue = plata). On a black and white printer the legend is lost. Make the money arrows dashed and update the legend.
10. **Annex H caption "Puntajes de 0 a 40"** with a 1 to 5 scale per criterion (minimum 8). Correct to "Puntajes sobre 40".
11. **Break-even rounding is mixed.** 904, 2.531, 279 and 355 are rounded up, but 1.150 (1.150,4), 550 (550,2) and 3.571 (3.571,4) are rounded down, which leaves the fixed cost slightly uncovered. Either write 1.151, 551 and 3.572 (p. 5 "¿Cierra?", Annex E.2, Annex A hoja 2) or prefix with "unos". Low priority.
12. **Annex A, hoja 1 results.** "Queda para la casa" shows $916.560 with the clause and $939.540 with the gota a gota, which at first glance says the clause is worse. Put "Casa menos deuda al día 30" first, or add "(sin contar lo que sigue debiendo)" to the "Queda para la casa" row.
13. **Page 4, point 2** "como cobra el propio informal" has no citation there; add [R20].
14. **Print density.** Body text 9,8 pt Charter and tables 8,5 pt are legible on Letter. Page 5 carries about 1.050 words and reads dense but acceptable. The prototype snapshot in Annex A uses 7,4 pt with 13 columns: legible on screen, tight on paper; raise to 7,8 pt if the annex page break allows. The page counter reads "x / 15"; not a problem because ANEXOS is explicit on page 6, but an evaluator skimming the footer sees 15. Optional: counter only in the body, or a line under the title "Cuerpo: páginas 1 a 5; anexos: 6 a 15".
15. **Style tells.** The "no es X, es Y" antithesis repeats (p. 1 "No es el precio... Tampoco es... Es la forma"; "tiempo, no plata"; "corre la deuda, no la achica"; "no por riesgo de crédito"; "no cuando el negocio quiere crecer"). Each works alone; together they sound templated. Rewrite two of them as plain statements.

## 4. Coverage of "Lo que debes entregar"

| Part | Question | Where | Status |
|---|---|---|---|
| 1 | Tamaño | p. 1 "Qué tan grande es" | OK |
| 1 | Consecuencias | p. 1 | OK |
| 1 | Por qué falla el formal | p. 1 | OK |
| 1 | Qué hace bien el informal | p. 1 | OK |
| 1 | Necesidades, comportamientos, barreras encontradas; habla con personas | p. 1 to 2, Tabla 1, Annex D | OK, honest framing of field evidence |
| 2 | Usuario exacto | p. 2 | OK |
| 2 | Problema específico | p. 2 | OK |
| 2 | Paso a paso | Tabla 2, Figura 1, Reglas | OK |
| 2 | Cómo resuelve el problema | p. 3 to 4, cuatro puntos | OK |
| 2 | A cuántas personas podría impactar | p. 3 (partial) | Must-fix 5 |
| 2 | Soluciones similares | p. 4 punto 4 and "A qué se parece" | OK |
| 2 | Qué aprendí de ellas | p. 4 "Lo que aprendí y usé" | OK |
| 3 | Inversión inicial, costos mensuales, ganancia por usuario (con impago), usuarios meses 3, 6 y 12, break-even, cuánto para sobrevivir | Tabla 3, "¿Cierra?", Annex E | OK except the funding source (must-fix 4) |
| 3 | Supuesto detrás de cada número | Tabla 3 column 3, Annex E.1 | OK |
| 4 | Dos alternativas reales: por qué parecían buenas y qué cambió | p. 5 Descarte 1 and 2 | OK |
| 4 | Riesgo real de la propuesta | p. 5 | OK, two layers, premise risk first |
| 5 | Prototipo: capturas, qué hace, qué no, tiempo, herramientas, a quién se lo mostré | Annex A | OK, all six items |

## 5. Field evidence and privacy

- Collaborator described correctly (conversations on 26 sep, oral summary in two voice notes, count unknown, "Yo no entrevisté vendedores en persona"). The quantifying phrase "eso les pasa a muchos de ellos" was cut and the cut is disclosed. Good.
- Informant described as second-hand, no sampling, bias to bad outcomes; no kinship stated. Good.
- The police-collector detail appears only in Annex D, framed as explanation, not data. Good.
- Place names (estación Universidades del MIO, galería Santa Elena, Aguablanca) come from the field site or from published studies and do not identify a person.
