# Review log

## Round 1 (27 sep 2026, about 03:00 to 04:00)

Inputs: `review-rubric-r1.md`, `review-facts-r1.md`, `review-compliance-r1.md`. Output: `informe.html` re-rendered to `MAKERS_SANTIAGO_ESPINOSA_CALI.pdf` (15 pages, body 5, ANEXOS at the top of page 6). `check.py`: ALL PASS. Backups of the round 0 files are in the session scratchpad (`r1/`).

### Changed: must-fix list

1. DANE 1.8% supplier credit (rubric 1). The body now states the literal reading (about 50 street vendors in Cali, 17.745 x 15,4% x 1,8%, own calculation, against 904 at break-even), the other reading (the survey does not count the daily fiado as credit; WIEGO [R23]) and the kill threshold: fewer than 40 vendors with daily fiado across the first 5 retailers means the model does not close. The threshold is repeated in "Cómo sé si me equivoqué".
2. Household floor on a rain day (rubric 2). Rule changed in the body, Table 2 and points 1 and 2: the vendor keeps up to $15.000 [S] for the household, the rest pays the fiado, the gap goes in thirds. `models/build_prototype.py` now has a household-floor input (B8) applied on both paths; the workbook and snapshot were rebuilt (14 of 14 checks OK). New example results: $46.820 deferred per rain day, thirds of about $15.600 (40% of a day's income), gota a gota interest $29.231 (76%), $63.043 owed at day 30, max balance carried by the retailer $93.640. E.3 is now labelled as an upper bound.
3. Third risk layer (rubric 3): the rule can be copied; what I charge for is the rule fixed in advance, the ledger of open bridges and eligibility, and the wholesaler deal. Month-3 signal added to "Cómo sé si me equivoqué". Point 3 now says "sin tener que decidir caso por caso si le creen al vendedor" (plural, to agree with "les").
4. Thesis scoped to the vendor who lives on daily fiado, with need and family shocks named as other ways in, and "Le gana en la tarde" (compliance 3).
5. New "Por qué la lluvia" paragraph before "Lo que no cubre": vacations and strikes are predictable, rain arrives after the fiado is taken, illness has no public datum, and R27 (44% of passes used for personal or family calamity; the debtor-requested pass raised default).
6. Table 2: new row "Esa tarde, al pagar" (retailer notes the balance, nobody decides until the notice). Rules: at most 2 deferred days open at once, a third consecutive rain day is handled as today. 5-day close window tied to the thirds (3 of thirds plus 2 of margin).
7. Table 2 week 1: I reach the retailer through the vendors the collaborator spoke with, go with one of them, bring the Annex F rain table and the free month. Point 3: "No llego en frío".
8. AI self-scores removed: Descarte 1 now gives the substantive reasons; Annex C keeps the adversarial review as method ("la usé para encontrar huecos, no como nota"); Annex H lost the score column and its caption, rows now in letter order.
9. Casaburi and Willis rewritten as the fact checker worded it (same insurance, 72% charged at harvest, 5% upfront), in point 4 and Annex J. AB InBev 93,6% removed from the body; kept only in Annex E.1 as a qualified reference ("cobra a distribuidores y bares"); the Annex J row is now "Impago bajo de lo aplazado: supuesto que mide el piloto [S]".
10. Closest precedent named in "A qué se parece": sovereign hurricane clauses, no figures. Novelty claim softened to "No encontré esa lógica en el crédito de mercancía ni en el de consumo (búsqueda limitada)".

Fact and compliance items, all applied: $1.117.131 reworded as originating, administering and collecting, with 100,3% as a separate result [R18, pp. 6 y 7]; verbatim informant quote; collaborator quote shown as said, with "la mercancía del día" marked as my reading to confirm; Descarte 1 inference now "de dos casos distintos de la informante saco una hipótesis"; Table 1 foreign evidence labelled (UNODC Costa Rica, Perú); R38 (Agencia PI, SIC order) added and cited in Annex D and Annex H; Annex J phone row corrected to 51,6% without a phone; "captación" wording fixed in point 1 and Annex J; terms defined ("un día de lluvia", "puente", "Cali A.M." expanded, CV removed from the body, option letters replaced by names or a pointer to Annex H); impact sentence (468 vendors in month 12, ceiling 17.745); `.bib a` hyphenation fix (printed URLs no longer carry fake hyphens).

Should-fix items applied: 14,2% base (4,9 million that operated in 2023); 15,4% base (those that operated in 2024) with tables; "que encontré"; "choque económico y familiar"; "vendedora de comida" everywhere; "en los días con dato"; R27 wording in point 4; [R20] in point 2; Kenya quote translated; "ticket", "link", "script" replaced; CREO with 15.779 beneficiaries [R31] (the one-million goal was not added because its source is not in Annex B); prototype sentence marked as an invented example month; byline matches the running header; money arrows dashed in Figure 1; "Queda para la casa" row says it does not subtract what is still owed; `models/rain_cali.py` written from the scratchpad script, extended to print the Annex F monthly table and runs, verified against the cached CSV (26 of 294, 27 of 340, runs 21 and 3, 2025: 23 of 307 with 18, 1 and 1) and referenced in Annex E and F.

### Changed to make room (body had to stay at 5 pages)

- Body type 9,8 pt to 9,5 pt, line height 1,36 to 1,32, tables 8,5 pt to 8,3 pt (overrides in the `informe.html` style block). This goes against compliance should-fix 14 (density) but was needed to fit about 650 words of required additions.
- Cut: the paragraph tracing the clause to option C (its point now lives in the Annex H row); the SFC 52,89% sentence (moved to the E.5 note, so R11 stays cited); the duplicated microcredit amount in point 4; the Table 1 row on collection days (still in point 2 and Annex J); the 36% repetition in Table 1; the list of other discarded options (pointer to Annex H); part of "A qué se parece" (digital ledger, two of the five differences); two sentences in "¿Cierra?" and Descarte 2.
- Table 2 labels shortened and one column rebalanced; Table 3 column widths set.

### New finding disclosed

With the household floor, a two-day rain streak stacks the thirds: on days 15 and 16 of the example the vendor pays $36.416 of deferred debt and keeps $2.184. Annex A now says so and proposes testing with the first retailer that the second day's thirds start after the first day's end. The rule in the body was not changed.

### Deliberately not changed

- Funding source for the $8,5 million (compliance 4): not confirmed by Santiago. I used the fallback wording pre-approved in `numbers.md` ("los pondría como capital de la SAS, nunca como préstamos del público [R15]"). Santiago must confirm the real source (own savings, family as shareholders, other) and then add one clause; `business_model.py` still prints "PENDING founder confirmation".
- Minimum wage source (compliance 8): cited as R39, Holland & Knight (Feb 2026), which I re-read today: $1.750.905, decree suspended on 12 Feb 2026 with effect only once a transitional decree is published. It is a law-firm note, not the official text; I could not reach an official page (web search budget exhausted; the MinTrabajo page showed no body text). Decreto 1469 is not cited as in force. Replace R39 with the official decree if Santiago has it.
- "algunos créditos agrícolas" as a precedent (rubric 10): not added, because no verified source; only the sovereign hurricane clauses are named, without figures.
- Three-model AI test (rubric 10): not run in this round, so it is not mentioned anywhere.
- BEES (fact 14, compliance 5): dropped instead of citing R35, because a text search of the saved 20-F found no BEES credit terms.
- Break-even rounding (fact 18, compliance 11) and the numbered list next to "3. Los números del negocio" (compliance 7): cosmetic, left as is to protect the page budget.
- "No es X, es Y" antitheses (compliance 15): only one rewritten ("corre la deuda sin achicarla"); the rest are load-bearing sentences.
- Annex A snapshot font (7,4 pt): unchanged.

## Round 3 (27 sep 2026, about 03:30): ENTREGA.md section 6, items 1 to 6

Inputs: `ENTREGA.md` section 6, `review-rubric-r2.md`, `numbers.md`, `models/business_model.py`, `models/build_prototype.py`, `docs/research/09-voz-del-usuario.md`. Output: `informe.html` re-rendered (15 pages, body 5, ANEXOS at the top of page 6, body 5.137 words). `check.py`: ALL PASS. Pre-round copy of `informe.html` in the session scratchpad (`informe_pre_r3.html`). No font size changed.

### Added (in priority order)

1. "Para quien paga": the retailer's cash on a rain day. 12 vendors x $46.820 deferred = about $562.000; a two-day run, 12 x $93.640 = $1,12 million (own calculation from Annex A). If he lacks it, the clause moves up to the wholesaler. Risk layer 2 now reads "si el minorista no tiene esos $562.000 de caja".
2. "Lo que no cubre": two-day runs leave $2.184 for the household (Annex A); the first thing I test is paying in sixths, about $7.800 a day per rain day (46.820 / 6; 20% of $38.600). Annex A now proposes the same test (sixths; 294 / 26 = about 11 selling days between rain days) instead of the sequential start, so body and annex agree.
3. Table 2, "Días de venta 1 a 3": each night the program asks the retailer "¿vendedor 3 pagó su tercio?"; the third yes closes the bridge. That is how the ledger is fed.
4. "Usuario, cliente y alcance": the real ceiling is vendors near one of the 3 IDEAM stations with current data (Univalle plus the two backups in Annex F), not all 17.745, and the distance at which station rain stops being cart rain is unmeasured. The minor-risk line now says this risk is small in the pilot and grows with scale.
5. Table 3, row 3: $4.000 is 2,5% of the $161.200 a month a vendor leaves the retailer (62.000 x 26 x 10% [S]; traced to `business_model.py` `payer_view` and prototype sheet 2, $1.934.400 a year / 12); with $30.000 of fiado it is 5,1%. Labelled own calculation.
6. Risk layer 1: full Cuadro 21.1 split (50,7% business, 28,9% personal, 20,5% both), confirmed in `docs/research/09-voz-del-usuario.md` (verification table: "confirmado") and `08-confianza-canales-fiado.md`; plus "el cuadro no separa pagarle al que fía de comprar mercancía".

### Cut to make room (tired-evaluator pass)

- Rubric r2 cuts: 35,6% in 24 cities (still in Annex G); Peru 36% (R21 still cited); the 96,5% deposit / 8,0% bank sentence (R7 and R9 still cited); CREO beneficiary count (R31 kept).
- Redundancy: the $15.000 floor repeated in point 2 and in "Lo que no cubre"; "no hubo rachas de tres" in "Reglas" (already in section 1); the insurance aside in point 1 (already in "Reglas"); the last list in "A qué se parece" folded into one sentence; Descarte 1's third reason shortened (it repeated the callout); the Annex H pointer merged into Descarte 2.

### Not changed

- Funding source for the $8,5 million: still the neutral fallback wording; Santiago must confirm.
- The sixths rule itself is not adopted in Table 2, Figure 1 or the prototype; it is stated as the first thing to test.
