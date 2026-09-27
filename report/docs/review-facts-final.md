# Final facts and compliance review: informe-docs.md

Date: 27 Sep 2026. Scope: every line changed against git HEAD, checked against `models/business_model.py` output, `docs/research/13a-financiacion.md`, `docs/research/13b-escala-latam.md`, `docs/research/02-comparacion-regional.md` and Anexo A.

## Result

One must-fix (blocking). Everything else passes.

### Must fix

1. Anexo C, verification stats read as a partition that does not add up. The text says "se revisaron 243 cifras: 192 confirmadas, 49 corregidas, 30 marcadas como no verificadas y 1 eliminada". Those parts sum to 272, not 243 (192 + 49 + 1 = 242, so the 30 unverified overlap with the other statuses). The numbers match the repo README line 32, so the source is the same, but a reader who adds them sees an arithmetic error in the method annex. Suggested replacement with the same length, so fit is unchanged:
   "En la primera pasada de verificación se revisaron 243 cifras: 192 quedaron confirmadas, 49 corregidas y 1 eliminada por fuente inexistente, y 30 se marcaron como no verificadas (una cifra puede tener más de una marca)."
   If the exact breakdown is known, better to state it so the parts sum to 243. Apply the same wording to README.md line 32 so the repo and the report agree.

## Checks that pass

### Tabla 3 against the model (LEAN_FREE_LEGAL and LEAN_PAID_LEGAL)

| Claim in report | Model output | OK |
|---|---|---|
| Inversión $0,3 M, o $3,3 M with paid legal opinion | 300,000 / 3,300,000 | yes |
| Costo mensual $430.000 months 1 to 6; $780.000 from month 7 | 430,000 then 780,000 (200k + 80k + 150k; accountant 350k from month 7) | yes |
| SAS $0,6 M in month 7 | 600,000 once in month 7 | yes |
| Por usuario $2.800 | 4,000 x 90% minus 800 = 2,800 | yes |
| Month 3: 27 paying, $108.000, $75.600; month 6: 108, $432.000, $302.400; month 12: 416, $1.664.000, $1.164.800; 40/144/468 enrolled; 4, 12, 36 retailers | identical | yes |
| Break-even 279 paying, month 10; $780.000 / $2.800 | 279, month 10 (278.6 rounds up) | yes |
| Para sobrevivir $3,4 M (free) and $6,4 M (paid), losses to month 9 | 3,386,800 and 6,386,800, deepest point month 9 | yes |
| Comparison with salary: $2.530.905, 904, month 22, $34,5 M | 2,530,905; 904; 22; 34,523,005 | yes |
| Conservative: no close with salary in 60 months; without salary month 27 and $15,1 M | not reached in 60; month 27; 15,138,000 | yes |
| "unos 50 en Cali ... frente a los 279 del equilibrio" | 17,745 x 15.4% x 1.8% = 49.2; 279 | yes |
| Month 12 enrolled 468 | 468 | yes |

Internal consistency: rows 1, 2, 5 and 6 all describe the same lean plan; row 4 ramp is the base ramp used by the lean model; the comparison line under the table and the "¿Cierra?" paragraph use the same with-salary numbers; Anexo B now says hoja 2 matches the comparison, not Tabla 3. Consistent with `report/numbers.md` section 1b.

Non-blocking notes (no change required):
- The conservative "sin salario ... mes 27 con $15,1 millones" uses the old cost basis (full $780.000 from month 1 plus the $3,9 M investment), not the lean structure. The number is correct as the model prints it, and it is more pessimistic than a lean conservative case would be, so it errs on the safe side.
- The conservative description dropped "$1.000 de costo directo"; still accurate, just less complete.

### Financing (13a)

- Fondo Emprender: only Convocatoria Nacional Focalizada 124 Catatumbo is open; no general or Valle call. Report says it helps only if a Cali call opens and "hoy no hay" [R31]. Matches.
- Fundación WWB Colombia: microempresarias, educación financiera, no published amounts. Report uses it as a pilot ally, not money [R37]. Matches.
- BID Lab: seed equity US$200K to US$500K, ecosystem projects US$750.000 to US$2M; used only for phase 3 with 12 months of pilot data, "no un ingreso proyectado" [R38]. Matches.
- Capital propio marked [S]; captación restriction cited [R21]. Matches the decision.
- Consultorio jurídico marked [S, no verificado]. Matches.

### Scale (13b and 02)

- SMN México and INAMHI Ecuador publish hourly rain without registration from undocumented viewer endpoints [R32; R33]: matches 13b rows 29 to 32.
- Perú 35% daily payment, 85% in Iquitos, IPE 2024 p. 15 [R12, p. 15]: matches 02 line 55.
- 5,7 M street vendors in five countries, WIEGO Brief 40 table 1 (5,730,702): matches. The report does not use the forbidden "el mercado son 5,7 millones" framing and says no revenue is counted outside Colombia.
- 38% in five cities including Lima, WIEGO IEMS p. 39 [R13, p. 39]: matches 13b row 25.

### References

- 38 references, defined R1 to R38 with no gaps; first citations in the body appear in strict order 1 to 38 (script check). R31 to R38 are the new or renumbered ones; the old R31 (Reporte de Inclusión Financiera) is now R35 and old R32 (Cole et al.) is now R36, and both body citations were updated.
- URLs of new references match those recorded in 13a and 13b (Fondo Emprender convocatorias page, SMN EMAs page, inamhi.gob.ec/info, WIEGO Brief 40 PDF, fundacionwwbcolombia.org, bidlab.org financing-products).

### Compliance

- No U+2013 or U+2014 in the .md, .txt or .docx; no spaced hyphen used as a dash.
- No markdown links, no HTML. URLs appear only as plain text in Anexo A and the repo line in Anexo C.
- Repo line present in Anexo C with https://github.com/espinosacodes/makers-builder-case and the stats (see must-fix 1).
- No personal names beyond the author byline and bibliographic authors; no age; informant and collaborator stay anonymous.
- No high school students or minors mentioned; interns not added.
- Own calculations and assumptions labeled ([S], "cálculo propio").

### Fit and derived files

- `fit.py --strict`: PASS, body ends on page 5 at 95%.
- `fit.py`: PASS, body ends on page 4 at 98%.
- `build_docx.py` rerun: `informe-docs.txt` byte-identical to the previous build; `Builder_Case_Docs.docx` paragraphs (101) and table cells identical; both contain the new Tabla 3, R38, Anexo D and repo line. Derived files are in sync with the .md. After applying must-fix 1, rerun `build_docx.py` and both fit tests.
