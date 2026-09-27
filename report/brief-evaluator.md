# Brief del arquitecto: evaluador primero

Fecha: 27 sep 2026, 02:30. Entrega: hoy 12:00 (hora Colombia). Archivo final: `report/MAKERS_SANTIAGO_ESPINOSA_CALI.pdf`.

Base leída: rúbrica (`docs/02`), caso y plataforma (`docs/00`, `docs/01`), respuestas predecibles (`docs/03`, sección 3), síntesis completa (`research/00-sintesis.md`, secciones 1 a 11.6; no hay 11.7), `research/12a`, `12b`, `12-mecanismos-dia-malo.md` (ya completo), campo (`docs/06`, `07`, `09`) y los tres scripts de `models/` (corridos hoy; resultados abajo).

Criterio de este brief: maximizar el bloque 1. Un evaluador que leyó 100 propuestas va a ver 60 variantes de "microcrédito por WhatsApp con tenderos aliados, cuota diaria, montos que suben, reporte positivo". Eso es lo que hay que evitar, aunque esté bien documentado.

---

## 1. Tesis del informe (una frase)

> **El crédito formal fracasa con el vendedor ambulante porque le vende plata con fecha fija a alguien cuyo problema es una fecha que mueve el clima; el gota a gota gana porque aparece la tarde del día malo, y lo que el vendedor le compra no es plata sino no quedar mal con quien le fía la mercancía de mañana.**

Frase de cierre del diagnóstico (segunda línea de la tesis, para el PDF): "El crédito sano ya existe: es el fiado diario sin interés de la cadena de mercancía. Lo que falta es que aguante un día de lluvia."

Por qué es tesis propia y no resumen de reportes:
- Da vuelta el marco del caso: el problema no es falta de crédito (el vendedor ya tiene crédito diario gratis) ni el precio (en cuota diaria el préstamo legal se ve solo 12% a 15% más barato; cálculo propio, `usury_cap.py`). Es la rigidez de una fecha en el único día en que no hubo ingreso.
- Conecta con la tesis 1 de la síntesis (el informal compite por la relación) pero la mueve: el vendedor no toma el gota a gota para tener una relación con el prestamista, sino para proteger otra relación, la del fiado, cuya sanción es la exclusión ("que no vuelva por acá", Martínez Benavides 2021, Cali).
- Es refutable en campo con una pregunta (E1 de `12-mecanismos`, sección 2.11): si el minorista ya espera un día sin problema, la tesis cae.

---

## 2. Mecanismo elegido: E "El puente del fiado", con tres refinamientos

### 2.1 En una frase

Cuando la estación del IDEAM marca día de lluvia, el vendedor que ya tiene historial con su minorista paga lo que no alcanzó a pagar ese día en sus tres días de venta siguientes, sin recargo; el minorista corre en la misma medida su pago al mayorista, y el mayorista carga ese plazo y nos paga una tarifa por vendedor activo. Nosotros ponemos el disparador, la regla y el registro. Nunca le prestamos al vendedor, nunca recibimos su plata y nunca lo contactamos para cobrar.

### 2.2 Refinamientos sobre la versión de `12-mecanismos`

1. **Contarlo como "la lluvia decide la fecha", no como "plazo para inventario".** En el texto, el sujeto del mecanismo es el dato público, no el crédito. Es lo que lo separa de la respuesta predecible 6 a los ojos del evaluador.
2. **Decir lo que no cubre, sin agregarle piezas.** Nada de comodines por enfermedad ni seguros encima. La pureza del disparador externo es lo que lo hace defendible (Brune, Giné y Karlan: la flexibilidad a pedido del deudor nuevo subió el impago en Barranquilla y Cartagena). El choque de salud o familiar (la vendedora de arepas de la informante) queda fuera y se dice.
3. **E2 solo como arranque acotado del piloto**, con tope de capital propio de $5 millones, y dicho así: "E2 no es negocio" (neto de -$14.537 por vendedor al año con 1% de impago del minorista; `bad_day_mechanisms.py`). No se presenta como segunda pata del modelo.

### 2.3 Por qué E y no los otros

| Mecanismo | Veredicto | Razón en una línea |
|---|---|---|
| **E. Puente del fiado** | **Elegido** | Único que nace del hallazgo de campo, no crea crédito, no necesita la confianza del vendedor y ataca el momento exacto en que nace el gota a gota |
| A. Ventanilla del tendero | Descarte 1 | Se lee como predecibles 3 + 7; con montos de ambulante pierde plata (neto de $5.857 al año con 1% de pérdida, -$2.143 con 1,5%); un prestamista legal sin amenaza queda último en la fila de pago (informante) |
| F. Día de lluvia pagado | Descarte 2 | Suena original y se cae con sus propios números: la prima del fiado entero es 43,8% del ingreso diario |
| C. Cuota diaria de la deuda mensual | Anexo | El usuario de carrito casi no tiene cuota formal mensual (solo 22,5% de los ambulantes que piden crédito va a una entidad regulada) |
| B. Alcancía con adelanto | Anexo | Es la predecible 8 con otro nombre |
| D. Consignación de madrugada | Anexo | Es la predecible 6; no toca el hogar |

### 2.4 Puntaje estimado (1 a 5) contra la rúbrica

| Criterio | E | A (re-puntuado con campo) | F | C |
|---|---|---|---|---|
| 01 Efectividad (causa raíz, un solo mecanismo) | 4 | 3 | 2 | 2 |
| 02 Especificidad (paso a paso) | 4 | 4 | 3 | 3 |
| 03 Creatividad (mecanismo, no nombre) | 5 | 2 | 3 | 3 |
| 04 Diagnóstico (tesis propia) | 4 | 4 | 3 | 3 |
| 05 Fuentes | 4 | 4 | 4 | 3 |
| 06 Trazabilidad | 5 | 4 | 3 | 3 |
| 07 Juicio cuantitativo | 3 | 2 | 3 | 2 |
| 08 Descartes y autocrítica | 4 | 3 | 3 | 3 |
| **Total (de 40)** | **33** | **26** | **24** | **22** |

Justificación de los puntajes de E que no son 5:
- 01 = 4: resuelve los cuatro puntos con una pieza, pero solo el choque de lluvia y solo para quien ya tiene fiado.
- 02 = 4: el paso a paso es completo, pero el monto del fiado, la hora de cobro del minorista y el plazo del minorista con su proveedor no están medidos.
- 04 y 05 = 4: el campo es de segunda mano (resumen oral de un colaborador, sin número de vendedores) y la informante no es usuaria.
- 07 = 3: la tarifa que paga el mayorista no tiene precedente; el impago de lo aplazado no tiene dato colombiano.
- 08 = 4: descartes con números propios y riesgo real nombrado; falta la validación en primera persona.

### 2.5 A qué respuesta predecible se parece y qué la hace distinta

Se parece a la **6 (crédito de proveedor o BNPL para inventario)**, y un poco a la **9 (cuaderno de fiado digital)**. En el mercado, lo más cercano es Tienda Pago (plazo de 7 días al pago del distribuidor, Perú y México) y el plazo de BEES. Hay que nombrarlos en el PDF antes de que lo haga el evaluador.

Lo que cambia en el mecanismo (no en el nombre):
1. **No crea crédito.** El crédito ya existe, es gratis y lo da otro. La 6 agrega una línea o alarga el plazo estándar; E deja el plazo normal en cero días y solo lo abre cuando pasa un evento.
2. **La decisión la toma un dato público, no una solicitud.** Nadie pide nada ni evalúa a nadie. La estación 0026055120 del IDEAM marca 5 mm o más entre 7 a. m. y 7 p. m. y la regla se aplica sola.
3. **El plazo lo carga el de arriba**, que hoy le pasa el choque al vendedor por la vía del gota a gota, y no un financiador nuevo que le presta al de abajo.
4. **Ataca la tarde del día malo**, el momento en que nace el primer gota a gota según el campo, no la necesidad de crecer el inventario.
5. **El usuario no paga nada** ni se inscribe con cédula. En la 6 el usuario paga el financiamiento; en la 9 el objetivo es crear historial para un tercero.

Prueba de originalidad para el anexo (hacerla solo si hay tiempo y reportarla tal como salga): pegar el enunciado del caso, con y sin el hallazgo de campo, en tres modelos y guardar las respuestas. Si alguno propone "aplazamiento del fiado atado a un índice de lluvia, cargado por el mayorista", decir que la originalidad está en el hallazgo. Si no se hace, no mencionarla.

---

## 3. El usuario exacto

**Quién.** Vendedor de carrito o ambulante que cada mañana saca fiada, sin interés, la mercancía del día a un minorista que le surte (y que a su vez compra a un mayorista), la paga esa tarde con lo que vendió, trabaja a la intemperie y no tiene RUT ni quiere tenerlo. Entra quien lleva al menos 4 semanas sacando fiado con ese minorista (supuesto, en la lógica de Battaglia et al. 2023 y Brune, Giné y Karlan 2025).

**Dónde.** Cali. Piloto alrededor de la estación Universidades del MIO (sur de Cali), donde el colaborador conversó con vendedores de carrito el 26 sep 2026. La estación del IDEAM más cercana con datos al día es Universidad del Valle (Meléndez, 0026055120), con respaldo en Base Aérea Marco Fidel Suárez. La distancia exacta entre la estación y el punto de venta no está medida: decirlo.

**Cliente que paga.** El mayorista que surte a esos minoristas. Si no hay mayorista dispuesto, el minorista (y hay que ver si le alcanza).

**Cuántos (con fuente, sin inventar).**
- Marco nacional: 286.061 vendedores ambulantes en 24 ciudades en 2025 (DANE, EMICRON Vendedores ambulantes 2025, Cuadro 24; alta). De los que pidieron crédito, 61,8% fue a un gota a gota (25.744 de 41.672; Cuadros 18 y 18.1; alta), frente a 11,3% en tiendas de barrio (EMICRON Panaderías y tiendas 2024, H.4.1).
- Cali: entre vendedores ambulantes endeudados del centro y la galería Santa Elena, 51,3% de la deuda era con gota a gota, a una tasa promedio de 20,4% mensual (Martínez y Rivera-Acevedo 2019, n = 300, datos de 2016; alta, dato viejo).
- 93,3% de los ambulantes no tiene RUT (19.145 de 286.061 lo tienen; EMICRON 2025, Cuadros 13 y 13.1; alta). Es la base del "no pedimos nada".
- Lo que no se sabe y hay que decir: cuántos ambulantes de Cali sacan fiado diario de mercancía. La encuesta del DANE casi no lo ve (solo 1,8% de los ambulantes que pidieron crédito se lo pidió a un proveedor), probablemente porque el vendedor no llama "crédito" a la mercancía del día (inferencia de `12a`, 4). El primer dato del piloto es ese conteo.
- Alcance del plan: 45 vendedores en el mes 3, 400 en el mes 6, 1.500 en el mes 12 (supuestos de la sección 6). No usar el 38% de WIEGO para multiplicar a Colombia.

---

## 4. El mecanismo paso a paso

### 4.1 Tabla para el PDF (página 3)

| Momento | Quién | Qué hace | Con qué | Dónde está la plata |
|---|---|---|---|---|
| Semana 0 | Yo | Constituyo la SAS (servicios de información); programo el disparador que lee cada noche la API del IDEAM (estación Univalle y de respaldo); armo el bot de WhatsApp para minoristas; un abogado revisa la "cláusula de lluvia" | SAS, script sobre datos.gov.co, WhatsApp | Capital propio en la cuenta de la SAS |
| Semana 1 | Yo y un mayorista | Le propongo la cláusula: en día de disparo, el pago de sus minoristas por lo que fiaron ese día se corre hasta 3 días de venta. Paga una tarifa mensual por vendedor activo. Le muestro el dato, que él mismo puede revisar | Conversación, acuerdo comercial de una página | Nada se mueve |
| Semana 1 | Mayorista y 3 minoristas | Cada minorista elige a los vendedores que entran (4 semanas o más de fiado con él) y se lo dice de palabra, con una tarjeta: "Si el IDEAM marca lluvia, lo de ese día me lo paga en los 3 días siguientes, sin recargo" | Su palabra, tarjeta física | Nada se mueve |
| Día normal, mañana y tarde | Vendedor y minorista | Igual que hoy: saca el fiado y lo paga en la tarde | Mercancía, efectivo o Nequi | Mercancía del minorista en el carrito; en la tarde, bolsillo del vendedor → caja del minorista |
| Día de lluvia, 7 a 9 p. m. | Disparador | Con el dato publicado (rezago observado de 1 a 1,5 horas) calcula si hubo 5 mm o más entre 7 a. m. y 7 p. m. Si sí, avisa: "Hoy fue día de lluvia (Univalle, 12 mm). Rige la cláusula" | API del IDEAM, WhatsApp | Nada se mueve |
| Esa noche | Minorista | Responde al bot quién no pudo pagar y cuánto ("Pedro 45"). Lo hace unas 2 veces al mes | WhatsApp | La deuda del vendedor sigue siendo la misma, con otra fecha |
| Esa noche | Bot | Le manda al mayorista el total aplazado por minorista y el calendario ("su pago de mañana baja en $135.000; se completa en 3 días de venta") | WhatsApp u hoja compartida | La cuenta por pagar del minorista se corre; el mayorista carga el plazo |
| Día siguiente | Minorista | Le fía como siempre. Este es el paso que evita el gota a gota | Mercancía | Mercancía del minorista en el carrito |
| Días de venta 1 a 3 | Vendedor y minorista | El vendedor paga lo del día más un tercio de lo aplazado; el minorista le paga al mayorista lo corriente más su parte; el bot confirma "puente cerrado" | Efectivo o Nequi, WhatsApp | Bolsillo del vendedor → minorista → mayorista |
| Reglas de borde | Disparador y minorista | Tope de 3 días de disparo seguidos y de 2 fiados aplazados por vendedor. Sin dato de ninguna estación, el minorista puede declarar el día una vez al mes. Si el vendedor no cierra el puente en 5 días de venta, decide el minorista como hoy y el vendedor queda fuera del siguiente puente. Nosotros nunca cobramos ni llamamos al vendedor | | La pérdida, si la hay, es de quien hoy fía |
| Fin de mes | Mayorista | Paga la tarifa por vendedor activo | Transferencia | Mayorista → SAS |
| Solo si no hay mayorista (E2, piloto) | Yo | Presto al minorista, con capital propio y tope de $5 millones, el total aplazado hasta 5 días de venta, por debajo de la usura ordinaria (29,24% E.A., sep 2026). Sigo sin prestarle al vendedor | Transferencia | SAS → minorista → SAS |

### 4.2 Cómo una sola pieza resuelve los cuatro puntos

La pieza es una: **un dato público de lluvia que corre las fechas de pago de una cadena de fiado que ya existe.**

| Punto del caso | Cómo lo resuelve la misma pieza | Hallazgo que lo sostiene |
|---|---|---|
| 1. No soy entidad financiera | No presto ni aseguro. El crédito (el fiado) ya existe y lo dan comerciantes a comerciantes; yo solo cambio la fecha con una regla pactada. No hay prima ni indemnización (no es seguro) ni desembolso al vendedor (no es crédito mío). La plata del vendedor nunca pasa por la SAS (sin riesgo de captación, Decreto 1981 de 1988). El vendedor no paga nada, porque cobrarle a cambio de un pago contingente se parecería a un seguro sin licencia | Frente 07; `12b`, pregunta abierta 2 |
| 2. Ingreso diario sin ahorro | El mecanismo existe solo para el día en que no hubo ingreso, que es cuando la falta de ahorro obliga a pedir. La devolución se reparte en el ritual que ya tiene (pagar cada tarde), en tercios, sin cuota nueva ni calendario mensual | 26 de 294 días de venta con disparo, 21 rachas de 1 día y 3 de 2 (cálculo propio, IDEAM) |
| 3. Desconocido de 22 años | El vendedor no tiene que confiar en mí: ni me conoce, su trato sigue con el minorista de siempre. Entro por arriba (un mayorista y pocos minoristas). Y a ellos no les pido que me crean: el disparador es un número del IDEAM que pueden revisar solos | Campo 09, hallazgos 1 y 2; confianza en desconocidos 5,6% (DANE ECP 2023) |
| 4. Ya existen soluciones | El gota a gota vende este mismo puente a 20% por préstamo y el "diario anticipado" de Corabastos a 10% en el día; Tienda Pago y BEES dan plazos fijos que invitan a saldos que crecen; los microseguros devuelven 32,3% de lo que cobran; Nequi, CREO y las microfinancieras cobran mensual (87,2% de los créditos formales). Nadie mueve la fecha de un crédito que ya existe con un dato externo | Pérez Cruz 2025; RIF 2025; Encuesta de Demanda 2022 |

Extra que el evaluador va a valorar: E no entra en la fila de pago (riesgo principal de A según la informante) porque no agrega un acreedor; y no pone efectivo ni cobro en ninguna tienda, así que esquiva el riesgo de seguridad del nodo (31 cobradiarios asesinados en Atlántico en 2025; media, prensa: solo en anexo).

---

## 5. Esquema página por página (unas 2.500 palabras más 4 tablas)

Formato sugerido: carta, márgenes de 2 cm, 10 a 10,5 pt, tablas en 8,5 a 9 pt. Citas cortas en el texto ("DANE, EMICRON 2025, C. 18.1") y referencias completas con URL en el anexo E. Cada cálculo propio dice "cálculo propio" y el script.

### Página 1. Diagnóstico: el problema no es falta de crédito (unas 480 palabras + tabla 1)

- Apertura (2 líneas): la tesis.
- Tamaño y quién: 286.061 ambulantes; 61,8% de los que piden crédito va al gota a gota frente a 11,3% en tiendas; el usuario central no es el del mostrador que pinta el caso. 14,2% de los micronegocios pidió crédito y 22,9% de ellos fue a un gota a gota (EMICRON 2024, H.2 y H.4).
- Por qué falla el formal (tres datos, sin triada retórica en el texto): aprobación de 92,9% pero 42,5% no pide por miedo a endeudarse, 14,6% por requisitos (H.3, H.5); originar un microcrédito cuesta $1.117.131 fijos (Asobancaria BE 1475); 87,2% de los créditos formales se paga en cuota mensual (Encuesta de Demanda 2022, p. 58); la usura popular productivo subió a 88,13% y la SFC no vio más acceso (SFC 2025). Cálculo propio: en cuota diaria el préstamo legal se ve solo 12% a 15% más barato ($3.436 frente a $4.000 diarios por cada $100.000 en 30 cuotas).
- Qué hace bien el informal: aparece el día que se necesita, selecciona por recomendación y renueva (IPE 2024, Perú: 93% paga, 82% llegó por recomendación). Su castigo en Cali es la amenaza (informante; UNODC 2025 para Costa Rica). Frase honesta: "la renovación es el premio y la amenaza el castigo".
- Consecuencias: deuda que paga deuda (informante: "para pagarle a uno, se meten en otro"; campo: "un gota a gota con otro gota a gota"; Karlan, Mullainathan y Roth 2019: pagarle al prestamista no saca de la trampa).
- Tabla 1 (6 filas máximo): 61,8% frente a 11,3%; 42,5% miedo; $1.117.131; 87,2%; 12% a 15% (propio); 51,3% en Cali (2016).
- No usar aquí: 12 millones, 4,4 millones, 666,5%, "3 a 4 veces" de la informante, 31 cobradiarios en el cuerpo.

### Página 2. Campo y punto ciego: el día de lluvia rompe un fiado que funciona (unas 520 palabras + tabla 2)

- Método en dos líneas, honesto: "Una informante de Cali que conoce varios casos de amigos y familiares (dos notas de voz, 27 sep 2026; segunda mano). Conversaciones con vendedores de carrito en la estación Universidades del MIO, hechas por un colaborador en mi nombre el 26 sep 2026; tengo su resumen oral, no el número exacto de vendedores ni citas por persona." Regla cumplida: nadie contactó prestamistas.
- Hallazgos del colaborador (09): fiado diario sin interés del minorista; cadena mayorista, minorista, vendedor; "llovió, entonces nadie va... no le puedo pagar. Y ahí es cuando entran con un gota a gota"; circularidad; no se formalizan por miedo a impuestos.
- Hallazgos de la informante (06 y 07): cobro 6 días a la semana que respeta el día sin venta; un choque hundió a la vendedora de arepas ("ni volvió a sacar el negocio"); la recomendación compra paciencia y quien recomienda no quiere cobrar; al gota a gota se le paga primero porque amenaza (hipótesis).
- Contraste con fuentes: WIEGO 2014, cinco ciudades, n = 743: "I take stock on credit every morning then pay back in the evening"; 38% de los ambulantes dice que el crédito del proveedor es muy importante (19% en plaza); el proveedor que fía también debe. Martínez Benavides 2021 (Cali): el fiado no cobra interés y castiga con exclusión.
- El número propio: estación IDEAM Univalle, 26 de 294 días de venta con 5 mm o más de día en los últimos 12 meses; 21 rachas de un día y 3 de dos, ninguna de tres; octubre de 2025 y mayo de 2026 con 7 días cada uno (cálculo propio sobre datos.gov.co; alta en el método, media en el dato por huecos). Lectura: el choque es frecuente y corto; es de tiempo, no de pérdida, cuando la mercancía no se daña.
- El punto ciego en una frase: "No encontré publicado el paso 'tomo un gota a gota para no perder el fiado de mañana'. Si se confirma en primera persona, es el momento de origen que nadie mira."
- La pregunta que cambia: de "¿cómo le presto más barato?" a "¿cómo evito que un día de lluvia rompa un fiado que ya funciona?". Casaburi y Willis 2018: el problema del pobre con el seguro es el momento del pago (72% frente a 5% de adopción).
- Tabla 2, hallazgo → decisión (8 filas): fiado diario → no crear crédito; cadena → el plazo lo carga el de arriba; gota a gota entra el día de lluvia → solo se activa ese día; exclusión → aplazamiento pactado antes para que no cuente como quedar mal; rachas de 1 a 2 días → tope de 3 días y devolución en tercios; flexibilidad a nuevos sube impago → solo con historial y disparador externo; no quieren rastro para la DIAN (93,3% sin RUT) → el vendedor no se inscribe ni da cédula; quien recomienda no quiere cobrar → nosotros nunca cobramos.

### Página 3. La propuesta (unas 560 palabras + tabla 3)

- Usuario exacto y cliente que paga (sección 3 de este brief), en 4 líneas.
- Tabla 3: el paso a paso (sección 4.1), compactado a 9 o 10 filas.
- Los cuatro puntos con la misma pieza (sección 4.2) en cuatro párrafos cortos, no en tabla, para no pasar de 4 tablas.
- Parecido con la predecible 6 y con Tienda Pago y BEES, y las cinco diferencias de mecanismo (sección 2.5), en un párrafo.
- Soluciones parecidas y qué aprendí (4 líneas): Corabastos (el puente existe y se paga a 10% en el día); BRAC (aplazar cuotas con historial bajó el impago); "pases" en Colombia (a clientes nuevos lo subieron); microseguros en Colombia (32,3% de siniestralidad: para un evento frecuente, asegurar es caro).
- Lo que no cubre, dicho: enfermedad, paros, vacaciones, mercancía que se pudre (la deuda se corre pero no se achica).
- Cuántos puede impactar (2 líneas, sección 3).

### Página 4. Los números (unas 420 palabras + tabla 4)

- Tabla 4 con las seis respuestas del caso (sección 6), cada una con su supuesto y su fuente en la misma fila.
- Párrafo: el costo del plazo es casi cero y lo que decide es el impago (tabla E1 de `12-mecanismos` en una línea).
- Párrafo "si el modelo no cierra, lo digo": el ingreso depende de una tarifa sin precedente; con $2.000 harían falta 5.000 vendedores. Lo que no cierra es el precio que paga el mayorista, no el riesgo.
- Dos líneas de E2: por qué no es negocio y por qué igual tiene tope.

### Página 5. Descartes, riesgo y lo que haría el lunes (unas 520 palabras)

- Descarte 1, A (sección 7.1), 150 palabras.
- Descarte 2, F (sección 7.2), 130 palabras.
- Una línea: "También consideré C, B, D, refinanciar la deuda del gota a gota y una app de préstamo; están en el anexo F con la razón de cada descarte."
- Riesgo real (sección 7.3), 130 palabras.
- Validación de la primera semana con criterios de muerte (sección 7.4), 100 palabras.

---

## 6. Plan de números (lo que el modelo tiene que calcular)

Recomendación: un script nuevo en inglés, `models/business_plan.py`, con los supuestos arriba como constantes y cada uno con su fuente en un comentario, más una tabla en el anexo B. Chequeo rápido hecho con esos supuestos (scratchpad `brief_numbers.py`): da los órdenes de magnitud de abajo. El modelo final debe recalcular todo.

### 6.1 Las seis respuestas

| # | Pregunta del caso | Propuesta de respuesta | Supuesto y fuente |
|---|---|---|---|
| 1 | Inversión inicial | Unos $10,8 millones: SAS y registro (unos $1 millón), abogado para la cláusula, E2 y la Ley 2439 (unos $3 millones), herramientas del bot y del disparador (unos $0,5 millones; lo programo yo), tarjetas y acuerdos impresos ($0,3 millones), transporte del piloto ($1 millón), reserva de E2 con tope de $5 millones | Estimaciones propias; verificar la tarifa de registro de la Cámara de Comercio de Cali antes de ponerla. La reserva de $5 millones sale de `12-mecanismos`, 2.10 |
| 2 | Costos mensuales | Meses 1 a 3 (piloto): unos $4 millones. Desde el mes 4: $10 millones (yo, una persona de campo, tecnología, contabilidad y abogado, transporte) | $10 millones es la convención de `unit_economics.py` y `bad_day_mechanisms.py`; el desglose es estimación propia |
| 3 | Cuánto gano por usuario | Tarifa de $4.000 por vendedor activo al mes, pagada por el mayorista (rango $2.000 a $6.000), menos unos $300 de mensajería: contribución de unos $3.700. El piloto (meses 1 a 3) es gratis. No pago: en E1 no presto, así que el impago del aplazado (2%, 5% o 10%) lo carga la cadena: $16.120 a $80.600 al año por vendedor con fiado de $62.000 y la mitad sin pagar. En E2 sí es mío: con 1% de impago del minorista pierdo $14.537 por vendedor al año | Tarifa sin precedente [S]. Anclas: $4.000 es 0,26% de lo que compra al mes un vendedor con fiado de $62.000; la cláusula le cuesta al mayorista de 1% a 4% del margen que deja cada vendedor (margen de 10% a 20% [S]). Mensajería: estimación propia, verificar precio de WhatsApp Business en Colombia. Impago: sin dato colombiano; referencia, mora del microcrédito 6,9% (jul 2026) |
| 4 | Usuarios e ingresos | Mes 3: 45 vendedores (1 mayorista, 3 minoristas con 15), ingreso $0. Mes 6: 400, unos $1,6 millones al mes. Mes 12: 1.500, unos $6 millones al mes | Supuestos de ritmo comercial [S]; 2.500 vendedores serían, por ejemplo, 125 minoristas con 20 cada uno |
| 5 | Break-even | Unos 2.700 vendedores activos ($10 millones / $3.700), hacia el mes 20 o 21 si después del mes 12 se suman unos 150 al mes | Cálculo propio sobre los supuestos de 3 y 4. Con tarifa de $2.000 serían 5.000; con $6.000, unos 1.750 |
| 6 | Cuánto necesito para sobrevivir | Del orden de $100 a $105 millones (inversión inicial más pérdidas acumuladas hasta el break-even; el peor punto acumulado da unos $104 millones en el chequeo rápido). De dónde: capital semilla (fellowship o ángel) y, antes de eso, que el primer mayorista pague el piloto si ve la retención de vendedores | Cálculo propio. Decir en el PDF que el modelo no cierra en 12 meses y por qué |

### 6.2 Supuestos clave y de dónde salen

| Supuesto | Valor | Fuente o razón |
|---|---|---|
| Días de disparo | 26 de 294 días de venta (8,8%) | Cálculo propio sobre IDEAM, estación 0026055120, 27 sep 2025 a 26 sep 2026, 5 mm o más entre 7:00 y 18:59, lunes a sábado |
| Umbral | 5 mm | Convención de `12b`; con 10 mm son unos 15 días; calibrar con ventas reales |
| Fiado diario | $62.000 como cota; $30.000 [S] | Ventas diarias de un ambulante (unos $95.000) menos ingreso mixto (unos $33.000); DANE vía frentes 01 y 08; media; no medido para carritos |
| Parte no pagada el día de lluvia | 50% o 100% | [S] |
| Plazo promedio del puente | 2,5 días | Devolución en tercios más domingos |
| Costo del dinero del mayorista | 20% E.A. [S] | Irrelevante: el plazo cuesta unos $1.000 a $2.000 por vendedor al año |
| Impago del aplazado | 2%, 5%, 10% [S] | Sin dato colombiano. Mientras quede por debajo de 10%, la cadena carga el choque más barato que el puente informal más barato conocido (10% en el día, Pérez Cruz 2025) |
| Ingreso mixto del ambulante | Unos $1,0 millón al mes; unos $38.000 por día de venta con 26 días | DANE, EMICRON 2025, Cuadro 24; cálculo propio. Usar una sola convención en todo el PDF (síntesis 10.3, #19) |
| Usura de referencia | 29,24% E.A. (ordinario); 88,13% (popular productivo urbano) | SFC, Resolución 1260 de 2026 (sep 2026; cambia el 1 de octubre) |

Número para mostrar el valor al usuario (no es ingreso nuestro): lo que le cobraría el puente informal más barato por el mismo plazo al año, de $39.000 a $161.200 por vendedor, frente a $0 con E (`bad_day_mechanisms.py`).

---

## 7. Descartes y riesgo

### 7.1 Descarte 1: A "La ventanilla del tendero" (microcrédito escalonado cobrado en la tienda)

- **Por qué parecía buena.** Fue la mejor de mi primera ronda (27 de 40 en mi propia revisión adversarial). Tomaba al usuario con más gota a gota (61,8% de los ambulantes que piden crédito), copiaba del informal lo que funciona (renovar como premio, cuota diaria, recomendación; 82% llega al prestamista por recomendación en Perú) y usaba a la tienda como punto de pago sin visitas de cobro, compatible con la Ley 2300.
- **Qué la mató.** (1) Mis propios números: con montos de ambulante ($100.000 a $250.000) y precio legal, el neto por usuario es $5.857 al año con 1% de pérdida por ciclo y -$2.143 con 1,5%; cubrir $10 millones de costo fijo pedía unos 20.500 usuarios activos, cerca de 80% de los ambulantes que el DANE registra en el gota a gota de 24 ciudades (`unit_economics.py`). (2) La informante: en Cali el cobro del informal es la amenaza, y un prestamista legal sin amenaza queda de último cuando no alcanza. (3) El campo cambió la pregunta: el vendedor de carrito ya tiene crédito diario gratis; no le falta un préstamo, le falta que el fiado aguante un día. (4) Un evaluador la leería como las respuestas 3 y 7.

### 7.2 Descarte 2: F "El día de lluvia pagado" (seguro paramétrico del fiado)

- **Por qué parecía buena.** Salió del mismo hallazgo y usa el mismo disparador público, sin reclamos ni verificación de ventas. Casaburi y Willis dicen cómo venderlo (cobrar la prima en el día bueno) y hay precedente de seguro paramétrico para trabajadoras informales en India (mencionar sin cifras: la fuente es débil).
- **Qué la mató.** La frecuencia. Un evento que pasa dos veces al mes no se asegura barato: pagar el fiado entero cada día de disparo exige una prima comercial de unos $16.636 por día de venta, 43,8% del ingreso mixto diario; cubrir solo una pérdida de $15.000 cuesta $4.025 diarios (10,6%). Una prima de $500 compra un pago de unos $1.863 (`bad_day_mechanisms.py`, con la siniestralidad de 32,3% de los microseguros colombianos, RIF 2025). Además necesita una aseguradora vigilada, pide cédula (contra lo que dijeron los vendedores sobre la DIAN) y la demanda de seguro de lluvia es baja aun a buen precio (Cole et al. 2013). La lección que me llevé a E: las pérdidas pequeñas y frecuentes se suavizan con plazo; se aseguran las raras.

### 7.3 Riesgo real principal

**Al de arriba hoy no le duele el día de lluvia.** Hoy el vendedor toma el gota a gota y le paga al minorista, y el minorista le paga al mayorista: el choque lo absorbe el vendedor a 20%, fuera de la cadena. Con E, el mayorista carga un plazo y un impago que hoy no carga, a cambio de algo diferido: que sus vendedores no se hundan y dejen de trabajar, como la vendedora de arepas. Y los proveedores se están endureciendo con las tiendas (comunicado de Fenalco 2026, sin metodología: citarlo con esa advertencia o no citarlo). Si el mayorista no ve la pérdida, no firma, y el ingreso del modelo es cero.

Riesgos que se nombran en una línea cada uno:
- **El hallazgo es de segunda mano.** Hace falta que al menos un vendedor cuente en primera persona "no le pude pagar y saqué un gota a gota". Sin eso, el hallazgo va como hipótesis.
- **Que el minorista ya espere.** Entonces E no agrega nada y el gota a gota se toma por otra razón (pérdida o gasto del hogar).
- **Riesgo de base:** llueve en Meléndez y no en el carrito, o al revés.
- **Mercancía perecedera:** la deuda se corre, no se achica.

### 7.4 Validación de la primera semana (criterios que matan la propuesta)

| Pregunta (pasado concreto) | A quién | Sigue si... | Se cae si... |
|---|---|---|---|
| "La última vez que llovió y no vendió, ¿qué le dijo el que le fía esa tarde? ¿Le esperó o le exigió ese día? ¿Al otro día le fió?" | Vendedor | 4 de 6 describen que se exige el mismo día o se corta el fiado | El minorista ya espera un día |
| "¿Usted le paga a su proveedor de contado cada día? Cuando llueve, ¿qué hace esa noche? ¿Cuántos vendedores perdió este año por deudas?" | Minorista (comerciante, no prestamista) | Paga a diario hacia arriba y ha perdido vendedores | Tiene plazo holgado y no pierde vendedores |
| "Lo que no vendió ese día, ¿se le dañó o lo vendió al otro día? ¿Cuánto saca fiado en un día normal?" | Vendedor | La mayor parte no se daña | La mayor parte se daña (entonces gana la devolución de lo no vendido) |
| Un mayorista acepta un piloto de 4 semanas con 3 minoristas | Mayorista | Acepta, aunque sea sin pagar en el piloto | Nadie acepta: pasar a E2 acotado o volver a C |

Métricas del piloto: vendedores inscritos por minorista, impago de lo aplazado (umbral para seguir: menos de 5%), vendedores que siguen activos a las 8 semanas frente a los que no entraron, y si los días de disparo coinciden con los días que los vendedores recuerdan como malos.

---

## 8. Anexos (desde una página nueva titulada "ANEXOS")

| Anexo | Contenido |
|---|---|
| A. Prototipo | El disparador funcionando: script que lee la API del IDEAM (datos.gov.co) y devuelve "hoy fue día de lluvia" con los mm de la estación; captura de su salida para una fecha real de disparo (por ejemplo, un día de octubre de 2025). Maqueta del mensaje de WhatsApp al minorista y al mayorista, la tarjeta física del vendedor y la cláusula de una página. Qué hace hoy, qué no hace (no hay bot conectado ni conciliación automática), cuánto tomó, con qué herramientas. Si nadie de campo lo vio, decirlo: "no se lo he mostrado a vendedores" |
| B. Modelo financiero | Tabla de las seis respuestas con todos los supuestos; sensibilidad a la tarifa ($2.000, $4.000, $6.000) y al impago (2%, 5%, 10%); tabla E1 y E2 de `bad_day_mechanisms.py`; tabla de usura de `usury_cap.py`; economía de A de `unit_economics.py` (sostiene el descarte). Nombres de los scripts |
| C. Método y uso de IA | Cómo investigué: 16 frentes de investigación con agentes de IA (Claude Code) sobre fuentes abiertas, cada uno con una tabla de verificación; una revisión adversarial que puntuó mis propios mecanismos y encontró 19 afirmaciones sin respaldo, que corregí o saqué; transcripción local de las notas de voz con Whisper; cálculos propios en Python sobre datos abiertos (DANE, IDEAM, SFC). Qué decidí yo: el cambio de A a E tras el campo, qué cifras no usar y por qué. Cifras que circulan y no usé (tabla 1.4 de la síntesis, resumida). El error del boletín EMICRON 2024 (p. 32) y cómo lo evité leyendo el anexo |
| D. Notas de campo | Informante: hallazgos anonimizados de las dos notas de voz, con cómo citarla y sus límites (segunda mano, sin muestreo, sesgo a lo memorable). Colaborador: transcripción del resumen oral y sus cinco hallazgos, con la advertencia de que no hay número de vendedores ni citas por persona. Guía de preguntas usada y reglas (sin contacto con prestamistas, tercera persona, línea 165 del GAULA). Nada de nombres ni detalles que identifiquen. No citar la tercera ronda a la informante: no fue respondida |
| E. Referencias | Lista completa con URL, agrupada en primarias (DANE, SFC, Banca de las Oportunidades, IDEAM, normas), académicas (WIEGO, Martínez Benavides, Martínez y Rivera-Acevedo, Karlan et al., Casaburi y Willis, Cole et al., Battaglia et al., Brune et al., Pérez Cruz, Palomino-Martínez, Apuntes 2026, IPE 2024) y prensa o empresas (marcadas como tales) |
| F. Mecanismos considerados | Tabla A a F con una línea cada uno, su puntaje de 8 criterios y la razón de descarte; los descartes de la síntesis (adelanto por QR, refinanciar al gota a gota, app de préstamo, cuaderno de fiado digital) |
| G. Datos de lluvia | Estación, periodo, umbral, días con datos, huecos (febrero de 2025, marzo de 2026 sospechoso, duplicados), rachas, meses con más disparos y la estación de respaldo |

---

## 9. Reglas que el redactor no puede romper

- Nada de raya ni semirraya en ningún lado, tampoco guion con espacios. Rangos con "a".
- Primera persona singular. Al colaborador y a la informante se los describe así, sin nombres ni barrios.
- Solo cifras confirmadas o de confianza alta, más cálculos propios rotulados. No usar: 12 millones, 4,4 millones, 1 de cada 4, $2.500 millones diarios, 666,5%, "fiado cayó 54%", 77% rural, 90% del IPES, "3 a 4 veces" de la informante, cifras de SEWA, 21,6%, los 7,6 créditos por persona como dato, 46% de corresponsales inactivos (usar 584.728 de 1.088.053 si hace falta), la liquidación de Juancho Te Presta (decir reorganización), 5 a 6 centavos por peso, siete millones de reportados.
- Cifras de confianza media (31 cobradiarios, 11,6% de crédito de proveedores en Cali con CV de 16,6%, Fenalco 2026, Tienda Pago) van al anexo o, si entran al cuerpo, con su advertencia.
- La usura cambia el 1 de octubre: poner "septiembre de 2026" junto a cada tope.
- El PDF se llama exactamente `MAKERS_SANTIAGO_ESPINOSA_CALI.pdf` y el cuerpo no pasa de 5 páginas carta.
