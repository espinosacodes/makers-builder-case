# 13b. Escala LatAm: ¿se puede replicar la "Cláusula de lluvia del fiado"?

Fecha: 27 sep 2026, consultas hechas entre 8:20 y 8:45 hora de Colombia. Frente de verificación para la ambición internacional de la propuesta. Pregunta: ¿existen en Perú, México, Ecuador y Brasil las tres piezas que el mecanismo necesita? (a) fiado diario de mercancía a vendedores ambulantes, (b) datos abiertos y casi en tiempo real de estaciones de lluvia, (c) préstamo tipo gota a gota entre vendedores. Más un tamaño con fuente de la población de vendedores ambulantes en la región.

Método: WebSearch estaba agotado (200 de 200). Todo lo nuevo se obtuvo abriendo directamente las páginas y los endpoints públicos con curl, y el PDF de WIEGO con `pdf2txt.sh`. Lo de gota a gota sale del frente 02 (`02-comparacion-regional.md`) sin reabrir fuentes. No se usó ningún dato que no se haya visto en pantalla; donde algo no se pudo abrir, se dice.

## 1. Hallazgos principales

1. **Hay 5,73 millones de vendedores ambulantes en solo cinco países de América Latina** (Brasil 2,31 M, México 1,78 M, Perú 1,18 M, Chile 0,24 M, El Salvador 0,22 M), más 2,04 millones de comerciantes de plaza. Son cifras de WIEGO sobre encuestas de fuerza laboral de cada país (Ramírez y Vanek 2024, tabla 1). Entre 77% y más de 90% de los ambulantes de esos países es informal. Colombia y Ecuador no están en ese informe.
2. **Solo en cinco capitales hay 1,2 millones de ambulantes**: Lima Metropolitana 447.004 (8,8% del empleo), Ciudad de México 342.427, São Paulo 210.629, Santiago 133.156, San Salvador 65.681 (misma fuente). El break-even del caso base (904 vendedores que pagan) es 0,20% de los ambulantes de Lima, 0,26% de los de CDMX o 0,016% de los cinco países. Es un denominador, no una demanda: no se sabe qué parte saca fiado ni en qué ciudades llueve lo suficiente.
3. **El dato de lluvia existe y es público en los cuatro países, pero con fricciones distintas.** México y Ecuador exponen JSON sin registro con rezago de menos de 3 horas; Brasil publica un CSV horario de todas sus estaciones automáticas, pero con un mes de rezago, y su endpoint de datos recientes no respondió sin token; Perú muestra tablas por estación detrás de un captcha de Cloudflare. Ninguno de los cuatro tiene lo que Colombia tiene en datos.gov.co (API documentada del IDEAM).
4. **El gota a gota con cuota diaria está documentado en los cuatro países y en al menos tres lo atribuyen a redes colombianas** (frente 02): en Perú 35% de los préstamos informales se paga a diario, 85% en Iquitos; en México 1.500 prestamistas "sudamericanos" en CDMX que exigen "tener negocio"; en Brasil R$ 1.000 en 20 cuotas diarias de R$ 70; en Ecuador el chulco cobra USD 1, 5 o 10 diarios. El producto que la cláusula quiere volver innecesario es el mismo en toda la región.
5. **La pieza más débil fuera de Colombia es (a), el fiado diario de mercancía.** La única evidencia con número es WIEGO 2014 en cinco ciudades, una de ellas Lima: 38% de los ambulantes dice que el crédito del proveedor es "muy importante" para elegirlo. No se encontró en esta pasada ninguna encuesta de México, Ecuador o Brasil que mida el fiado de mercancía a ambulantes. Igual que en Colombia (EMICRON, frente 12a), es probable que las encuestas oficiales no lo capturen porque el vendedor no lo llama "crédito" (inferencia).
6. **Iquitos es el mejor candidato fuera de Colombia para un segundo piloto** (inferencia propia): es la ciudad peruana con más gota a gota (31% de los hogares del Oriente con préstamo informal y 85% de pago diario, IPE 2024), dos de cada tres prestamistas son extranjeros, sobre todo colombianos, y SENAMHI tiene una estación automática ("Amazonas", código 103065) en la ciudad. Lima, la ciudad con más ambulantes, es costa desértica con lluvia escasa, así que ahí el disparador de lluvia probablemente no aplica (conocimiento general, no se verificó con dato de SENAMHI).

## 2. Tabla de datos

| Dato | Cifra | País | Año | Fuente | URL | Confianza |
|---|---|---|---|---|---|---|
| Vendedores ambulantes, nacional | Brasil 2.309.349 (2,7% del empleo); México 1.781.373 (3,0%); Perú 1.183.845 (6,3%); Chile 236.995 (3,0%); El Salvador 219.140 (8,0%). Suma 5.730.702 (cálculo propio) | 5 países LAC | Brasil y Chile 2020, El Salvador 2021, México 2023, Perú 2019 | Ramírez Reynoso y Vanek, WIEGO Statistical Brief No. 40 (jul 2024), tabla 1, p. 3 | https://www.wiego.org/wp-content/uploads/2024/11/wiego-statistics-brief-no-40.pdf | alta (leído en el PDF) |
| Comerciantes de plaza (market traders), nacional | Brasil 506.978; México 976.236; Perú 351.029; Chile 145.749; El Salvador 62.781. Suma 2.042.773 (cálculo propio) | 5 países LAC | ídem | ídem, tabla 1 | ídem | alta |
| Vendedores ambulantes en la ciudad principal | Lima Metropolitana 447.004 (8,8%); CDMX 342.427 (3,6%); São Paulo 210.629 (2,2%); Santiago 133.156 (3,7%); San Salvador 65.681 (8,8%). Suma 1.198.897 (cálculo propio) | 5 ciudades | ídem | ídem, tabla 1 | ídem | alta |
| Informalidad de los ambulantes | más de 90% en México, Perú y El Salvador; entre 77% y 79% en Brasil y Chile | 5 países LAC | ídem | ídem, p. 5 | ídem | alta |
| Mujeres entre los ambulantes | Perú 68%, México 56%, Brasil 53% | ídem | ídem | ídem, p. 4 | ídem | alta |
| Ambulantes que dicen que el crédito del proveedor es "muy importante" | 38% (plaza 19%; perecederos 48%; mujeres 37%, hombres 24%) | Accra, Ahmedabad, Durban, Lima, Nakuru (n = 743) | encuesta 2012, pub. 2014 | Roever, WIEGO IEMS Sector Report: Street Vendors, 2.3.2, p. 39 | https://www.wiego.org/sites/default/files/publications/files/IEMS-Sector-Full-Report-Street-Vendors.pdf | alta (sin desglose por ciudad en el texto leído) |
| Lima: la deuda como respuesta a choques | "You have to ask for credit"; "When they take your things you lose everything, and you have to look for someone to loan you money to start all over again"; "The bank won't loan to you, but there are lenders" | Lima | 2012 / 2014 | ídem, tabla 21, p. 51 | ídem | alta (citas de grupos focales) |
| SENAMHI: estaciones en el mapa de datos | 696 estaciones: 313 automáticas (211 meteorológicas, 102 hidrológicas) y 383 marcadas "REAL" (313 meteorológicas, 70 hidrológicas); 11 automáticas meteorológicas en Lima Metropolitana; una en Iquitos ("Amazonas", 103065) | Perú | 27 sep 2026 | SENAMHI, Mapa de estaciones (conteo propio sobre la lista embebida en la página) | https://www.senamhi.gob.pe/mapas/mapa-estaciones-2/ | alta (conteo propio) |
| SENAMHI: acceso a los datos | tabla mensual por estación (San Borja: meses desde 2021-09 hasta 2026-09) detrás de una verificación de Cloudflare ("Por favor, verifica que no eres un robot"); no se encontró API documentada; hay un mapa aparte de descarga de datos históricos | Perú | 27 sep 2026 | SENAMHI, página de estación y "Descarga de datos Meteorológicos" | https://www.senamhi.gob.pe/mapas/mapa-estaciones-2/map_red_graf.php?cod=112193&estado=AUTOMATICA&tipo_esta=M&cate=EMA&cod_old= ; https://www.senamhi.gob.pe/?p=descarga-datos-hidrometeorologicos | alta (lo que se vio); no se pasó el captcha, así que no se vio la frecuencia de los datos |
| SMN México: red de EMAs | lista oficial de 193 estaciones (EMAS.xlsx); el visor devuelve 233 estaciones (200 del SMN: 140 EMA y 60 ESMA; 33 oceanográficas de SEMAR) | México | 27 sep 2026 | SMN (CONAGUA), página EMAs, "Descargar lista de estaciones" y visor sivea_v3 | https://smn.conagua.gob.mx/es/observando-el-tiempo/estaciones-meteorologicas-automaticas-ema-s | alta (conteo propio) |
| SMN México: frescura del dato | lluvia de la última hora (per=B1): 60 estaciones con dato de las 06:45 hora local cuando eran cerca de las 07:30 en CDMX; lluvia de 24 horas (per=B24): 201 estaciones, cierre a las 07:40 del 26 sep; 6 estaciones en CDMX. JSON sin registro. La página advierte: "La presente información es publicada tal cual es" | México | 27 sep 2026 | SMN, endpoints internos del visor: `getPrecipitacion.php?per=B1` y `per=B24` | https://smn.conagua.gob.mx/tools/GUI/sivea_v3/php/getPrecipitacion.php?per=B24 | media (funciona hoy, pero son endpoints del visor, no una API documentada; pueden cambiar) |
| INAMHI Ecuador: red | 1.894 estaciones en el visor; 202 automáticas transmitiendo, 156 automáticas sin transmisión, 1.518 manuales sin transmisión; en el cantón Quito 50 no manuales transmitiendo, en Guayaquil 6 | Ecuador | 27 sep 2026 | INAMHI, Visor Hidrometeorológico, endpoint `api_visor/station_information/estaciones/visores/` | https://inamhi.gob.ec/info/ | alta (conteo propio) |
| INAMHI Ecuador: frescura del dato | lluvia horaria por estación vía POST sin registro; estación Songa (Guayaquil): último dato 06:00 hora local del 27 sep, consultado a las 8:35 (unas 2,5 horas de rezago); la serie tiene huecos (sin datos del 14 al 17 sep) | Ecuador | 27 sep 2026 | INAMHI, `api_visor/station_data_automaticas/get_precipitation/` | https://inamhi.gob.ec/api_visor/station_data_automaticas/get_precipitation/ | media (endpoint del visor, no documentado; con otro formato de fecha devolvió error) |
| INAMHI: boletín diario Guayaquil y Durán | lluvia de 24 horas (07h00 a 07h00) en unas 25 estaciones y pluviómetros; boletín Nro 181 del 25 sep 2026; en PDF | Ecuador | 25 sep 2026 | INAMHI, Boletín Condiciones Meteorológicas Guayaquil y Durán | https://www.inamhi.gob.ec/guayaquil/registrodgy.pdf | alta |
| INAMHI: cómo se pide información | el enlace "Pasos para adquirir información Meteorológica e Hidrológica" de la portada es un video en Google Drive; no se vio | Ecuador | 2026 | INAMHI, portada | https://www.inamhi.gob.ec/ | baja (no se pudo ver el contenido) |
| INMET Brasil: estaciones | 673 estaciones automáticas en el catálogo; 519 "Operante" y 154 "Pane" | Brasil | 27 sep 2026 | INMET, `apitempo.inmet.gov.br/estacoes/T` (JSON abierto) | https://apitempo.inmet.gov.br/estacoes/T | alta (conteo propio) |
| INMET: datos históricos | un ZIP por año con CSV horario por estación ("PRECIPITAÇÃO TOTAL, HORÁRIO (mm)"); el archivo 2026 llega hasta el 31-08-2026 | Brasil | 27 sep 2026 | INMET, Dados Históricos | https://portal.inmet.gov.br/dadoshistoricos | alta |
| INMET: datos recientes por API | `apitempo.inmet.gov.br/estacao/<fechas>/A652` y `/estacao/dados/<fecha>/<hora>` devolvieron HTTP 204 (sin contenido) sin credenciales | Brasil | 27 sep 2026 | prueba propia | https://apitempo.inmet.gov.br/estacao/2026-09-20/2026-09-26/A652 | media (no se verificó el procedimiento para pedir token) |
| Gota a gota, Perú | 9,3% de hogares urbanos con prestamista informal; 35% de esos préstamos con pago diario (Iquitos 85%); Oriente 31% | Perú | 2024 | IPE para Asbanc, vía frente 02 | https://ipe.org.pe/wp-content/uploads/2024/10/IPE_El_mercado_de_credito_informal_en_el_Peru.pdf | alta |
| Gota a gota, México | cerca de 1.500 prestamistas sudamericanos en CDMX desde 2015; requisito: tener negocio e identificación; 1 a 3% diario | México | 2019 | CONDUSEF, vía frente 02 | https://revista.condusef.gob.mx/wp-content/uploads/2019/04/PDF-s_230_gota.pdf | alta |
| Gota a gota, Brasil | R$ 1.000 en 20 cuotas diarias de R$ 70; red colombiana presa en Teresina (Operação Macondo) | Brasil | 2025 | G1 Piauí, vía frente 02 | https://g1.globo.com/pi/piaui/noticia/2025/12/12/agiotas-emprestimos-com-juros-multas-piaui.ghtml | media |
| Gota a gota, Ecuador | chulco con cuota de USD 1, 5 o 10 diarios; 1.354 denuncias por usura (2021 a oct 2025), 3 condenas | Ecuador | 2021 a 2025 | Primicias (Equifax y Fiscalía), vía frente 02 | https://www.primicias.ec/economia/prestamos-informales-chulco-chulqueros-tasas-intimidacion-violencia-denuncias-110347/ | media |

## 3. Por país: las tres piezas

| Pieza | Perú | México | Ecuador | Brasil |
|---|---|---|---|---|
| (a) Fiado diario de mercancía | Parcial: Lima es una de las cinco ciudades del 38% de WIEGO y sus grupos focales hablan de crédito y prestamistas; sin cifra propia de Lima | No encontrado en esta pasada | No encontrado | No encontrado |
| (b) Estaciones de lluvia abiertas | Sí, 313 automáticas; tablas mensuales detrás de captcha; sin API | Sí, unas 200 EMAs y ESMAs; JSON sin registro, rezago menor a 1 hora; red fina (6 en CDMX) | Sí, 202 automáticas transmitiendo; JSON horario sin registro, rezago de unas 2,5 horas, con huecos; boletín diario en PDF para Guayaquil | Sí, 519 operantes; CSV horario con un mes de rezago; tiempo real sin respuesta sin token |
| (c) Gota a gota diario | Sí, fuerte (35% diario; Iquitos 85%) | Sí (CONDUSEF 2019, CDMX) | Sí (chulco diario) | Sí (agiotas, cuotas diarias) |
| Ambulantes (WIEGO 2024) | 1,18 M; Lima 447 mil | 1,78 M; CDMX 342 mil | sin dato en el informe | 2,31 M; São Paulo 211 mil |

Lectura: (b) y (c) se replican; (a) es la hipótesis que hay que validar en campo en cada país, igual que se validó en Cali.

## 4. Cómo usar esto en el informe sin inflar números

- **Frase defendible:** "El mecanismo se apoya en dos cosas que ya existen en al menos cuatro países más: prestamistas de cuota diaria que atienden a vendedores y redes públicas de estaciones automáticas de lluvia. Solo en Brasil, México, Perú, Chile y El Salvador hay 5,7 millones de vendedores ambulantes (WIEGO 2024)."
- **Frase que no se puede escribir:** "El mercado son 5,7 millones de vendedores." No se sabe cuántos sacan fiado diario, ni cuántos viven donde llueve lo bastante para que el disparador importe.
- **Cota ilustrativa, no estimación:** si en Lima el 38% de WIEGO se leyera como "depende del fiado" (no es lo que mide, y el dato no es de Lima sola), serían unos 170.000 ambulantes. Sirve para mostrar orden de magnitud, no para un modelo.
- **Orden de expansión sugerido (inferencia):** Colombia (IDEAM con API) primero; luego Guayaquil o Quito (JSON horario y gota a gota diario), CDMX en temporada de lluvias (JSON casi en tiempo real) e Iquitos (gota a gota más alto de Perú y estación automática). Lima solo si el disparador cambia de lluvia a otro choque verificable.
- **El costo técnico de cada país nuevo es bajo pero no cero:** leer México y Ecuador es un script como el del IDEAM; Brasil exige pedir token o esperar el CSV mensual; Perú exige un convenio o un acceso sin captcha. Esto es un supuesto de trabajo, no se cotizó.

## 5. Lo que no se encontró o no se pudo abrir

- Encuestas de México, Ecuador y Brasil sobre ambulantes que compran mercancía fiada. No se pudo buscar (WebSearch agotado). Fuentes candidatas para una pasada futura, sin haber verificado que midan esto: INEGI ENAMIN (micronegocios, México), INEC Ecuador, pesquisas de Sebrae o IBGE sobre ambulantes (Brasil), y los perfiles estadísticos de WIEGO de México, Perú y Brasil citados en el Brief 40.
- Total de ambulantes para toda América Latina. WIEGO y OIT no dan una cifra regional en lo leído; el Brief 40 cubre cinco países de la región. Colombia tiene 286.061 unidades ambulantes en 24 ciudades (EMICRON 2025, frente 01), que no es comparable (unidades y solo 24 ciudades, frente a trabajadores nacionales).
- La página de WIEGO sobre vendedores ambulantes (`/informal-economy/occupational-groups/street-vendors`) da 404 tras el rediseño del sitio.
- Frecuencia de lluvia en Lima, Iquitos, CDMX y Guayaquil: no se verificó en esta pasada. Lo de Lima seca y el resto lluvioso es conocimiento general.
- El video de INAMHI sobre cómo pedir información, y las condiciones para obtener token de INMET.

## 6. Referencias

- Ramírez Reynoso, T. y Vanek, J. (2024). *Street Vendors and Market Traders in 12 Countries: A Statistical Profile*. WIEGO Statistical Brief No. 40. https://www.wiego.org/wp-content/uploads/2024/11/wiego-statistics-brief-no-40.pdf
- Roever, S. (2014). *Informal Economy Monitoring Study Sector Report: Street Vendors*. WIEGO. https://www.wiego.org/sites/default/files/publications/files/IEMS-Sector-Full-Report-Street-Vendors.pdf
- SENAMHI. Mapa de estaciones y Descarga de datos. https://www.senamhi.gob.pe/mapas/mapa-estaciones-2/ ; https://www.senamhi.gob.pe/?p=descarga-datos-hidrometeorologicos
- SMN, CONAGUA. Estaciones Meteorológicas Automáticas. https://smn.conagua.gob.mx/es/observando-el-tiempo/estaciones-meteorologicas-automaticas-ema-s
- INAMHI. Visor Hidrometeorológico y Boletín Guayaquil y Durán. https://inamhi.gob.ec/info/ ; https://www.inamhi.gob.ec/guayaquil/registrodgy.pdf
- INMET. Dados Históricos y catálogo de estaciones. https://portal.inmet.gov.br/dadoshistoricos ; https://apitempo.inmet.gov.br/estacoes/T
- IPE (2024), CONDUSEF (2019), G1 Piauí (2025), Primicias (2025): ver `02-comparacion-regional.md`.

## 7. Método por fuente

| Fuente | Cómo se leyó |
|---|---|
| WIEGO Brief 40 | PDF descargado y leído (páginas 1 a 6, tabla 1) |
| WIEGO IEMS 2014 | PDF descargado; secciones 2.3.1, 2.3.2 y tabla 21 |
| SENAMHI | HTML del mapa (lista de estaciones embebida, conteo propio) y página de una estación; captcha no superado |
| SMN | HTML de la página, EMAS.xlsx y JSON del visor (conteo propio) |
| INAMHI | JS del visor para ubicar endpoints; JSON de estaciones y de lluvia horaria; PDF del boletín |
| INMET | HTML de Dados Históricos, primeros 2 MB del ZIP 2026 y JSON del catálogo |
