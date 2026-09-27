# Brief de arquitectura: ángulo VIABILIDAD PRIMERO

Autor: arquitecto de viabilidad (uno de tres). Fecha: 27 sep 2026, madrugada. Para: quien escriba `MAKERS_SANTIAGO_ESPINOSA_CALI.pdf`.

Base leída: rúbrica (`docs/02`), caso y plataforma (`docs/00`, `docs/01`), síntesis completa (`docs/research/00-sintesis.md`, secciones 1 a 11.6; no existe 11.7), frentes 12, 12a y 12b, campo (`docs/06`, `docs/07`, `docs/09`) y los modelos. La tercera ronda con la informante (`docs/08`) no tiene respuesta: no se cita en ninguna parte.

Modelo nuevo de este brief: `models/fiado_bridge_viability.py` (código en inglés, corre con `python3`). Usa una base de costos de piloto de una persona, no la convención de $10 millones al mes de `unit_economics.py` y `bad_day_mechanisms.py`. Esa diferencia se explica en la sección 6.

Regla de escritura para todo el PDF: primera persona singular, español directo, sin rayas ni guiones espaciados, rangos con "a" (20 a 30%). Cada cifra con fuente; cada cálculo propio rotulado "cálculo propio" con su script.

---

## 1. La tesis en una frase

> **El gota a gota no le gana al sistema formal por prestar plata, sino por vender tiempo: el vendedor de carrito ya tiene un crédito diario que funciona y es gratis, el fiado de su minorista, y el gota a gota entra la tarde en que la lluvia rompe ese fiado, cobrando 20% por uno a tres días de plazo que la propia cadena podría dar casi gratis; el formal no lo ve porque ofrece dinero a 30 días donde lo que falta son 48 horas.**

Por qué es tesis propia y no resumen de reportes:
- **Qué falla en el formal:** vende producto (dinero, en cuota mensual, con costo fijo por operación). 87,2% del crédito formal se paga en cuota mensual (Encuesta de Demanda 2022, p. 58); originar un microcrédito cuesta $1.117.131 fijos (Asobancaria BE 1475, 2025). Ninguna de las dos cosas sirve para un hueco de 1 a 3 días.
- **Qué hace bien el informal:** tiene dos piezas y casi todos miran solo la cara. La pieza sana es el fiado de mercancía: diario, sin interés, basado en conocer a la persona y con la exclusión como sanción (campo 09; WIEGO 2014; Martínez Benavides 2021). La pieza cara, el gota a gota, está ahí la tarde del choque, sin preguntas, y cobra según los días de venta (informante: seis días a la semana y no cobra el día que ella no sale).
- **Refutable:** se cae si el minorista ya espera un día cuando llueve (entonces el gota a gota se toma por otra cosa). Esa es la pregunta de campo E1 del frente 12.

Frase de apoyo para la página 1 (cálculo propio, `models/usury_cap.py`): en pesos por día, un préstamo legal se ve apenas 12 a 15% más barato que el gota a gota ($3.436 frente a $4.000 diarios por cada $100.000 en 30 cuotas). Competir por precio no mueve al usuario. Competir por tiempo sí cambia el problema.

---

## 2. El mecanismo elegido

**Elección: E1 "El puente del fiado", refinado por viabilidad.** Es el mecanismo E de `12-mecanismos-dia-malo.md` con cuatro decisiones de viabilidad que lo cambian:

1. **No presto en la fase 1.** La variante E2 (prestarle el flotante al minorista) se descarta como línea de ingreso: con 1% de impago del minorista pierde $14.537 por vendedor al año (`bad_day_mechanisms.py`). Queda solo como herramienta con tope de capital propio si un minorista compra de contado y no hay mayorista que cargue el plazo, y no entra al plan base.
2. **Pagador flexible:** paga quien carga el plazo. Lo ideal es el mayorista (tiene balance y volumen, WIEGO muestra que el minorista también debe); si no hay mayorista dispuesto, paga el minorista. El precio es el mismo: $4.000 por vendedor activo al mes, con el primer mes gratis.
3. **Base de costos de piloto de una persona** ($2,53 millones al mes, con salario mínimo para mí), no de un equipo de $10 millones.
4. **No hay contacto con el vendedor.** El bot solo habla con el minorista y el mayorista. El vendedor se entera por su minorista y por una tarjeta física. Esto elimina la Ley 2300 del camino (no hay cobranza) y respeta lo que dijeron en campo sobre no dejar rastro ante la DIAN.

**En una frase:** cuando la estación del IDEAM en la Universidad del Valle marca 5 mm o más de lluvia entre 7 a. m. y 7 p. m., el vendedor que ya tiene historial con su minorista paga el fiado de ese día en tercios durante los tres días de venta siguientes, sin recargo; el minorista corre en la misma medida su pago al mayorista; yo pongo el disparador público, la regla y el registro, y cobro una tarifa a quien carga el plazo. Nadie le presta plata al vendedor y ninguna plata pasa por mi empresa.

### Puntajes 1 a 5 en los 8 criterios

Los de A, B, C y D son los de la revisión adversarial (síntesis 10.2). Los de E y F son míos, con el mismo criterio de dureza.

| Criterio | E1 puente del fiado (elegido) | A ventanilla del tendero | C cuota diaria de la deuda mensual | F día de lluvia pagado |
|---|---|---|---|---|
| 01 Efectividad (causa raíz, un solo mecanismo) | 4 | 3 | 3 | 2 |
| 02 Especificidad | 4 | 4 | 3 | 3 |
| 03 Creatividad | 4 | 2 | 3 | 3 |
| 04 Diagnóstico | 4 | 4 | 3 | 4 |
| 05 Fuentes | 4 | 4 | 3 | 4 |
| 06 Trazabilidad | 5 | 4 | 3 | 3 |
| 07 Juicio cuantitativo | 3 | 3 | 2 | 3 |
| 08 Descartes y autocrítica | 4 | 3 | 3 | 3 |
| **Total (de 40)** | **32** | **27** | **23** | **25** |

Por qué E1 frente a los demás, en criterio de viabilidad:
- **Frente a A:** A presta a precio legal montos de ambulante y pierde plata (neto de -$26.143 a +$5.857 por usuario al año; necesita unos 20.500 usuarios activos para cubrir costos; síntesis 6.0 y 10.4.5). E1 no presta, así que no tiene pérdida de crédito propia, no necesita capital de préstamo y no entra a la fila de pago donde el acreedor sin amenaza queda de último (informante, 07 hallazgo 7).
- **Frente a C:** C depende de un precio que ningún acreedor ha pagado y casi no llega al ambulante (solo 22,5% de los ambulantes que piden crédito va a una entidad regulada, EMICRON ambulantes 2025). E1 tiene el mismo problema de "quién paga", pero el pagador está en la misma cadena y tiene un beneficio medible (retener vendedores).
- **Frente a F:** F le cobraría al vendedor de 6% a 44% de su ingreso diario por un evento que pasa unas dos veces al mes (sección 7).
- **Nota 07:** le pongo 3 y no 4 a E1 porque el monto del fiado, la tarifa y el impago del aplazado no están medidos. Lo que sube la nota es mostrarlo sin maquillaje.
- **Nota 04:** 4 y no 5 porque el hallazgo de campo es un resumen oral de un colaborador, sin número de vendedores ni citas por persona.

### A qué respuesta predecible se parece y qué lo hace distinto en mecanismo

Se parece a la **6 (crédito de proveedor o BNPL para inventario)** y, por el registro, a la **9 (cuaderno de fiado digital)**. En el mercado se parece a Tienda Pago ("págalo en 7 días") y al plazo de BEES. Lo distinto está en el mecanismo:

1. **No crea crédito.** El crédito ya existe, es gratis y lo da otro. La 6 alarga el plazo estándar o abre una línea; E1 deja el plazo en cero días y solo lo abre cuando pasa un evento.
2. **Lo activa un dato público, no una solicitud.** Nadie pide nada y nadie negocia: la decisión la toma la lluvia medida por el IDEAM. Eso quita el "¿de verdad no vendió?" que hoy obliga al minorista a cobrar el mismo día.
3. **Carga el plazo quien hoy le pasa el choque al vendedor**, no un financiador nuevo.
4. **Ataca el momento en que nace el gota a gota** (la tarde del día malo), no la necesidad de crecer.
5. **El usuario no paga nada.** En la 6 y en la 9 el usuario o el tendero pagan por el crédito o por la app.
6. **El registro no es el producto.** El cuaderno digital (9) murió como negocio (OkCredit, Treinta; síntesis 7.3); aquí el registro solo existe para cerrar el puente, unas dos veces al mes.

Prueba para el anexo (solo si se hace antes de entregar, y decir el resultado tal cual): pegar el caso más el hallazgo de campo en tres modelos de IA y ver si alguno propone "aplazamiento del fiado atado a un índice de lluvia, pagado por la cadena". Si alguno lo propone, la originalidad está en el hallazgo, no en el mecanismo, y se dice.

---

## 3. El usuario exacto

**Quién:** vendedor de carrito que cada mañana saca fiado, sin interés, la mercancía del día a un minorista que le surte, y le paga en la tarde. Trabaja en la calle, sin local, con ingreso diario. Para entrar al puente necesita al menos 4 semanas de historial con ese minorista [supuesto], porque la flexibilidad a clientes nuevos subió el impago en Barranquilla y Cartagena y a clientes con historial lo bajó (Brune, Giné y Karlan 2025; Battaglia et al. 2023).

**Dónde:** corredor de universidades del sur de Cali, alrededor de la estación Universidades del MIO, donde se hicieron las conversaciones de campo. La estación del IDEAM usada como disparador está en el campus de Meléndez de la Universidad del Valle, en la misma zona (distancia no medida: decirlo).

**Cuántos, con fuente, sin inventar:**
- Colombia, 24 ciudades: 286.061 vendedores ambulantes en 2025; de los que pidieron crédito, 61,8% fue a un gota a gota, frente a 11,3% en tiendas y panaderías (DANE, EMICRON Vendedores ambulantes 2025, Cuadros 18, 18.1 y 24; EMICRON Panaderías y tiendas 2024, Cuadro H.4.1; alta).
- Cali: en una encuesta a 300 vendedores ambulantes del centro y de la galería Santa Elena, 51,3% de su deuda era con gota a gota, a 20,4% mensual en promedio, y 27% tenía varios préstamos a la vez (Martínez y Rivera-Acevedo, Data in Brief 2019, datos de 2016; alta, dato viejo: decir el año).
- Cali A.M.: el crédito de proveedores es 11,6% de los micronegocios que pidieron crédito, frente a 3,0% en las 24 ciudades (cálculo propio sobre EMICRON 24 ciudades 2025, Cuadro H.4_24C; CV de 16,6%, precisión baja: decirlo).
- **No existe una cifra de cuántos vendedores de carrito hay en Cali ni cuántos sacan fiado.** No se estima en el cuerpo. El tamaño del piloto se construye de abajo hacia arriba: minoristas por vendedores por minorista (sección 6).
- Opcional, solo en anexo: en Cali A.M., 3.130 micronegocios acudieron al gota a gota en 2024 (8,8% de los que pidieron crédito) frente a 4.105 que usaron crédito de proveedores (cálculo propio de este brief sobre el mismo Cuadro H.4_24C; CV de 18,0% y 16,6%, precisión baja). Sirve para decir que en Cali el crédito de la cadena pesa tanto como el gota a gota, pero con esa precisión no va al cuerpo.

**Qué problema específico resuelvo:** el primer gota a gota que se toma para no perder el fiado de mañana después de un día sin ventas por lluvia. No resuelvo la necesidad del hogar, la enfermedad, las vacaciones universitarias ni la deuda que ya existe con un gota a gota. Decirlo en el PDF.

---

## 4. El mecanismo paso a paso

### Tabla para el PDF (versión compacta, 9 filas)

| Momento | Quién | Qué hace | Con qué | Dónde está la plata |
|---|---|---|---|---|
| Semana 0 | Yo | Constituyo una SAS de servicios de información. Programo un script que cada noche lee la API del IDEAM (estación Universidad del Valle; respaldo: Base Aérea Marco Fidel Suárez) y un bot de WhatsApp para minoristas y mayoristas. Un abogado revisa la cláusula | SAS (Ley 1258 de 2008), datos.gov.co, WhatsApp | Capital propio en la cuenta de la SAS |
| Semana 1 | Yo, un mayorista o un minorista | Propongo la "cláusula de lluvia": en día de disparo, lo que el minorista fió a sus vendedores ese día se paga en los tres días de venta siguientes, sin recargo. Primer mes gratis; después, $4.000 por vendedor activo al mes | Una página de acuerdo comercial y el dato público, que él puede revisar | Nada se mueve |
| Semana 1 | Minorista | Escoge a los vendedores que entran (4 semanas de historial) y se lo dice a cada uno de palabra, con una tarjeta | Su palabra, tarjeta física | Nada se mueve |
| Día normal | Vendedor y minorista | Igual que hoy: fiado en la mañana, pago en la tarde | Mercancía, efectivo o Nequi | Bolsillo del vendedor, luego caja del minorista |
| Día de lluvia, 7 a 9 p. m. | Mi programa | Con el dato publicado (rezago de cerca de 1,5 horas), calcula si hubo 5 mm o más. Si sí, avisa: "Hoy fue día de lluvia (Univalle, 12 mm). Rige la cláusula" | API del IDEAM, WhatsApp | Nada se mueve |
| Esa noche | Minorista | Responde con quién no pudo pagar y cuánto ("Pedro 45") | WhatsApp | La deuda del vendedor sigue siendo con el minorista, con otra fecha |
| Días de venta 1 a 3 siguientes | Vendedor y minorista | El vendedor paga lo del día más un tercio de lo aplazado; el bot concilia y confirma "puente cerrado" | Efectivo o Nequi | Bolsillo del vendedor, caja del minorista, pago corrido al mayorista |
| Si no cierra en 5 días de venta | Minorista | Decide él, como hoy con su fiado. Yo solo marco al vendedor como no elegible para el siguiente disparo. Nunca cobro ni contacto al vendedor | | La pérdida es de quien carga el plazo |
| Fin de mes | Mayorista o minorista | Paga la tarifa por vendedor activo | Transferencia | Única entrada de mi empresa |

Reglas que van debajo de la tabla (una línea cada una):
- Tope de 3 días de disparo seguidos y saldo aplazado máximo de 2 fiados por vendedor [supuesto]. Cubre todas las rachas observadas: en los últimos 12 meses hubo 21 rachas de un día y 3 de dos, ninguna de tres o más (cálculo propio sobre IDEAM, frente 12).
- Si falta el dato de las dos estaciones, el minorista puede declarar el día, como máximo una vez al mes, y se revisa cuando llegue el dato.
- Sin recargo para el vendedor, siempre: cobrarle a cambio de algo que se activa con la lluvia se parecería a un seguro sin licencia (frente 12b).
- Extensión que se prueba solo después del mes 4 y solo si el impago del aplazado queda bajo 3%: un día malo "ganado" al mes sin lluvia (enfermedad, choque familiar), para vendedores con 8 semanas sin atrasos. Viene del caso de la vendedora de arepas (informante) y de Battaglia et al. No entra al plan base.

### Cómo UNA pieza resuelve los cuatro puntos

La pieza es una sola: **un dato público de lluvia que corre las fechas de pago de una cadena de fiado que ya existe.**

1. **No soy entidad financiera.** No presto ni aseguro. El crédito ya existe (el fiado) y lo dan comerciantes a comerciantes, sin interés, así que no hay usura que calcular. No hay prima ni indemnización (no es seguro) y no hay desembolso al vendedor (no es crédito mío). La plata del vendedor nunca pasa por mi cuenta, así que no hay captación (Decreto 1981 de 1988). Lo que vendo es un servicio de información: disparador, regla y registro. Opera desde el día 1 con una SAS. Lo que queda para el abogado: si una regla de aplazamiento pagada por la cadena puede leerse como seguro (respuesta prudente: el vendedor no paga nada y yo no indemnizo a nadie).
2. **Ingreso diario sin ahorro.** El mecanismo solo actúa el día en que no hubo ingreso, que es exactamente cuando la falta de ahorro obliga a pedir prestado. La devolución va por tercios dentro del ritual que ya tiene (pagarle al minorista cada tarde): no hay cuota nueva, ni calendario mensual, ni saldo mínimo.
3. **Soy un desconocido de 22 años.** El vendedor no tiene que confiar en mí: ni siquiera me conoce, y su trato sigue siendo con el minorista de siempre (la recomendación y la paciencia viven en esa relación, informante 07 hallazgo 1). Al minorista tampoco le pido que me crea: el disparador es un número del IDEAM que puede revisar solo, el primer mes es gratis y no pone plata en mis manos. Tengo que ganarme a unos pocos minoristas y a un mayorista, no a miles de vendedores. Y como quien recomienda no quiere cobrar (informante 07 hallazgo 2), nadie en la cadena asume un papel nuevo de cobrador.
4. **El problema ya tiene soluciones.** Todas venden dinero (bancos, microfinancieras, Nequi, programas públicos) o, en el agro, seguros. Ninguna corre la fecha de un crédito que ya existe con un dato público (no encontrado en las fuentes revisadas, frente 12b 6.3; búsqueda limitada, decirlo). Lo que aprendí de ellas y usé: el crédito atado a mercancía que rota se paga muy bien (AB InBev, 93,6% al día, 20-F 2025); mover el pago en el tiempo sube la adopción más que indemnizar (Casaburi y Willis 2018: 72% frente a 5%); el mercado ya paga caro este puente ("diario anticipado" a 10% en el día en Corabastos, Pérez Cruz 2025).

---

## 5. Esquema página por página

Presupuesto total del cuerpo: unas 2.450 palabras más 4 tablas compactas. Letra de 10 a 10,5 pt, márgenes de 2 cm, tablas a 8,5 pt. La plantilla de prueba de `report/informe.html` sirve para medir cuántas palabras caben por página: medir antes de escribir y recortar prosa, no tablas.

### Página 1. Diagnóstico: el tamaño, el daño y por qué el formal no llega (unas 560 palabras, sin tabla)

- Encabezado: título, nombre, Cali, fecha. Debajo, la tesis de la sección 1 en negrita (una frase).
- **Tamaño (unas 150 palabras).** 5.297.252 micronegocios con 6.879.489 personas ocupadas (EMICRON 2024, Cuadro I.1). 14,2% pidió crédito y de ellos 22,9% fue a un gota a gota: 160.724 negocios, un piso oficial (EMICRON 2024, H.2 y H.4). El usuario no es el tendero del enunciado: entre ambulantes que piden crédito, 61,8% va al gota a gota; en tiendas, 11,3%. Cali: 51,3% de la deuda de ambulantes con gota a gota a 20,4% mensual (datos de 2016). Nota de rigor en una línea: el boletín del DANE dice que 77% del crédito rural es gota a gota, pero el anexo muestra 9,8% (síntesis 1.3); cité el anexo.
- **Consecuencias (unas 120 palabras).** La trampa: deuda que paga deuda ("para pagarle a uno, se meten en otro", informante; El País Cali 2018). Pagarle la deuda al prestamista no saca de la trampa: la mayoría vuelve a deber en seis semanas (Karlan, Mullainathan y Roth 2019). La coerción: la amenaza es la principal forma de cobro (UNODC 2025, Costa Rica) y en los casos que conoce la informante de Cali es lo primero que aparece. El caso de la vendedora de arepas que pidió para crecer y, tras un choque, "ni volvió a sacar el negocio" (segunda mano, como ilustración).
- **Por qué falla el formal (unas 170 palabras).** No es el precio: la usura del crédito popular productivo subió de 52,89% a 88,13% E.A. y la SFC no vio más acceso (Resolución 1260 de 2026; SFC 2025). No es la falta de cuentas: 96,5% de los adultos tiene un depósito y 8,0% pidió a un banco (RIF 2025; Findex 2025). Es la forma: cuesta $1.117.131 originar cada microcrédito y uno de 1 SMMLV cuesta 100,3% de lo prestado (Asobancaria BE 1475); 87,2% se paga en cuota mensual. Y el usuario ni pide: 42,5% no pide por miedo a endeudarse, 14,6% por requisitos, 6,5% por la tasa (EMICRON 2024, H.3). Cálculo propio: en pesos por día el legal se ve solo 12 a 15% más barato.
- **Qué hace bien el informal (unas 120 palabras).** Llega la misma tarde, sin papeles; cobra en los días de venta (informante: seis días, no el día que ella no sale; Palomino-Martínez 2025); renueva al que paga (IPE 2024: 93% paga, 82% llega por recomendación). Y hay una pieza que casi nadie mira: el fiado de mercancía, diario, sin interés y con la exclusión como sanción (Martínez Benavides 2021; WIEGO 2014, 38% de los ambulantes dice que el crédito del proveedor es "muy importante").

### Página 2. Lo que encontré y el día que rompe la cadena (unas 480 palabras más Tabla 1)

- **Método de campo en dos líneas, honesto.** Conversaciones con vendedores de carrito en la estación Universidades del MIO, hechas por un colaborador en mi nombre en la mañana del 26 sep 2026; tengo su resumen oral, no el número exacto de vendedores ni citas por persona. Una informante de Cali que conoce varios casos de amigos y familiares (dos notas de voz, 27 sep 2026; segunda mano, sin muestreo). No contactamos prestamistas. Yo no entrevisté vendedores en persona.
- **Hallazgos de campo (unas 200 palabras).** (1) La cadena mayorista, minorista, vendedor: el vendedor saca fiado sin interés lo del día. (2) "Hay días en que... llovió, entonces nadie va... No le puedo pagar. Y ahí es cuando entran con un gota a gota", y se vuelve circular. (3) No se formalizan: primero no saben cómo, luego no quieren impuestos (DANE: 93,3% de los ambulantes no tiene RUT). (4) De la informante: la recomendación compra paciencia, quien recomienda no quiere cobrar, y la familia financia la salida.
- **El dato que lo convierte en diseño (unas 120 palabras).** Cálculo propio sobre la estación del IDEAM en la Universidad del Valle: 26 de 294 días de venta con 5 mm o más de lluvia diurna en los últimos 12 meses (unos 2 al mes), concentrados en octubre y mayo; 21 rachas de un día y 3 de dos, ninguna más larga. El choque es frecuente y corto. Lo que falta ese día no es capital, es tiempo. El gota a gota se toma para proteger la relación con quien fía, porque la sanción del fiado es la exclusión ("que no vuelva por acá").
- **La pregunta que cambió mi propuesta (una línea):** de "¿cómo le presto más barato?" a "¿cómo evito que un día de lluvia rompa un fiado que ya funciona?".
- **Tabla 1. Qué existe y qué deja (6 filas, unas 90 palabras):** microfinancieras (cuota mensual, ticket promedio de $9,96 millones, RIF 2025); Nequi (cuota mensual con fianza: $1 millón queda en $1.119.000, simulador oficial); crédito de proveedor tipo Tienda Pago y BEES (plazo fijo sobre mercancía; fuente de la empresa y 20-F); microseguros (siniestralidad 32,3%, RIF 2025; ningún producto para el día de lluvia urbano); "diario anticipado" (10% en el día, Pérez Cruz 2025); gota a gota (20% por préstamo, llega esa tarde). Columna final: "qué me enseñó".
- **Una línea de lección:** todos venden dinero o indemnización; nadie mueve la fecha del crédito que ya existe.

### Página 3. La propuesta: el puente del fiado (unas 470 palabras más Tabla 2)

- **Usuario exacto (unas 90 palabras):** sección 3 de este brief, con las cifras con fuente y la frase "no hay cifra de cuántos carritos hay en Cali".
- **El mecanismo en una frase (unas 60 palabras).**
- **Tabla 2. Paso a paso (9 filas):** la tabla de la sección 4.
- **Reglas en cuatro líneas:** historial, tope de 3 días y 2 fiados, respaldo del dato, sin recargo.
- **Cómo una pieza resuelve los cuatro puntos (unas 230 palabras):** los cuatro párrafos de la sección 4, apretados.
- **Trazabilidad:** en lugar de una tabla completa (va en anexo), una línea que diga de dónde sale cada rasgo: disparador externo (Brune, Giné y Karlan; Battaglia et al.), tope de 3 días (IDEAM), el minorista como nodo (campo), sin contacto con el vendedor (informante 07 hallazgo 2; Ley 2300), sin cédula ni app (campo hallazgo 5), mover el pago y no indemnizar (Casaburi y Willis).

### Página 4. Por qué es distinto y los números (unas 420 palabras más Tabla 3)

- **Qué lo diferencia (unas 130 palabras):** se parece a la respuesta 6 y a la 9; las seis diferencias de mecanismo de la sección 2, en prosa corta.
- **Tabla 3. Los números del negocio:** las seis respuestas con su supuesto (sección 6 de este brief).
- **Lectura honesta (unas 170 palabras):** el costo real para la cadena es pequeño (el plazo cuesta unos $2.000 por vendedor al año; lo que pesa es el impago del aplazado); con salario mínimo para mí el modelo no cierra en el primer año y llega al equilibrio en el mes 22 con unos 900 vendedores; sin salario, en el mes 10. Lo que decide todo es un precio que nadie ha pagado todavía: la tarifa. Por eso el piloto la cobra desde el mes 2 y el mes 3 dice si sigo.
- **Frase de cierre de la página:** "Si el modelo no cierra, será por la tarifa, no por el riesgo de crédito, porque no presto."

### Página 5. Lo que descarté, el riesgo real y cómo sé si me equivoqué (unas 470 palabras, Tabla 4 opcional)

- **Descarte 1: A, la ventanilla del tendero (unas 130 palabras).** Sección 7 de este brief.
- **Descarte 2: F, el día de lluvia pagado (unas 120 palabras).** Sección 7.
- (Si cabe, Tabla 4 de dos filas: "qué me hizo creer / qué lo mató", A y F. Si no cabe, prosa.)
- **Riesgo real (unas 120 palabras):** "al de arriba hoy no le duele el día de lluvia" (sección 7), con los secundarios en una línea.
- **Qué mide el piloto y cuándo lo mato (unas 80 palabras):** criterios de la sección 7.
- **Cierre (unas 20 palabras):** una frase sobre impacto posible sin inflarlo: "Si funciona en un corredor, se replica por mayorista, no por vendedor".

Checklist del cuerpo: 5 páginas carta como máximo; "ANEXOS" arranca en página nueva; cero rayas; sin nombres de personas; cada número con fuente o rótulo "cálculo propio"; pasar `report/check.py`.

---

## 6. Plan de números

### Lo que el modelo tiene que responder (valores de `models/fiado_bridge_viability.py`)

| Pregunta del caso | Respuesta base | Supuesto detrás y de dónde sale |
|---|---|---|
| 1. Inversión inicial | **$3,9 millones** | Registro de la SAS $600.000 (costo 2026 no encontrado en fuentes: estimado); concepto de un abogado financiero sobre 5 preguntas $3 millones (cotización pendiente); tarjetas y material $300.000. Bot y disparador: trabajo propio, sin costo en efectivo. No hay capital de préstamo porque no presto |
| 2. Costos mensuales | **$2,53 millones** | Mi salario, 1 SMMLV de 2026: $1.750.905 (Decreto 1469 de 2025, vía frente 07); transporte y campo $200.000; celular y datos $80.000; número de WhatsApp Business, servidor y herramientas $150.000; contador para la SAS y la factura electrónica $350.000. Todo salvo el salario es supuesto |
| 3. Margen por usuario (incluye no pago) | **$2.800 por vendedor al mes** | Tarifa de $4.000 (supuesto, sin precedente de precio) por 90% cobrado (10% de pagadores que no pagan o se van) menos $800 de costo directo (mensajes y tarjeta). El no pago del aplazado lo carga la cadena, no yo: con fiado de $62.000 e impago de 3%, son unos $48.000 por vendedor al año para quien carga el plazo (se muestra aparte, en la vista del pagador) |
| 4. Usuarios y dinero en los meses 3, 6 y 12 | **40, 144 y 468 vendedores** (27, 108 y 416 pagando); contribución de **$76.000, $302.000 y $1,16 millones** al mes | 4, 12 y 36 minoristas con 10, 12 y 13 vendedores cada uno [supuestos]. Primer mes gratis por minorista. Entrada por los contactos del colaborador en la estación Universidades y luego por referidos entre minoristas que le compran al mismo mayorista |
| 5. Break-even | **904 vendedores; mes 22** | $2,53 millones divididos por $2.800. Con 4 minoristas nuevos al mes desde el mes 7 y 13 vendedores por minorista |
| 6. Cuánto para sobrevivir y de dónde | **$34,5 millones** con mi salario; **$8,5 millones** si trabajo sin salario hasta el equilibrio (mes 10, 279 vendedores) | Inversión inicial más pérdidas acumuladas hasta el punto más bajo. Fuente: ahorros propios y aportes de capital de mi familia a la SAS (pocos aportantes identificados, como capital y no como préstamos, para no acercarme a la captación). No cuento con el fellowship como fuente de dinero porque no sé si lo da |

### Sensibilidades que van en una línea o en el anexo

| Tarifa por vendedor al mes | Equilibrio con mi salario | Equilibrio sin salario |
|---|---|---|
| $2.000 | 2.531 vendedores; no llega en 36 meses (caja necesaria $67,5 millones) | 780 vendedores; mes 19 ($12,4 millones) |
| $4.000 (base) | 904; mes 22 ($34,5 millones) | 279; mes 10 ($8,5 millones) |
| $6.000 | 550; mes 15 ($25,8 millones) | 170; mes 8 ($7,5 millones) |

### Vista del que paga (para convencer al mayorista o al minorista)

Por vendedor al año, con fiado de $62.000 [cota superior: ventas diarias de un ambulante, unos $95.000, menos su ingreso mixto, unos $33.000; DANE vía frentes 01 y 08; no medido para carritos] y 26 días de disparo:
- Monto aplazado: $1,61 millones. Costo del dinero del plazo: unos $2.000 (a 20% E.A., supuesto). Impago de 1%, 3% o 10% del aplazado: $16.120, $48.360 o $161.200. Tarifa: $48.000.
- Con un margen bruto de 10% sobre lo que ese vendedor compra fiado [supuesto sin fuente, rango 10 a 20% en el frente 12], el vendedor le deja $1,93 millones al año. **La cláusula se paga sola si le evita perder 1 de cada 20 vendedores al año** (5,1% con 3% de impago; 10,9% con 10%; 6,1 a 13,6% si el fiado es de $30.000).
- Para el vendedor, el mismo día resuelto afuera cuesta $6.200 en el "diario anticipado" (10% en el día) o $12.400 en un ciclo de gota a gota al 20% sobre $62.000. Con el puente: $0.

### Por qué no uso la convención de $10 millones al mes

`unit_economics.py` y `bad_day_mechanisms.py` usan $10 millones de costo fijo para comparar mecanismos entre sí. Para responder "cuánto necesito antes de mi primer usuario y hasta el equilibrio" hay que usar lo que de verdad gastaría un piloto de una persona. Con $10 millones, el equilibrio a $4.000 sería de unos 3.570 vendedores (a $2.800 de contribución); decirlo en el anexo para que no parezca que escondo el escenario grande.

### Supuestos que el PDF tiene que marcar como supuestos (y qué los mueve)

| Supuesto | Valor | Qué pasa si está mal |
|---|---|---|
| Umbral de lluvia que tumba la venta | 5 mm entre 7 a. m. y 7 p. m. | Con 10 mm son 15 días en 12 meses en vez de 26: menos costo para la cadena, menos cobertura |
| Fiado diario de un carrito | $30.000 a $62.000 | Escala el costo de la cadena, no mi margen |
| Impago del aplazado | 1 a 10% | Es el número que decide si la cadena acepta; sin dato colombiano. Referencias: mora del microcrédito 6,9% (jul 2026); AB InBev 93,6% al día |
| Tarifa | $4.000 | Mueve el equilibrio de 550 a 2.531 vendedores |
| Vendedores por minorista | 10 a 13 | Si son 5, el equilibrio pide el doble de minoristas |
| Nodos nuevos por mes | 4 desde el mes 7 | Con 2 al mes desde el inicio, el equilibrio con salario llega hacia el mes 39 y la caja necesaria sube a unos $55 millones (cálculo propio con el mismo script) |

Números que NO se usan en ninguna parte (síntesis 1.3, 1.4 y 11.2): "12 millones de colombianos", "4,4 millones de adultos", "uno de cada cuatro", "$2.500 millones diarios", "200.000 familias", "91% de las micro", "90% de los vendedores de Bogotá", "77% rural", "fiado cayó 54%", "666,5%", "3,6 millones de Brilla", "132.000 de Pideky", "13,8% de reseñas", "5 a 6 centavos por peso", "US$3.400 millones", "siete millones de reportados", el "3 a 4 veces lo que sacan" de la informante, los 50.000 de SEWA y los "164 días de lluvia" de Wikipedia (usar el cálculo propio sobre el IDEAM). Tampoco "46% de corresponsales inactivos" (usar 584.728 activos de 1.088.053, BdO 2026, si hace falta) ni "cayó 18%" en microcréditos.

---

## 7. Dos descartes reales y el riesgo real

### Descarte 1. A, "la ventanilla del tendero" (fue mi mecanismo principal hasta el 26 sep)

- **Por qué parecía bueno.** Era el mejor puntuado (27 de 40). Copiaba lo que hace bien el informal: cuota diaria que el deudor paga donde ya pasa, renovación como premio (90% de clientes rotativos en Palmira; IPE: 93% paga) y el tendero como aval que ya conoce al vendedor.
- **Qué lo mató.** (1) Los números: a precio legal (tope de 3,71% por ciclo de 36 cuotas en sep 2026) y con montos que un ambulante puede sostener, el neto va de -$26.143 a +$5.857 por usuario al año y necesitaría unos 20.500 usuarios activos para cubrir costos, casi todos los ambulantes que el DANE registra en el gota a gota de 24 ciudades (cálculo propio, `unit_economics.py`; síntesis 10.4.5). (2) La fila de pago: la informante cuenta que al gota a gota se le paga primero porque amenaza y al banco se le deja de pagar porque al final negocia; un prestamista legal sin amenaza queda de último (hipótesis de segunda mano, decirlo así). (3) El campo movió el nodo: quien le da crédito diario al vendedor es el minorista que le surte, no el tendero de barrio, y la premisa de que el tendero necesita efectivo no tenía dato (94,4% de los tenderos usa efectivo, Fenaltiendas 2024).

### Descarte 2. F, "el día de lluvia pagado" (seguro paramétrico vía aseguradora)

- **Por qué parecía bueno.** Salía directo del hallazgo de campo, sonaba original (no está entre las 10 respuestas predecibles), el dato del IDEAM es público y el riesgo lo cargaría una aseguradora vigilada, así que resolvía la licencia.
- **Qué lo mató.** La frecuencia. El disparo ocurre en 26 de 294 días de venta. Pagar el fiado entero cada día de lluvia exige una prima comercial de unos $16.600 por día de venta, 44% del ingreso mixto diario; cubrir solo una pérdida de $15.000 cuesta unos $4.000 diarios, 11% (cálculo propio con la siniestralidad de microseguros de 32,3%, RIF 2025; `bad_day_mechanisms.py`). Un seguro para algo que pasa dos veces al mes es un gasto fijo. Además la demanda de seguro de lluvia es baja aun a buen precio (Cole et al. 2013) y la póliza pide cédula, contra lo que dijeron los vendedores sobre no dejar rastro. Lo que me llevé de F: el problema es de tiempo, no de estado (Casaburi y Willis 2018), y eso es E.

(Otras dos candidatas que no entran al cuerpo pero sí al anexo: C, porque casi no llega al ambulante; y la "guía de préstamos" que propuse en la segunda conversación con la informante, que en su forma simple es educación financiera, la respuesta predecible 5.)

### El riesgo real de mi propuesta

**Al de arriba hoy no le duele el día de lluvia.** Hoy el vendedor toma el gota a gota y le paga al minorista, y el minorista le paga al mayorista: el choque lo absorbe el vendedor, a 20%, fuera de la cadena. Con el puente, quien carga el plazo asume un costo y un impago que hoy no tiene, a cambio de algo diferido y difícil de ver: que sus vendedores no se hundan y dejen de trabajar. Además, los proveedores se están endureciendo (Fenalco 2026, dato de comunicado, confianza media: decirlo). Si el pagador no ve la pérdida, no paga, y entonces no hay negocio aunque el mecanismo funcione.

Riesgos secundarios en una línea: que el minorista ya espere un día (entonces el hallazgo apunta a otra cosa); riesgo de base entre la estación de Meléndez y el carrito; impago del aplazado sin dato; mercancía perecedera (el puente corre la deuda, no la achica); el hallazgo central viene de un resumen oral de segunda mano y necesita al menos un vendedor que lo cuente en primera persona.

**Qué mide el piloto y cuándo lo mato (va en la página 5):**
- Mes 1: de los primeros minoristas, cuántos aceptan la cláusula gratis. Si ninguno de 5 acepta, paso a C.
- Mes 2 y 3: puentes cerrados en 5 días de venta; si menos de 90%, subo el historial exigido o paro.
- Mes 3: cuántos pagan la tarifa. Si menos de la mitad paga $4.000, pruebo $2.000 con el mayorista; si tampoco, el modelo no cierra y lo digo.
- Todo el piloto: cuántos vendedores inscritos tomaron un gota a gota en un día de disparo (pregunta en tercera persona, sin contactar prestamistas).

---

## 8. Anexos (después de la página 5, en página nueva con el título "ANEXOS")

- **A. Prototipo.** Lo mínimo que puede existir antes del mediodía: (1) un script que lea la API del IDEAM para la estación 0026055120, calcule el disparador de la noche anterior y escriba el mensaje "Hoy fue día de lluvia (Univalle, X mm). Rige la cláusula"; (2) una hoja de cálculo que lleve el registro de un minorista con tres vendedores y cierre el puente en tercios; (3) la tarjeta física. Formato del caso: capturas, qué hace hoy, qué no hace (no envía WhatsApp real, no tiene estación de respaldo, no lo ha usado ningún minorista), cuánto tomó, con qué herramientas. Decir la verdad: no se lo mostré a ningún vendedor ni minorista.
- **B. Números.** Tablas completas de `usury_cap.py` (tope legal por plazo y modalidad), `unit_economics.py` (A), `bad_day_mechanisms.py` (E1, E2 y F) y `fiado_bridge_viability.py` (plan base, sensibilidades, vista del pagador, escenario de $10 millones). Cada tabla con el comando que la reproduce.
- **C. Dato de lluvia.** Tabla mensual de disparos de la estación Universidad del Valle (frente 12b y 12), definición del disparador, huecos de la serie (58 días de 2025 sin cobertura diurna completa, marzo de 2026 sospechoso, duplicados) y URL de datos.gov.co.
- **D. Notas de campo.** Resumen anonimizado de las conversaciones en la estación Universidades (quién las hizo, cuándo, que es un resumen oral, que no sé cuántos vendedores fueron) y de las dos notas de voz de la informante (hallazgos, sin nombres ni barrios). Reglas seguidas: sin contacto con prestamistas, sin grabar a nadie sin permiso, línea 165 del GAULA a mano. Las preguntas de campo pendientes (E1, E2, E3 y F2 del frente 12) como "lo que falta saber".
- **E. Método y uso de IA, sin adornos.** Qué hice yo y qué hizo la IA: usé Claude (Claude Code con agentes) para investigar por frentes, verificar cada cifra contra la fuente, correr una revisión adversarial con la rúbrica, escribir los scripts de cálculo y redactar borradores; transcribí las notas de voz con Whisper en local; las decisiones (qué descartar, a quién escuchar, qué mecanismo elegir) y la coordinación del campo fueron mías. Qué cambié de idea y por qué (A, luego el hallazgo de campo, luego F, luego E). Si se hizo la prueba de las tres IA, su resultado.
- **F. Fuentes.** Primero las primarias (DANE, SFC, Banca de las Oportunidades, IDEAM, normas, papers), luego las secundarias, con URL y fecha de consulta. Las 10 fuentes núcleo de la síntesis 9 más IDEAM, WIEGO 2014, Martínez Benavides 2021, Martínez y Rivera-Acevedo 2019, Casaburi y Willis 2018, Cole et al. 2013, Pérez Cruz 2025.
- **G. Trazabilidad completa.** La tabla hallazgo a decisión del frente 12, sección 2.7, recortada a los rasgos que quedaron en E1.
- **H. Preguntas para el abogado.** (1) ¿Puede leerse como seguro una regla de aplazamiento pagada por la cadena si el vendedor no paga nada? (2) Umbral de SAGRILAFT y registro de bases de datos ante la SIC. (3) Si alguna vez se usa E2: ¿la tarifa pagada por un tercero cuenta como interés (Ley 2439 de 2024) entre comerciantes?

---

## Notas para quien escriba el PDF

- El frente 12 dice "21 rachas de un día y 3 de dos" (últimos 12 meses) y el 12b dice "18 de un día, 1 de dos y 1 de tres" (2025). Usar la serie de 12 meses y la frase "ninguna pasó de tres días", que es cierta en ambas.
- El frente 12 usa un plazo de puente de 2,5 días y el 12b de un día; el costo del dinero es irrelevante en los dos (decenas a unos miles de pesos al año).
- No llamar "entrevistas mías" a lo del MIO. Decir "conversaciones de un colaborador en mi nombre".
- La informante es "una informante de Cali que conoce varios casos de amigos y familiares". Nunca como dato, nunca con nombres, nunca con el caso del cobrador policía salvo como ilustración de por qué el deudor no acude a la policía (y mejor dejarlo fuera del cuerpo).
