# Números del negocio: Cláusula de lluvia del fiado

Para el redactor. Todo sale de `python3 models/business_model.py` (corrido el 27 sep 2026). La hoja `report/prototipo.xlsx` reproduce el caso base con fórmulas vivas y da los mismos valores (verificado con `models/build_prototype.py`). [S] marca un supuesto propio sin dato. Todo cálculo es "cálculo propio, Anexo E".

## 1. Las seis respuestas (Tabla 3 del cuerpo)

| # | Pregunta | Caso base | Caso conservador | Supuesto y fuente |
|---|---|---|---|---|
| 1 | Inversión inicial | $3,9 millones | $3,9 millones | Registro de la SAS $0,6 millones [S, sin cotización]; concepto de un abogado $3 millones [S, cotización pendiente]; tarjetas y material $0,3 millones [S]. El programa y el bot los hago yo ($0 en efectivo). $0 de capital para prestar, porque la SAS no presta |
| 2 | Costo fijo mensual | $2.530.905 | $2.530.905 | Mi salario, 1 salario mínimo de 2026 ($1.750.905); transporte y campo $200.000; celular y datos $80.000; WhatsApp Business, servidor y herramientas $150.000; contador $350.000. Todo [S] salvo el salario |
| 3 | Cuánto deja cada usuario al mes | $2.800 por vendedor inscrito | $2.200 | Tarifa de $4.000 que paga quien fía [S, sin precedente de precio] por la parte cobrada (90% base, 80% conservador) [S], menos $800 o $1.000 de mensajes y tarjeta [S]. El impago que me toca es el de la tarifa. No presto ni muevo la plata del vendedor, así que no tengo cartera; el impago de lo aplazado lo carga quien fía (sección 3) |
| 4 | Usuarios e ingresos, mes 3 | 40 inscritos, 27 pagan; $108.000 facturados, $75.600 de contribución | 21 inscritos, 12 pagan; $48.000 y $26.400 | Base: 4 minoristas con 10 vendedores cada uno [S]. Conservador: 3 con 7 [S]. Primer mes gratis por minorista |
| 4 | Mes 6 | 144 inscritos, 108 pagan; $432.000 y $302.400 | 48 y 40; $160.000 y $88.000 | Base: 12 minoristas con 12. Conservador: 6 con 8 |
| 4 | Mes 12 | 468 inscritos, 416 pagan; $1.664.000 y $1.164.800 | 144 y 128; $512.000 y $281.600 | Base: 36 minoristas con 13; 4 minoristas nuevos al mes desde el mes 7 [S]. Conservador: 18 con 8; 2 nuevos al mes desde el mes 7 [S] |
| 5 | Break-even | 904 vendedores que pagan; mes 22 | 1.150 vendedores; no llega en 60 meses | Costo fijo / contribución por vendedor. 904 son 5,1% de los 17.745 ambulantes de Cali A.M. (DANE, EMICRON 24 ciudades 2025, C. D.1_24C, CV 8,4%); no sé cuántos sacan fiado |
| 6 | Cuánto necesito para sobrevivir | $34,5 millones (punto más bajo en el mes 21) | Más de $76 millones a 36 meses y sigue cayendo | Inversión inicial más pérdidas acumuladas hasta el punto más bajo. Sin mi salario: $8,5 millones y equilibrio en el mes 10 (base); $15,1 millones y mes 27 (conservador). De dónde sale: sección 6 |

Versión corta para el cuerpo (si no cabe la de dos casos): usar la columna base y una línea: "En un caso conservador (la mitad del ritmo, 8 vendedores por minorista y 20% de tarifas sin cobrar) el modelo no cierra con mi salario en 60 meses; sin salario cierra en el mes 27 con $15,1 millones".

## 2. Supuestos que mueven el resultado

| Supuesto | Valor | Fuente o razón | Si está mal |
|---|---|---|---|
| Tarifa | $4.000 al mes por vendedor [S] | Sin precedente | Con $2.000 el equilibrio pide 2.531 vendedores y no llega en 36 meses ($67,5 millones de caja); con $6.000, 550 vendedores en el mes 15 ($25,8 millones) |
| Vendedores por minorista | 10 a 13 base, 5 a 8 conservador [S] | Sin dato; primera pregunta de campo | Es lo que separa el caso base del conservador |
| Ritmo | 4 minoristas nuevos al mes (base), 2 (conservador), desde el mes 7 [S] | Capacidad de una persona | Con 2 al mes y mi salario no cierra en 60 meses |
| Tarifa sin cobrar | 10% base, 20% conservador [S] | Sin dato | Cada 10 puntos quita $400 por vendedor al mes |
| Días de disparo | 26 al año | IDEAM 0026055120: 26 de 294 días de venta con 5 mm o más, 27 sep 2025 a 26 sep 2026 (cálculo propio) | Solo mueve el costo de quien fía, no mi margen |
| Fiado diario | $30.000 [S] a $62.000 | $62.000 es cota superior: ventas diarias del ambulante menos su ingreso (DANE, EMICRON ambulantes 2025); no medido para carritos | Escala el costo de quien fía |
| Impago de lo aplazado | 1%, 3% o 10% [S] | Sin dato colombiano. Referencia: mora del microcrédito formal 6,9% (El Tiempo con datos de la SFC, jul 2026; prensa) | Decide si quien fía acepta |
| Margen bruto de quien fía | 10% [S] | Sin fuente | Solo mueve el argumento de venta |
| Ingreso del vendedor | $38.600 por día de venta | Unos $1,0 millón al mes en 26 días (DANE, EMICRON ambulantes 2025, C. 24) | Única convención del PDF |

## 3. Vista de quien paga (el minorista o el mayorista), por vendedor al año

Todo el fiado del día de lluvia aplazado, 26 días al año, plazo promedio de 2,5 días [S], costo del dinero de quien fía 20% efectivo anual [S], margen bruto 10% [S].

| Fiado diario | Impago de lo aplazado | Aplazado al año | Costo del plazo | Impago | Tarifa | Se paga sola si evita perder |
|---|---|---|---|---|---|---|
| $30.000 | 1% | $780.000 | $975 | $7.800 | $48.000 | 6,1% de sus vendedores al año |
| $30.000 | 3% | $780.000 | $975 | $23.400 | $48.000 | 7,7% |
| $30.000 | 10% | $780.000 | $975 | $78.000 | $48.000 | 13,6% |
| $62.000 | 1% | $1.612.000 | $2.014 | $16.120 | $48.000 | 3,4% |
| $62.000 | 3% | $1.612.000 | $2.014 | $48.360 | $48.000 | 5,1% (1 de cada 20) |
| $62.000 | 10% | $1.612.000 | $2.014 | $161.200 | $48.000 | 10,9% |

Lectura: el plazo casi no cuesta (unos $2.000 al año por vendedor); lo que pesa es la tarifa y el impago de lo aplazado, que no está medido.

## 4. Vista del vendedor: cubrir el fiado de un día de lluvia

Ingreso de $38.600 por día de venta.

| Camino | Fiado de $30.000 | Fiado de $62.000 | Fuente |
|---|---|---|---|
| Gota a gota, 20% por préstamo | $6.000 (16% de un día) | $12.400 (32%) | Enunciado del caso; 20,4% mensual en Cali (Martínez y Rivera-Acevedo 2019) |
| Préstamo de un día, 10% ("diario anticipado") | $3.000 (8%) | $6.200 (16%) | Pérez Cruz 2025, Corabastos (Bogotá) |
| Préstamo diario legal al tope de usura, 3,09% plano en 30 cuotas | $927 (2%) | $1.916 (5%) | `models/usury_cap.py`, usura del popular productivo urbano de septiembre de 2026 (SFC, Resolución 1260 de 2026). No existe a este monto: el ticket promedio del microcrédito es de $8,43 a $9,96 millones |
| Cláusula de lluvia | $0 | $0 | El vendedor no paga nada |

En el prototipo (30 días de venta, 3 días de disparo, fiado de $62.000): el camino del gota a gota termina en 3 préstamos, 2 de ellos para cubrir también cuotas del anterior, con $19.866 de interés (51% del ingreso de un día) y $42.846 todavía debidos al día 30. Con la cláusula, $0 de recargo y nada pendiente al día 30; quien fía cargó como máximo $63.640 durante 3 días.

Lo que la cláusula no cubre: si la mercancía se daña, pagar el fiado en tercios le cuesta $10.333 (27%) a $20.667 (54%) de cada uno de esos tres días (50% o 100% de $62.000 sin pagar).

## 5. Lectura honesta (texto casi literal para la página 5)

Con mi salario, el modelo no cierra en los primeros 12 meses: en el mes 12 pierdo $1,37 millones al mes y llego al equilibrio en el mes 22, con unos 900 vendedores que pagan y $34,5 millones de caja. En el caso conservador no cierra en 60 meses con salario: con 2 minoristas nuevos al mes y 8 vendedores cada uno, una persona no llega a 1.150 vendedores. Sin salario cierra en el mes 10 (base) o en el 27 (conservador). Si no cierra, será por volumen y por una tarifa que nadie ha pagado todavía, no por riesgo de crédito, porque no presto. Lo que lo haría cerrar es vender por mayorista (un contrato trae varios minoristas) en vez de minorista por minorista. Por eso el piloto cobra desde el segundo mes y el mes 3 me dice si sigo: si menos de la mitad de los minoristas paga los $4.000, pruebo $2.000 con el mayorista; si tampoco, el modelo no cierra y lo digo.

Con un equipo de $10 millones al mes harían falta unos 3.571 vendedores que pagan.

## 6. De dónde sale la plata

**PENDIENTE: confirmar con Santiago antes de escribir** (brief-final, 9.1 fila 6 y punto 93). Propuesta de estructura: aportes de capital a la SAS (ahorro propio y, si aplica, familiares como socios), nunca préstamos recibidos del público, para no acercarme a la captación (Decreto 1981 de 1988). No cuento con el fellowship como fuente. Si Santiago no confirma, escribir solo: "Los $8,5 millones del arranque sin salario los pondría como capital de la SAS; la diferencia hasta $34,5 millones sería capital semilla que hoy no tengo."

## 7. Cómo se reproduce

- `python3 models/business_model.py`: las seis respuestas en los dos casos, con y sin salario, la sensibilidad de la tarifa, el equipo de $10 millones, la vista de quien paga, la del vendedor y la carga con mercancía que se daña.
- `<venv>/bin/python models/build_prototype.py`: construye `report/prototipo.xlsx`, evalúa sus fórmulas, las compara con el modelo en Python (14 de 14 iguales) y escribe `report/prototipo-snapshot.html`.
