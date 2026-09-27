# B1. Tamaño del problema y datos oficiales (Colombia)

Estado: completo

Notas de método:
- Los cuadros de DANE se leyeron directamente de los anexos Excel oficiales, no de notas de prensa. Cuando el boletín PDF y el anexo no coinciden, se usa el anexo y se reporta la discrepancia.
- Los cálculos propios (porcentajes por ciudad, conversiones de tasas, cruces con microdatos) se marcan como "cálculo propio" y dicen de qué cuadro o archivo salen.
- Confianza: alta (fuente primaria abierta y leída), media (fuente secundaria seria, o cálculo propio con muestra pequeña), baja (sin fuente original).
- EMICRON pregunta por el crédito del "año anterior": la edición 2024 describe solicitudes hechas en 2023; la edición 24 ciudades 2025 describe solicitudes hechas en 2024.
- La WebSearch de esta sesión estaba agotada. La ronda nueva se hizo con descargas directas (curl), WebFetch y cálculos sobre microdatos oficiales ya descargados.

## 1. Resumen ejecutivo

1. Colombia tiene 5,3 millones de micronegocios (2024) que ocupan 6,9 millones de personas; en la GEIH, 14,96 millones de los 24,53 millones de ocupados trabajan en microempresas y el 84,7% de ellos es informal (may a jul 2026). El dueño típico se lleva alrededor de $1,1 millones al mes; un vendedor ambulante, unos $33.000 al día.
2. Solo 14,2% de los micronegocios pidió crédito en 2023 (17,8% en 2022). De los que pidieron, 60,0% fue a una entidad regulada y 22,9% a un gota a gota (160.724 micronegocios, cerca de 3% del total). La demanda de crédito cae; la parte que se lleva el gota a gota se mantiene alrededor de 23%.
3. Lo sorprendente es dónde se concentra: en las 24 ciudades, siete ciudades del Caribe reúnen el 80,1% de los micronegocios que acudieron al gota a gota en 2024. En ellas, 16,0% de TODOS los micronegocios pidió a un gota a gota; en las otras 17 ciudades, 1,3%. Barranquilla A.M.: 20,2%. Bogotá: 0,4%. La concentración subió de 64% (2022) a 80% (2024).
4. Y en quién: entre vendedores ambulantes que piden crédito, 61,8% va al gota a gota (46,4% en 2019). Entre tiendas de barrio, solo 11,3%. El tendero con local está bastante bancarizado; el ambulante no.
5. El banco no pierde por rechazar sino porque no le piden: 92,9% de las solicitudes se aprueban y solo 14,6% de los que no piden dice no cumplir requisitos. La razón número uno es "miedo a las deudas, no le gusta endeudarse" (42,5%; en Atlántico 77,5%).
6. El crédito del micronegocio sostiene el hogar: en ciudades 28,7% del crédito obtenido fue a gastos personales y 16,4% a ambos. El competidor del gota a gota es la liquidez del hogar, no solo el capital de trabajo.
7. Colombia tiene cuentas pero no crédito: 96,5% de los adultos tiene un depósito según registros (RIF 2025), pero solo 57,1% dice tener cuenta y apenas 8,0% pidió prestado a un banco en el último año (Findex 2024, menos que 12,9% en 2021). Casi la mitad (49,9%) no podría reunir fondos de emergencia en 30 días o le sería muy difícil.
8. El tamaño del gota a gota en adultos es incierto y las cifras chocan en un orden de magnitud: 0,9% de los adultos pidió a un gota a gota (Encuesta de Demanda 2022, la más reciente), frente a "37,3% de hogares" con crédito informal (ANIF y Colombia Fintech) o "uno de cada cuatro colombianos" (DataCrédito 2020, sin método visible). La única cifra de volumen es de la Dijín en 2017: $2.500 millones al día. No existe una estimación oficial.
9. El precio: 20 a 40% mensual según UNODC (2024); ANIF estima 382% efectivo anual para hogares y 666% para mipymes (encuesta publicada en 2025). El 41% de los hogares y el 52% de las mipymes que lo usan pagan a diario.
10. Error a tener en cuenta: el boletín técnico EMICRON 2024 (p. 32) dice que en el campo "la mayor fuente de financiamiento son los prestamistas gota a gota con el 77,0%"; el anexo oficial dice lo contrario (77,0% entidad regulada, 9,8% gota a gota). Quien cite el boletín sin abrir el anexo dirá lo contrario de la realidad.

## 2. Tabla de datos clave

| Dato | Cifra | País | Año del dato | Fuente | URL | Confianza |
|---|---|---|---|---|---|---|
| Número de micronegocios (hasta 9 ocupados) | 5.297.252 | Colombia (24 departamentos) | 2024 | DANE, EMICRON 2024, anexo, Cuadro I.1 | https://www.dane.gov.co/files/operaciones/EMICRON/anex-EMICRON-2024.xlsx | alta |
| Personal ocupado en micronegocios | 6.879.489 personas | Colombia | 2024 | DANE, EMICRON 2024, Cuadro I.1 | idem | alta |
| Ventas o ingresos de los micronegocios | $191,2 billones COP nominales | Colombia | 2024 | DANE, Boletín técnico EMICRON 2024 (30 jul 2025), sección 1.1 | https://www.dane.gov.co/files/operaciones/EMICRON/bol-EMICRON-2024.pdf | alta |
| Ingreso mixto promedio por micronegocio | aprox. $1.092.855 COP al mes | Colombia | 2024 | Cálculo propio: ingreso mixto anual del Cuadro I.1 entre número de micronegocios y 12 | https://www.dane.gov.co/files/operaciones/EMICRON/anex-EMICRON-2024.xlsx | media (cálculo sobre dato alta) |
| Micronegocios creados con ahorros personales / con préstamo bancario / con prestamistas | 61,4% / 8,8% / 2,4% | Colombia | 2024 | DANE, EMICRON 2024, Cuadro C.4 y boletín p. 26 | idem | alta |
| Micronegocios que solicitaron crédito | 14,2% (702.293) en 2023; 17,8% (867.586) en 2022 | Colombia | 2023 y 2022 | DANE, EMICRON 2024 y 2023, Cuadro H.2 | https://www.dane.gov.co/files/operaciones/EMICRON/anex-EMICRON-2024.xlsx ; https://www.dane.gov.co/files/operaciones/EMICRON/anex-EMICRON-2023.xlsx | alta |
| Entre quienes pidieron crédito: a prestamista gota a gota | 22,9% (160.724) en 2023; 23,3% (201.965) en 2022 | Colombia | 2023 y 2022 | DANE, EMICRON 2024 y 2023, Cuadro H.4 | idem | alta |
| Entre quienes pidieron: entidad regulada / familia o amigos / proveedores / microcrediticias | 60,0% / 12,9% / 2,7% / 1,1% | Colombia | 2023 | DANE, EMICRON 2024, Cuadro H.4 | idem | alta |
| Gota a gota entre solicitantes: cabeceras vs rural | 27,5% vs 9,8% (rural: 77,0% a entidad regulada) | Colombia | 2023 | DANE, EMICRON 2024, Cuadro H.4 | idem | alta |
| Solicitudes aprobadas (todas las fuentes) | 92,9% | Colombia | 2023 | DANE, EMICRON 2024, Cuadro H.5 | idem | alta |
| Razones para NO pedir: miedo a deudas / no lo necesita / no cumple requisitos / intereses altos / reportado | 42,5% / 31,3% / 14,6% / 6,5% / 3,1% | Colombia | 2023 | DANE, EMICRON 2024, Cuadro H.3 | idem | alta |
| No pidieron por miedo a endeudarse, en Atlántico | 77,45% de los no solicitantes | Colombia, Atlántico | 2022 (EMICRON 2023) | Banca de las Oportunidades, "Panorama de la exclusión financiera y el crédito informal en los micronegocios colombianos" (sep 2025), p. 8 | https://www.bancadelasoportunidades.gov.co/sites/default/files/2025-09/Panorama%20de%20la%20Exclusi%C3%B3n%20Financiera%20y%20el%20Cr%C3%A9dito%20Informal%20en%20los%20Micronegocios%20Colombianos.pdf | alta |
| Uso del crédito obtenido: negocio / gastos personales / ambos | 60,8% / 20,5% / 18,7% | Colombia | 2022 | DANE, EMICRON 2023, Cuadro H.6 | https://www.dane.gov.co/files/operaciones/EMICRON/anex-EMICRON-2023.xlsx | alta |
| 24 ciudades: pidieron crédito | 14,2% (320.854 de 2.263.322) | Colombia, 24 ciudades y A.M. | 2024 | DANE, EMICRON 24 ciudades 2025, Cuadro H.2_24C | https://www.dane.gov.co/files/operaciones/EMICRON/anex-EMICRON-24Ciudades-2025.xlsx | alta |
| 24 ciudades: entre solicitantes, a gota a gota / regulada / familia | 35,6% (114.337) / 41,6% / 17,6% | Colombia, 24 ciudades | 2024 | DANE, boletín EMICRON 24 ciudades 2025 (30 jul 2026), p. 40, y Cuadro H.4_24C | https://www.dane.gov.co/files/operaciones/EMICRON/bol-EMICRON-24Ciudades-2025.pdf | alta |
| 24 ciudades: uso del crédito (negocio / personal / ambos) | 54,9% / 28,7% / 16,4% | Colombia, 24 ciudades | 2024 | DANE, EMICRON 24 ciudades 2025, Cuadro H.6_24C | https://www.dane.gov.co/files/operaciones/EMICRON/anex-EMICRON-24Ciudades-2025.xlsx | alta |
| 24 ciudades: micronegocios que no ahorraron | 79,1% | Colombia, 24 ciudades | 2024 | Cálculo propio sobre DANE, EMICRON 24 ciudades 2025: el Cuadro H.8_24C cuenta 473.273 micronegocios que ahorraron, de 2.263.322 (Cuadro H.2_24C) | idem | media (cálculo propio sobre dato alta) |
| Siete ciudades del Caribe concentran a los micronegocios que acuden al gota a gota | 80,1% (91.605 de 114.337); era 64,4% en 2022 y 70,5% en 2023 | Colombia, 24 ciudades | 2024 | Cálculo propio sobre Cuadros H.4_24C de 2023, 2024 y 2025 | idem | media (cálculo propio sobre dato alta) |
| Porcentaje del total de micronegocios que pidió a gota a gota | Barranquilla A.M. 20,2%; Cartagena 17,0%; Caribe (7 ciudades) 16,0%; resto 1,3%; Bogotá 0,4%; Medellín A.M. 0,2% | Colombia | 2024 | Cálculo propio sobre Cuadros H.2_24C y H.4_24C | idem | media (Bogotá y Medellín con CV mayor a 15%) |
| Vendedores ambulantes: entre solicitantes, a gota a gota | 61,8% (25.744 de 41.672); 46,4% en 2019 | Colombia, 24 ciudades | 2024 | DANE, EMICRON Vendedores ambulantes 2025, Cuadros 18 y 18.1 | https://www.dane.gov.co/files/operaciones/EMICRON/anex-EMICRONVendedoresAmbulantes-2025.xlsx | alta |
| Vendedores ambulantes: ingreso mixto promedio | aprox. $1.003.293 al mes (unos $33.000 al día) | Colombia, 24 ciudades | 2025 | Cálculo propio sobre Cuadro 24 | idem | media |
| Panaderías y tiendas de barrio: pidieron crédito / a gota a gota entre solicitantes | 19,0% (27,0% en 2019) / 11,3% (69,9% a regulada) | Colombia | 2024 | DANE, EMICRON Panaderías y tiendas de barrio 2024, Cuadros H.2 y H.4; boletín p. 25 | https://www.dane.gov.co/files/operaciones/EMICRON/bol-EMICRON-PanaderiasTiendasBarrio-2024.pdf | alta |
| Informalidad laboral | 54,6% nacional; 40,6% 13 ciudades; 83,2% centros poblados y rural [NO VERIFICADO] | Colombia | may a jul 2026 | DANE, GEIH, boletín Ocupación informal (11 sep 2026), p. 1 | https://www.dane.gov.co/files/operaciones/GEIH/bol-GEIHEISS-may-jul2026.pdf | alta |
| Informalidad en microempresas (hasta 10 trabajadores) | 84,7% | Colombia | may a jul 2026 | DANE, GEIH, boletín, Tabla 1, p. 8 | idem | alta |
| Ocupados en microempresas / informales en microempresas | 14,96 de 24,53 millones (61%) / 12,66 de 13,40 millones informales (94,5%) | Colombia | may a jul 2026 | DANE, GEIH, anexo, hoja "Tamaño de empresa" (proporciones: cálculo propio) | https://www.dane.gov.co/files/operaciones/GEIH/anex-GEIHEISS-may-jul2026.xlsx | alta |
| Trabajadores por cuenta propia | 10,13 millones (41,3% de los ocupados), 83,3% informales | Colombia | may a jul 2026 | DANE, GEIH, anexo, hoja "Posición ocupacional" | idem | alta |
| Adultos con al menos un crédito formal (incluye comercio y telcos) | 20,3 millones (51,6%) | Colombia | 2025 | Banca de las Oportunidades y SFC, Reporte de Inclusión Financiera 2025 (ago 2026), Gráfica 1, p. 43 | https://www.superfinanciera.gov.co/loader.php?lServicio=Tools2&lTipo=descargas&lFuncion=descargar&idFile=1082980 | alta |
| Adultos con crédito en entidades vigiladas SFC / con crédito de comercio | 35,6% / 20,9% | Colombia | 2025 | RIF 2025, Gráfica 1, p. 43 | idem | alta |
| Adultos con microcrédito formal (Grupo ABC) | 5,8% (5,6% en 2024; 18 a 25 años: 2,7%; Atlántico: 3,0%, el tercero más bajo) | Colombia | 2025 | RIF 2025, Gráfica 2, p. 44 (nacional) y pp. 54 a 55 (departamentos y edad) | idem | alta |
| Adultos con al menos un producto de depósito | 96,5% (37,9 millones); 85,5% activo | Colombia | 2025 | RIF 2025, nota de la SFC | https://www.superfinanciera.gov.co/publicaciones/10116222/reporte-de-inclusion-financiera-2025-avances-en-depositos-credito-cobertura-y-transacciones/ | alta |
| Adultos con cuenta (encuesta) | 57,1% (entidad financiera 43,4%; dinero móvil 39,1%) | Colombia | 2024 | Banco Mundial, Global Findex Database 2025 (archivo CSV oficial) | https://thedocs.worldbank.org/en/doc/be6615202d1f08a25855c8ac2d615122-0050012025/related/GlobalFindexDatabase2025.csv | alta |
| Pidió prestado: cualquier fuente / formal / banco / familia o amigos | 46,3% / 13,5% / 8,0% / 19,4% | Colombia | 2024 | Global Findex 2025 (borrow_any_t_d, fin22a_22a1_22g_d, fin22a, fin22b) | idem | alta |
| Compró comida fiada / pidió prestado para negocio | 21,3% / 7,6% | Colombia | 2024 | Global Findex 2025 (fin22f, fin22e) | idem | alta |
| Fondos de emergencia en 30 días: no posible / posible pero muy difícil | 12,8% / 37,1% | Colombia | 2024 | Global Findex 2025 (fin24aN, fin24aVD) | idem | alta |
| Fuente principal de emergencia: familia o amigos / préstamo de banco, empleador o prestamista / ahorro | 45,1% / 9,1% / 11,7% | Colombia | 2024 | Global Findex 2025 (fin24fam, fin24bor, fin24sav) | idem | alta |
| Adultos que solicitaron crédito a "prestamista (ej. gota a gota)" | 0,88% de adultos; 5,1% de quienes pidieron crédito (Caribe: 10,3%) | Colombia | abr a may 2022 | Cálculo propio ponderado sobre microdatos de la Encuesta de Demanda de Inclusión Financiera 2022 (n = 5.610; 59 casos) | https://www.bancadelasoportunidades.gov.co/sites/default/files/2022-10/Encuesta_demanda_2022_microdatos.xlsx | media (pocos casos) |
| Solicitantes de crédito que acudieron a fuentes informales (familia, gota a gota, fiado, cadenas, empeño) | 29% | Colombia | 2022 | Encuesta de Demanda de Inclusión Financiera 2022 (Banca de las Oportunidades, SFC, BanRep), p. 10 | https://www.bancadelasoportunidades.gov.co/sites/default/files/2022-12/Encuesta%20de%20demanda%202022%20VF.pdf | alta |
| Adultos que obtuvieron préstamo de "prestamista, gota a gota o paga diario" (12 meses) | 4,4% (independientes 8,1%; asalariados 2,7%) | Colombia | dic 2014 a feb 2015 | Cálculo propio ponderado sobre microdatos de la PRIMERA Encuesta de Demanda (n = 1.417; re publicados en jul 2025) | https://www.bancadelasoportunidades.gov.co/sites/default/files/2025-07/SP-14-038794-01-02-microdatos%20InclusionFinancieraPersonas-V1.xlsx | media (dato viejo, 75 casos) |
| Microempresarios que usaron prestamista o gota a gota (12 meses) | 9% (estrato 1: 16%) | Colombia | dic 2014 a feb 2015 | Banca de las Oportunidades, Estudio de Demanda para Analizar la Inclusión Financiera en Colombia (primera toma) | https://www.bancadelasoportunidades.gov.co/sites/default/files/2018-02/Informe%20Estudio_demanda.pdf | alta (dato viejo) |
| Hogares y empresas que recurren a crédito informal "como el gota a gota" | 37,3% de hogares; 55% de empresas (91% en micro y de subsistencia [NO VERIFICADO]) | Colombia | encuesta publicada ene y jun 2025 | ANIF y Colombia Fintech, Encuesta de endeudamiento (1.221 personas y 1.009 mipymes) | https://anif.com.co/informe-semanal/encuesta-de-endeudamiento-una-nueva-perspectiva-de-la-exclusion-financiera-liderada-por-anif-y-colombia-fintech/ | media (definición amplia de "informal") |
| Participación del gota a gota en la deuda de los hogares | 12,1% del stock promedio ($10,3 millones por hogar); 17,7% en hogares con ingreso de hasta 1 SMMLV | Colombia | 2025 | ANIF y Colombia Fintech, "Análisis de cambios metodológicos de la tasa de usura y su impacto en la inclusión financiera", p. 4 | https://anif.com.co/wp-content/uploads/anif-colombia-fintech-analisis-de-cambios-metodologicos-de-la-tasa-de-usura-y-su-impacto-en-la-inclusion-financiera-un-enfoque-para-el-desarrollo-economico-sostenible-en-colombia-1.pdf | alta sobre lo publicado; media sobre el método |
| Tasa efectiva anual del gota a gota estimada por encuesta | 382,2% hogares; 666,5% mipymes (bancos: 17,9% y 12,7%) | Colombia | 2025 | ANIF y Colombia Fintech, mismo documento, pp. 7 y 8 (Gráficos 5 y 6) | idem | media |
| Frecuencia de pago del gota a gota | 41% de hogares paga a diario, 29,5% mensual; 52,2% de mipymes a diario, 35,9% semanal | Colombia | 2025 | ANIF y Colombia Fintech, mismo documento, p. 11 | idem | media |
| Tasa del gota a gota según UNODC | 20 a 40% (usualmente mensual), sin cambios sustanciales desde 2013 | Colombia | 2024 | UNODC ROCOL, S.A.G.A., "Gota a gota: se lavan activos, el préstamo fácil" | https://saga.unodc.org.co/es/gota-a-gota-se-lavan-activos-el-prestamo-facil | media |
| Dinero que "mueve" el gota a gota según la Dijín | $2.500 millones COP al día nacional; $1.000 millones al día en Bogotá; 137 municipios afectados | Colombia | 2017 | Portafolio (22 oct 2017), citando a la Dijín de la Policía; sin método | https://www.portafolio.co/tendencias/el-gota-a-gota-el-prestamo-que-se-convierte-en-un-infierno-510881 | baja (cifra policial vía prensa, vieja, sin método) |
| Monto y plazo típicos | menos de $1 millón; pagos diarios, semanales o quincenales; 1 a 5 meses; "uno de cada cuatro ciudadanos" lo usaría | Colombia | 2020 | DataCrédito Empresas (2020), citado por López, Manrique y Kalmanovitz (2026), p. 45; original devolvió HTTP 403 | https://www.datacreditoempresas.com.co/blog-datacredito-empresas/indicadores-de-credito-en-colombia/ | baja |
| Comerciantes de plazas de mercado de Bogotá que han usado gota a gota | 92% (muestra aleatoria de 100, oct 2023) | Colombia, Bogotá | 2023 | López, Manrique y Kalmanovitz, Apuntes 53(101), 2026, sección 3 | https://doi.org/10.21678/apuntes.101.2604 | media (muestra pequeña) |

## 3. Hallazgos por tema

### 3.1 Cuántos micronegocios hay y cuánto pesan

- 5.297.252 micronegocios en 2024 (24 departamentos; excluye Amazonas, Arauca, Casanare, Guainía, Guaviare, Putumayo, Vaupés y Vichada), 6.879.489 ocupados y $191,2 billones de ventas. Fuente: DANE, EMICRON 2024, Cuadro I.1 y boletín técnico (30 jul 2025). (alta)
- Cómo se crearon: 61,4% con ahorros personales, 15,5% no requirió financiación, 10,6% préstamos familiares, 8,8% préstamos bancarios, 2,4% prestamistas (Cuadro C.4). Entre vendedores ambulantes, los prestamistas financian la creación del 6,1% (EMICRON Vendedores ambulantes 2025, Cuadro 7). (alta)
- Dónde operan (2024): 30,6% en la vivienda, 17,4% puerta a puerta, 13,5% finca, 12,5% local, 11,3% vehículo, 9,6% ambulante (Cuadro D.1). La mayoría no tiene un local fijo. (alta)
- Medios de pago: 97,5% acepta efectivo y 38,9% transferencia (nacional 2024, cálculo sobre Cuadro H.1); en las 24 ciudades en 2025 la transferencia ya llega a 71,8% (Cuadro H.1_24C). Tarjetas: menos de 3%. (alta)
- Ingreso: el ingreso mixto promedio fue de aprox. $1,09 millones al mes por micronegocio en 2024; vendedores ambulantes 2025: aprox. $1,0 millón al mes (unos $33.000 diarios); tiendas de barrio 2024: ventas de aprox. $5,37 millones al mes e ingreso mixto de $1,19 millones (cálculos propios sobre Cuadros I.1, 24 y J.1). (media)
- Formalidad del negocio (EMICRON 2023, vía Banca de las Oportunidades): 10,49% registrado en cámara de comercio (7,78% activo); 65,55% no lleva registros contables y 29,46% lleva cuentas en cuadernos u hojas. "Panorama de la exclusión financiera y el crédito informal en los micronegocios colombianos" (sep 2025), p. 2. (alta)
- Mercado laboral (GEIH may a jul 2026): informalidad 54,6% (55,0% un año antes); microempresas 84,7%; 94,5% de los informales trabaja en microempresas; 10,13 millones de cuenta propia, 83,3% informales. Ciudades más informales: Sincelejo 65,2%, Riohacha 61,9%, Cúcuta 61,9%; menos: Bogotá 32,6%. Boletín pp. 1, 7, 8 y anexo. (alta)
- Prensa sobre BanRep (La República, 18 feb 2025): estudio de Ruiz Martínez y Tobar Cruz con EMICRON 2019 a 2022 estima que 77% de los micronegocios opera en la informalidad y que tener crédito formal sube 10,5 p.p. la probabilidad de formalizarse. https://www.larepublica.co/economia/banco-de-la-republica-estima-que-77-de-los-micronegocios-opera-en-la-informalidad-4065067 (media: no se abrió el documento de BanRep).

### 3.2 Cuántos piden crédito, a quién, con qué resultado y para qué (EMICRON)

| Indicador (nacional) | Solicitudes de 2022 (EMICRON 2023) | Solicitudes de 2023 (EMICRON 2024) |
|---|---|---|
| Pidieron crédito | 17,8% (867.586) | 14,2% (702.293) |
| A institución regulada | 56,7% | 60,0% |
| A gota a gota | 23,3% (201.965) | 22,9% (160.724) |
| A familiares o amigos | 15,0% | 12,9% |
| A proveedores | 3,1% | 2,7% |
| Aprobación | 94,1% | 92,9% |
| Razón principal para no pedir: miedo a deudas | 44,3% | 42,5% |

Fuente: anexos EMICRON 2023 y 2024, Cuadros H.2 a H.5. (alta)

Lectura:
- El gota a gota es la segunda fuente en todas las ediciones y pesa alrededor de 23% entre solicitantes. Lo que cae es la demanda total de crédito. Sobre el total de micronegocios, el gota a gota alcanzó a unos 160.724 en 2023, cerca de 3,0% (cálculo propio).
- La aprobación de 92,9% mezcla bancos con prestamistas y familia, que casi nunca rechazan; no prueba que el banco apruebe.
- El filtro está antes de pedir. Entre los que no pidieron: 42,5% miedo a endeudarse, 31,3% no lo necesita, 14,6% no cumple requisitos (Cuadro H.3). La autoexclusión pesa tres veces más que los requisitos.
- Uso: en 2022, 60,8% para el negocio, 20,5% gastos personales, 18,7% ambos (Cuadro H.6, EMICRON 2023).
- Error del boletín (verificado en la imagen de la página 32 del PDF): el Gráfico 25 del boletín EMICRON 2024 corre una fila las columnas de cabeceras y rural (pone 54,0 y 77,0 a los prestamistas, que son los valores de la entidad regulada) y el texto concluye que en lo rural "la mayor fuente de financiamiento son los prestamistas gota a gota con el 77,0%". El anexo (Cuadro H.4) y sus conteos (17.929 de 182.136 en rural; 142.795 de 520.157 en cabeceras) muestran 9,8% rural y 27,5% en cabeceras. Además la tabla se titula "Razones para no solicitar crédito" y el texto de la p. 31 dice que "el 85,8% realizó alguna gestión para solicitar un crédito", cuando 85,8% es la proporción que NO pidió. Citar siempre el anexo. https://www.dane.gov.co/files/operaciones/EMICRON/bol-EMICRON-2024.pdf (alta)

24 ciudades y áreas metropolitanas (solicitudes de 2024, boletín del 30 jul 2026):
- 14,2% pidió crédito; entre ellos 41,6% a regulada, 35,6% a gota a gota, 17,6% a familia, 3,0% a proveedores, 1,6% a microcrediticias, 0,1% casa de empeño. Solo 3,9% no fue aprobado. 79,1% de los micronegocios no ahorró. (alta)
- Concentración territorial (cálculo propio): siete ciudades del Caribe reúnen 91.605 de los 114.337 micronegocios que acudieron al gota a gota (80,1%): Barranquilla A.M. 47.446; Cartagena 21.229; Valledupar A.M. 7.731; Sincelejo 6.232; Santa Marta 4.050; Montería 3.063; Riohacha 1.854. Esas ciudades tienen el 25% de los micronegocios de las 24 ciudades. En ellas 16,0% de todos los micronegocios pidió a un gota a gota, frente a 1,3% en el resto. La participación del Caribe subió de 64,4% (2022) a 70,5% (2023) y 80,1% (2024). (media)
- Entre solicitantes, en Barranquilla A.M. el gota a gota supera a la banca (57,3% frente a 18,0%); en Sincelejo 75,7% frente a 10,7%. En Bogotá es al revés (74,9% banca, 5,1% gota a gota). (media, cálculo propio)
- Uso en ciudades: 54,9% negocio, 28,7% gastos personales, 16,4% ambos (Cuadro H.6_24C). (alta)
- Para cruzar con la oferta: Atlántico, el departamento de Barranquilla, tiene uno de los accesos más bajos a microcrédito formal del país (3,0% de adultos, RIF 2025, p. 54) y el porcentaje más alto de micronegocios que no piden crédito por miedo a endeudarse (77,45%, Banca de las Oportunidades, Panorama 2025, p. 8). Hipótesis (no verificada): en Atlántico el "miedo a endeudarse" puede estar alimentado por la experiencia con el cobro del gota a gota.

Segmentos:
- Vendedores ambulantes (24 ciudades, actualizado 18 sep 2026): 286.061 unidades en 2025 (Cuadro 24); 270.144 funcionaron en 2024 y son la base de la pregunta de crédito (Cuadro 16); 15,4% de ellos pidió crédito en 2024; 61,8% de ellos a gota a gota, 22,5% a regulada, 12,8% a familia. En 2019: 46,4% gota a gota y 40,8% banca. Razones para no pedir: 44,6% miedo, 29,4% no cumple requisitos (el doble del promedio). (alta)
- Panaderías y tiendas de barrio (2024; 540.233 unidades según Cuadro J.1; 488.459 funcionaron en 2023 y son la base de la pregunta de crédito, Cuadro H.2): 19,0% pidió crédito (27,0% en 2019; caída significativa en 2024); 69,9% a regulada, 11,8% familia, 11,3% gota a gota (10.453), 5,6% proveedores; 78,0% lo usó para el negocio; 20,8% tuvo capacidad de ahorro. Razones para no pedir: 45,7% miedo, 29,5% no lo necesita, 10,4% requisitos, 8,6% intereses. (alta)
- Construcción (2024): 56,3% regulada y 25,3% gota a gota entre solicitantes (resumen de búsqueda del boletín EMICRON Sector Construcción 2024, 10 jun 2026; no se abrió el anexo). (media)
- EMICRON no pregunta monto, plazo ni tasa del crédito. Esa información no existe en la estadística oficial de micronegocios.

### 3.3 Crédito informal en adultos (demanda)

Global Findex 2025 (campo 2024, adultos de 15 años o más; valores leídos de la base oficial):
- Cuenta 57,1% (59,7% en 2021); en entidad financiera 43,4% (55,9% en 2021); dinero móvil 39,1% (21,8% en 2021).
- Pidió prestado: cualquier fuente 46,3%; formal 13,5% (19,0% en 2021); banco 8,0% (12,9% en 2021); familia o amigos 19,4% (29,1% en 2021); club de ahorro 1,3%; para salud 14,7%; para negocio 7,6%; comida fiada 21,3%.
- Emergencia en 30 días: 12,8% no podría y 37,1% podría con mucha dificultad. Fuente principal: familia 45,1%, trabajo 15,2%, ahorro 11,7%, préstamo de banco, empleador o prestamista 9,1%, vender algo 5,2%.
- Comparación 2024 (formal / familia): Perú 20,8% / 20,8%; México 15,1% / 17,1%; Colombia 13,5% / 19,4%.
- Limitación: la base pública no separa al prestamista informal (queda mezclado en fin24bor). No hay cifra Findex 2025 de gota a gota para Colombia.
Fuente: https://www.worldbank.org/en/publication/globalfindex/download-data (alta).

Encuesta de Demanda de Inclusión Financiera (Banca de las Oportunidades con SFC y BanRep):
- A 26 sep 2026 la edición más reciente publicada es la tercera toma, 2022 (confirmado en la página de encuestas de demanda de Banca de las Oportunidades). https://www.bancadelasoportunidades.gov.co/es/publicaciones/encuestas-de-demanda
- 2022 (campo 5 abr a 27 may 2022; 5.610 encuestas; margen 1,8%): 71,4% de los adultos no tenía crédito ni pidió; barrera principal "no querer tener deudas" (65,4%), luego ingresos bajos (28,3%) y costo (27,8%). 29% de los solicitantes fue a fuentes informales. Informe pp. 10 y 11. (alta)
- Cálculo propio con microdatos 2022 (factor Fexp_Reg_Rur): 17,1% de los adultos pidió crédito; 0,88% pidió a un gota a gota (5,1% de los solicitantes; 59 casos). Caribe: 10,3% de los solicitantes; cuenta propia: 7,5% frente a 2,5% de empleados. Otras fuentes entre solicitantes: bancos 68,3%, almacén 13,6%, familia 7,5%, fiado o tendero 6,5%. (media)
- La encuesta 2022 incluyó un experimento de lista (pregunta 609, con la frase "Prefiero acudir a un gota a gota que a un banco") para medir la preferencia sin que la persona la declare. El resultado no aparece en el informe y la base pública no trae la variable de grupo (control o tratamiento), así que no se pudo calcular. (hallazgo alta; resultado no encontrado)
- Primera toma (campo 3 dic 2014 a 20 feb 2015; 1.417 personas y 1.213 microempresarios): cálculo propio sobre los microdatos que Banca de las Oportunidades volvió a publicar en jul 2025: 4,4% de los adultos obtuvo préstamo de "prestamista, gota a gota o paga diario" en 12 meses (independientes 8,1%, asalariados 2,7%); 13,0% de quienes obtuvieron algún préstamo lo obtuvo de un gota a gota. Entre esos usuarios, el destino declarado de sus créditos fue más a menudo gasto del hogar (38,7%), emergencias (23,2%) y pagar otras deudas (15,3%) que iniciar un negocio (8,0%); la pregunta de destino no está ligada a la fuente, así que es indicativa. El informe de esa toma reporta que 9% de los microempresarios usó prestamista o gota a gota (estrato 1: 16%) y que "por cada dos personas que acuden a familiares o amigos, una acude al prestamista", opción que se toma "cuando la necesidad es muy apremiante". Atención: estos microdatos NO son de 2025; la fecha de publicación del archivo (2025-07) confunde. (media para los cálculos; alta para el informe)

Otras encuestas:
- ANIF y Colombia Fintech (1.221 personas y 1.009 mipymes, publicado ene y jun 2025): 37,3% de los hogares y 55% de las empresas recurren a crédito informal "como el gota a gota"; en micro y de subsistencia, 91% [NO VERIFICADO]. El gota a gota es 12,1% del stock de deuda promedio de los hogares ($10,3 millones) y 17,7% en hogares que ganan hasta 1 SMMLV; en mipymes es 8,8% del stock (deuda promedio $28 millones). Fuente: PDF citado en la tabla, pp. 3 a 5, y Informe semanal del 27 ene 2025. (media: "informal" incluye familia, cadenas y empeño; el año de campo no se indica en el resumen.)
- López, Manrique y Kalmanovitz (2026), encuesta aleatoria a 100 comerciantes de plazas de mercado de 8 localidades de Bogotá (2 a 9 oct 2023): 92% ha usado gota a gota; entre quienes no, 82% prefiere a la familia; 86% usa Nequi o Daviplata; 51% no usa productos de crédito o ahorro tradicionales; 56% desconoce el microcrédito formal; 72% cambiaría el gota a gota por un producto formal. https://revistas.up.edu.pe/apuntes/es/article/download/2604/1974/8560 (media)

### 3.4 Oferta formal (Reporte de Inclusión Financiera 2025)

- 20,3 millones de adultos (51,6%) con al menos un crédito formal en 2025: 15,3 millones (38,9%) con el sector financiero y 10,98 millones (28,0%) con el no financiero (comercio 20,9%, telcos 7,8%). Microfinancieras no vigiladas 2,3%; fintech no vigiladas 0,4%. Datos de TransUnion. RIF 2025, Gráfica 1, p. 43. (alta)
- Microcrédito formal: 5,8% de adultos en 2025 (5,6% en 2024; RIF 2025, Gráfica 2, p. 44); alto en Putumayo 13,2%, Huila 12,9%, Nariño 12,3%; bajo en Vichada 2,3%, La Guajira 2,9%, Atlántico 3,0%. Por región: Centro Sur 11,7%; Caribe 4,5%. Por edad: 18 a 25 años 2,7%; 41 a 65 años 8,0%. RIF 2025, pp. 54 a 56. (alta)
- Depósitos: 96,5% de los adultos (37,9 millones); 85,5% activo. (alta)
- Desembolsos 2025: en consumo distinto de tarjeta y rotativo el monto promedio pasó de $8,1 a $11,3 millones; en tarjeta y rotativo bajó a $217.702 por operación. RIF 2025, p. 65. El crédito de consumo formal se mueve hacia tickets grandes. (alta)
- Asobancaria (28 ago 2026) propone un programa público privado de rebancarización para llevar el crédito formal de 51,6% a 75% de los adultos (de 20 a 30 millones), con 5 millones como meta rápida, para combatir el gota a gota; no cuantifica el gota a gota. (alta)
- ANIF (22 sep 2026) sostiene que un techo de usura que no refleje el riesgo empuja a los perfiles riesgosos al gota a gota y que flexibilizarlo podría sumar $11,8 billones a la cartera de consumo y $13,0 billones a la comercial. https://anif.com.co/comentario-economico/proteger-sin-excluir-el-reto-de-la-tasa-de-usura/ (media: es la posición del gremio).

### 3.5 Tamaño del mercado del gota a gota (quién lo estimó y cómo)

No existe una estimación oficial (DANE, SFC, BanRep, Fiscalía) del valor de la cartera gota a gota en Colombia. Lo que hay:

| Quién | Cifra | Año | Método | Confianza |
|---|---|---|---|---|
| Dijín, Policía Nacional (vía Portafolio) | "mueve cada día hasta $2.500 millones" nacional y $1.000 millones en Bogotá; 137 municipios con el problema, 17 bajo control directo del crimen organizado; unos 400 procesos penales en un año | 2017 | No declarado (investigación de 8 meses de la Dijín) | baja |
| Conversión propia de la cifra Dijín | Si los $2.500 millones son flujo diario, equivalen a unos $0,9 billones al año (no se sabe si son desembolsos o cobros) | 2017 | $2.500 millones por 365 días | baja |
| DataCrédito Empresas (vía López et al. 2026) | "uno de cada cuatro ciudadanos" | 2020 | No visible (la página devuelve 403) | baja |
| ANIF y Colombia Fintech | 37,3% de hogares y 55% de empresas con crédito informal; el gota a gota es 12,1% del stock de deuda de los hogares | 2025 | Encuestas nacionales a 1.221 personas y 1.009 mipymes | media |
| DANE, EMICRON (piso en micronegocios) | 160.724 micronegocios pidieron a un gota a gota en 2023 (201.965 en 2022); 114.337 en 24 ciudades en 2024 | 2022 a 2024 | Encuesta oficial, pregunta directa | alta |
| Encuesta de Demanda 2022 (cálculo propio) | 0,88% de unos 36,1 millones de adultos (suma de factores), es decir unas 317.000 personas | 2022 | Microdatos, pregunta directa, 59 casos | media |
| Primera Encuesta de Demanda (cálculo propio) | 4,4% de unos 31,6 millones de adultos, unas 1,4 millones de personas | 2014 a 2015 | Microdatos, 75 casos | media (viejo) |
| UNODC S.A.G.A. | No estima volumen; tasas de 20 a 40% | 2024 | Análisis institucional | media |

Lectura: las cifras de adultos van de 0,3 a 1,4 millones de personas en encuestas oficiales, frente a cifras gremiales o comerciales que implican 10 millones o más. La diferencia puede venir de (a) subregistro por vergüenza o miedo en encuestas cara a cara, (b) definiciones amplias de "informal" que incluyen familia y fiado, y (c) poblaciones distintas (hogares endeudados, pymes, plazas de mercado). Para el PDF conviene usar el piso oficial (EMICRON) y mostrar el rango, en lugar de una cifra única.

### 3.6 Montos, plazos y tasas del gota a gota según fuentes creíbles

- Tasas nominales: 20 a 40%, usualmente mensual, "desde 2013 no se aprecian cambios sustanciales" (UNODC 2024); 20 a 30% mensual (López et al. 2026, p. 46); "20 por ciento o más" por un plazo de unos 26 días (Dijín vía Portafolio 2017).
- Tasas efectivas estimadas por encuesta (ANIF y Colombia Fintech 2025): 382,2% anual para hogares y 666,5% para mipymes. Comparación de la misma encuesta: cooperativas 15,6%, bancos 17,9%, microfinancieras 26,5%, crédito digital 29,6%; cadenas y proveedores comerciales para hogares, más de 160%. Para mipymes: bancos 12,7%, cooperativas 20,3%, microfinancieras 25%, digitales 22,6%, casas de empeño 34,6%, cadenas 48,1%. (media)
- Frecuencia y plazo (ANIF 2025): 41% de los hogares paga a diario y 29,5% mensual; 52,2% de las mipymes paga a diario y 35,9% semanal; el plazo habitual para 3 de cada 4 mipymes es de hasta 2 meses. ANIF afirma además que los usuarios "terminan pagando hasta 3,2 veces el monto inicial en 2 meses" (hogares) y "más de 9 veces" (mipymes). Esas multiplicaciones son incompatibles con sus propias tasas (382% anual equivale a unos 14% mensual, es decir 1,3 veces en 2 meses), por lo que probablemente reflejan renovaciones encadenadas o un error de cálculo. Citarlas con cautela. (media a baja)
- Montos: menos de $1 millón, pagos diarios, semanales o quincenales, plazos de 1 a 5 meses (DataCrédito 2020; baja). "Préstamos rápidos de hasta $5 millones" y préstamos grandes con escritura como garantía (Portafolio 2017; baja). ANIF da el stock promedio de deuda gota a gota por hogar de forma indirecta: 12,1% de $10,3 millones, unos $1,25 millones (cálculo propio; no se sabe si el promedio incluye hogares sin deuda gota a gota). Banda histórica "R-15" en Cali (1996): $100.000 a $3 millones al 5 a 20% (López et al., p. 46).
- Conversiones propias (cálculo, no dato): un préstamo "al 20%" pagado en 24 cuotas diarias (lunes a sábado, unas 4 semanas) equivale a 1,5% por cuota, unos 47% efectivo mensual y más de 10.000% efectivo anual si se renueva de forma continua; en 30 cuotas diarias, unos 44% mensual. 382% EA equivale a 14,0% mensual; 666% EA a 18,5% mensual. La usura de consumo de feb 2024 (34,97% EA) equivale a 2,53% mensual. Implicación: las cifras "anuales" subestiman el costo cuando el cobro es diario y el capital se amortiza desde el primer día.
- Cómo lo percibe el usuario (plazas de mercado de Bogotá, 2023): 63% prefiere el precio en pesos ("recibe 100.000, paga 110.000 en un mes") y no en tasa; 57,6% prefiere $1 millón hoy a $1,5 millones en un año; 56% necesita el desembolso en máximo una semana; 66% considera aceptable pagar en tres meses y 22% entre tres y seis meses; 31% no conoce la usura. (media)

## 4. Intentos previos

| Actor | Qué hizo | Resultado medido | Por qué funcionó o falló | Fuente |
|---|---|---|---|---|
| Secretaría de Desarrollo Económico de Bogotá | "Ciérrale la llave al gota a gota" (2024 a 2025): primero créditos de $50.000 a $500.000 sin intereses; luego vitrina de aliados (AAvance, Monet, Plurall, Quipu) | No se encontraron cifras de desembolsos ni de pago | Requisitos de ingreso mínimo ($1.044.000), cuenta, antigüedad del negocio (6 meses en Quipu) e ingreso de más de $1 millón por 3 meses (Monet) dejan fuera al vendedor diario. Además, Bogotá es donde menos se usa el gota a gota entre micronegocios (0,4%) | https://desarrolloeconomico.gov.co/gota-a-gota/ ; https://desarrolloeconomico.gov.co/848-de-los-micronegocios-en-bogota-no-acude-al-sistema-financiero-observatorio-de-desarrollo-economico-de-bogota/ (media) |
| Alcaldía de Barranquilla, CrediChévere | Crédito municipal de hasta $14 millones al 2,5% mensual y hasta 24 meses | "Casi $11.000 millones" en 4.563 créditos hasta jun 2025 (promedio implícito de unos $2,4 millones, cálculo propio) | Llega a la ciudad correcta (la de mayor uso de gota a gota), pero 4.563 créditos frente a unos 47.000 micronegocios que acudieron al gota a gota en Barranquilla A.M. en 2024, y con cuota mensual. No hay datos de mora | El Heraldo, 24 ago 2025: https://www.elheraldo.co/judicial/2025/08/24/por-que-estan-matando-a-los-cobradiarios-en-barranquilla-y-su-area-metropolitana/ (media; detalle en frente B5) |
| Asobancaria | Propuesta de programa público privado de rebancarización (ago 2026) | Propuesta, sin resultados | Ataca el acceso formal; no toca el ritmo diario ni la autoexclusión por miedo a deudas | https://www.asobancaria.com/comunicados-de-prensa/asobancaria-propone-al-gobierno-trabajar-en-un-programa-publico-privado-de-rebancarizacion-para-combatir-el-gota-a-gota/ (alta) |
| Sistema de microcrédito formal | Oferta de bancos y microfinancieras | 5,8% de adultos con microcrédito (2025); solo 1,1% de los micronegocios solicitantes fue a microcrediticias (2023); en ambulantes la banca pasó de 40,8% (2019) a 22,5% (2024) de los solicitantes | Fuerte en el sur y en lo rural; débil en el Caribe urbano (Atlántico 3,0%) y entre jóvenes (2,7%) | RIF 2025; EMICRON 2024 H.4; EMICRON Vendedores ambulantes 2025 (alta) |

Los demás programas (CREO, Banco de las Oportunidades de Medellín, microfinancieras) se documentan en el frente B5.

## 5. Lo que casi nadie dice

1. El gota a gota de micronegocios urbanos es un fenómeno del Caribe y cada vez más: siete ciudades concentran 80% de los usuarios (64% en 2022). En Barranquilla uno de cada cinco micronegocios pidió a un gota a gota en 2024; en Bogotá, menos de uno de cada 200. Importa porque un piloto diseñado y probado en Bogotá puede no encontrar usuarios, y porque la ciudad a elegir para el trabajo de campo cambia la conclusión.
2. El usuario no es "el tendero" sino el ambulante: 61,8% de los ambulantes que piden crédito van al gota a gota, frente a 11,3% de las tiendas. La "persona de 15 años detrás de un mostrador" del reto está relativamente bien servida por la banca. Importa para elegir el segmento.
3. La barrera es no pedir, no ser rechazado: 92,9% de aprobación y 42,5% de "miedo a endeudarse" entre los que no piden (77,5% en Atlántico). Una solución que solo "facilite el acceso" ataca la barrera menor. Importa para el diseño: el producto tiene que sentirse distinto de "una deuda".
4. El crédito del negocio paga el hogar: 45% del crédito obtenido en ciudades va total o parcialmente a gastos personales, y en la encuesta 2014 a 2015 los usuarios de gota a gota lo usaban más para gastos del hogar, emergencias y otras deudas que para iniciar negocios. Importa porque productos atados a inventario o proveedor no cubren la necesidad principal.
5. Cuentas sí, crédito no: 96,5% de adultos con depósito en registros, pero 8,0% pidió a un banco en 2024 (12,9% en 2021) y 86% de los comerciantes de plaza encuestados en Bogotá usa Nequi o Daviplata mientras 92% usa gota a gota. El canal digital ya está; lo que falta no es la cuenta.
6. La brecha entre fuentes es de un orden de magnitud (0,9% de adultos en la encuesta oficial frente a 37,3% de hogares en la encuesta gremial). Nadie tiene una cifra seria del tamaño en pesos; la única cifra de volumen es policial y de 2017. Importa para el juicio cuantitativo del PDF: mejor mostrar un rango con supuestos que repetir "uno de cada cuatro".
7. El precio que el usuario procesa es en pesos por día, no en tasa (63% lo prefiere así), y la tasa "anual" que circula subestima el costo real de un préstamo diario amortizado. Comparar "382% frente a 25%" no es cómo decide el usuario.
8. Dato oficial con error: el boletín EMICRON 2024 afirma que en el campo domina el gota a gota (77%); el anexo dice que domina el crédito regulado (77%) y el gota a gota es 9,8%. Verificar siempre el anexo.
9. La misma encuesta ANIF que reporta 382% anual dice que los hogares pagan "hasta 3,2 veces" el préstamo en 2 meses, lo que no cuadra con esa tasa. Las cifras de costo del gota a gota que circulan en prensa no son consistentes entre sí.

## 6. Hipótesis que la evidencia refuta

- "La mayoría de los micronegocios usa gota a gota": falso a nivel nacional (22,9% de los que piden, cerca de 3% del total, EMICRON 2024). Cierto para ambulantes (61,8% de los que piden) y para el Caribe urbano.
- "El banco rechaza a los micronegocios": el rechazo medido es bajo; la autoexclusión (miedo a deudas) domina.
- "El problema es no tener cuenta": la tenencia de depósitos es casi universal en registros y el uso de billeteras es alto entre usuarios de gota a gota; el uso de crédito formal es lo que cae.
- "El gota a gota financia inventario": para buena parte de los usuarios financia el hogar, emergencias y otras deudas.
- "El gota a gota es un problema rural": en EMICRON es sobre todo urbano (27,5% de los solicitantes en cabeceras frente a 9,8% en lo rural), contra lo que dice el propio boletín DANE.
- "El gota a gota está creciendo en todo el país": entre micronegocios el número bajó (201.965 en 2022 a 160.724 en 2023 a nivel nacional); lo que crece es su concentración en el Caribe y su peso entre ambulantes.

## 7. Preguntas abiertas para campo (y cómo preguntarlas sin sesgar)

1. ¿Por qué el gota a gota domina en Barranquilla y casi no aparece en Bogotá? ¿Oferta (redes que llegan a la puerta), demanda o subregistro? Cómo preguntar: "Cuénteme quién pasa por su negocio en una semana normal, desde el lunes." Anotar si aparece el cobrador sin mencionarlo.
2. ¿Qué significa "miedo a endeudarse"? ¿Miedo al banco, al reporte en centrales o al cobro del gota a gota? Cómo preguntar: "La última vez que pensó en pedir plata prestada y no la pidió, ¿qué pasó? ¿Qué le preocupaba?"
3. ¿Para qué se usó realmente el último préstamo (negocio, hogar, otra deuda)? Cómo preguntar: "Con esa plata, ¿qué fue lo primero que pagó?" En lugar de "¿para qué lo pidió?"
4. ¿Cuánto paga al día y durante cuántos días? (sin pedir tasa). Cómo preguntar: "Si alguien le presta 200.000, ¿cuánto se paga al día y cuántos días?" En tercera persona para reducir vergüenza.
5. ¿Cuántos préstamos encadena y con cuántos prestamistas a la vez? Cómo preguntar: "¿Alguna vez un préstamo terminó justo cuando empezó otro? Cuénteme esa vez."
6. ¿Qué tan subregistrado está el gota a gota en encuestas? Cómo preguntar: comparar la respuesta directa ("¿usted ha usado?") con la indirecta ("de cada 10 vecinos de este sector, ¿cuántos cree que tienen uno?").
7. ¿El ambulante y el tendero son el mismo problema? Entrevistar ambos por separado y comparar frecuencia de ingreso, dónde guardan la plata y quién les fía.
8. ¿Cuánto tiempo aguanta el negocio sin ventas? Cómo preguntar: "La última vez que no pudo vender tres días seguidos, ¿cómo pagó lo de la casa?"

## 8. Bibliografía

Fuentes primarias oficiales:
- DANE. Encuesta de Micronegocios (EMICRON) 2024, anexos y boletín técnico (30 jul 2025). https://www.dane.gov.co/files/operaciones/EMICRON/anex-EMICRON-2024.xlsx ; https://www.dane.gov.co/files/operaciones/EMICRON/bol-EMICRON-2024.pdf
- DANE. EMICRON 2023, anexos (31 may 2024). https://www.dane.gov.co/files/operaciones/EMICRON/anex-EMICRON-2023.xlsx
- DANE. EMICRON 24 ciudades y áreas metropolitanas 2025, anexos y boletín (30 jul 2026). https://www.dane.gov.co/files/operaciones/EMICRON/anex-EMICRON-24Ciudades-2025.xlsx ; https://www.dane.gov.co/files/operaciones/EMICRON/bol-EMICRON-24Ciudades-2025.pdf
- DANE. EMICRON 24 ciudades 2023 y anexo de ciudades 2024 (para la serie). https://www.dane.gov.co/files/operaciones/EMICRON/anex-EMICRON-24Ciudades-2023.xlsx ; https://www.dane.gov.co/files/operaciones/EMICRON/anex-Ciudades-EMICRON-2024.xlsx
- DANE. EMICRON Vendedores ambulantes 2025 (actualizado 18 sep 2026). https://www.dane.gov.co/files/operaciones/EMICRON/anex-EMICRONVendedoresAmbulantes-2025.xlsx ; https://www.dane.gov.co/files/operaciones/EMICRON/bol-EMICRONVendedoresAmbulantes-2025.pdf
- DANE. EMICRON Panaderías y tiendas de barrio 2024 (actualizado 8 may 2026). https://www.dane.gov.co/files/operaciones/EMICRON/anex-EMICRON-PanaderiasTiendasBarrio-2024.xlsb ; https://www.dane.gov.co/files/operaciones/EMICRON/bol-EMICRON-PanaderiasTiendasBarrio-2024.pdf
- DANE. EMICRON Sector Construcción 2024 (10 jun 2026). https://www.dane.gov.co/files/operaciones/EMICRON/bol-EMICRON-SectorConstruccion-2024.pdf
- DANE. GEIH, Ocupación informal, trimestre móvil mayo a julio 2026 (11 sep 2026), boletín y anexo. https://www.dane.gov.co/files/operaciones/GEIH/bol-GEIHEISS-may-jul2026.pdf ; https://www.dane.gov.co/files/operaciones/GEIH/anex-GEIHEISS-may-jul2026.xlsx
- Banca de las Oportunidades y Superintendencia Financiera. Reporte de Inclusión Financiera 2025 (ago 2026). https://www.superfinanciera.gov.co/loader.php?lServicio=Tools2&lTipo=descargas&lFuncion=descargar&idFile=1082980 ; nota: https://www.superfinanciera.gov.co/publicaciones/10116222/reporte-de-inclusion-financiera-2025-avances-en-depositos-credito-cobertura-y-transacciones/
- Banca de las Oportunidades, SFC y Banco de la República. Encuesta de Demanda de Inclusión Financiera 2022 (ago 2022), informe y microdatos. https://www.bancadelasoportunidades.gov.co/sites/default/files/2022-12/Encuesta%20de%20demanda%202022%20VF.pdf ; https://www.bancadelasoportunidades.gov.co/sites/default/files/2022-10/Encuesta_demanda_2022_microdatos.xlsx ; formulario: https://www.bancadelasoportunidades.gov.co/sites/default/files/2022-08/Formulario%20Encuesta%20de%20Demanda%202021_1.pdf
- Banca de las Oportunidades. Estudio de Demanda para Analizar la Inclusión Financiera en Colombia (primera toma, campo 2014 a 2015) y microdatos re publicados en 2025. https://www.bancadelasoportunidades.gov.co/sites/default/files/2018-02/Informe%20Estudio_demanda.pdf ; https://www.bancadelasoportunidades.gov.co/sites/default/files/2025-07/SP-14-038794-01-02-microdatos%20InclusionFinancieraPersonas-V1.xlsx
- Banca de las Oportunidades. Panorama de la exclusión financiera y el crédito informal en los micronegocios colombianos (sep 2025). https://www.bancadelasoportunidades.gov.co/sites/default/files/2025-09/Panorama%20de%20la%20Exclusi%C3%B3n%20Financiera%20y%20el%20Cr%C3%A9dito%20Informal%20en%20los%20Micronegocios%20Colombianos.pdf
- Banca de las Oportunidades. Caracterización de las unidades económicas de baja escala: enfoque regional 2025-II (ago 2026). https://www.bancadelasoportunidades.gov.co/sites/default/files/2026-08/caracterizacion-de-las-unidades-economicas-de-baja-escala.pdf
- Banco Mundial. The Global Findex Database 2025 (base de datos y glosario). https://www.worldbank.org/en/publication/globalfindex/download-data ; https://thedocs.worldbank.org/en/doc/be6615202d1f08a25855c8ac2d615122-0050012025/related/GlobalFindexDatabase2025.csv

Organismos, gremios y academia:
- UNODC ROCOL, S.A.G.A. (2024). Gota a gota: se lavan activos, el préstamo fácil. https://saga.unodc.org.co/es/gota-a-gota-se-lavan-activos-el-prestamo-facil
- ANIF y Colombia Fintech (2025). Análisis de cambios metodológicos de la tasa de usura y su impacto en la inclusión financiera. https://anif.com.co/wp-content/uploads/anif-colombia-fintech-analisis-de-cambios-metodologicos-de-la-tasa-de-usura-y-su-impacto-en-la-inclusion-financiera-un-enfoque-para-el-desarrollo-economico-sostenible-en-colombia-1.pdf
- ANIF (27 ene 2025). Encuesta de endeudamiento: una nueva perspectiva de la exclusión financiera. https://anif.com.co/informe-semanal/encuesta-de-endeudamiento-una-nueva-perspectiva-de-la-exclusion-financiera-liderada-por-anif-y-colombia-fintech/
- ANIF (22 sep 2026). Proteger sin excluir: el reto de la tasa de usura. https://anif.com.co/comentario-economico/proteger-sin-excluir-el-reto-de-la-tasa-de-usura/
- Asobancaria (28 ago 2026). Propuesta de programa público privado de rebancarización. https://www.asobancaria.com/comunicados-de-prensa/asobancaria-propone-al-gobierno-trabajar-en-un-programa-publico-privado-de-rebancarizacion-para-combatir-el-gota-a-gota/
- López Rivera, E., Manrique Chaparro, O. L. y Kalmanovitz Krauter, S. (2026). Los préstamos «gota a gota» en Bogotá: un análisis de necesidades, sesgos cognitivos y exclusión financiera. Apuntes 53(101). https://doi.org/10.21678/apuntes.101.2604 ; PDF: https://revistas.up.edu.pe/apuntes/es/article/download/2604/1974/8560

Prensa y gobierno local (secundarias):
- Portafolio (22 oct 2017). El gota a gota, el préstamo que se convierte en un infierno (cifras de la Dijín). https://www.portafolio.co/tendencias/el-gota-a-gota-el-prestamo-que-se-convierte-en-un-infierno-510881
- La República (18 feb 2025). La informalidad está presente en 77% de los micronegocios. https://www.larepublica.co/economia/banco-de-la-republica-estima-que-77-de-los-micronegocios-opera-en-la-informalidad-4065067
- El Heraldo (24 ago 2025). Por qué están matando a los cobradiarios en Barranquilla (incluye cifras de CrediChévere). https://www.elheraldo.co/judicial/2025/08/24/por-que-estan-matando-a-los-cobradiarios-en-barranquilla-y-su-area-metropolitana/
- Secretaría de Desarrollo Económico de Bogotá: https://desarrolloeconomico.gov.co/gota-a-gota/ ; https://desarrolloeconomico.gov.co/848-de-los-micronegocios-en-bogota-no-acude-al-sistema-financiero-observatorio-de-desarrollo-economico-de-bogota/
- DataCrédito Empresas (2020). Indicadores de crédito en Colombia (no accesible, HTTP 403). https://www.datacreditoempresas.com.co/blog-datacredito-empresas/indicadores-de-credito-en-colombia/

No encontrado (dicho explícitamente):
- Una estimación oficial o académica con método del valor total de la cartera gota a gota en Colombia.
- Una Encuesta de Demanda de Inclusión Financiera posterior a 2022.
- Resultados publicados del experimento de lista de la Encuesta de Demanda 2022.
- Resultados nacionales de EMICRON 2025 (a la fecha solo están publicados 24 ciudades 2025 y trimestrales).
- Montos promedio y plazos del crédito de micronegocios en EMICRON (la encuesta no los pregunta).

## Verificación

Revisión independiente hecha el 26 sep 2026. Los anexos DANE, el RIF 2025 y la base Findex se volvieron a descargar desde las URL citadas y se leyeron de nuevo; los PDF se abrieron desde sus URL oficiales.

| Claim | Resultado | Nota |
|---|---|---|
| 5.297.252 micronegocios y 6.879.489 ocupados (EMICRON 2024, Cuadro I.1) | confirmado | Anexo oficial, actualizado 30 jul 2025. Ventas: 191.166.139.848 miles de pesos, es decir $191,2 billones. |
| Ingreso mixto aprox. $1.092.855 al mes | confirmado | Ingreso mixto del Cuadro I.1 (69.469.539.519 miles) entre 5.297.252 y 12. |
| Pidieron crédito: 14,2% (702.293) en 2023; 17,8% (867.586) en 2022 | confirmado | Cuadro H.2 de los anexos 2024 y 2023. La base es 4.946.334 micronegocios que funcionaron en 2023, no los 5,3 millones. |
| Gota a gota entre solicitantes: 22,9% (160.724) en 2023; 23,3% (201.965) en 2022; regulada 60,0% | confirmado | Cuadro H.4 de ambos anexos. |
| Aprobación 92,9% y razones para no pedir (42,5% / 31,3% / 14,6% / 6,5% / 3,1%) | confirmado | Cuadros H.5 y H.3, EMICRON 2024. |
| Error del boletín EMICRON 2024 (rural 77,0% gota a gota) frente al anexo (9,8%) | confirmado | Boletín p. 32 dice textualmente "prestamistas gota a gota con el 77,0%"; el Cuadro H.4 da 27,5% en cabeceras y 9,8% en rural. También confirmado el "85,8% realizó alguna gestión" (p. 31), que es la proporción que no pidió. |
| 24 ciudades: 14,2% pidió; 35,6% (114.337) gota a gota, 41,6% regulada, 17,6% familia; uso 54,9% / 28,7% / 16,4% | confirmado | Cuadros H.2_24C, H.4_24C y H.6_24C; boletín p. 40, fechado 30 jul 2026. |
| Siete ciudades del Caribe: 80,1% (91.605 de 114.337); 16,0% frente a 1,3%; Barranquilla 20,2%, Bogotá 0,4% | confirmado | Recalculado desde H.2_24C y H.4_24C. Las 7 ciudades tienen el 25,2% de los micronegocios. No se recalcularon las series 2022 y 2023 (64,4% y 70,5%). |
| 79,1% no ahorró (24 ciudades) | corregido | La cifra cuadra, pero no es un valor publicado: sale de restar los 473.273 que ahorraron (H.8_24C) del total. Se marcó como cálculo propio y se bajó a media. |
| Ambulantes: 61,8% (25.744 de 41.672) a gota a gota; 46,4% en 2019; ingreso mixto aprox. $1,0 millón al mes | confirmado | Cuadros 18, 18.1 y 24 del anexo actualizado 18 sep 2026. |
| Ambulantes: "270.144 unidades" | corregido | El Cuadro 24 da 286.061 micronegocios en 2025; 270.144 es la base de la pregunta de crédito (los que funcionaron en 2024, Cuadro 16). |
| Tiendas de barrio: 19,0% pidió (27,0% en 2019); 11,3% gota a gota, 69,9% regulada | confirmado | Boletín pp. 25 y siguientes y anexo .xlsb, Cuadro H.2. |
| Tiendas de barrio: "488.459 unidades" | corregido | El Cuadro J.1 da 540.233 micronegocios en 2024; 488.459 es la base de la pregunta de crédito (Cuadro H.2). |
| GEIH may a jul 2026: 54,6% nacional, 40,6% 13 ciudades, 84,7% en microempresas; 14,96 de 24,53 millones; 94,5%; 10,13 millones cuenta propia, 83,3% informales | confirmado | Boletín del 11 sep 2026 (Tabla 1) y anexo, hojas "Prop informalidad", "Tamaño de empresa" y "Posición ocupacional". |
| GEIH: 83,2% en centros poblados y rural | no verificado | La p. 1 del boletín es un gráfico sin texto extraíble y no se buscó en el anexo. |
| RIF 2025: 20,3 millones (51,6%) con crédito formal; 35,6% SFC; 20,9% comercio; 96,5% (37,9 millones) con depósito | confirmado | PDF oficial de la SFC, pp. 6, 22 y 43. |
| RIF 2025: microcrédito formal 5,6% de adultos | corregido | La Gráfica 2 (p. 44) da 5,8% en 2025; 5,6% es el valor de 2024. Se confirmaron 18 a 25 años 2,7%, Atlántico 3,0% (tercero más bajo), Putumayo 13,2%. |
| Findex 2025: cuenta 57,1%; formal 13,5%; banco 8,0% (12,9% en 2021); familia 19,4%; emergencia 12,8% / 37,1% | confirmado | CSV oficial del Banco Mundial, filas de Colombia 2024 y 2021. |
| Encuesta de Demanda 2022: 29% de los solicitantes fue a fuentes informales; 65,4% no quiere deudas | confirmado | Informe p. 10. |
| Atlántico: 77,45% de los no solicitantes por miedo a endeudarse | confirmado | Banca de las Oportunidades, Panorama (sep 2025), p. 8, con base en EMICRON 2023. |
| ANIF y Colombia Fintech: 37,3% de hogares y 55% de empresas; muestra 1.221 personas y 1.009 mipymes | confirmado | Informe semanal del 27 ene 2025 y PDF de usura, p. 3. |
| ANIF: 91% en micro y de subsistencia | no verificado | No aparece en la versión de la página que se pudo leer ni en el PDF de usura. |
| ANIF: 12,1% del stock ($10,3 millones), 17,7% hasta 1 SMMLV; 382,2% y 666,5% EA; 41% y 52,2% pagan a diario | confirmado | PDF de ANIF y Colombia Fintech, pp. 4, 7, 8 y 11. |
| UNODC: 20 a 40%, usualmente mensual, sin cambios sustanciales desde 2013 | confirmado | Página S.A.G.A. de UNODC ROCOL (2024). |
| Dijín vía Portafolio: $2.500 millones al día; $1.000 millones en Bogotá; 137 municipios | confirmado | Portafolio, 22 oct 2017. La nota también dice "20 por ciento o más" en unos 26 días. Sigue siendo cifra policial sin método (confianza baja). |
| Asobancaria: de 51,6% a 75% de adultos, 5 millones como meta rápida, sin cuantificar el gota a gota | confirmado | Comunicado del 28 ago 2026. |
| ANIF 22 sep 2026: $11,8 billones en consumo y $13,0 billones en comercial | confirmado | Comentario económico "Proteger sin excluir". |
