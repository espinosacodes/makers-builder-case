# B10. Puntos ciegos y ángulos contrarian

Estado: completo

Frente B10 del prompt maestro. Supuesto de partida: las 10 respuestas predecibles de docs/03-analisis-del-caso.md ya se intentaron y fallaron. Aquí se busca lo que casi nadie mira. Fecha de corte: 26 de septiembre de 2026.

Nota de método: buena parte de las cifras colombianas salen de leer directamente los anexos en Excel del DANE (EMICRON 2023 y 2024), los boletines sectoriales EMICRON (tiendas 2024, ambulantes 2025) y los microdatos de la Encuesta de Demanda de Inclusión Financiera 2022 de Banca de las Oportunidades. Cuando una cifra es cálculo propio sobre microdatos se dice explícitamente. El presupuesto de búsqueda web de la sesión estaba agotado, así que la investigación nueva se hizo con descargas directas, lectura de PDF y búsquedas por otro buscador.

## 1. Resumen ejecutivo

1. **El usuario típico del gota a gota no es el tendero, es el vendedor ambulante.** De los ambulantes que pidieron crédito, 61,8% fue a gota a gota (2025); de las tiendas y panaderías, 11,3% (2024); el promedio de micronegocios, 22,9% (2024). El tendero "de 15 años detrás del mostrador" pide sobre todo a bancos y cooperativas (69,9%). Diseñar para el tendero puede ser diseñar para el segmento equivocado; el tendero sirve más como nodo que como usuario.
2. **El precio casi no aparece como razón.** Solo 6,5% de los micronegocios que no pidieron crédito citó intereses altos; 42,5% citó miedo a endeudarse (2024). En ambulantes: 2,3% frente a 44,6%. En una encuesta a 100 comerciantes de plazas de Bogotá, 60,9% no supo elegir entre la misma tasa expresada como 50% efectivo anual y 3,44% mensual.
3. **La deuda paga deuda.** En Perú, la primera razón para pedir a un prestamista es "pagar otras deudas" (36% en 2024). En Colombia, 21,6% de quienes tenían crédito formal lo usó para pagar otros créditos (cálculo propio, 2022). Pagarle la deuda al prestamista no rompe el ciclo: se vuelve a deber en seis semanas (India y Filipinas).
4. **Hogar y negocio son la misma caja.** 36,5% del crédito que consiguen los micronegocios va total o parcialmente a gastos personales, y 74,7% de los que ahorran usa el ahorro en el hogar (2024). Un producto "solo para capital de trabajo" deja por fuera la mitad de la necesidad.
5. **No es falta de productos de ahorro: "no alcanza".** 95,9% de los micronegocios que no ahorraron dijo que no le alcanzó; 0,2% dijo que no le ofrecieron productos. El que ahorra, ahorra en la casa (61,1%). Las natilleras son marginales (3,6%), y el ahorro en clubes es de 5,4% de los adultos en Colombia frente a 24,9% en Ghana y 33,9% en Kenia (en Brasil es 5,6%, parecido a Colombia).
6. **La visita diaria es un servicio por el que la gente paga.** En Ghana el ahorrador le paga al recolector susu un día de depósitos por mes; en India el pigmy deposit a domicilio existe desde 1928; en Filipinas la recolección a domicilio subió el ahorro 25%. En Pakistán, ahorro y crédito con cuota fija se demandan como el mismo producto.
7. **El tendero ya es prestamista, y ese crédito se está contrayendo.** 36% de las tiendas mantiene el fiado (2026); 54,1% de los tenderos dijo que el fiado disminuyó (dic 2024; la prensa lo reportó como "el fiado cayó 54%", que no es lo que dice la encuesta). Al mismo tiempo, 20,91% de los tenderos ahora tiene que pagar de contado al proveedor (2026).
8. **Hay actores con cobro y confianza instalados que nadie usa para esto.** Empresas de servicios públicos (7,0% de quienes piden crédito; Brilla, que reporta más de 3,6 millones de usuarios beneficiados desde 2007, cobra en la factura del gas), almacenes (13,6%), funerarias y cementerios (31,4%, el principal canal por el que se compran seguros) y corresponsales (31,5%). Pero Brilla Negocios exige ser dueño del predio y titular de la factura: excluye justo a quien arrienda y al ambulante.
9. **Mecanismos de afuera que no han llegado:** sobregiro en el momento del pago (Fuliza: 7,9 millones de clientes en Kenia), crédito escalonado para vendedores ambulantes que se desbloquea al pagar y premia pagos digitales (PM SVANidhi, India), pago diario con bloqueo del activo (M-KOPA, 3 millones de clientes activos).
10. **La deuda tiene calendario, pero Colombia no lo mide.** No se encontró ninguna serie pública colombiana de demanda de crédito informal por mes. Solo hay señales: 12,5% de los micronegocios que ahorra lo hace para surtir en temporada alta, 15,3% del crédito formal de los adultos va a matrículas, y en México los casos de apps "montadeudas" suben 33% en enero. Es una pregunta para campo.

## 2. Tabla de datos clave

| Dato | Cifra | País | Año del dato | Fuente | URL | Confianza |
|---|---|---|---|---|---|---|
| Micronegocios que pidieron crédito en el año anterior | 14,2% (702.293 de 4.946.334) | Colombia | 2023 (encuesta 2024) | DANE, EMICRON 2024, anexo, cuadro H.2 | https://www.dane.gov.co/files/operaciones/EMICRON/anex-EMICRON-2024.xlsx | alta |
| De los que pidieron crédito, cuántos acudieron a gota a gota | 22,9% total; 27,5% cabeceras; 9,8% rural | Colombia | 2023 (encuesta 2024) | DANE, EMICRON 2024, anexo, cuadro H.4 | https://www.dane.gov.co/files/operaciones/EMICRON/anex-EMICRON-2024.xlsx | alta |
| Mismo dato un año antes | 23,3% (201.965 micronegocios) | Colombia | 2022 (encuesta 2023) | DANE, EMICRON 2023, anexo, cuadro H.4 | https://www.dane.gov.co/files/operaciones/EMICRON/anex-EMICRON-2023.xlsx | alta |
| Vendedores ambulantes que pidieron crédito: fuente gota a gota | 61,8% (22,5% institución regulada; 12,8% familia; 1,8% proveedores) | Colombia, 24 ciudades | 2024 (encuesta 2025) | DANE, Boletín técnico EMICRON Vendedores ambulantes 2025, p. 26 | https://www.dane.gov.co/files/operaciones/EMICRON/bol-EMICRONVendedoresAmbulantes-2025.pdf | alta |
| Panaderías y tiendas de barrio que pidieron crédito: fuente gota a gota | 11,3% (69,9% institución regulada; 5,6% proveedores) | Colombia | 2024 | DANE, Boletín técnico EMICRON Panaderías y tiendas de barrio 2020 a 2024, p. 25 | https://www.dane.gov.co/files/operaciones/EMICRON/bol-EMICRON-PanaderiasTiendasBarrio-2024.pdf | alta |
| Tiendas y panaderías que no pidieron crédito | 81,0% | Colombia | 2024 | DANE, mismo boletín, p. 24 | https://www.dane.gov.co/files/operaciones/EMICRON/bol-EMICRON-PanaderiasTiendasBarrio-2024.pdf | alta |
| Tenderos que dicen necesitar crédito "en estos momentos" | 61,2% (n=464) | Colombia | dic 2024 | Fenalco, Encuesta Fenaltiendas 2024, p. 36 | https://drive.google.com/file/d/1YlAOFTsXqTx0uRc7Nx3yyCo0IDbH4Y7h/view | alta (gráfico leído) |
| Uso que le darían los tenderos al crédito | Surtido 63,03%; modernización 25,35%; pagar otras deudas 5,99%; activos 5,63% | Colombia | dic 2024 | Fenalco, Encuesta Fenaltiendas 2024, p. 37 | https://drive.google.com/file/d/1YlAOFTsXqTx0uRc7Nx3yyCo0IDbH4Y7h/view | alta |
| Tenderos que dicen que el fiado disminuyó | 54,1% sí; 45,9% no | Colombia | dic 2024 | Fenalco, Encuesta Fenaltiendas 2024, p. 35 | https://drive.google.com/file/d/1YlAOFTsXqTx0uRc7Nx3yyCo0IDbH4Y7h/view | alta |
| Tiendas que mantienen el fiado | 36% | Colombia | 2026 | P&G (María Carolina Pacheco), citado por RedExpertos (28 ago 2026) | https://redexpertos.co/nueve-de-cada-diez-hogares-compran-en-la-tienda-de-barrio-el-corazon-del-consumo-colombiano/ | media |
| Tenderos que aumentaron el fiado para retener clientes / lo redujeron / no fían | 20,45% / 25,9% / 26,8% | Colombia | 2026 | Encuesta Fenaltiendas 2026, citada por Semana (12 may 2026) | https://www.semana.com/economia/macroeconomia/articulo/tiendas-de-barrio-solo-sobreviviendo-el-cliente-tiene-menos-plata-y-el-alza-del-salario-minimo-que-se-hizo/202642/ | media |
| Tenderos con más restricciones de proveedores / exigencia de pago de contado | 39,55% / 20,91% | Colombia | 2026 | Fenalco, "La mayoría de tiendas de barrio operan en modo supervivencia" | https://www.fenalco.com.co/blog/noticias-10/la-mayoria-de-tiendas-de-barrio-operan-en-modo-supervivencia-ante-caida-de-ingresos-y-presion-de-costos-en-2026-fenalco-8830 | media |
| Tenderos que gastan más de 10% del ingreso mensual en arriendo y servicios | 60,45% | Colombia | 2026 | Fenalco, misma nota | https://www.fenalco.com.co/blog/noticias-10/la-mayoria-de-tiendas-de-barrio-operan-en-modo-supervivencia-ante-caida-de-ingresos-y-presion-de-costos-en-2026-fenalco-8830 | media |
| Razón principal para no pedir crédito: miedo a las deudas | 42,5% (tasas altas: 6,5%) | Colombia | 2023 (encuesta 2024) | DANE, EMICRON 2024, anexo, cuadro H.3 | https://www.dane.gov.co/files/operaciones/EMICRON/anex-EMICRON-2024.xlsx | alta |
| Ambulantes: razón para no pedir crédito | 44,6% miedo a deudas; 29,4% no cumple requisitos; 2,3% intereses altos | Colombia, 24 ciudades | 2025 | DANE, Boletín Vendedores ambulantes 2025, p. 25 | https://www.dane.gov.co/files/operaciones/EMICRON/bol-EMICRONVendedoresAmbulantes-2025.pdf | alta |
| Tiendas: razón para no pedir crédito | 45,7% miedo; 8,6% intereses altos | Colombia | 2024 | DANE, Boletín Panaderías y tiendas 2024, p. 24 | https://www.dane.gov.co/files/operaciones/EMICRON/bol-EMICRON-PanaderiasTiendasBarrio-2024.pdf | alta |
| Uso del crédito obtenido: gastos personales o mixto | 21,0% solo personales + 15,5% negocio y personales = 36,5% | Colombia | 2023 (encuesta 2024) | DANE, EMICRON 2024, anexo, cuadro H.6 | https://www.dane.gov.co/files/operaciones/EMICRON/anex-EMICRON-2024.xlsx | alta |
| Crédito usado para mejorar condiciones de créditos vigentes / emergencias del negocio | 2,9% / 9,9% | Colombia | 2023 (encuesta 2024) | DANE, EMICRON 2024, anexo, cuadro H.6A | https://www.dane.gov.co/files/operaciones/EMICRON/anex-EMICRON-2024.xlsx | alta |
| Micronegocios que ahorraron | 18,1% | Colombia | 2023 (encuesta 2024) | DANE, EMICRON 2024, anexo, cuadro H.7 | https://www.dane.gov.co/files/operaciones/EMICRON/anex-EMICRON-2024.xlsx | alta |
| Razón para no ahorrar | "No le alcanzó" 95,9%; no confía en entidades 0,2%; no le han ofrecido productos 0,2% | Colombia | 2023 (encuesta 2024) | DANE, EMICRON 2024, anexo, cuadro H.7B | https://www.dane.gov.co/files/operaciones/EMICRON/anex-EMICRON-2024.xlsx | alta |
| Uso del ahorro | Hogar 74,7%; cubrir el negocio en días malos 43,8%; surtir para temporada alta 12,5%; pagar deudas del negocio 9,2% | Colombia | 2023 (encuesta 2024) | DANE, EMICRON 2024, anexo, cuadro H.7A | https://www.dane.gov.co/files/operaciones/EMICRON/anex-EMICRON-2024.xlsx | alta |
| Dónde ahorran los que ahorran | Vivienda 61,1%; institución financiera 32,6%; cadena o natillera 3,6% | Colombia | 2023 (encuesta 2024) | DANE, EMICRON 2024, anexo, cuadro H.8 | https://www.dane.gov.co/files/operaciones/EMICRON/anex-EMICRON-2024.xlsx | alta |
| Micronegocios sin registros contables | 65,55% sin registros; 29,46% en cuaderno u hoja | Colombia | 2023 | Banca de las Oportunidades, "Panorama de la exclusión financiera y el crédito informal en los micronegocios colombianos" (2025), p. 2 | https://www.bancadelasoportunidades.gov.co/sites/default/files/2025-09/Panorama%20de%20la%20Exclusi%C3%B3n%20Financiera%20y%20el%20Cr%C3%A9dito%20Informal%20en%20los%20Micronegocios%20Colombianos.pdf | alta |
| Adultos que pidieron crédito: a fuentes informales / almacenes / servicios públicos | 29% / 13,6% / 7,0% | Colombia | 2022 | Banca de las Oportunidades, Encuesta de Demanda de Inclusión Financiera 2022, p. 10 | https://www.bancadelasoportunidades.gov.co/sites/default/files/2022-12/Encuesta%20de%20demanda%202022%20VF.pdf | alta |
| Adultos que pidieron crédito al "fiado/tendero" / al gota a gota | 6,5% / 5,1% (ponderados) | Colombia | 2022 | Cálculo propio sobre microdatos de la Encuesta de Demanda 2022 (pregunta 303, factor Fexp_Reg_Rur; el cálculo reproduce el 13,6% de almacenes y el 6,9% de servicios públicos del informe) | https://www.bancadelasoportunidades.gov.co/sites/default/files/2022-10/Encuesta_demanda_2022_microdatos.xlsx | media (cálculo propio) |
| Último crédito formal aprobado usado para "pagar otros créditos o préstamos" | 21,6% (ponderado; n=1.246) | Colombia | 2022 | Cálculo propio, microdatos Encuesta de Demanda 2022 (pregunta 307b) | https://www.bancadelasoportunidades.gov.co/sites/default/files/2022-10/Encuesta_demanda_2022_microdatos.xlsx | media (cálculo propio) |
| Último crédito formal usado para matrículas o gastos de educación | 15,3% (ponderado) | Colombia | 2022 | Cálculo propio, misma fuente (pregunta 307h) | https://www.bancadelasoportunidades.gov.co/sites/default/files/2022-10/Encuesta_demanda_2022_microdatos.xlsx | media (cálculo propio) |
| Adultos que no piden crédito porque no quieren tener deudas | 65,4% (alto costo: 27,8%) | Colombia | 2022 | Banca de las Oportunidades, Encuesta de Demanda 2022, p. 10 | https://www.bancadelasoportunidades.gov.co/sites/default/files/2022-12/Encuesta%20de%20demanda%202022%20VF.pdf | alta |
| Canal para adquirir seguros: funerarias y cementerios / servicios públicos | 31,4% / 11,2% | Colombia | 2022 | Banca de las Oportunidades, Encuesta de Demanda 2022, cap. 4 | https://www.bancadelasoportunidades.gov.co/sites/default/files/2022-12/Encuesta%20de%20demanda%202022%20VF.pdf | alta |
| Lugar más usado para operaciones financieras: corresponsales | 31,5% | Colombia | 2022 | Banca de las Oportunidades, Encuesta de Demanda 2022, p. 10 | https://www.bancadelasoportunidades.gov.co/sites/default/files/2022-12/Encuesta%20de%20demanda%202022%20VF.pdf | alta |
| Créditos formales con cuota mensual | 87,2% | Colombia | 2022 | Banca de las Oportunidades, Encuesta de Demanda 2022, p. 58 | https://www.bancadelasoportunidades.gov.co/sites/default/files/2022-12/Encuesta%20de%20demanda%202022%20VF.pdf | alta |
| Comerciantes de plazas de mercado de Bogotá que han usado gota a gota / usan Nequi o Daviplata | 92% / 86% (n=100) | Colombia (Bogotá) | oct 2023 | López Rivera, Manrique y Kalmanovitz, "Los préstamos gota a gota en Bogotá", Apuntes (Univ. del Pacífico), 2026 | https://revistas.up.edu.pe/index.php/apuntes/article/view/2604 | alta (muestra pequeña) |
| Misma encuesta: elección entre "50% efectivo anual" y "3,44% efectivo mensual" (casi la misma tasa) | 60,9% "ninguno de los dos"; 15,2% y 10,9% eligen una; 13% no sabe | Colombia (Bogotá) | oct 2023 | Misma fuente, figura 6 | https://revistas.up.edu.pe/index.php/apuntes/article/view/2604 | alta (muestra pequeña) |
| Misma encuesta: dispuestos a pagar más por un mes extra de plazo | La mitad de los encuestados | Colombia (Bogotá) | oct 2023 | Misma fuente, figura 4 | https://revistas.up.edu.pe/index.php/apuntes/article/view/2604 | alta (muestra pequeña) |
| Motivo principal para pedir a un prestamista: pagar otras deudas | 36% (2024); 39% (2022) | Perú (5 ciudades, 1.203 prestatarios) | 2024 | IPE por encargo de Asbanc, "El mercado de crédito informal en el Perú", p. 10 | https://ipe.org.pe/wp-content/uploads/2024/10/IPE_El_mercado_de_credito_informal_en_el_Peru.pdf | alta (financiado por gremio bancario) |
| Prestatarios informales con más de un crédito en 12 meses; promedio de créditos en el año | 55%; 2,7 créditos | Perú | 2023 a 2024 | IPE, mismo informe, p. 7 | https://ipe.org.pe/wp-content/uploads/2024/10/IPE_El_mercado_de_credito_informal_en_el_Peru.pdf | alta |
| Prestatarios informales que valoran las condiciones como favorables; que volverían al prestamista | 45%; 38% | Perú | 2024 | IPE, mismo informe, p. 20 | https://ipe.org.pe/wp-content/uploads/2024/10/IPE_El_mercado_de_credito_informal_en_el_Peru.pdf | alta |
| Adultos que ahorraron en club de ahorro o con persona fuera de la familia | Colombia 5,4%; México 12,6%; Perú 6,9%; Brasil 5,6%; Ghana 24,9%; Kenia 33,9% (corregido: el 24,2% que se atribuía a Brasil es de Botsuana) | Varios | 2024 | Banco Mundial, The Little Data Book on Financial Inclusion 2025 (Global Findex), p. 44 impresa (p. 53 del PDF) para Colombia | https://thedocs.worldbank.org/en/doc/be6615202d1f08a25855c8ac2d615122-0050012025/related/Little-Data-Book-2025-Web.pdf | alta |
| Adultos que pidieron prestado (cualquier fuente) vs formalmente | 46,3% vs 13,5% | Colombia | 2024 | Banco Mundial, Little Data Book 2025, p. 44 impresa (p. 53 del PDF) | https://thedocs.worldbank.org/en/doc/be6615202d1f08a25855c8ac2d615122-0050012025/related/Little-Data-Book-2025-Web.pdf | alta |
| Brilla (Promigas): crédito cobrado en la factura del gas | "Más de 3,6 millones de usuarios" beneficiados (acumulado desde 2007, no clientes activos); cartera $2,11 billones (cierre 2023) | Colombia | 2023 | Valora Analitik (30 ene 2024) | https://www.valoraanalitik.com/brilla-se-consolida-en-colombia-y-apuesta-por-nueva-linea-de-credito/ | media |
| Brilla: créditos en 9 meses, estratos 1 a 3, crédito promedio | 388.352 créditos por $994.898 millones (ene a sep 2024); 94% estratos 1 a 3; promedio $2,5 millones | Colombia | 2024 | Notas Económicas (dic 2024) | https://www.notaseconomicas.com/2024/12/promigas-celebra-50-anos-con-emision-de-bonos-para-los-hogares-brilla/ | media |
| Brilla Negocios: requisitos | Personas con actividad formal o informal que sean "dueños de los predios, titulares de la factura"; capital de trabajo a 9 meses; activos a 60 meses; cobro en la factura del gas | Colombia (Caribe) | consultado sep 2026 | Gases del Caribe, página Brilla Negocios | https://www.brillagascaribe.com/brilla-negocios | alta |
| Fuliza (sobregiro en el momento del pago en M-PESA) | 7,9 millones de clientes; transacciones por KShs 1,0 billón (trillion); ingreso KShs 4.100 millones | Kenia | año fiscal abr 2024 a mar 2025 | Safaricom, Annual Report 2025 | https://www.safaricom.co.ke/annualreport_2025/wp-content/uploads/2025/08/safaricom-annual-report.pdf | alta |
| Pochi La Biashara (cobro para comerciantes informales en M-PESA) | 1,1 millones de comerciantes | Kenia | año fiscal 2025 | Safaricom, Annual Report 2025 | https://www.safaricom.co.ke/annualreport_2025/wp-content/uploads/2025/08/safaricom-annual-report.pdf | alta |
| PM SVANidhi (India): crédito escalonado para vendedores ambulantes | ₹10.000 a 1 año; al pagar, hasta ₹20.000 y luego ₹50.000; subsidio de interés de 7% anual si paga a tiempo; cashback de ₹50 a ₹100 al mes por pagos digitales | India | desde jun 2020 | Wikipedia, "Pradhan Mantri SVANidhi Scheme" (fuente oficial MoHUA bloqueada desde Colombia) | https://en.wikipedia.org/wiki/Pradhan_Mantri_SVANidhi_Scheme | media |
| Pigmy deposit: recolección diaria a domicilio por agente del banco | Desde 1928 (Syndicate Bank); depósitos diarios desde 5 rupias | India | histórico | Wikipedia, "Pigmy Deposit Scheme" | https://en.wikipedia.org/wiki/Pigmy_Deposit_Scheme | media |
| M-KOPA: pago diario con bloqueo del dispositivo | 3 millones de clientes activos; más de USD 2.000 millones en crédito | Kenia, Uganda, Nigeria, Ghana, Sudáfrica | 2025 | M-KOPA, página de impacto | https://m-kopa.com/impact/ | media (fuente de la empresa) |
| Pagar la deuda del prestamista no saca de la trampa | La mayoría volvió a endeudarse en 6 semanas; a 1 o 2 años, igual que el control | India y Filipinas | 2007 y 2010 | Karlan, Mullainathan y Roth, "Debt Traps?", AER: Insights 1(1), 2019 | https://www.aeaweb.org/articles?id=10.1257/aeri.20180030 | alta |
| La demanda de crédito responde más al plazo que a la tasa | Tamaño del préstamo mucho más sensible al plazo que a la tasa | Sudáfrica | experimento publicado 2008 | Karlan y Zinman, AER 98(3), 2008 | https://www.povertyactionlab.org/sites/default/files/research-paper/208%20Credit%20Elasticities%20June%2008.pdf | alta |
| Una foto en la publicidad equivale a bajar la tasa | Foto de mujer atractiva = aumento de demanda similar a bajar 25% la tasa | Sudáfrica | publicado 2010 | Bertrand, Karlan, Mullainathan, Shafir y Zinman, QJE 2010 | https://isps.yale.edu/research/publications/isps10-006 | media (resumen de ISPS) |
| Elasticidad precio de largo plazo (contrapeso) | -1,9 a 29 meses (de -1,1 año 1 a -2,9 año 3) | México (Compartamos) | publicado 2019 | Karlan y Zinman, Review of Economic Studies 86(4), 2019 | https://www.nber.org/papers/w19106 | media |
| Recolector de depósitos a domicilio | +188 pesos de ahorro (+25%); 38 de 137 aceptaron, 20 lo usaron regularmente; 4 pesos por visita | Filipinas | 2004 | Ashraf, Karlan y Yin, "Deposit Collectors" | https://navaashraf.com/wp-content/uploads/2016/07/depositcollectors_aeap.pdf | alta |
| Susu: el ahorrador paga un día de depósitos por mes | Comisión de un día de cada ciclo mensual (tasa implícita negativa) | Ghana | 2009 a 2010 (IPA); 2025 (prensa) | IPA, "Savings Account Labeling for Susu Customers in Ghana" | https://poverty-action.org/study/savings-account-labeling-susu-customers-ghana | alta |
| Crédito y ahorro, "dos caras de la misma rupia" | 53% aceptó ambos contratos; 2/3 consistentes con demanda de suma global y dificultad para ahorrar | Pakistán | publicado 2018 | Afzal, d'Adda, Fafchamps, Quinn y Said, Economic Journal 2018 (resumen de la RES) | https://res.org.uk/mediabriefing/saving-and-borrowing-poor-households-in-pakistan-see-no-distinction-among-microfinance-products/ | media |
| Pago mensual vs semanal | 51% menos probable sentirse "preocupado, tenso o ansioso" (n=200) | India | publicado 2012 | Field, Pande, Papp y Park, PLoS ONE 2012 | https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0045679 | alta |
| Liquidez adelantada: pagan deudas primero y producen más | +7% de producción | India | publicado 2021 | Kaur, Mullainathan, Oh y Schilbach, NBER w28338 | https://www.nber.org/papers/w28338 | alta |
| Crédito digital: varios préstamos a la vez | 14% pagaba varios préstamos simultáneos; 16% pidió a familia para pagar; cerca de la mitad se atrasó | Kenia | 2017 | CGAP (15 mar 2018) | https://www.cgap.org/blog/kenyas-digital-credit-revolution-five-years-on | media |
| Apps "montadeudas" en la cuesta de enero | +33% de casos en enero | México (CDMX) | ene 2025 | Consejo Ciudadano para la Seguridad y Justicia, citado por Infobae (14 ene 2025) | https://www.infobae.com/mexico/2025/01/14/prestamos-fraudulentos-montadeudas-crecen-33-por-ciento-en-enero-alerta-consejo-ciudadano/ | media |

## 3. Hallazgos por tema (puntos ciegos)

Ranking: primero lo que tiene evidencia más fuerte y es menos obvio. Para cada punto: evidencia, fuente y cómo cambia el diseño.

### PC1. El usuario del gota a gota es el ambulante, no el tendero (evidencia fuerte; muy poco obvio)

- Evidencia: de los vendedores ambulantes que pidieron crédito, 61,8% fue a gota a gota (24 ciudades, 2025). De las panaderías y tiendas de barrio, 11,3% (2024). Del total de micronegocios, 22,9% (2024) y 23,3% (2023). En tiendas, 69,9% fue a instituciones reguladas. Fuentes: boletines DANE EMICRON Vendedores ambulantes 2025 (p. 26) y Panaderías y tiendas de barrio 2024 (p. 25); anexos EMICRON 2023 y 2024, cuadro H.4.
- En plazas de mercado de Bogotá (encuesta de 100 comerciantes, oct 2023), 92% había usado gota a gota (López Rivera et al., Apuntes 2026). Ese es el mismo perfil: puesto, no local.
- Contradicción en fuente oficial: el boletín técnico EMICRON 2024 (p. 32) dice que en centros poblados y rural disperso "la mayor fuente de financiamiento" son los gota a gota "con el 77,0%". El anexo en Excel (cuadro H.4) muestra que ese 77,0% corresponde a instituciones reguladas y que el gota a gota rural es 9,8% (27,5% en cabeceras). El texto del boletín cruzó las columnas. Quien cite "77% rural gota a gota" está citando un error. El gota a gota es un fenómeno urbano.
- Cómo cambia el diseño: el caso pinta a alguien "detrás de un mostrador". Ese perfil tiene acceso relativamente bueno al crédito regulado y usa poco el gota a gota. Donde el informal domina es en el ambulante urbano (sin local fijo, sin factura de servicios a su nombre, ingreso diario). Opción de diseño: el ambulante como usuario y el tendero como nodo físico (punto fijo, con efectivo, que ve al ambulante a diario y ya fía).

### PC2. El precio no es la variable de decisión (evidencia fuerte; contraria al discurso público)

- Colombia: solo 6,5% de los micronegocios que no pidieron crédito citó intereses altos; 42,5% citó miedo a las deudas (EMICRON 2024, H.3). Ambulantes: 2,3% frente a 44,6% (2025). Tiendas: 8,6% frente a 45,7% (2024). Adultos: 65,4% no quiere tener deudas frente a 27,8% alto costo (Encuesta de Demanda 2022).
- Comerciantes de plazas en Bogotá (2023): ante dos préstamos con casi la misma tasa, una expresada como 50% efectivo anual y otra como 3,44% efectivo mensual, 60,9% respondió "ninguno de los dos" y 13% no supo. La mitad pagaría más por un mes extra de plazo. 56% quiere el desembolso en máximo una semana (Apuntes 2026).
- Perú (2024): 55% de los prestatarios informales dice que prefiere el informal por la rapidez; 45% califica las condiciones como favorables pese a las amenazas (IPE 2024).
- Experimentos: en Sudáfrica el monto pedido responde mucho más al plazo que a la tasa (Karlan y Zinman 2008); una foto en la publicidad movió la demanda tanto como bajar la tasa 25% (Bertrand et al. 2010).
- Matiz: con Compartamos en México la demanda sí es elástica a la tasa en el largo plazo (-1,9 a 29 meses; Karlan y Zinman 2019). El precio importa en volumen, pero no explica quién entra.
- Cómo cambia el diseño: competir "por tasa" ataca la variable equivocada. Las variables que mueven la decisión son velocidad, plazo y el miedo a quedar "endeudado". Un mecanismo que no se sienta como deuda (o que tenga salida sin castigo en un día malo) y que exprese el costo en pesos por día ataca las causas declaradas.

### PC3. Deudas que pagan deudas (evidencia fuerte en la región; poco medida en Colombia)

- Perú: "pagar otras deudas" es el motivo principal para pedir a un prestamista (36% en 2024, 39% en 2022); al menos un tercio de ellos debía a entidades financieras o estaba reportado (IPE 2024, p. 10). 55% pidió más de un crédito informal en el último año, 2,7 en promedio.
- Colombia: 21,6% de los adultos con crédito formal aprobado lo usó para pagar otros créditos (cálculo propio, Encuesta de Demanda 2022). En micronegocios: 2,9% usó el crédito para mejorar condiciones de créditos vigentes y 9,2% de los que ahorraron usó el ahorro para pagar deudas del negocio (EMICRON 2024). En tenderos que piden crédito de hasta $1 millón, 6,25% lo quiere para pagar otras deudas (Fenaltiendas 2024) [NO VERIFICADO; el gráfico general de la p. 37 da 5,99% para "pagar otras deudas"].
- Un trabajo de grado de la Universidad Militar Nueva Granada cita un estudio del CEDE (Uniandes, 2010) en que madres usan el gota a gota sobre todo para pagar servicios públicos y surtir negocios del hogar, y menciona casos de "cubrir un préstamo gota a gota con otro". Original del CEDE no consultado (confianza baja). URL del trabajo: https://repository.umng.edu.co/server/api/core/bitstreams/c5aa8b9b-3e28-461d-9c91-a09d1c6737cc/content
- Kenia (crédito digital, 2017): 14% pagaba varios préstamos de distintos proveedores a la vez; 16% pidió a familia para pagar (CGAP 2018).
- Karlan, Mullainathan y Roth (2019): pagarle la deuda al vendedor de mercado no rompe el ciclo; la mayoría vuelve a deber en seis semanas y a los dos años no hay diferencia con el control.
- Cómo cambia el diseño: un préstamo "más barato para sustituir el gota a gota" probablemente se sume en vez de reemplazar, porque la necesidad de liquidez vuelve. La unidad de diseño no es el préstamo: es la semana de caja y lo que pasa el día que la venta no alcanza para la cuota.

### PC4. Hogar y negocio son la misma caja (evidencia fuerte)

- 36,5% de los micronegocios que obtuvieron crédito lo usó total o parcialmente en gastos personales (EMICRON 2024, H.6; en 2023 era 39,2%). 74,7% de los que ahorraron usó el ahorro en gastos del hogar y 43,8% para cubrir el negocio cuando no alcanzan los ingresos (H.7A). 65,55% no lleva registros y 29,46% usa cuaderno u hoja (Panorama BDO, datos 2023).
- Perú (2024): después de pagar deudas (36%), los motivos son montar o invertir en negocio (22%), salud (19%) y educación (17%) (IPE 2024).
- Cómo cambia el diseño: un producto "para capital de trabajo" que exige uso productivo excluye la mitad de la necesidad. Si la necesidad dominante es suavizar el hogar (matrícula, arriendo, servicios, salud), el ancla puede ser esos pagos y no el inventario.

### PC5. El ahorro no falla por acceso sino porque "no alcanza"; las natilleras son marginales en Colombia (evidencia fuerte)

- 81,9% de los micronegocios no ahorró; de ellos, 95,9% dijo "no le alcanzó", 0,2% "no confía en las entidades" y 0,2% "no le han ofrecido productos" (EMICRON 2024, H.7 y H.7B).
- De los que ahorran: 61,1% en la vivienda, 32,6% en una entidad, 3,6% en cadena o natillera (H.8).
- Global Findex (datos 2024): 5,4% de los adultos colombianos ahorró en un club de ahorro o con persona fuera de la familia, frente a 24,9% en Ghana y 33,9% en Kenia. Brasil (5,6%), México (12,6%) y Perú (6,9%) están en el rango bajo, así que el ahorro en clubes es poco común en toda la región, no solo en Colombia.
- 86% de los comerciantes de plazas en Bogotá usa Nequi o Daviplata y aun así 92% ha usado gota a gota (Apuntes 2026). Tener cuenta no es el cuello de botella.
- Cómo cambia el diseño: "digitalizar la natillera" parte de una institución pequeña en este segmento, y "primero ahorra, después te presto" choca con que 96% dice que no le alcanza. El ahorro real es efectivo en la casa, en sumas pequeñas, que se gasta en el hogar. El mecanismo tiene que capturar la suma en el momento en que existe (al cierre del día) y no pedir un saldo previo.

### PC6. La gente paga por ahorrar y la visita del cobrador es un servicio (evidencia fuerte fuera de LatAm; casi inexistente en Colombia)

- Ghana: el recolector susu pasa a diario y al final del mes devuelve lo ahorrado quedándose con un día de depósitos (tasa implícita negativa). IPA lo documenta con 2.100 clientes de 5 sucursales bancarias (2009 a 2010), donde los bancos ya pagan a los recolectores por comisión.
- India: el pigmy deposit (Syndicate Bank, 1928) recoge depósitos diarios a domicilio con un agente del banco, pensado para jornaleros y pequeños comerciantes.
- Filipinas (2004): recolección a domicilio a 4 pesos por visita subió el ahorro 188 pesos (+25%) y bajó levemente el endeudamiento; adopción baja (38 de 137 aceptaron, 20 lo usaron con regularidad) y más alta entre quienes vivían lejos del banco (Ashraf, Karlan y Yin).
- Kenia: vendedoras de mercado usaron cuentas con tasa negativa (cargos de retiro) y aumentaron inversión; 41% del grupo tratado las usó (Dupas y Robinson 2013, resumen de Harvard Growth Lab).
- Pakistán: 53% aceptó tanto contratos de crédito como de ahorro con cuota fija; la distinción es "en gran parte ilusoria" (Afzal et al. 2018).
- Cómo cambia el diseño: el gota a gota vende junto con la plata un cobrador que pasa todos los días. Esa visita tiene valor aunque no haya préstamo. Un mecanismo de cuota diaria que primero construye una suma y luego la adelanta puede cobrarse como servicio sin ser crédito, lo cual toca la restricción de "no soy entidad vigilada". Riesgo documentado: la adopción voluntaria de la recolección es baja si no viene atada a una necesidad inmediata.

### PC7. Actores del ecosistema con cobro y confianza instalados (evidencia media a fuerte)

- Empresas de servicios públicos: 7,0% de los adultos que pidieron crédito en 2022 lo pidió a una de ellas; 11,2% compró seguros por ese canal. Brilla (Promigas) presta con base en el buen pago de la factura y cobra en la misma factura: más de 3,6 millones de usuarios beneficiados desde 2007 (acumulado), cartera de $2,11 billones (2023), 94% estratos 1 a 3.
- Límite clave: Brilla Negocios presta a actividades "formales o informales", pero solo a "dueños de los predios, titulares de la factura". El que arrienda el local y el ambulante quedan fuera por diseño. Ese es exactamente el segmento con más gota a gota (PC1).
- Almacenes: 13,6% de quienes pidieron crédito (2022). Funerarias y cementerios: principal canal de adquisición de seguros (31,4% en la encuesta). Corresponsales: el lugar más usado para operaciones financieras (31,5%).
- Proveedores: solo 2,7% de los micronegocios que pidieron crédito fue a proveedores (2024); 5,6% en tiendas; 1,8% en ambulantes. Y el crédito de proveedor se está cerrando: 20,91% de los tenderos ahora debe pagar de contado y 11,82% tiene plazos más cortos (Fenalco 2026).
- Cómo cambia el diseño: la infraestructura de cobro recurrente que ya confían los hogares de bajos ingresos (factura, cuota de funeraria, almacén) existe. Pero está amarrada a la titularidad de un inmueble. Un mecanismo que "preste" esa relación de confianza a quien no es titular (por ejemplo, el tendero titular como ancla del ambulante que le compra) es un hueco que nadie cubre.

### PC8. El tendero ya es prestamista, y su crédito se está encogiendo (evidencia media)

- 6,5% de los adultos que pidieron crédito en 2022 lo pidió al "fiado/tendero", más que al gota a gota en esa misma encuesta (5,1%) (cálculo propio ponderado).
- 36% de las tiendas mantiene el fiado (P&G, 2026). En diciembre de 2024, 54,1% de los tenderos dijo que el fiado disminuyó (Fenaltiendas, n=464). La prensa (por ejemplo Infobae, 26 feb 2025) lo reportó como "el fiado cayó 54%", que no es lo que mide la pregunta.
- En 2026, 20,45% de los tenderos aumentó el fiado para retener clientes, 25,9% lo redujo y 26,8% no fía (Fenaltiendas 2026, vía Semana). Al mismo tiempo, 39,55% enfrenta más restricciones de proveedores y 20,91% debe pagar de contado.
- Cómo cambia el diseño: el tendero está en sándwich: fía a clientes sin saber cuándo le pagan y el proveedor le exige contado. Parte de su hueco de caja es plata prestada a vecinos. Un mecanismo que convierta el fiado del tendero en algo cobrable (o que le financie ese fiado) ataca un hueco real y usa una relación de crédito que ya funciona sin papeles.

### PC9. La deuda tiene calendario, pero Colombia no lo mide (evidencia débil; hueco de datos)

- No se encontró ninguna serie pública colombiana de demanda de crédito informal por mes (ni DANE, ni Banca de las Oportunidades, ni Banco de la República). Esto en sí es un hallazgo: nadie sabe cuándo se origina la deuda.
- Señales indirectas: 12,5% de los micronegocios que ahorra lo hace para "surtir el negocio para temporadas altas" (EMICRON 2024, H.7A); 15,3% del crédito formal de los adultos se usó en matrículas o educación (cálculo propio, 2022); 17% de los prestatarios informales en Perú pidió para educación (2024); 60,45% de los tenderos gasta más de 10% de su ingreso mensual en arriendo y servicios (2026), un pago con fecha fija.
- México: los casos de apps de préstamo extorsivas crecen 33% en la cuesta de enero (Consejo Ciudadano, vía Infobae, ene 2025). Una nota de Costa Rica (Monumental, ene 2026) dice lo mismo sin cifra.
- Cómo cambia el diseño: si la deuda se origina en fechas predecibles (surtido de diciembre, matrícula de enero y febrero, arriendo del día 1), un mecanismo que acumule antes de la fecha puede reemplazar el crédito en esos picos. Es la pregunta de campo más valiosa (sección 7).

### PC10. Mecanismos de otros países que no han llegado a LatAm (evidencia media)

- Fuliza (Kenia): sobregiro que se activa en el momento de pagar con M-PESA cuando el saldo no alcanza (la forma exacta de repago no se verificó en la fuente leída). 7,9 millones de clientes y transacciones por KShs 1,0 billón (trillion) en el año fiscal 2025 (Safaricom). Lo nuevo no es el crédito sino el momento: el préstamo ocurre dentro del pago, no en una solicitud.
- Pochi La Biashara (Kenia): cuenta de cobro para comerciantes informales dentro de M-PESA, sin registro mercantil: 1,1 millones de comerciantes (2025).
- PM SVANidhi (India, desde 2020): crédito para vendedores ambulantes identificados por la alcaldía: ₹10.000 a un año; si paga, sube a ₹20.000 y luego a ₹50.000; subsidio de interés de 7% si paga a tiempo y cashback mensual por pagos digitales. Combina tres cosas que en Colombia están separadas: identificación del ambulante por la autoridad local, escalera de montos y premio por usar pagos digitales.
- M-KOPA (África): el cliente paga diario por un teléfono o panel solar y el aparato se bloquea si no paga; la garantía es el uso del activo, no el cobrador. 3 millones de clientes activos.
- Pigmy deposit (India) y susu (Ghana): ver PC6.
- Cómo cambia el diseño: Bre-B y los pagos por QR en Colombia permiten, en principio, un "Fuliza del surtido" (el faltante se cubre en el momento de pagar al proveedor y se descuenta de las ventas del día). No encontré evidencia de que exista en Colombia (búsqueda limitada).

### PC11. El costo oculto de la deuda es cognitivo y termina en el negocio (evidencia fuerte, académica)

- Trabajadores en India que recibieron liquidez antes pagaron deudas de inmediato y luego produjeron 7% más con menos errores (Kaur et al. 2021).
- Pago mensual en vez de semanal: 51% menos probabilidad de sentirse ansioso por el pago (Field, Pande, Papp y Park 2012). Un periodo de gracia de dos meses aumentó inversión y ganancias, aunque subió el default (Field et al., AER 2013).
- Microempresas en Kenia pierden 5 a 8% de sus ganancias por no tener sencillo para dar vueltas (Beaman, Magruder y Robinson 2014).
- Cómo cambia el diseño: el frente de valor puede ser bajar la ansiedad de la cuota (flexibilidad ligada a ventas) más que bajar la tasa.

## 4. Intentos previos

| Actor | Qué hizo | Resultado medido | Por qué funcionó o falló | Fuente |
|---|---|---|---|---|
| Karlan, Mullainathan y Roth (investigadores) | Pagaron la deuda con prestamistas de vendedores de mercado (Chennai 2007; Cagayan de Oro 2007 y 2010) y dieron capacitación financiera | La mayoría volvió a endeudarse en 6 semanas; a 1 o 2 años sin diferencia con el control | Choques de ingreso y consumo, sesgo al presente, falta de un medio de ahorro; la capacitación no alcanza | https://www.aeaweb.org/articles?id=10.1257/aeri.20180030 |
| Promigas (Brilla) | Crédito no bancario desde 2007 a usuarios de gas, aprobado por buen pago y cobrado en la factura; línea Brilla Negocios | Más de 3,6 millones de usuarios beneficiados (acumulado) y cartera de $2,11 billones (2023); 94% estratos 1 a 3; "bajos niveles de cartera en mora" [NO VERIFICADO: la frase no aparece en la nota de Valora Analitik citada y no hay cifra pública de mora] | Usa una relación de pago ya existente y un canal de cobro que el cliente no quiere perder; excluye a quien no es titular del predio | https://www.valoraanalitik.com/brilla-se-consolida-en-colombia-y-apuesta-por-nueva-linea-de-credito/ ; https://www.brillagascaribe.com/brilla-negocios |
| Green Bank of Caraga (Filipinas) | Recolección de depósitos a domicilio por 4 pesos por visita | +25% de saldo; aceptación 28% (38/137); uso regular 15% (20/137) | Reduce costos de transacción y da compromiso; baja demanda voluntaria | https://navaashraf.com/wp-content/uploads/2016/07/depositcollectors_aeap.pdf |
| Ghana Co-operative Susu Collectors Association | Digitalización de la recolección susu (apps y recibos digitales) | No se encontraron cifras de adopción | El valor del susu está en su inserción comunitaria; formalizar agresivamente puede destruirlo (columna de la Ghana Fintech and Payments Association, oct 2025) | https://www.myjoyonline.com/beyond-mobile-money-the-quiet-struggle-to-modernize-ghanas-ancient-susu-system/ |
| Crédito digital en Kenia (M-Shwari, KCB M-Pesa y otros) | Préstamos instantáneos por celular | 27% de adultos con al menos un préstamo digital (2017); cerca de la mitad se atrasó; 13% admitió default; 14% con varios préstamos simultáneos | Velocidad sin calce con flujo de caja: deuda que paga deuda | https://www.cgap.org/blog/kenyas-digital-credit-revolution-five-years-on |
| Safaricom (Fuliza) | Sobregiro en el momento del pago con M-PESA | 7,9 millones de clientes (FY2025); 48% del crecimiento del ingreso de crédito | El crédito vive dentro del pago; no requiere solicitud ni cobrador | https://www.safaricom.co.ke/annualreport_2025/wp-content/uploads/2025/08/safaricom-annual-report.pdf |
| Gobierno de India (PM SVANidhi) | Crédito escalonado para ambulantes con subsidio por pago a tiempo y cashback digital | No se encontró cifra de desembolsos ni de mora en fuente accesible (portal oficial bloqueado desde Colombia) | Usa a la alcaldía para identificar al ambulante y la escalera de montos como incentivo | https://en.wikipedia.org/wiki/Pradhan_Mantri_SVANidhi_Scheme |
| Alcaldía de Bogotá | Crédito contra el gota a gota: $50.000 a $500.000 a 30 días, con ingreso mínimo de $1.044.000 | No se encontraron resultados publicados | El requisito de ingreso mensual demostrable excluye al ambulante de ingreso diario | https://www.infobae.com/colombia/2024/08/28/el-20-de-los-negocios-que-estan-empezando-en-bogota-acuden-a-prestamistas-informarles-o-gota-a-gota/ |

## 5. Lo que casi nadie dice

1. **El DANE publicó un dato mal y se puede estar citando.** El boletín EMICRON 2024 dice que en lo rural el gota a gota es "la mayor fuente" con 77,0%; el anexo muestra que es 9,8% y que el 77,0% es de instituciones reguladas. Importa porque empuja a diseñar para el campo cuando el gota a gota es urbano (27,5% en cabeceras).
2. **El tendero no es el cliente del gota a gota; el ambulante sí.** 11,3% frente a 61,8%. Importa porque el enunciado del caso sugiere el perfil equivocado; el tendero es más útil como nodo, ancla o garante que como usuario.
3. **El gota a gota compite con el fiado, no con el banco.** En la encuesta de demanda 2022, más adultos pidieron crédito al tendero (6,5%) que al gota a gota (5,1%). El tendero es un prestamista sin interés que se está quedando sin caja (54,1% dice que el fiado bajó; 20,91% paga de contado al proveedor). Importa porque su crisis de liquidez es un punto de entrada con incentivos alineados.
4. **La tasa casi no pesa, el "miedo a la deuda" sí.** 6,5% vs 42,5%, y 60,9% no puede comparar dos formas de expresar la misma tasa. Importa porque el mecanismo debe venderse en pesos por día y con salida en días malos, no con una tasa menor.
5. **La deuda paga deuda y el préstamo barato se suma, no sustituye.** 36% en Perú; 21,6% del crédito formal en Colombia; seis semanas para volver a deber en India y Filipinas. Importa porque una propuesta de "refinanciar el gota a gota" tiene evidencia en contra.
6. **La titularidad del inmueble es la frontera invisible.** Brilla presta a informales, pero solo si son dueños del predio y titulares de la factura. Importa porque todos los canales de cobro "confiables" (factura, predial, servicios) dejan por fuera al arrendatario y al ambulante, que es donde vive el gota a gota.
7. **La gente paga por que alguien le recoja la plata.** Susu, pigmy y la cuota diaria del gota a gota comparten el mismo servicio: una visita que obliga. Importa porque ese servicio se puede cobrar sin prestar (y sin licencia de crédito).
8. **Ahorro y crédito son el mismo producto para el usuario.** Pakistán (53% acepta ambos) y el uso del ahorro en Colombia (74,7% al hogar). Importa porque la frontera legal entre "prestar" y "ahorrar" no existe en la cabeza del usuario, y el diseño puede elegir el lado legalmente más fácil.
9. **Nadie mide cuándo nace la deuda.** No hay serie mensual de crédito informal en Colombia. Importa porque quien la tenga (aunque sea con 30 entrevistas) tiene un diagnóstico que nadie más tiene.
10. **Bancarizado no significa protegido.** 86% de comerciantes de plazas usa Nequi o Daviplata y 92% ha usado gota a gota. Importa porque "abrir cuentas" ya está hecho y no resolvió nada.

## 6. Hipótesis que la evidencia refuta

- **"El gota a gota prospera porque el banco es caro."** Refutada como explicación principal: solo 6,5% de los micronegocios que no piden crédito cita intereses; 42,5% cita miedo a endeudarse (EMICRON 2024).
- **"El usuario del gota a gota es el tendero."** Refutada: 11,3% de las tiendas que pidieron crédito fue a gota a gota, frente a 61,8% de los ambulantes.
- **"El gota a gota domina en lo rural."** Refutada: 9,8% rural frente a 27,5% en cabeceras (EMICRON 2024, anexo). La cifra de 77% es un error de columnas del boletín.
- **"Si le pagamos o refinanciamos la deuda, sale del ciclo."** Refutada: se vuelve a deber en seis semanas (Karlan, Mullainathan y Roth 2019); 36% de los préstamos informales en Perú son para pagar otras deudas.
- **"Falta acceso a productos de ahorro."** Refutada para micronegocios: 95,9% no ahorra porque no le alcanza; 0,2% porque no le ofrecieron productos.
- **"Digitalizar natilleras llega a mucha gente."** Débil: 3,6% de los micronegocios que ahorran usa cadenas y 5,4% de los adultos usa clubes de ahorro (frente a 24,9% en Ghana y 33,9% en Kenia; Brasil está en 5,6%).
- **"El crédito de proveedor es la salida natural."** Débil en Colombia: 2,7% de los micronegocios que piden crédito va a proveedores, y los proveedores están exigiendo contado a 20,91% de los tenderos (2026).
- **"El crédito del micronegocio es para el negocio."** Refutada en parte: 36,5% va a gastos personales total o parcialmente.
- **"El problema es la bancarización."** Refutada: 86% de los comerciantes de plazas en Bogotá usa billeteras digitales y 92% ha usado gota a gota.
- **"El fiado cayó 54%."** Mal leída en prensa: la encuesta dice que 54,1% de los tenderos percibe que el fiado disminuyó, no que el volumen cayera 54%.

## 7. Preguntas abiertas para campo

Todas en pasado concreto (estilo The Mom Test). Nunca preguntar "¿usaría?". Para gota a gota, preguntar en tercera persona.

1. **Calendario de la deuda.** "Piense en la última vez que le faltó plata para algo del negocio o de la casa. ¿Qué mes era? ¿Qué había que pagar ese día?" Luego: "¿Y la vez anterior?" Registrar mes y motivo (arriendo, matrícula, surtido de diciembre, servicio, proveedor). No preguntar "¿en qué meses le falta plata?", porque invita a generalizar.
2. **Deuda que paga deuda.** "La última vez que alguien del barrio pidió un préstamo diario, ¿para qué era la plata?" y "¿Conoce a alguien que tenga dos al tiempo?" En tercera persona para reducir vergüenza.
3. **Ambulante vs tendero.** Entrevistar ambos perfiles por separado. A ambulantes: "¿Dónde guarda la plata al final del día? ¿Quién le presta cuando no alcanza para surtir?" A tenderos: "¿A cuántos ambulantes o vecinos les vende fiado? ¿Cuánto tiene fiado hoy en el cuaderno? ¿Me muestra la última página?"
4. **El fiado del tendero.** "¿Cuánto le quedaron debiendo el mes pasado y cuánto le pagaron?" "¿Qué hace cuando el proveedor viene y no le alcanza?" (Hecho pasado, no opinión.)
5. **Precio vs forma.** Mostrar dos préstamos iguales expresados distinto (pesos por día vs tasa) y observar cuál entiende, sin preguntar cuál prefiere en abstracto. Mejor aún: "¿Cuánto paga al día hoy? ¿Cuánto recibió?" y calcular nosotros.
6. **Valor de la visita.** "¿Alguien pasa a cobrarle o a recogerle plata? ¿Cada cuánto? ¿Qué pasa el día que no tiene?" Buscar si hay natilleras o "cadenas" con recolector.
7. **Titularidad.** "¿A nombre de quién llega el recibo de la luz o el gas de donde trabaja?" Mide cuántos quedan fuera de los canales tipo Brilla.
8. **Hogar vs negocio.** "Del último préstamo o del último ahorro, ¿en qué se fue la plata, peso por peso?" Sin sugerir categorías.
9. **Días malos.** "¿Cuándo fue el último día que no alcanzó para la cuota? ¿Qué hizo?" Revela la política real de mora del informal y lo que el usuario valora de ella.

## 8. Bibliografía

Fuentes primarias colombianas
- DANE. Encuesta de Micronegocios EMICRON 2024, anexos estadísticos (cuadros H.2 a H.8). https://www.dane.gov.co/files/operaciones/EMICRON/anex-EMICRON-2024.xlsx
- DANE. EMICRON 2023, anexos estadísticos. https://www.dane.gov.co/files/operaciones/EMICRON/anex-EMICRON-2023.xlsx
- DANE. Boletín técnico EMICRON 2024. https://www.dane.gov.co/files/operaciones/EMICRON/bol-EMICRON-2024.pdf
- DANE. Boletín técnico EMICRON Panaderías y tiendas de barrio 2020 a 2024 (8 may 2026). https://www.dane.gov.co/files/operaciones/EMICRON/bol-EMICRON-PanaderiasTiendasBarrio-2024.pdf
- DANE. Boletín técnico EMICRON Vendedores ambulantes 2025 (18 sep 2026). https://www.dane.gov.co/files/operaciones/EMICRON/bol-EMICRONVendedoresAmbulantes-2025.pdf
- Banca de las Oportunidades. Encuesta de Demanda de Inclusión Financiera 2022 (informe). https://www.bancadelasoportunidades.gov.co/sites/default/files/2022-12/Encuesta%20de%20demanda%202022%20VF.pdf
- Banca de las Oportunidades. Encuesta de Demanda 2022, microdatos. https://www.bancadelasoportunidades.gov.co/sites/default/files/2022-10/Encuesta_demanda_2022_microdatos.xlsx
- Banca de las Oportunidades. Formulario de la Encuesta de Demanda publicado en 2022-08 (preguntas 303 y 307, que coinciden con las variables de los microdatos 2022). https://www.bancadelasoportunidades.gov.co/sites/default/files/2022-08/Formulario%20Encuesta%20de%20Demanda%202021_1.pdf
- Banca de las Oportunidades. Panorama de la exclusión financiera y el crédito informal en los micronegocios colombianos (2025). https://www.bancadelasoportunidades.gov.co/sites/default/files/2025-09/Panorama%20de%20la%20Exclusi%C3%B3n%20Financiera%20y%20el%20Cr%C3%A9dito%20Informal%20en%20los%20Micronegocios%20Colombianos.pdf
- Fenalco. Encuesta Fenaltiendas 2024 (dic 2024, n=464). https://drive.google.com/file/d/1YlAOFTsXqTx0uRc7Nx3yyCo0IDbH4Y7h/view
- Fenalco. "La mayoría de tiendas de barrio operan en modo supervivencia ante caída de ingresos y presión de costos en 2026". https://www.fenalco.com.co/blog/noticias-10/la-mayoria-de-tiendas-de-barrio-operan-en-modo-supervivencia-ante-caida-de-ingresos-y-presion-de-costos-en-2026-fenalco-8830
- Gases del Caribe. Brilla Negocios. https://www.brillagascaribe.com/brilla-negocios

Estudios y literatura
- López Rivera, E., Manrique Chaparro, O. L. y Kalmanovitz, S. (2026). Los préstamos gota a gota en Bogotá: un análisis de necesidades, sesgos cognitivos y exclusión financiera. Apuntes. https://revistas.up.edu.pe/index.php/apuntes/article/view/2604
- IPE por encargo de Asbanc (2024). El mercado de crédito informal en el Perú. https://ipe.org.pe/wp-content/uploads/2024/10/IPE_El_mercado_de_credito_informal_en_el_Peru.pdf
- Banco Mundial (2025). The Little Data Book on Financial Inclusion 2025. https://thedocs.worldbank.org/en/doc/be6615202d1f08a25855c8ac2d615122-0050012025/related/Little-Data-Book-2025-Web.pdf
- Karlan, D., Mullainathan, S. y Roth, B. (2019). Debt Traps? Market Vendors and Moneylender Debt in India and the Philippines. AER: Insights 1(1). https://www.aeaweb.org/articles?id=10.1257/aeri.20180030 (working paper: https://www.ipr.northwestern.edu/documents/working-papers/2018/wp-18-05.pdf)
- Karlan, D. y Zinman, J. (2008). Credit Elasticities in Less-Developed Economies. AER 98(3). https://www.povertyactionlab.org/sites/default/files/research-paper/208%20Credit%20Elasticities%20June%2008.pdf
- Karlan, D. y Zinman, J. (2019). Long-Run Price Elasticities of Demand for Credit: Evidence from a Countrywide Field Experiment in Mexico. REStud 86(4). https://www.nber.org/papers/w19106
- Bertrand, M., Karlan, D., Mullainathan, S., Shafir, E. y Zinman, J. (2010). What's Advertising Content Worth? QJE. https://isps.yale.edu/research/publications/isps10-006
- Ashraf, N., Karlan, D. y Yin, W. Deposit Collectors. https://navaashraf.com/wp-content/uploads/2016/07/depositcollectors_aeap.pdf
- IPA. Savings Account Labeling for Susu Customers in Ghana. https://poverty-action.org/study/savings-account-labeling-susu-customers-ghana
- Afzal, U., d'Adda, G., Fafchamps, M., Quinn, S. y Said, F. (2018). Two Sides of the Same Rupee? Economic Journal (resumen RES). https://res.org.uk/mediabriefing/saving-and-borrowing-poor-households-in-pakistan-see-no-distinction-among-microfinance-products/
- Dupas, P. y Robinson, J. (2013). Savings Constraints and Microenterprise Development. AEJ: Applied. https://www.gap.hks.harvard.edu/savings-constraints-and-microenterprise-development-evidence-field-experiment-kenya
- Field, E., Pande, R., Papp, J. y Park, Y. J. (2012). Repayment Flexibility Can Reduce Financial Stress. PLoS ONE. https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0045679
- Field, E., Pande, R., Papp, J. y Rigol, N. (2013). Does the Classic Microfinance Model Discourage Entrepreneurship Among the Poor? AER 103(6). https://www.aeaweb.org/articles?id=10.1257/aer.103.6.2196
- Kaur, S., Mullainathan, S., Oh, S. y Schilbach, F. (2021). Do Financial Concerns Make Workers Less Productive? NBER w28338. https://www.nber.org/papers/w28338
- Beaman, L., Magruder, J. y Robinson, J. (2014). Minding Small Change among Small Firms in Kenya. JDE 108. https://ideas.repec.org/a/eee/deveco/v108y2014icp69-86.html
- CGAP (2018). Kenya's Digital Credit Revolution Five Years On. https://www.cgap.org/blog/kenyas-digital-credit-revolution-five-years-on
- Trabajo de grado UMNG sobre gota a gota (cita CEDE 2010 y Rodríguez Raga 2019). https://repository.umng.edu.co/server/api/core/bitstreams/c5aa8b9b-3e28-461d-9c91-a09d1c6737cc/content

Empresas, programas y prensa
- Safaricom (2025). Annual Report FY2025. https://www.safaricom.co.ke/annualreport_2025/wp-content/uploads/2025/08/safaricom-annual-report.pdf
- M-KOPA. Impact. https://m-kopa.com/impact/
- Wikipedia. Pradhan Mantri SVANidhi Scheme. https://en.wikipedia.org/wiki/Pradhan_Mantri_SVANidhi_Scheme
- Wikipedia. Pigmy Deposit Scheme. https://en.wikipedia.org/wiki/Pigmy_Deposit_Scheme
- Valora Analitik (30 ene 2024). Brilla crece en Colombia y apuesta por nueva línea de crédito. https://www.valoraanalitik.com/brilla-se-consolida-en-colombia-y-apuesta-por-nueva-linea-de-credito/
- Notas Económicas (dic 2024). Promigas celebra 50 años con emisión de bonos para hogares Brilla. https://www.notaseconomicas.com/2024/12/promigas-celebra-50-anos-con-emision-de-bonos-para-los-hogares-brilla/
- MyJoyOnline (6 oct 2025). Beyond Mobile Money: The Quiet Struggle to Modernize Ghana's Ancient Susu System. https://www.myjoyonline.com/beyond-mobile-money-the-quiet-struggle-to-modernize-ghanas-ancient-susu-system/
- RedExpertos (28 ago 2026). Nueve de cada diez hogares compran en la tienda de barrio. https://redexpertos.co/nueve-de-cada-diez-hogares-compran-en-la-tienda-de-barrio-el-corazon-del-consumo-colombiano/
- Semana (12 may 2026). Tiendas de barrio solo sobreviviendo. https://www.semana.com/economia/macroeconomia/articulo/tiendas-de-barrio-solo-sobreviviendo-el-cliente-tiene-menos-plata-y-el-alza-del-salario-minimo-que-se-hizo/202642/
- Infobae (26 feb 2025). Crisis en las tiendas de barrio en Colombia. https://www.infobae.com/colombia/2025/02/26/crisis-en-las-tiendas-de-barrio-en-colombia-este-es-el-alto-porcentaje-que-reporto-bajas-en-las-ventas-segun-fenalco/
- Infobae (28 ago 2024). El 20% de los negocios que están empezando en Bogotá acuden a prestamistas informales. https://www.infobae.com/colombia/2024/08/28/el-20-de-los-negocios-que-estan-empezando-en-bogota-acuden-a-prestamistas-informarles-o-gota-a-gota/
- Infobae México (14 ene 2025). Montadeudas crecen 33% en enero. https://www.infobae.com/mexico/2025/01/14/prestamos-fraudulentos-montadeudas-crecen-33-por-ciento-en-enero-alerta-consejo-ciudadano/

## Anexo: material del intento anterior descartado o corregido

- Fuentes que no se pudieron abrir en esta sesión (bloqueo o muro anti bots): portal oficial de PM SVANidhi (MoHUA, bloqueado desde Colombia), Banco de la República borrador 956 sobre crédito formal e informal con datos ELCA, PDF completo de la encuesta de endeudamiento ANIF y Colombia Fintech (solo para afiliados). Quedan como pendientes.

- El resumen automático de WebFetch sobre el PDF de Ashraf, Karlan y Yin decía "Kenia, ahorro +60%, 50 chelines por visita". Es falso: el texto real del PDF habla de Filipinas, +188 pesos (+25%) y 4 pesos por visita. Se usó el texto del PDF.
- El resumen de PLoS ONE (Field et al. 2012) agregó "sin aumento significativo del default"; no está en el abstract y no se usa.
- La cifra "el fiado cayó 54%" de prensa se corrigió con el gráfico original de Fenaltiendas 2024 (p. 35).
- Una ficha del Senado (30 may 2024) atribuye al DANE que el gota a gota pasó de 13% a 24% entre 2019 y 2021 como fuente del crédito de micronegocios; no se verificó en los anexos 2019 y 2021 (confianza baja). https://www.senado.gov.co/index.php/component/content/article/13-senadores/5570-aprobado-proyecto-de-ley-para-combatir-orestamos-gota-a-gota-y-promover-la-competencia-justa-en-el-sector-financiero

## Verificación

Revisión de verificación hecha el 26 de septiembre de 2026 sobre las fuentes originales (descarga directa de los anexos y PDF, y lectura de las páginas web citadas). Se revisaron 29 afirmaciones (agrupadas por fuente) de las que depende una propuesta.

| Claim | Resultado | Nota |
|---|---|---|
| EMICRON 2024: 14,2% de micronegocios pidió crédito (702.293 de 4.946.334), cuadro H.2 | confirmado | Anexo en Excel descargado de nuevo; valores idénticos. |
| EMICRON 2024: gota a gota 22,9% total, 27,5% cabeceras, 9,8% rural; regulada 77,0% rural (H.4) | confirmado | Anexo H.4. El boletín técnico EMICRON 2024, p. 32, sí dice "gota a gota con el 77,0%" en lo rural y su gráfico 25 tiene las columnas cruzadas; el error del DANE es real. |
| EMICRON 2023: gota a gota 23,3% (201.965), H.4; uso personal 39,2% en 2023 | confirmado | Anexo 2023: 23,28% y 201.964,97; 20,47% + 18,74% = 39,2%. |
| Ambulantes 2025: 61,8% gota a gota; 22,5% regulada; 12,8% familia; 1,8% proveedores; razones 44,6% / 29,4% / 2,3% | confirmado | Boletín Vendedores ambulantes 2025, p. 25 y 26, 24 ciudades. El crédito se refiere a 2024. |
| Tiendas y panaderías: 11,3% gota a gota; 69,9% regulada; 5,6% proveedores; 81,0% no pidió; 45,7% miedo; 8,6% intereses | confirmado | Boletín Panaderías y tiendas de barrio, p. 24 y 25. |
| EMICRON 2024: razones para no pedir crédito (42,5% miedo; 6,5% intereses), H.3 | confirmado | 42,51% y 6,48%. |
| EMICRON 2024: uso del crédito (21,0% + 15,5% = 36,5%), H.6; H.6A 2,9% y 9,9% | confirmado | 21,03% + 15,49%; 2,94% y 9,88%. |
| EMICRON 2024: ahorro 18,1%; no le alcanzó 95,9%; 0,2% y 0,2%; uso 74,7% / 43,8% / 12,5% / 9,2%; dónde 61,1% / 32,6% / 3,6% | confirmado | H.7, H.7A, H.7B, H.8. "No le han ofrecido productos" es 0,15% y "no confía" 0,24%; ambos redondean a 0,2%. |
| Encuesta de Demanda 2022: 29% informal, 13,6% almacenes, 7,0% servicios públicos; 65,4% no quiere deudas y 27,8% alto costo; 31,5% corresponsales | confirmado | Informe, p. 10. |
| Encuesta de Demanda 2022: 87,2% cuota mensual; seguros por funerarias 31,4% y servicios públicos 11,2% | confirmado | p. 58 y p. 74 (capítulo de seguros). |
| Findex / Little Data Book 2025: ahorro en clubes, Brasil 24,2% | corregido | En el PDF, Brasil marca 5,6%; el 24,2% es de Botsuana (página contigua). Se corrigió en tabla, resumen, PC5 y sección 6. Colombia 5,4%, México 12,6%, Perú 6,9%, Ghana 24,9% y Kenia 33,9% sí coinciden. |
| Findex / Little Data Book 2025: Colombia 46,3% pidió prestado vs 13,5% formal; página citada p. 45 | corregido | Cifras correctas; la página de Colombia es la 44 impresa (53 del PDF), no la 45 (que es Brasil). |
| López Rivera, Manrique y Kalmanovitz (Apuntes 101, 2026): n=100, 2 a 9 de octubre de 2023; 92% gota a gota; 86% Nequi o Daviplata; figura 6 (15,2% / 10,9% / 60,9% / 13%); la mitad pagaría más por más plazo; 56% quiere desembolso en máximo una semana | confirmado | PDF del artículo. 3,44% mensual compuesto equivale a 50,0% anual, así que las dos opciones son la misma tasa. |
| IPE 2024 (Perú): pagar otras deudas 36% (2024) y 39% (2022); negocio 22%, salud 19%, educación 17%; 55% más de un crédito; 2,7 créditos; 55% por rapidez; 45% favorable; 38% volvería; 1.203 encuestas | confirmado | p. 7, 10, 11 y 20. Pregunta de opción múltiple: los motivos no suman 100%. |
| Fenaltiendas 2024: 54,1% dice que el fiado disminuyó; 61,2% necesita crédito; uso 63,03% / 25,35% / 5,99% / 5,63%; n=464, dic 2024 | confirmado | Gráficos de las p. 35, 36 y 37 leídos como imagen desde el PDF de la encuesta. |
| Fenaltiendas, variante "6,25% de quienes piden hasta $1 millón lo quiere para pagar otras deudas" (PC3) | no verificado | No se encontró esa cifra en el PDF; el gráfico general da 5,99%. Marcado en el texto. |
| Fenalco 2026: 39,55% más restricciones de proveedores; 20,91% pago de contado; 11,82% plazos más cortos; 60,45% gasta más de 10% en arriendo y servicios | confirmado | Nota de Fenalco citada. |
| 36% de las tiendas mantiene el fiado (P&G vía RedExpertos, 28 ago 2026) | confirmado | La cifra está en la nota, con una nota al pie cuya fuente no se muestra en la página. Se mantiene confianza media. |
| Brilla: 3,6 millones de usuarios y cartera $2,11 billones (2023) | corregido | Valora Analitik (30 ene 2024) dice "ha beneficiado a más de 3,6 millones de usuarios" (acumulado desde 2007), no clientes actuales. La nota no menciona mora: la frase "bajos niveles de cartera en mora" queda marcada como no verificada. El 94% de estratos 1 a 3 (Notas Económicas) no se revisó. |
| Brilla Negocios: solo "dueños de los predios, titulares de la factura", actividad formal o informal, 9 meses capital de trabajo, 60 meses activos | confirmado | Página de Gases del Caribe; dice "disponible inicialmente", o sea que la restricción podría cambiar. |
| Safaricom FY2025: Fuliza 7,9 millones de clientes, KShs 1,0 billón (trillion) en transacciones, ingreso KShs 4.100 millones, 48% del crecimiento del ingreso de crédito; Pochi 1,1 millones de comerciantes | confirmado | Annual Report 2025 descargado del enlace citado. |
| Karlan, Mullainathan y Roth (AER: Insights 2019): la mayoría vuelve a deber en seis semanas; a 1 o 2 años igual que el control; Chennai 2007, Cagayan de Oro 2007 y 2010 | confirmado | Resumen en la página de la AEA y texto del working paper. |
| Ashraf, Karlan y Yin, Deposit Collectors: Filipinas, +188 pesos (+25%), 38 de 137 aceptaron, 20 uso regular, 4 pesos por visita | confirmado | PDF citado. |
| Karlan y Zinman 2008: el monto responde más al plazo que a la tasa | confirmado | Texto del artículo (AER 98:3). |
| Field, Pande, Papp y Park (PLoS ONE 2012): 51% menos probable sentirse preocupado, tenso o ansioso | confirmado | Resumen del artículo. |
| Kaur et al. (NBER w28338): +7% de producción | confirmado | Resumen en NBER (0,11 desviaciones estándar). |
| CGAP 2018 (Kenia): 27% con préstamo digital; 14% con varios préstamos; 16% pidió prestado para pagar; cerca de la mitad se atrasó; 13% default | confirmado | Blog de CGAP citado. |
| M-KOPA: más de 3 millones de clientes activos; más de USD 2.000 millones en crédito | confirmado | Página de impacto de la empresa (fuente interesada). |
| PM SVANidhi: ₹10.000 a 1 año, luego ₹20.000 y ₹50.000; subsidio 7%; cashback ₹50 a ₹100 al mes; desde 1 jun 2020 | confirmado | Solo contra Wikipedia (fuente secundaria); se mantiene confianza media. |

Afirmaciones no revisadas en esta pasada (quedan con la confianza que les dio el autor): cálculos propios sobre microdatos de la Encuesta de Demanda 2022 (6,5% fiado, 5,1% gota a gota, 21,6% y 15,3%), Panorama BDO (65,55% sin registros), Fenaltiendas 2026 vía Semana, Notas Económicas sobre Brilla, susu (IPA), Afzal et al., Bertrand et al., Karlan y Zinman 2019, pigmy deposit, montadeudas en México y la nota de Infobae sobre el crédito de la Alcaldía de Bogotá.
