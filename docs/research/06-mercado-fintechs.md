# B6. Mercado, fintechs y analogías globales

Estado: completo

Fecha de corte: 26 de septiembre de 2026. Frente: punto 6 del prompt maestro (mercado y competidores).

Nota de método: este archivo combina (a) material recuperado de un intento previo interrumpido (búsquedas, páginas y PDF realmente abiertos, entre ellos filings de la SEC de MercadoLibre, StoneCo, PagSeguro, Credicorp, AB InBev y Coca-Cola FEMSA, el informe anual 2025 de Safaricom, FinAccess Kenya 2024 y el informe de sostenibilidad 2025 de Nutresa) y (b) unas 13 consultas nuevas de esta sesión. El presupuesto de WebSearch de la sesión se agotó (200 de 200), así que las consultas nuevas fueron WebFetch y curl a URLs conocidas. Por eso quedan huecos declarados: estado actual de Chiper y Aflore, crédito a tiendas de Postobón y Coca-Cola FEMSA, cifras de Konfío y Clip.

Confianza: **alta** = fuente primaria abierta (filing, informe oficial, documento de la empresa); **media** = prensa económica seria; **baja** = cifra vista solo en resumen de buscador o sin fuente original.

---

## 1. Resumen ejecutivo

1. **En Colombia murieron o se encogieron las B2B que hacían logística e inventario, no las que cobraban por pagos.** Frubana (US$271 millones levantados) cerró Colombia y México en febrero de 2024 y todo en julio de 2025; Tul sobrevivió cerrando Ecuador, despidiendo más de 100 personas y dejando de vender inventario propio para volverse marketplace; Treinta pasó de "superapp de tenderos" a software con IA para pymes en EE. UU. y LatAm. La causa documentada no fue la mora de los tenderos sino costos logísticos, márgenes bajos y fondeo que se cortó con tasas altas.
2. **Las que prestan a micronegocios a escala lo hacen cobrando de un flujo que ya controlan.** Bold (Colombia) descuenta 10% de cada venta del datáfono; Mercado Pago tiene más de US$2.000 millones en crédito a comercios (4T25); Kopo Kopo presta tras 60 días de transacciones en el till de M-Pesa; Yape presta a 5,6 millones de peruanos con tickets de S/220 a menos de un mes. El crédito es la segunda capa sobre pagos, nunca la primera.
3. **Cobrar de las ventas no elimina el riesgo.** StoneCo, con todos los datos de ventas de sus comercios, reportó en 1T26 un costo de riesgo de 21,9% y NPL mayor a 90 días de 6,98%; la empresa atribuye el alza a tendencias de mora del mercado que llevaron a un TPV minorista de sus clientes más débil de lo esperado, a casos puntuales de su mesa dedicada y a cosechas nuevas peores. Cuando el negocio vende menos, la "cuota automática" también cae. PagBank, el otro gigante brasileño, tiene 72% de su cartera en crédito de nómina y solo 9% en préstamos.
4. **Los productos que llegan a la base de la pirámide son diminutos, cortos y con precio en tarifa fija.** Tala: US$36 promedio, 28 días, cargo único de ~15%, mora de 5% (estudio con aprobación aleatoria, 2025). Yape: S/220 a menos de un mes. Fuliza: sobregiro sobre el saldo de M-Pesa, 7,9 millones de clientes. En contraste, el Crédito Negocios de Nequi es de $100.000 a $10 millones con cuota **mensual** fija.
5. **Los cuadernos de fiado digitales consiguieron millones de usuarios y casi cero ingresos.** OkCredit (India) perdió Rs 428,5 crore para facturar ~Rs 9 crore desde su fundación y llegó a gastar Rs 297 por cada rupia de ingreso (FY22). Khatabook facturaba sobre todo servicios a su propia matriz. Treinta dejó el marketplace. La respuesta predecible número 9 ya fue probada.
6. **Las cerveceras y distribuidoras no le prestan plata a la tienda: le dan plazo sobre su propio producto y tercerizan el crédito.** AB InBev reporta solo US$58 millones de "loans to customers" en todo el mundo frente a US$4.261 millones en cuentas por cobrar comerciales (93,6% al día) en 2025. Bavaria habla de "acceso a crédito" en BEES y de una alianza con CAF (2025), pero no publica montos ni mora.
7. **El canal de las distribuidoras ya llega a más tiendas que cualquier fintech de tenderos.** Nutresa: Pideky con 132.000 clientes en Colombia y más de COP 500.000 millones en ventas (2025) [NO VERIFICADO]. Bavaria: 128.000 tiendas en su programa 2026 y cerveza hasta 50% del ingreso diario de una tienda.
8. **La fintech de Medellín que "iba a acabar con el gota a gota" quebró por fondeo, no por los clientes.** Juancho Te Presta: reorganización en diciembre de 2024, pasivos de $39.755 millones y liquidación judicial en 2026; exigía ingreso mínimo de $1,5 millones y sin reportes negativos (es decir, no atendía al usuario del gota a gota) y enfrenta denuncias por presunta captación masiva.
9. **Los neobancos colombianos crecieron en consumo, no en micronegocio.** Nu Colombia (5 millones de clientes, 2026) no tiene producto para negocios; Lulo Bank siguió en pérdida en 2025 y se movió a empresas; Nequi (21,9 millones de cuentas activas) presta con cuota mensual y fianza del FGA. El único con producto atado a ventas diarias es Bold.
10. **Kenia muestra el costo de escalar crédito digital:** el porcentaje de deudores que no pagó nada subió de 10,7% (2021) a 16,6% (2024), y solo 45.150 comercios tienen sobregiro de M-Pesa frente a 1,8 millones de comercios que cobran con M-Pesa (2,5%).

---

## 2. Tabla de datos clave

| dato | cifra | país | año | fuente | URL | confianza |
|---|---|---|---|---|---|---|
| Capital levantado por Frubana antes de cerrar | US$271 millones | CO, MX, BR | 2025 | Forbes Colombia, "Frubana pone fin a sus operaciones" | https://forbes.co/2025/08/14/negocios/frubana-pone-fin-a-sus-operaciones/ | media |
| Participación de Brasil en ingresos de Frubana al salir de CO y MX | 60% | BR | 2024 | La República, "Frubana anunció cierre de operaciones en Colombia y México" | https://www.larepublica.co/empresas/frubana-cierra-en-colombia-3803987 | media |
| Restaurantes atendidos por Frubana en Colombia | más de 30.000 | CO | 2024 | La República (mismo artículo) | https://www.larepublica.co/empresas/frubana-cierra-en-colombia-3803987 | media |
| Serie B de Tul | US$181 millones | CO | 2022 | Valora Analitik, "Plataforma Tul anuncia recorte de personal" | https://www.valoraanalitik.com/plataforma-tul-anuncia-recorte-de-personal-y-revisa-estrategia-en-colombia-y-mexico/ | media |
| Despidos Tul | más de 100 personas | CO, MX | 2023 | Valora Analitik (17 ene 2023) | misma URL | media |
| Ferreterías atendidas por Tul | más de 8.000 (de menos de 50 en 2020) | CO | 2024 | El Colombiano, 28 feb 2024 | https://www.elcolombiano.com/negocios/empresas/la-historia-de-tul-el-marketplace-de-los-ferreteros-que-sobrevivio-a-la-crisis-y-espera-vender-us-10-millones-mensuales-PN23843639 | media |
| Pagos digitales en Tul Colombia | 65% (antes 100% efectivo) | CO | 2023 | Forbes Colombia, 8 mar 2023 | https://forbes.co/emprendedores/la-gran-apuesta-es-ser-rentables-tenemos-caja-para-mas-de-tres-anos-ceo-de-tul | media |
| Serie A de Treinta | US$46 millones | CO | 2022 | TechCrunch, 20 abr 2022 | https://techcrunch.com/2022/04/20/payu-doubles-down-on-latam-fintech-acquires-ding-and-leads-46m-investment-in-superapp-treinta-in-colombia/ | media |
| Negocios registrados en el marketplace de Treinta vs meta | 36.000 vs 90.000 | CO | 2023 | Startups Latam | https://startupslatam.com/tras-cerrar-la-serie-a-mas-alta-de-colombia-treinta-quiere-alcanzar-90-mil-usuarios-en-su-nuevo-marketplace-durante-2023/ | baja (resumen de buscador) |
| Descripción actual de Treinta | "Software and AI tools for SMBs in the US and Latin America", 60 empleados | CO, EE. UU. | 2026 | Y Combinator | https://www.ycombinator.com/companies/treinta | alta |
| Aflore: préstamo promedio y mora | US$630; 5,7% | CO | 2022 | Polymath Ventures (inversionista), caso | https://polymathv.substack.com/p/lessons-aflore-fintech-company-bringing-formal-financial-services-vulnerable-populations-latin-america | media |
| Juancho Te Presta: pasivos al entrar a reorganización | $39.755,9 millones (a 31 ago 2024) | CO | 2024 | La República, 12 jul 2025 | https://www.larepublica.co/finanzas/juancho-te-presta-recibe-denuncias-penales-por-presunta-captacion-masiva-de-dinero-4178752 | media |
| Juancho Te Presta: requisitos | ingreso mínimo $1,5 millones, sin moras, créditos de $1 a 5 millones | CO | 2026 | El Colombiano, 5 abr 2026 | https://www.elcolombiano.com/medellin/investigacion-juancho-te-presta-esteban-saldarriaga-medellin-BF35215150 | media |
| Mora del crédito digital en Colombia | más de 15%, hasta 25% en carteras riesgosas; covenants de fondeo de 5 a 8% | CO | 2026 | ENTER.CO, 18 jul 2026 (no cita fuente primaria) | https://www.enter.co/fintech/el-riesgo-fintech-de-colombia-como-la-cartera-vencida-esta-afectando-la-promesa-del-credito-digital/ | baja |
| Addi: clientes, comercios, mora 90 días | 5,5 millones; 76.000; 1,1% | CO | 2026 | Tekios, 2 jul 2026 | https://tekiosmag.com/2026/07/02/fitech-addi-lleva-ocho-trimestres-rentables-y-acaba-de-cerrar-su-serie-d-con-us86-millones/ | media |
| Nu Colombia: clientes y depósitos | 5 millones; más de $10 billones | CO | 2026 | Mobile Time, 26 may 2026 | https://mobiletime.la/noticias/26/05/2026/nu-colombia-cumple-cinco-anos/ | media |
| Nu Préstamo Ligero: tasa máxima | 64,35% E.A. ($100.000 a $5 millones) | CO | 2025 | LatamFintech | https://www.latamfintech.co/articles/nu-colombia-lanza-tarjeta-de-credito-para-personas-sin-historial-y-prestamos-digitales-en-colombia | media |
| Lulo Bank: pérdida | $47.966 millones | CO | 2025 | Las2orillas / Forbes Colombia | https://forbes.co/2026/02/23/economia-y-finanzas/el-banco-y-la-corporacion-financiera-de-jaime-gilinski-sorprenden-con-utilidades-destacadas-en-2025 | baja (resumen de buscador) |
| Bold: comercios y mecanismo de crédito | 500.000; cupo $300.000 a $30 millones, se paga con 10% de cada venta, ~6 meses | CO | 2025 | Valora Analitik vía Yahoo, 7 ene 2025 | https://es-us.finanzas.yahoo.com/noticias/bold-posicion%C3%B3-dat%C3%A1fonos-revela-estrategia-230000433.html | media |
| Bold: crédito acumulado y fuerza de ventas | más de $110.000 millones; 700 vendedores directos | CO | 2025 | Bloomberg Línea, 31 mar 2025 | https://www.bloomberglinea.com/latinoamerica/colombia/bold-el-neobanco-de-las-pymes-suma-500000-clientes-en-colombia-y-lanzara-tarjeta-de-credito-2/ | media |
| Wompi: volumen y comercios activos | ~$50 billones; 40.000 comercios al mes | CO | 2025 | Colombia Fintech, 16 ene 2026 | https://colombiafintech.co/2026/01/16/wompi-proceso-transacciones-por-50-billones-en-2025-130-mas-que-en-2024/ | media |
| Nequi: cuentas y activas | 27,4 millones; 21,9 millones activas | CO | 2025 | Grupo Cibest, informe 4T25, p. 1 | https://plataforma.valoraanalitik.com/informacion-relevante/grupo-cibest-s.a.-4t25-espaol.pdf | alta |
| Nequi: créditos desembolsados y monto promedio | más de 590.000; $2,4 millones; 68% a no bancarizados o con poco historial | CO | 2025 | Ecosistema Startup, 17 mar 2026 (no cita fuente) | https://ecosistemastartup.com/nequi-expande-cartera-de-credito-con-analitica-avanzada/ | baja |
| Nequi: costo de riesgo | 9 a 10% | CO | 2025 | solo resumen de buscador, fuente original no encontrada | n/d | baja |
| Nequi Crédito Negocios | $100.000 a $10 millones, 1 a 36 cuotas mensuales, 1,79% a 1,91% m.v., débito automático del saldo | CO | 2025 | El Heraldo, 29 abr 2025; reglamento Nequi | https://www.nequi.com.co/informacion-legal/prestamo-propulsor/reglamento-credito-negocios | alta |
| Daviplata: usuarios y conversión de ofertas | 19,5 millones; 1 a 1,5 millones de ofertas al mes; conversión 8 a 10% | CO | 2026 | Valora Analitik vía Yahoo, 17 mar 2026 | https://es-us.noticias.yahoo.com/entrevista-apuesta-cr%C3%A9dito-daviplata-evoluci%C3%B3n-170000401.html | media |
| Mercado Pago: crédito a comercios | más de US$2.000 millones | LatAm | 2025 | MercadoLibre, 8-K 4T25 (Ex. 99.1) | https://www.sec.gov/Archives/edgar/data/1099590/000109959026000003/meli-20260224xex991.htm | alta |
| Mercado Pago: cartera total, NIMAL | US$12.500 millones (+90%); NIMAL 23,3% | LatAm | 2025 | mismo | misma URL | alta |
| StoneCo: costo de riesgo y NPL | 21,9%; NPL 15 a 90 días 4,97%; NPL > 90 días 6,98% | BR | 1T26 | StoneCo, earnings release 1T26 | https://www.sec.gov/Archives/edgar/data/1745431/000207097926000265/earningsrelease1q26.htm | alta |
| StoneCo: tasa mensual promedio del crédito | 3,3% | BR | 1T26 | mismo | misma URL | alta |
| StoneCo: saldo de comercios con más de 90 días | 8,6% (jun 2026) vs 5,1% (dic 2025) | BR | 2026 | cálculo propio sobre nota 5.4.1 de EEFF 30 jun 2026 | https://www.sec.gov/Archives/edgar/data/1745431/000207097926000274/stoneco_06x2026.htm | alta (cálculo propio) |
| PagBank: composición de cartera | R$4.623 millones: nómina R$3.318, tarjeta R$898, préstamos R$408 | BR | 2026 | PagSeguro, 6-K ago 2026, nota 9 | https://www.sec.gov/Archives/edgar/data/1712807/000155485526001791/MainDocument.htm | alta |
| Yape: MAU, cartera, clientes con crédito | 16,7 millones; S/1.800 millones; 5,6 millones | PE | 2T26 | Credicorp, earnings release 2T26 (6-K 17 ago 2026) | https://www.sec.gov/Archives/edgar/data/1001290/000114036126033379/ef20080305_ex99-1.htm | alta |
| Yape: tickets | una cuota ~S/220 a menos de un mes; cuotas ~S/850 a 9 meses; pyme ~S/3.300 a 10 meses | PE | 2T26 | mismo | misma URL | alta |
| Yape: ingreso vs gasto por MAU | S/11,1 vs S/6,0 al mes | PE | 2T26 | mismo | misma URL | alta |
| Fuliza: clientes, ingreso | 7,9 millones; KShs 4.100 millones | KE | FY2025 (a mar 2025) | Safaricom, Annual Report 2025, p. 100 | https://www.safaricom.co.ke/annualreport_2025/wp-content/uploads/2025/08/safaricom-annual-report.pdf | alta |
| Comercios M-Pesa con sobregiro vs comercios | 45.150 vs 1,8 millones (LNM + Pochi) | KE | FY2025 | mismo, p. 100 | misma URL | alta |
| Deudores kenianos que no pagaron nada | 16,6% (10,7% en 2021) | KE | 2024 | CBK, KNBS, FSD Kenya, FinAccess 2024, p. 55 | https://finaccess.knbs.or.ke/reports-and-datasets | alta |
| Negocios kenianos que financian operación con ingresos reinvertidos | 82,1% | KE | 2024 | FinAccess 2024, p. 69 | misma URL | alta |
| M-Shwari: efecto en resiliencia | toma 34%; 6,3 pp menos probabilidad de dejar de cubrir gastos ante choque | KE | 2019 | Bharadwaj, Jack y Suri, NBER w25604 | https://www.nber.org/papers/w25604 | alta |
| Tala: préstamo, plazo, cargo, mora en experimento | US$36; ~28 días; ~15% cargo único; 5% mora; ingreso +21% | KE | 2025 | HBS Working Knowledge (Kang, Chen, Even-Tov, Wittenberg-Moerman) | https://www.library.hbs.edu/working-knowledge/how-40-dollar-loans-lifted-lives-in-kenya | media (resumen del paper) |
| Tala: clientes y crédito acumulado | más de 15 millones; más de US$10.000 millones | global | 2026 | web corporativa | https://tala.co/ | media (autodeclarado) |
| OkCredit: pérdidas vs ingresos acumulados | Rs 428,5 crore vs ~Rs 9 crore | IN | 2023 | Entrackr, 4 dic 2023 | https://entrackr.com/2023/12/okcredit-lost-rs-428-cr-to-earn-rs-9-cr-since-incorporation/ | media |
| OkCredit: gasto por rupia de ingreso | Rs 297 | IN | FY22 | Entrackr, 21 dic 2022 | https://entrackr.com/2022/12/five-year-old-okcredit-spends-rs-297-to-earn-a-rupee-in-fy22/ | media |
| Khatabook: ingresos FY22 y origen | Rs 71 crore, 77,5% por servicios a su matriz Kyte; pérdida Rs 111 crore | IN | FY22 | Entrackr, 23 nov 2022 | https://entrackr.com/2022/11/khatabook-ends-fy22-with-4x-growth-in-revenue-and-rs-111-cr-loss/ | media |
| AB InBev: préstamos a clientes vs cuentas por cobrar | US$58 millones vs US$4.261 millones (93,6% al día) | global | 2025 | AB InBev, 20-F 2025, nota 19 | https://www.sec.gov/Archives/edgar/data/1668717/000119312526088105/d65314d20f.htm | alta |
| Bavaria: tiendas y peso de la cerveza | más de 500.000 negocios en canal tradicional; cerveza hasta 50% del ingreso diario; 50 a 200 unidades al día | CO | 2025 | Bavaria, nota de prensa 5 ago 2025 | https://www.bavaria.co/noticia/bavaria-invierte-mas-100000-millones-ano-desarrollo-sus-clientes-lanza-nueva-0 | media (autodeclarado) |
| Emprendedores Bavaria | más de 80.000 tenderos desde 2017; "30% más de ingreso diario" | CO | 2025 | Bavaria, alianza con CAF, 1 ago 2025 | https://www.bavaria.co/noticia/bavaria-firma-alianza-con-caf-para-impulsar-inclusion-financiera-digitalizacion | baja (sin metodología) |
| Nutresa Pideky | más de 132.000 clientes; más de COP 500.000 millones en ventas | CO | 2025 | Grupo Nutresa, Informe de sostenibilidad 2025, p. 50 | https://data.gruponutresa.com/informes/2025/Informe-de-sostenibilidad-resumen-grupo-nutresa.pdf | media [NO VERIFICADO: el PDF devuelve 403 en la verificación] |
| Kueski: CAT promedio de ejemplo | 153,31% | MX | 2026 | web Kueski (calculado 2 mar 2026) | https://www.kueski.com/ | alta |

---

## 3. Hallazgos por tema

### 3.1 Startups B2B para tenderos en Colombia: qué pasó

**Frubana (cerró).** Marketplace y mayorista digital de frutas, verduras y abarrotes para restaurantes y tiendas; tenía Frupay (pagos y crédito). Suspendió Colombia y México el 19 de febrero de 2024 con la frase "Las condiciones macroeconómicas no han sido favorables, impidiéndonos reunir los recursos necesarios" (La República). Última entrega en Brasil el 30 de julio de 2025 (Forbes Colombia). El Colombiano recoge "altos costos logísticos" y competencia de Rappi e iFood. Un análisis de insolvencias (Concordia Simple) resume: "El modelo sobrevivía gracias a rondas de inversión; cuando el mercado se volvió más exigente (tasas altas, menos liquidez) el financiamiento se cortó"; fue un "cierre ordenado", no una quiebra formal (https://concordiasimple.com/quiebra-frubana-lecciones-emprendedores-latam/, confianza media). No se encontró cifra de mora de Frupay: la muerte fue por economía de la logística, no por el crédito.

**Tul (sobrevivió encogiéndose).** Marketplace de materiales para ferreterías. Tras la Serie B de US$181 millones (enero 2022) cerró Ecuador (2022), despidió más de 100 personas en Colombia y México (enero 2023) y, según su CEO, optó "por dejar de vender productos directamente, permitiendo que otros distribuidores presenten artículos en el marketplace" (El Colombiano, 28 feb 2024). En marzo de 2023 decía tener caja para más de tres años y que "la gran apuesta es ser rentables", sin más expansión geográfica (Forbes Colombia). Ofrece crédito a ferreteros de $500.000 a $100 millones a 30, 45 o 60 días (Pulzo/La República, fecha no verificada, confianza baja) y tenía una línea de crédito de $38.000 millones para construir historial propio (Forbes 2023). En septiembre de 2026 el sitio tul.com.co sigue activo como "marketplace de construcción" (verificado con curl). Lección: la B2B sobrevive cuando deja de cargar inventario y logística y se queda con la plataforma.

**Chiper (estado no verificado).** Marketplace B2B para tiendas de barrio con entrega en menos de 24 horas; Serie B de US$53 millones (noviembre 2021). Dice atender 110.000 tiendas en Brasil, México, Colombia y Chile (texto corporativo sin fecha, confianza baja). Desde julio de 2023 opera en Chile como Chiper Copec (alianza con la petrolera Copec), con más de 6.000 almacenes (copecwind.cl, sin fecha). No encontré noticias de cierre ni cifras 2024 a 2026; chiper.co responde con una aplicación web sin contenido legible. **Hueco declarado.**

**Treinta (pivotó dos veces).** Nació como cuaderno digital de ventas, gastos y deudas (fiado); en 2022 levantó US$46 millones para un marketplace mayorista (36.000 negocios registrados a mediados de 2023 frente a una meta de 90.000) y lanzó un datáfono con 2,99% de comisión. En 2026 Y Combinator la describe como "Software and AI tools for SMBs in the US and Latin America", con 60 empleados y "7 millones" de negocios, y sus fundadores lanzaron idealane, un constructor de apps con IA (febrero 2026). El sitio treinta.co sigue ofreciendo inventario, ventas y "control de deudas". No encontré un comunicado sobre el cierre del marketplace. Lección: millones de descargas de un cuaderno de fiado no se traducen en un negocio de crédito ni de abastecimiento.

**Aflore (estado no verificado).** Modelo de "asesores" o "banqueras comunitarias": personas con buen manejo financiero que refieren y acompañan créditos a su red, con app. Datos de su inversionista Polymath (2022): 76% de asesoras mujeres, préstamo promedio US$630, mora 5,7%, margen 8%. US$17 millones desembolsados en siete años y US$10 millones de deuda de Accial Capital (2020). Un perfil de Crunchbase o similar menciona 14.000 asesores (sin fecha, confianza baja). En septiembre de 2026 www.aflore.co no responde (falla de conexión vía CloudFront); no encontré noticias de cierre, liquidación ni venta. **Hueco declarado.** Es el caso más cercano a "tomar prestada la confianza" (H6) y merece una entrevista o búsqueda en Supersociedades.

### 3.2 Fintechs de crédito y pagos en Colombia

- **Addi** (BNPL de consumo en comercios): licencia de compañía de financiamiento (Resolución 2036 de 2024, permiso de funcionamiento abril 2026), 5,5 millones de clientes, 76.000 comercios, mora a 90 días de 1,1%, ocho trimestres rentables y Serie D de US$86 millones (2026). Despidió personal en 2022 (Bloomberg Línea). Su usuario es el consumidor que compra en el comercio, no el micronegocio. Su baja mora viene de prestar en el punto de venta para una compra concreta, con el comercio como canal.
- **Nu Colombia**: compañía de financiamiento desde enero de 2024; 5 millones de clientes (15% de adultos) y más de $10 billones en depósitos (mayo 2026); tarjeta Abrecaminos garantizada con un depósito para quien no tiene historial; Préstamo Ligero hasta 64,35% E.A. No encontré producto para negocios.
- **Lulo Bank** (Gilinski): pérdida de $47.966 millones en 2025 (confianza baja) y, en junio de 2025, anuncio de entrada "muy duro" al segmento de empresas (Valora Analitik).
- **Movii** (SEDPE): 146 empleados y 85,81% de Tranza Holding a diciembre de 2025 (según resumen del informe financiero; los PDF devolvieron 404). Las SEDPE registraron pérdidas en 2023 y 2024 (Infobae/Valora). No ofrece crédito propio verificado.
- **Bold**: datáfono y cuenta para pequeños comercios; 500.000 clientes; crédito de $300.000 a $30 millones que se paga con **10% de cada venta**, en promedio en seis meses, con más de $5.000 millones desembolsados al mes; obtuvo licencia de compañía de financiamiento (Valora, enero 2025, confianza media); 700 vendedores directos. No publica mora. Es el análogo colombiano de Kopo Kopo y Stone.
- **Wompi** (Bancolombia): pasarela y QR interoperable Bre-B; ~$50 billones procesados y 40.000 comercios activos mensuales en 2025; 10.800 corresponsales. No es producto de crédito.
- **Nequi**: 27,4 millones de cuentas y 21,9 millones activas (dic 2025, Cibest, alta); cartera superior a $1,3 billones (3T25, La República) y "generó utilidades" en septiembre de 2025; desde el 1 de septiembre de 2026 opera como Nequi S.A. Compañía de Financiamiento separada de Bancolombia (Infobae). Crédito Negocios: cuota fija **mensual** ("cada mes vencido deberás pagar... la cuota fija"), débito automático de cualquier saldo, fianza del FGA o FNG y seguro de vida obligatorio. Préstamo Propulsor con comisión de fianza de 0 a 17,8% del crédito (El Tiempo, 12 may 2025). Nequi presta con la lógica del banco (mensual, fianza, reporte a centrales), pero con distribución digital.
- **Daviplata**: 19,5 millones de usuarios; 1 a 1,5 millones de ofertas de crédito al mes con conversión de 8 a 10% (marzo 2026). Ese 90% que no acepta la oferta es un dato interesante: la oferta preaprobada no es la barrera.
- **Juancho Te Presta y Lineru/Zinobe**: ver sección 4. Muestran que el cuello de botella de una originadora sin licencia es el fondeo.

### 3.3 Mercado Pago, Stone, PagSeguro y Yape: los que ya cobran del flujo

- **Mercado Pago**: cartera de US$12.500 millones (+90%), crédito a comercios por encima de US$2.000 millones, NIMAL 23,3% (4T25). [NO VERIFICADO: la carta a accionistas del 8-K 4T25 no trae un NPL 15 a 90 días de 6,7% para la cartera total; solo reporta 4,4% para la cartera de tarjeta de crédito.] La carta a accionistas dice que las carteras de consumo y comercio "provide us with the greatest flexibility to price across a wider range of risk profiles". En México crece "onboarding long-tail and SMB merchants, many of whom are accepting digital payments for the first time". No encontré cifras de crédito a comercios en Colombia.
- **StoneCo**: cartera de R$3.225 millones (1T26), de la cual R$2.861 millones (89%) es crédito a comercios; tasa promedio 3,3% mensual; costo de riesgo 21,9%; la empresa atribuye el deterioro a "early signs of weaker performance in newer vintages" y a "softer-than-expected retail TPV among portfolio clients". Con los EEFF de junio de 2026, el saldo de comercios con más de 90 días pasó de 5,1% a 8,6% en seis meses (cálculo propio).
- **PagSeguro/PagBank**: de R$4.623 millones de cartera (junio 2026), R$3.318 millones son crédito de nómina y solo R$408 millones son préstamos. El crédito no garantizado a pequeños comercios quedó marginal.
- **Yape** (BCP, Perú): 16,7 millones de MAU con 69 transacciones al mes cada uno; gana S/11,1 y gasta S/6,0 por MAU al mes; 45% de su ingreso ajustado por riesgo viene de pagos y 28% de crédito; ya dio crédito a 5,6 millones de personas con tickets de S/220 a menos de un mes. Primero se volvió hábito diario y después prestó poco y corto.

### 3.4 Distribuidoras de consumo masivo y crédito para tiendas

- **Bavaria / BEES (AB InBev)**: el 20-F 2025 describe "our business-to-business platform, BEES, which provides e-commerce and fintech solutions to retailers and services to our wholesalers". Bavaria dice que BEES incluye "acceso a crédito" y que Emprendedores Bavaria da capacitación, digitalización y crédito (nota del 5 ago 2025), además de una alianza con CAF (1 ago 2025) para "modelos de financiamiento adaptados" en coordinación con fintechs. **No publica montos, aliados financieros ni mora.** El balance global de AB InBev muestra solo US$58 millones en préstamos a clientes: el crédito que ve la tienda es plazo comercial sobre producto o un tercero financiero. El 20-F también menciona el programa Emprendedores en Colombia, Perú y Ecuador.
- **Nutresa**: Pideky (plataforma de pedidos para tiendas) con 132.000 clientes en Colombia y más de COP 500.000 millones en ventas en 2025; 1,7 millones de clientes en la región. No encontré producto de crédito.
- **Coca-Cola FEMSA**: su 20-F 2025 habla de Juntos+ (plataforma omnicanal) y Juntos+ Advisor (herramienta de la fuerza de ventas con IA). No encontré mención de crédito a tiendas.
- **Postobón**: su sala de prensa (2023 a 2026) no mostró programa de crédito a tenderos; sí plataformas para proveedores (pago anticipado de facturas vía Affirmatum). **Hueco declarado.**
- **Lección**: el actor que ya tiene la relación, la visita semanal y el dato de compra de la tienda (la distribuidora) decide **no** poner su balance en préstamos de caja y se limita al plazo sobre su propio inventario. Eso sugiere que el riesgo percibido del efectivo libre es muy distinto al del inventario propio.

### 3.5 México: Kueski, Konfío, Clip, Stori

- **Kueski**: SOFOM ENR (no requiere autorización de la SHCP), más de 40 millones de préstamos, préstamos de $60 a $26.000 MXN (web consultada en sep 2026), CAT promedio de ejemplo de 153,31% (marzo 2026) y 0% en el primer préstamo como gancho.
- **Konfío**: unicornio (US$1.300 millones, 2021) de crédito a pymes con datos alternativos; cerró su ERP Gestionix en octubre de 2023 para "mantener nuestro foco" en servicios financieros (Contxto); línea de MXN 4.100 millones de Goldman Sachs y Gramercy (marzo 2023). Su web bloqueó el acceso; no obtuve cifras de cartera ni de mora.
- **Clip**: terminal con 2,99% + $1 + IVA y "préstamos para negocios" sin detalle público del mecanismo de repago.
- **Stori**: SOFIPO, más de 5 millones de clientes, tarjeta para personas sin historial. Es consumo, no micronegocio.

### 3.6 África: M-Pesa, M-Shwari, Fuliza, Kopo Kopo, Moniepoint, Tala

- **Fuliza** (sobregiro de M-Pesa, clasificado como producto bancario en FinAccess 2024, p. 20): 7,9 millones de clientes y 18,4% de adultos lo usan. Su lógica es un sobregiro que se cubre solo con el siguiente ingreso a la billetera, sin cuota.
- **Comercios**: 1,8 millones de comercios cobran con M-Pesa, de ellos 1,15 millones con Pochi la Biashara (billetera para negocios informales, que separa la plata del negocio de la personal), pero solo 45.150 tienen sobregiro de comercio. Safaricom anuncia "a term loan for Pochi and LNM merchants while supporting Fuliza Biashara partners in managing non-performing loans (NPLs) for overdraft". Traducción: aun con el mejor dato de flujo del mundo, el sobregiro a comercios tiene problemas de mora.
- **M-Shwari**: 34% de toma y mejora de resiliencia ante choques (NBER 2019).
- **Kopo Kopo**: da el till de Lipa na M-Pesa y luego "Business Cash Advance" de hasta KES 15 millones tras 60 días de transacciones; licencia CBK de Digital Credit Provider. Moniepoint la compró en 2023, pero en 2026 TechCabal dice que esa entrada "stalled" y Moniepoint compró 78% de Sumac Microfinance Bank porque la licencia de captación es "essential requirement for its credit-led expansion strategy".
- **Moniepoint** (Nigeria): mayor adquirente POS de Nigeria, 20 millones de negocios y personas al mes, US$294.000 millones procesados en 2025; su banco de microfinanzas desembolsó más de ₦1 billón en 2025 (Wikipedia, confianza media). Modelo: agentes y POS primero, crédito después.
- **Tala**: más de 15 millones de clientes; en México opera como SOFOM ENR; línea de US$150 millones de Neuberger Berman (2025); Forbes (sep 2025) la titula "Unprofitable Microlending Fintech Makes Big Bet On Global Expansion" (no pude abrir el texto). Pivota hacia stablecoins y crédito tokenizado (2025 a 2026). El estudio con aprobación aleatoria de solicitudes rechazadas (Kang y otros, 2025) encontró mora de 5% e ingreso 21% mayor con préstamos de US$36 a 28 días.
- **FinAccess 2024**: la mora total subió a 16,6% de los deudores, y 82,1% de los negocios se financia con sus propias ventas.

### 3.7 India e Indonesia: Khatabook, OkCredit, BukuWarung

- **OkCredit**: cuaderno digital gratuito (más de 10 millones de descargas); pérdidas acumuladas de Rs 428,5 crore; despidió 35% en 2022 y cerró OkShop; en 2020 pidió licencia NBFC (titular de Entrackr, confianza baja).
- **Khatabook**: mismo producto; US$187 millones levantados; FY22 con ingresos que venían sobre todo de servicios a su matriz; despidos en 2023 "in line with our profitability goals" y meta de cartera de préstamos de Rs 1.000 crore; Inc42 reporta un derrumbe de ingresos de FY24 a FY25 sin explicación (confianza baja).
- **BukuWarung**: sobrevivió convirtiéndose en agente de pagos: PPOB (recargas y pagos de servicios), QRIS, EDC y mini ATM, con préstamos y BNPL mayorista vía prestamistas registrados en la OJK. Dice tener 8 millones de usuarios.
- **Lección**: el cuaderno solo vale si se vuelve caja registradora o agente de pagos, porque ahí está el ingreso.

---

## 4. Intentos previos (tabla de empresas)

| empresa | país | producto | usuario | modelo de ingresos | estructura legal | cifras (usuarios, cartera, mora) | estado actual (sep 2026) | lección | fuente |
|---|---|---|---|---|---|---|---|---|---|
| Tul | CO, MX, BR | marketplace de materiales + crédito a 30 a 60 días | ferreterías | comisión de marketplace; crédito | SAS con línea bancaria | más de 8.000 ferreterías (2024); US$181 M Serie B; mora no publicada | viva, se encogió: cerró Ecuador, despidos, dejó venta directa | sin inventario propio sobrevive; el crédito es de proveedor a 30 a 60 días, no de caja | Valora 2023; El Colombiano 2024; Forbes 2023 |
| Chiper | CO, MX, BR, CL | abastecimiento B2B en menos de 24 h | tiendas de barrio | margen mayorista | SAS; en Chile alianza con Copec | dice 110.000 tiendas (sin fecha); Chile más de 6.000 | no verificado; activa en Chile | depender de un aliado corporativo (Copec) fue su forma de sobrevivir en Chile | Copec Wind; TechCrunch 2021 |
| Frubana | CO, MX, BR | mayorista digital de perecederos + Frupay | restaurantes y tiendas | margen mayorista, pagos | SAS | US$271 M levantados; 80.000 clientes; 900 empleados | cerró (CO y MX feb 2024; BR jul 2025) | logística de bajo margen financiada con VC muere cuando sube la tasa | La República 2024; Forbes 2025; Concordia Simple |
| Treinta | CO y 18 países, EE. UU. | cuaderno digital, luego marketplace y datáfono | micronegocios | suscripción, comisiones | empresa YC W21 | "7 millones" de negocios; marketplace 36.000 registrados (2023) | pivotó a software con IA para pymes en EE. UU. y LatAm | el fiado digital no monetiza por sí solo | YC 2026; Fondo 2026 |
| Aflore | CO | crédito vía asesoras comunitarias | hogares y microempresarios de bajos ingresos | intereses | Aflore S.A.S. (no vigilada) con deuda de Accial | préstamo US$630; mora 5,7% (2022); US$17 M desembolsados (2020) | no verificado; web caída en sep 2026 | confianza prestada de un par reduce mora, pero escala y fondeo son el límite | Polymath 2022; LatamFintech 2020 |
| Juancho Te Presta | CO | crédito digital de $1 a 5 millones en 24 h | asalariados e independientes con ingreso de $1,5 M o más | intereses | SAS no vigilada, fondeada por inversionistas | 30.000 a 35.000 créditos; pasivos $39.755 M | en liquidación judicial (2026) | fondeo roto y posible captación ilegal; no atendía al usuario del gota a gota | La República 2025; El Colombiano 2026 |
| Addi | CO | BNPL en comercio | consumidores | intereses y comisión al comercio | compañía de financiamiento (2026) | 5,5 M clientes; mora 90 d 1,1% | viva y rentable | prestar en el punto de venta con el comercio como canal funciona; no es crédito a micronegocio | Tekios 2026 |
| Nu Colombia | CO | tarjeta, ahorro, préstamos | personas | intereses, intercambio | compañía de financiamiento (2024) | 5 M clientes; 1 M primera tarjeta | viva | tarjeta garantizada por depósito para quien no tiene historial | Mobile Time 2026 |
| Lulo Bank | CO | banco digital | personas, ahora empresas | margen | banco | cartera más de $450.000 M; mora ~5% (2025) | viva, en pérdida | un banco digital sin canal propio no llega al micronegocio | Valora 2025 |
| Movii | CO | billetera, remesas | no bancarizados | comisiones | SEDPE | más de 5 M usuarios (sin fecha) | viva; SEDPE en pérdida 2023 y 2024 | la billetera sin crédito ni ecosistema no rinde | resumen de buscador; Valora |
| Bold | CO | datáfono, cuenta, crédito que se paga con 10% de ventas | pequeños comercios | comisión por transacción, intereses | compañía de financiamiento (dato de prensa) | 500.000 comercios; más de $110.000 M prestados | viva, creciendo | el repago como porcentaje de la venta es el mecanismo colombiano más cercano al flujo diario, pero exige que la venta pase por su datáfono | Bloomberg Línea 2025; Valora 2025 |
| Wompi | CO | pasarela, QR, corresponsales | comercios | comisión | unidad de Bancolombia | $50 billones; 40.000 comercios | viva | infraestructura de pagos, no crédito | Colombia Fintech 2026 |
| Nequi | CO | billetera, crédito bajo monto, Crédito Negocios | personas y negocios | intereses, fianza, comisiones | compañía de financiamiento desde sep 2026 | 21,9 M activas; cartera más de $1,3 billones | viva, rentable desde 2025 | tiene la base y el dato, pero cobra cuota mensual con fianza | Cibest 4T25; reglamento Nequi |
| Daviplata | CO | billetera, nanocrédito, adelanto | personas y comercios | intereses | producto de Davivienda (estado societario 2026 no verificado) | 19,5 M usuarios; conversión de ofertas 8 a 10% | viva, en equilibrio operativo | la oferta preaprobada existe y la mayoría no la toma | Valora 2026 |
| Mercado Pago (crédito a comercios) | MX, BR, AR | capital de trabajo a vendedores y comercios con POS | comercios | intereses | entidades reguladas por país | crédito a comercios más de US$2.000 M; NPL 15 a 90 d de la cartera total [NO VERIFICADO] (el 8-K solo da 4,4% en tarjeta) | viva | el marketplace y el POS abaratan adquisición y cobranza | MELI 8-K 4T25 |
| BEES (AB InBev) y Bavaria | CO y global | pedidos B2B, promociones, "acceso a crédito" | tiendas | margen de producto; fintech | subsidiaria de AB InBev | 128.000 tiendas en programa 2026; préstamos a clientes US$58 M globales | viva | la cervecera no presta caja; da plazo y terceriza | AB InBev 20-F 2025; Bavaria 2025 y 2026 |
| Nutresa (Pideky) | CO | pedidos digitales | tiendas | margen de producto | parte de Grupo Nutresa | 132.000 clientes; más de COP 500.000 M | viva | canal digital con alcance comparable a fintechs, sin crédito conocido | Informe 2025 |
| Coca-Cola FEMSA (Juntos+) | MX, CO y otros | plataforma omnicanal y asesor de ventas | tiendas | margen de producto | FEMSA | sin cifras de crédito | viva | no se encontró crédito a tiendas | 20-F 2025 |
| Postobón | CO | no encontrado | tiendas | margen de producto | privada | no encontrado | n/d | hueco declarado | sala de prensa Postobón |
| Kueski | MX | préstamo personal y BNPL | personas | intereses altos | SOFOM ENR | más de 40 M préstamos; CAT ejemplo 153% | viva | la SOFOM ENR permite prestar sin licencia de captación | web Kueski 2026 |
| Tala | KE, MX, PH, IN y otros | microcrédito por app | personas y micronegocios | cargo único por préstamo | SOFOM ENR en MX | 15 M clientes; mora 5% en experimento | viva, no rentable según Forbes 2025; pivote a stablecoins | tickets de US$36 a 28 días funcionan, pero la rentabilidad global es esquiva | HBS 2025; tala.co |
| Konfío | MX | crédito a pymes, terminal | pymes | intereses | no verificado | US$706 M en deuda (2023) | viva, cerró Gestionix (2023) | abandonar el software para concentrarse en crédito | Contxto 2023 |
| Clip | MX | terminal, préstamos | comercios | comisión 2,99% + $1 | no verificado | no encontrado | viva | sin datos públicos de crédito | clip.mx |
| Stori | MX | tarjeta para sin historial | personas | intereses | SOFIPO | más de 5 M clientes | viva | consumo, no micronegocio | storicard.com |
| Yape | PE | billetera y micropréstamos | personas y pymes | pagos 45%, crédito 28% | producto de BCP | 16,7 M MAU; 5,6 M con crédito; S/1.800 M | viva, rentable por MAU | primero hábito diario, después crédito diminuto | Credicorp 2T26 |
| Stone | BR | POS y capital de trabajo | comercios | comisiones e intereses | StoneCo Ltd. (Nasdaq) | cartera R$3.225 M; costo de riesgo 21,9% | viva, con deterioro | cobrar del TPV no protege cuando cae la venta | Stone 1T26 |
| PagSeguro | BR | POS, banco | comercios y personas | comisiones, intereses | PagBank (banco) | 72% de cartera en nómina | viva | se replegó a crédito garantizado por nómina | PagSeguro 2T26 |
| M-Shwari | KE | ahorro y préstamo en M-Pesa | personas | cargo por préstamo | producto bancario sobre M-Pesa | toma 34% | viva | resiliencia ante choques, no crecimiento del negocio | NBER 2019 |
| Fuliza | KE | sobregiro en M-Pesa | personas y comercios | cargos diarios | producto bancario sobre M-Pesa | 7,9 M clientes; 45.150 comercios con sobregiro | viva | se paga solo con el siguiente ingreso; en comercios la mora es un problema | Safaricom AR 2025 |
| Kopo Kopo | KE | till de M-Pesa + adelanto de efectivo | comercios | comisiones e intereses | Digital Credit Provider (CBK) | hasta KES 15 M tras 60 días | viva; adquirida por Moniepoint (2023) y esa estrategia "stalled" | el dato de flujo no basta sin licencia de captación | TechCrunch 2023; TechCabal 2026 |
| Moniepoint | NG, KE | POS, banca, crédito | comercios y agentes | comisiones, intereses | banco de microfinanzas | 20 M usuarios; US$294.000 M procesados (2025) | viva, unicornio | agentes y POS primero, crédito después, y compra licencias | TechCabal 2026; moniepoint.com |
| Khatabook | IN | cuaderno digital, préstamos | comerciantes | software, servicios, préstamos | privada | 10 M MAU (FY22); pérdida Rs 111 crore | viva, con despidos y caída de ingresos | cuaderno sin modelo de ingresos | Entrackr 2022 y 2023 |
| OkCredit | IN | cuaderno digital | comerciantes | publicidad, suscripción | privada | pérdidas Rs 428,5 crore vs ingresos Rs 9 crore | viva según su web, con 35% de despidos (2022) | el caso más claro de que el fiado digital no monetiza | Entrackr 2023 |
| BukuWarung | ID | cuaderno, pagos, PPOB, EDC, préstamos | warungs | comisiones de pagos y agente | privada con prestamistas OJK | 8 M usuarios | viva, pivotó a agente de pagos | el cuaderno sobrevive si se vuelve punto de pago | bukuwarung.com |

---

## 5. Lo que casi nadie dice

1. **Las fintechs colombianas de micronegocios no murieron por mora sino por fondeo y logística.** Frubana, Tul y Juancho Te Presta documentan tasas altas, rondas que no llegaron (Almavest comprometió US$10 millones y desembolsó US$3 millones) y costos logísticos. Implicación: cualquier diseño que dependa de capital de terceros tiene que sobrevivir a un año de tasas altas. Un mecanismo que no inmovilice capital propio es más robusto que uno que "presta mejor".
2. **El repago automático sobre ventas se vuelve procíclico.** Stone: la cuota cae justo cuando la venta cae, y el saldo mayor a 90 días de comercios pasó de 5,1% a 8,6% en seis meses. El "adelanto sobre ventas con datáfono" (respuesta predecible 10) hereda el riesgo del negocio. Para un tendero con ingreso diario y sin ahorro, el día malo es justo el día en que necesita la plata.
3. **La distribuidora tiene el canal, la visita y el dato, y aun así no presta caja.** AB InBev tiene US$58 millones en préstamos a clientes contra US$4.261 millones de cuentas por cobrar comerciales, con 93,6% al día. Es decir, las tiendas pagan muy bien el plazo sobre producto (la mercancía se vende sola y el preventista vuelve la semana siguiente). Esto separa dos riesgos: el crédito atado a inventario que rota es bueno; el efectivo libre es otro negocio.
4. **El canal que más tiendas toca en Colombia no es una fintech.** Pideky (132.000 clientes, Nutresa), BEES y el programa de Bavaria (128.000 tiendas en 2026) igualan o superan la base activa que tuvieron Chiper o Treinta. La confianza del tendero ya está en manos del preventista, que visita con frecuencia fija (ver B8 para la frecuencia).
5. **Los productos que funcionan en la base se miden en días y en pesos, no en meses y en tasa.** Yape S/220 a menos de un mes; Tala US$36 a 28 días con cargo único de 15% y 5% de mora; Fuliza como sobregiro. En Colombia la oferta formal digital (Nequi, Nu) sigue con montos promedio de $2,3 a 2,4 millones pagados en cuotas mensuales (dato de confianza baja), lo que calza con el asalariado y no con el ingreso diario.
6. **Hay mucha oferta preaprobada que nadie toma.** Daviplata convierte solo 8 a 10% de 1 a 1,5 millones de ofertas mensuales. Si el problema fuera acceso, la conversión sería mayor. Pregunta de campo: ¿por qué un tendero con Daviplata o Nequi sigue usando el gota a gota?
7. **Los cuadernos de fiado tuvieron adopción masiva y ningún negocio.** OkCredit gastó Rs 297 por cada rupia facturada; Khatabook facturaba a su matriz; Treinta pivotó a EE. UU. El dato del fiado existe, pero nadie ha podido cobrarlo ni usarlo para prestar.
8. **Con el mejor dato de flujo del mundo, el sobregiro a comercios de M-Pesa llega a 2,5% de los comercios y tiene problemas de mora.** Safaricom habla de apoyar a sus socios de Fuliza Biashara con los NPL. Kopo Kopo, dueña de ese dato, tampoco le bastó a Moniepoint, que tuvo que comprar un banco para captar depósitos. El cuello de botella está en el fondeo y la licencia, no en el scoring.
9. **La fintech "anti gota a gota" de Medellín no atendía al usuario del gota a gota.** Juancho Te Presta pedía ingreso de $1,5 millones y cero moras, y se fondeó con inversionistas de $100 millones o más, lo que hoy se investiga como posible captación masiva. Hay dos lecciones: el segmento real queda por fuera de cualquier filtro formal, y fondearse con plata del público sin licencia es un riesgo penal (ver B7).
10. **El único modelo colombiano con mora baja publicada y usuario de bajos ingresos (Aflore, 5,7%) se basaba en una persona de la comunidad que responde socialmente,** no en datos. Su estado actual es desconocido y es el caso que más vale investigar en fuentes societarias.

---

## 6. Hipótesis que la evidencia refuta

- **"Con datos de ventas se resuelve el riesgo."** Stone tiene el TPV completo de sus comercios y reporta 21,9% de costo de riesgo (1T26). Safaricom tiene el flujo M-Pesa y habla de NPL en sobregiros a comercios.
- **"Con suficiente capital de riesgo se construye el canal B2B."** Frubana levantó US$271 millones y cerró; Tul sobrevivió cuando dejó de cargar inventario.
- **"Digitalizar el fiado genera historial y luego crédito."** OkCredit, Khatabook y Treinta tuvieron millones de usuarios y no convirtieron ese dato en un negocio de crédito.
- **"Las distribuidoras ya financian a las tiendas."** Financian producto con plazo, no caja: los préstamos a clientes de AB InBev son marginales (US$58 millones globales en 2025). No encontré programas de crédito de caja de Postobón, Nutresa ni Coca-Cola FEMSA.
- **"Los neobancos van a atender al micronegocio."** Nu Colombia no tiene producto para negocios; Lulo pierde plata y se va a empresas medianas y grandes; Nequi Crédito Negocios exige cuota mensual, fianza y seguro.
- **"Si la mora es baja, el producto funciona para este usuario."** Addi (1,1%) presta a consumidores bancarizables en comercios aliados. La mora baja se explica por la selección de clientes y no se puede trasladar al tendero.
- **"Cobrar como porcentaje de la venta alinea el crédito con el flujo diario y elimina el problema."** Alinea el ritmo, pero traslada el riesgo del negocio al prestamista (Stone) y exige que la venta pase por un POS o QR del prestamista (Bold), algo que no ocurre con un negocio en efectivo.

---

## 7. Preguntas abiertas (para campo) y cómo preguntarlas sin sesgo

1. **¿Qué plazo le dan hoy sus proveedores y cómo se comporta con cada uno?** "La última vez que le llegó el pedido de [cerveza, gaseosa, galletas], ¿cómo lo pagó? ¿El mismo día, a la semana? ¿Qué pasó la última vez que no tenía para pagarle?" (Busca: el plazo de la distribuidora como sustituto del gota a gota y la mora real con el preventista.)
2. **¿Le han ofrecido crédito Nequi, Daviplata, Bold o BEES y qué hizo?** "¿Le ha llegado alguna oferta de préstamo al celular? ¿Qué hizo con ella? ¿Por qué?" No pregunte "¿usaría un crédito de Nequi?".
3. **¿Cuánto de sus ventas pasa por QR o datáfono?** "Ayer, de cada diez clientes, ¿cuántos le pagaron con QR o tarjeta?" (Define si el repago sobre ventas digitales es viable en este segmento.)
4. **¿Qué pasó el último día malo?** "Cuénteme del último día que vendió mucho menos de lo normal. ¿De dónde sacó para pagar lo que debía ese día?" (Evalúa el riesgo procíclico del hallazgo 5.2.)
5. **¿Qué apps de tienda instaló y dejó de usar?** "¿Ha usado Chiper, Treinta, Tul, Pideky o BEES? ¿Cuál sigue usando y por qué dejó las otras?" (Explica por qué murieron las B2B desde el lado del usuario.)
6. **¿Alguien de su barrio le presta o le consigue crédito a otros tenderos?** "¿Conoce a alguien que le ayude a otros a conseguir plata o a hacer trámites de crédito? ¿Cómo funciona?" (Pregunta por el modelo Aflore sin nombrarlo.)
7. **¿Quién le visita con más frecuencia y a quién le ha pedido un favor de plata?** "¿Qué vendedores lo visitan cada semana? ¿Alguna vez uno de ellos le esperó un pago o le prestó?"
8. **Para el preventista (no para el tendero):** "¿Cuántas tiendas de su ruta le quedan debiendo? ¿Qué hace la empresa cuando una no paga?" (Mora real del crédito de proveedor.)

---

## 8. Bibliografía

**Colombia, startups B2B y fintechs**
- La República. "Frubana anunció cierre de operaciones en Colombia y México para centrarse en Brasil" (feb 2024). https://www.larepublica.co/empresas/frubana-cierra-en-colombia-3803987
- Forbes Colombia. "Frubana pone fin a sus operaciones y cierra su último mercado en Brasil" (14 ago 2025). https://forbes.co/2025/08/14/negocios/frubana-pone-fin-a-sus-operaciones/
- El Colombiano. "La historia detrás del cierre de Frubana y Merqueo". https://www.elcolombiano.com/negocios/historia-detras-cierre-frubana-y-merqueo-colombia-america-latina-LP29733329
- Concordia Simple. "Casos de insolvencias: Frubana". https://concordiasimple.com/quiebra-frubana-lecciones-emprendedores-latam/
- Valora Analitik. "Plataforma Tul anuncia recorte de personal y revisa estrategia en Colombia y México" (17 ene 2023). https://www.valoraanalitik.com/plataforma-tul-anuncia-recorte-de-personal-y-revisa-estrategia-en-colombia-y-mexico/
- Forbes Colombia. "La gran apuesta es ser rentables, tenemos caja para más de tres años: CEO de Tul" (8 mar 2023). https://forbes.co/emprendedores/la-gran-apuesta-es-ser-rentables-tenemos-caja-para-mas-de-tres-anos-ceo-de-tul
- El Colombiano. "La historia de Tul, el marketplace de los ferreteros que sobrevivió a la crisis" (28 feb 2024). https://www.elcolombiano.com/negocios/empresas/la-historia-de-tul-el-marketplace-de-los-ferreteros-que-sobrevivio-a-la-crisis-y-espera-vender-us-10-millones-mensuales-PN23843639
- TechCrunch. "Chiper aims to ease inventory burdens for Latin American corner stores" (18 nov 2021). https://techcrunch.com/2021/11/18/chiper-latin-america-corner-store/
- Copec Wind. "Chiper Copec". https://www.copecwind.cl/portafolio/chiper
- TechCrunch. "PayU doubles down on LatAm fintech... $46M investment in superapp Treinta" (20 abr 2022). https://techcrunch.com/2022/04/20/payu-doubles-down-on-latam-fintech-acquires-ding-and-leads-46m-investment-in-superapp-treinta-in-colombia/
- La República. "App Treinta lanzó datáfono" (14 jul 2022). https://www.larepublica.co/finanzas/app-treinta-lanzo-datafono-para-conectar-a-tenderos-y-aportar-a-la-inclusion-financiera-3403695
- Y Combinator. "Treinta". https://www.ycombinator.com/companies/treinta
- Fondo. "idealane Launches" (9 feb 2026). https://www.fondo.com/blog/idealane-launches
- Polymath Ventures. "Lessons from Aflore" (14 ene 2022). https://polymathv.substack.com/p/lessons-aflore-fintech-company-bringing-formal-financial-services-vulnerable-populations-latin-america
- LatamFintech. "Aflore consigue US$6,6 millones". https://www.latamfintech.co/articles/con-su-concepto-de-banqueras-comunitarias-en-colombia-aflore-consigue-us-6-6-millones-en-inversion-en-colombia
- La República. "Juancho Te Presta estaría lidiando con presuntas denuncias penales" (12 jul 2025). https://www.larepublica.co/finanzas/juancho-te-presta-recibe-denuncias-penales-por-presunta-captacion-masiva-de-dinero-4178752
- El Colombiano. "Fintech paisa que prometió acabar el gota a gota se quebró" (5 abr 2026). https://www.elcolombiano.com/medellin/investigacion-juancho-te-presta-esteban-saldarriaga-medellin-BF35215150
- ENTER.CO. "El riesgo fintech de Colombia" (18 jul 2026). https://www.enter.co/fintech/el-riesgo-fintech-de-colombia-como-la-cartera-vencida-esta-afectando-la-promesa-del-credito-digital/
- Tekios. "Addi lleva ocho trimestres rentables" (2 jul 2026). https://tekiosmag.com/2026/07/02/fitech-addi-lleva-ocho-trimestres-rentables-y-acaba-de-cerrar-su-serie-d-con-us86-millones/
- ABC Economía. "Addi se convierte en compañía de financiamiento" (9 abr 2026). https://abceconomia.co/2026/04/09/addi-se-convierte-en-compania-de-financiamiento/
- Bloomberg Línea. "Colombian startups Addi, Hunty confirm layoffs" (14 jun 2022). https://www.bloomberglinea.com/english/colombian-startups-addi-hunty-confirm-layoffs-as-merqueo-exits-mexico/
- Mobile Time. "Nu Colombia cumple cinco años" (26 may 2026). https://mobiletime.la/noticias/26/05/2026/nu-colombia-cumple-cinco-anos/
- LatamFintech. "Nu Colombia lanza tarjeta de crédito para personas sin historial". https://www.latamfintech.co/articles/nu-colombia-lanza-tarjeta-de-credito-para-personas-sin-historial-y-prestamos-digitales-en-colombia
- Valora Analitik. "Lulo Bank entrará al segmento empresarial" (7 jun 2025). https://www.valoraanalitik.com/lulo-bank-entrara-al-segmento-empresarial/
- Bloomberg Línea. "Bold suma 500.000 clientes" (31 mar 2025). https://www.bloomberglinea.com/latinoamerica/colombia/bold-el-neobanco-de-las-pymes-suma-500000-clientes-en-colombia-y-lanzara-tarjeta-de-credito-2/
- Yahoo Finanzas / Valora. "Bold revela estrategia 2025" (7 ene 2025). https://es-us.finanzas.yahoo.com/noticias/bold-posicion%C3%B3-dat%C3%A1fonos-revela-estrategia-230000433.html
- Colombia Fintech. "Wompi procesó transacciones por $50 billones en 2025" (16 ene 2026). https://colombiafintech.co/2026/01/16/wompi-proceso-transacciones-por-50-billones-en-2025-130-mas-que-en-2024/
- Grupo Cibest. Informe de resultados 4T25 (23 feb 2026). https://plataforma.valoraanalitik.com/informacion-relevante/grupo-cibest-s.a.-4t25-espaol.pdf
- La República. "Grupo Cibest, tercer trimestre de 2025" (6 nov 2025). https://www.larepublica.co/finanzas/resultados-empresariales-grupo-cibest-tercer-trimestre-de-2025-4264515
- Nequi. Reglamento Crédito Negocios. https://www.nequi.com.co/informacion-legal/prestamo-propulsor/reglamento-credito-negocios
- El Heraldo. "Así funciona el crédito de Nequi para comerciantes" (29 abr 2025). https://www.elheraldo.co/economia/2025/04/29/asi-funciona-el-credito-de-nequi-para-comerciante-prestan-hasta-10-millones-de-pesos/
- El Tiempo. "Intereses y embargos: lo que cobra Nequi si entra en mora con su préstamo Propulsor" (12 may 2025). https://www.eltiempo.com/economia/finanzas-personales/intereses-y-embargos-lo-que-cobra-nequi-si-entra-en-mora-con-su-prestamo-propulsor-3452875
- Ecosistema Startup. "Nequi expande cartera de crédito" (17 mar 2026). https://ecosistemastartup.com/nequi-expande-cartera-de-credito-con-analitica-avanzada/
- Infobae. "Nequi se separó de Bancolombia" (5 ago 2026). https://www.infobae.com/colombia/2026/08/05/nequi-se-separo-de-bancolombia-estos-son-los-nuevos-canales-donde-los-clientes-podran-realizar-sus-transacciones/
- Yahoo / Valora. "Entrevista: la apuesta por el crédito de DaviPlata" (17 mar 2026). https://es-us.noticias.yahoo.com/entrevista-apuesta-cr%C3%A9dito-daviplata-evoluci%C3%B3n-170000401.html

**Distribuidoras**
- AB InBev. Form 20-F 2025 (3 mar 2026). https://www.sec.gov/Archives/edgar/data/1668717/000119312526088105/d65314d20f.htm
- Coca-Cola FEMSA. Form 20-F 2025 (16 abr 2026). https://www.sec.gov/Archives/edgar/data/910631/000162828026025313/kof-20251231.htm
- Bavaria. "Bavaria firma alianza con CAF" (1 ago 2025). https://www.bavaria.co/noticia/bavaria-firma-alianza-con-caf-para-impulsar-inclusion-financiera-digitalizacion
- Bavaria. "Bavaria invierte más de $100.000 millones al año en el desarrollo de sus clientes" (5 ago 2025). https://www.bavaria.co/noticia/bavaria-invierte-mas-100000-millones-ano-desarrollo-sus-clientes-lanza-nueva-0
- Bavaria. "Con inversión de $115.000 millones Bavaria impulsa el desarrollo de sus clientes" (9 jun 2026). https://www.bavaria.co/noticia/con-inversion-115000-millones-bavaria-impulsa-desarrollo-sus-clientes-convierte
- Grupo Nutresa. Informe de sostenibilidad 2025 (resumen). https://data.gruponutresa.com/informes/2025/Informe-de-sostenibilidad-resumen-grupo-nutresa.pdf
- Postobón. Sala de prensa. https://www.postobon.com/sala-prensa/comunicados-2026

**LatAm**
- MercadoLibre. 8-K, Ex. 99.1, resultados 4T25 (24 feb 2026). https://www.sec.gov/Archives/edgar/data/1099590/000109959026000003/meli-20260224xex991.htm
- StoneCo. Earnings release 1T26 (14 may 2026). https://www.sec.gov/Archives/edgar/data/1745431/000207097926000265/earningsrelease1q26.htm
- StoneCo. Estados financieros intermedios a 30 jun 2026. https://www.sec.gov/Archives/edgar/data/1745431/000207097926000274/stoneco_06x2026.htm
- PagSeguro Digital. 6-K, estados financieros a 30 jun 2026. https://www.sec.gov/Archives/edgar/data/1712807/000155485526001791/MainDocument.htm
- Credicorp. Earnings release 2T26 (6-K, 17 ago 2026). https://www.sec.gov/Archives/edgar/data/1001290/000114036126033379/ef20080305_ex99-1.htm
- Kueski. Sitio web (consultado 2026). https://www.kueski.com/
- Stori. Sitio web. https://www.storicard.com/
- Clip. Sitio web. https://clip.mx/
- Contxto. "Konfío shuts down Gestionix" (2023). https://contxto.com/en/news/konfio-shuts-down-gestionix-to-strengthen-focus-on-financial-services-for-smes/
- Bloomberg Línea. "Konfío capta crédito por MXN 4.100 millones de Goldman Sachs y Gramercy" (2 mar 2023). https://www.bloomberglinea.com/2023/03/02/fintech-konfio-capta-credito-por-mxn4100-millones-de-goldman-sachs-y-gramercy/

**África**
- Safaricom. Annual Report and Financial Statements 2025. https://www.safaricom.co.ke/annualreport_2025/wp-content/uploads/2025/08/safaricom-annual-report.pdf
- CBK, KNBS, FSD Kenya. 2024 FinAccess Household Survey. https://finaccess.knbs.or.ke/reports-and-datasets
- Bharadwaj, Jack y Suri. "Fintech and Household Resilience to Shocks: Evidence from Digital Loans in Kenya", NBER w25604 (2019). https://www.nber.org/papers/w25604
- HBS Working Knowledge. "How $40 Loans Lifted Lives in Kenya" (24 abr 2025). https://www.library.hbs.edu/working-knowledge/how-40-dollar-loans-lifted-lives-in-kenya
- Tala. Sitio y sala de prensa. https://tala.co/ y https://tala.co/press/
- Forbes. "Unprofitable Microlending Fintech Makes Big Bet On Global Expansion" (25 sep 2025, no se pudo abrir). https://www.forbes.com/sites/jeffkauflin/2025/09/25/unprofitable-microlending-fintech-makes-big-bet-on-global-expansion/
- Kopo Kopo. Sitio web. https://kopokopo.co.ke/
- TechCrunch. "Moniepoint cleared to acquire Kenyan fintech Kopo Kopo" (22 ago 2023). https://techcrunch.com/2023/08/22/moniepoint-cleared-to-acquire-kenyan-fintech-kopo-kopo/
- TechCabal. "Nigeria's Moniepoint enters Kenya with 78% stake in Sumac Microfinance" (26 mar 2026). https://techcabal.com/2026/03/26/nigerias-moniepoint-enters-kenya-with-78-stake-in-sumac-microfinance/
- Moniepoint. Crédito. https://moniepoint.com/credit

**Asia**
- Entrackr. "OkCredit lost Rs 428 Cr to earn Rs 9 Cr since incorporation" (4 dic 2023). https://entrackr.com/2023/12/okcredit-lost-rs-428-cr-to-earn-rs-9-cr-since-incorporation/
- Entrackr. "Five-year-old OkCredit spends Rs 297 to earn a rupee in FY22" (21 dic 2022). https://entrackr.com/2022/12/five-year-old-okcredit-spends-rs-297-to-earn-a-rupee-in-fy22/
- Entrackr. "Khatabook ends FY22 with 4x growth in revenue and Rs 111 Cr loss" (23 nov 2022). https://entrackr.com/2022/11/khatabook-ends-fy22-with-4x-growth-in-revenue-and-rs-111-cr-loss/
- Entrackr. "Peak XV-backed Khatabook lays off over 40 employees" (1 sep 2023). https://entrackr.com/2023/09/peak-xv-backed-khatabook-lays-off-over-40-employees/
- Inc42. "Khatabook". https://inc42.com/company/khatabook/
- OkCredit. Sitio web. https://okcredit.in/
- BukuWarung. Sitio web. https://bukuwarung.com/

---

## Verificación

Revisión de hechos del 26 de septiembre de 2026 sobre 19 afirmaciones, elegidas entre las cifras de la tabla de datos clave, las marcadas como "alta" y las que sostienen la propuesta. Se abrió cada fuente citada (filings de la SEC descargados con curl, PDF extraídos con pypdf y páginas web con WebFetch). El presupuesto de WebSearch ya estaba agotado, así que no hubo búsquedas de fuentes alternativas.

| claim | resultado | nota |
|---|---|---|
| StoneCo 1T26: costo de riesgo 21,9%; NPL 15 a 90 días 4,97%; NPL > 90 días 6,98%; tasa mensual 3,3% | confirmado | Earnings release 1T26 en la SEC. Cartera total R$3.224,9 millones, de ella R$2.860,9 millones a comercios (89%). Se precisó la explicación: la empresa atribuye el deterioro a tendencias de mora del mercado que debilitaron el TPV minorista, a casos de su mesa dedicada y a cosechas nuevas, no solo a la caída del TPV. |
| Mercado Pago 4T25: crédito a comercios más de US$2.000 millones; cartera US$12.500 millones (+90%); NIMAL 23,3% | confirmado | 8-K Ex. 99.1: "our merchant credit portfolio now exceeds $2bn"; "grew 90% YoY in Q4'25 to reach $12.5bn"; "NIMAL of 23.3%". Citas textuales sobre flexibilidad de precio y comercios long-tail en México también confirmadas. |
| Mercado Pago 4T25: NPL 15 a 90 días de 6,7% | no verificado | El documento citado no trae esa cifra para la cartera total; solo da 4,4% para la cartera de tarjeta de crédito. Marcado en el texto y en la tabla de empresas. |
| Yape 2T26: 16,7 millones de MAU; cartera S/1.800 millones; 5,6 millones de clientes con crédito; tickets S/220, S/850 y S/3.300; ingreso S/11,1 vs gasto S/6,0 por MAU; 45% pagos y 28% crédito | confirmado | Earnings release 2T26 de Credicorp. Los 5,6 millones son clientes alcanzados por desembolsos acumulados, no clientes con saldo vigente. |
| PagBank jun 2026: cartera R$4.623 millones; nómina R$3.318; tarjeta R$898; préstamos R$408 | confirmado | 6-K, nota 9 (valores netos de pérdida esperada). 72% y 9% son cálculos correctos. |
| AB InBev 2025: préstamos a clientes US$58 millones vs cuentas por cobrar comerciales US$4.261 millones, 93,6% al día | confirmado | 20-F 2025, nota 19: préstamos a clientes 6 no corrientes + 52 corrientes; de 4.261, 3.990 sin deterioro ni vencimiento (93,6%, cálculo). |
| AB InBev: BEES como "a purpose-built global B2B platform" operada por una subsidiaria 100% | corregido | Esa cita no aparece en el 20-F descargado. Se reemplazó por la cita textual encontrada: "our business-to-business platform, BEES, which provides e-commerce and fintech solutions to retailers and services to our wholesalers". Mención de Emprendedores en Colombia, Perú y Ecuador confirmada. |
| Fuliza FY2025: 7,9 millones de clientes; ingreso KShs 4.100 millones; 45.150 comercios con sobregiro; 1,8 millones de comercios | confirmado | Safaricom Annual Report 2025. La URL hoy devuelve 403; se verificó sobre el texto del mismo PDF descargado antes en esta sesión. La cita sobre "Fuliza Biashara partners in managing non-performing loans" también aparece. |
| FinAccess 2024: 16,6% de deudores no pagó nada (10,7% en 2021); 82,1% de negocios reinvierte ingresos | confirmado | Copia local del 2024 FinAccess Household Survey (CBK, KNBS, FSD Kenya, dic 2024). La URL citada es la página índice de informes, no el PDF directo. |
| M-Shwari: toma 34%; 6,3 pp menos probabilidad de dejar de cubrir gastos | confirmado | Resumen de NBER w25604 (Bharadwaj, Jack y Suri, 2019). |
| Tala (estudio): US$36, ~28 días, cargo ~15%, mora 5%, ingreso +21% | confirmado | HBS Working Knowledge, 24 abr 2025; autores Kang, Chen, Even-Tov y Wittenberg-Moerman. La mora se define como préstamo impago un año después del vencimiento. Se mantiene "media" porque es resumen del paper. |
| Nequi dic 2025: 27,4 millones de cuentas, 21,9 millones activas | confirmado | Informe 4T25 de Grupo Cibest, p. 1. |
| Bold: 500.000 clientes; más de $110.000 millones en crédito; ~700 vendedores | confirmado | Bloomberg Línea, 31 mar 2025. El artículo habla de "prácticamente 700 personas" en calle. El 10% de cada venta viene de otra fuente (Valora vía Yahoo) que no se reabrió. |
| Frubana: US$271 millones levantados; última entrega en Brasil 30 jul 2025; salida de CO y MX feb 2024 | confirmado | Forbes Colombia, 14 ago 2025. |
| Juancho Te Presta: pasivos $39.755 millones a 31 ago 2024; reorganización; Almavest US$10 millones comprometidos y US$3 millones desembolsados | confirmado | La República, 12 jul 2025; reorganización del 5 dic 2024. La liquidación judicial de 2026 no se reverificó. |
| OkCredit: pérdidas acumuladas Rs 428,5 crore vs ingresos ~Rs 9 crore | confirmado | Entrackr, 4 dic 2023, acumulado FY18 a FY23. |
| Addi: 5,5 millones de clientes; 76.000 comercios; mora 90 días 1,1%; Serie D US$86 millones | confirmado | Tekios, 2 jul 2026. |
| Kueski: CAT promedio 153,31% (2 mar 2026); más de 40 millones de préstamos; rango de montos | corregido | CAT y número de préstamos confirmados en kueski.com. El monto mínimo que muestra la web es $60 MXN, no $200; se corrigió. |
| Nutresa Pideky: 132.000 clientes; más de COP 500.000 millones en ventas (2025) | no verificado | El PDF del informe devuelve 403 a curl y a WebFetch y no se pudo buscar otra fuente. Se bajó la confianza a media y se marcó en el resumen y en la tabla. |
