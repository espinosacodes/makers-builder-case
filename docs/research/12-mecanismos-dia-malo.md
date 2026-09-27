# 12. Dos mecanismos que nacen del día malo: E "El puente del fiado" y F "El día de lluvia pagado"

Fecha: 27 sep 2026. Estado: completo, con huecos declarados en la sección 7.

Base: hallazgo de campo de `docs/09-resumen-entrevistas-carritos.md` (vendedores de carrito en la estación Universidades del MIO, Cali; conversaciones hechas por un colaborador el 26 sep 2026, resumen oral), informante clave (`docs/06-respuesta-mama.md` y `docs/07-respuesta-mama-2.md`), frentes `12a-fiado-y-dia-malo.md` y `12b-proteccion-dia-malo.md`, y secciones 2, 3, 6, 7, 10 y 11 de `00-sintesis.md`.

Método: en esta pasada no se hicieron búsquedas web nuevas (el presupuesto de WebSearch de la sesión estaba agotado según los frentes 12a y 12b). Todo lo externo sale de fuentes ya leídas y verificadas por otros frentes, con su confianza original. Lo nuevo de este archivo es el diseño, un recálculo propio de la serie de lluvia del IDEAM (últimos 12 meses, lunes a sábado) y la economía unitaria, reproducible con `models/bad_day_mechanisms.py`. No se contactó a nadie ni se buscó a ningún prestamista.

Convención de confianza: **alta** (fuente primaria leída o cálculo propio reproducible sobre datos abiertos), **media** (secundaria seria, primaria leída por otro frente, o cálculo sobre un supuesto), **baja** (sin fuente original leída). Todo lo marcado **[S]** es un supuesto sin dato.

## 0. Veredicto corto

1. **El día de lluvia es sobre todo un problema de tiempo y solo a veces de pérdida.** Si la mercancía no se daña, el vendedor no perdió plata: perdió el plazo. El gota a gota le vende ese plazo a 20% por préstamo. Si la mercancía es perecedera, sí hay pérdida. E responde a lo primero y F a lo segundo. Es la distinción "tiempo frente a estado" de Casaburi y Willis (2018).
2. **E "El puente del fiado" es el candidato fuerte.** No le presta al vendedor ni lo asegura. Mueve las fechas de pago de una cadena de fiado que ya existe cuando un dato público de lluvia se dispara, y el plazo lo carga el de arriba (el mayorista). Resuelve las tres restricciones del caso con una sola pieza. Su riesgo real no es legal ni de impago. Es que hoy **al mayorista no le duele el día de lluvia**, porque el gota a gota absorbe el choque por él y le pagan igual.
3. **F "El día de lluvia pagado" no sobrevive a sus propios números como mecanismo principal.** En Cali el disparador se activa en 26 de 294 días de venta (8,8%). A esa frecuencia, pagar el fiado entero cada día de lluvia exige una prima comercial de unos $16.600 por día de venta, 44% del ingreso mixto diario. Cubrir solo una pérdida de $15.000 cuesta unos $4.000 diarios (11%). Un seguro para un evento de dos veces al mes es casi un gasto fijo. F sirve como **descarte con números propios** (es la respuesta que "suena original" y se cae) o, a lo sumo, como una capa futura de "mes malo" de una aseguradora.
4. **Lo que decide entre los dos es una pregunta de campo:** ¿lo que no se vendió el día de lluvia se daña o se vende al otro día?

## 1. El hallazgo y la pregunta de diseño

- **Lo que se oyó en campo** (09, hallazgos 1 a 4): el vendedor de carrito saca fiado, sin interés, lo que va a vender en el día al minorista, que a su vez le compra al mayorista. "Hay días en que, no sé, llovió, entonces nadie va... No le puedo pagar. Y ahí es cuando entran con un gota a gota... y tienen que pagar un gota a gota con otro gota a gota."
- **Lo que ya estaba documentado:** el fiado de mercancía de mañana a tarde para vendedores sin mostrador (WIEGO 2014: "I take stock on credit every morning then pay back in the evening"; 38% de los ambulantes dice que el crédito del proveedor es "muy importante"); el proveedor que fía también debe (WIEGO, Accra); la sanción del fiado es la exclusión ("que no vuelva por acá", Martínez Benavides 2021); un gota a gota paga otro (El País 2018; informante).
- **Lo que no está publicado en lo que se pudo leer:** el primer paso, "tomo un gota a gota para no perder el fiado de mañana". Es la parte original del hallazgo (12a, sección 3.3).
- **Pregunta de diseño:** no "¿cómo le presto más barato al vendedor?", sino **"¿cómo evito que un día de lluvia rompa un fiado que ya funciona?"**.
- **Inferencia propia que sostiene todo el diseño:** el vendedor no toma el gota a gota por la plata, sino para proteger la relación con quien le fía. Si no paga ese día, lo tratan como "mala paga" y pierde el fiado de mañana, es decir, el trabajo de mañana. Por eso paga 20% por un plazo que vale decenas de pesos. Si el aplazamiento está pactado antes, no pagar el día de lluvia deja de ser "quedar mal", y el motivo para ir al gota a gota desaparece.

### Datos del disparador (recálculo propio)

Estación IDEAM 0026055120 "Universidad del Valle" (Meléndez, Cali), lluvia acumulada entre 7:00 y 18:59, días con al menos 60 de 72 registros de 10 minutos. Guion en `scratchpad/rain_cali.py` (frente 12b) y consulta propia sobre el mismo archivo.

| Dato | Valor | Periodo | Confianza |
|---|---|---|---|
| Días de venta (lunes a sábado) con 5 mm o más | 26 de 294 con datos (8,8%) | 27 sep 2025 a 26 sep 2026 | alta en el método; media en el dato (huecos) |
| Igual, todos los días | 27 de 340 (7,9%) | ídem | ídem |
| Igual, 2025 | 23 de 307 (7,5%) | 2025 | ídem (frente 12b) |
| Rachas de días seguidos con disparo | 21 de un día y 3 de dos días; ninguna de 3 o más | 27 sep 2025 a 26 sep 2026 | ídem |
| Meses con más disparos | oct 2025: 7; may 2026: 7; dic 2025 y abr 2026: 3; feb y mar 2026: 0 | ídem | ídem (mar 2026 con 2,6 mm es sospechoso, frente 12b) |
| Días que pasan del tercer disparo del mes | 8 (4 en oct 2025 y 4 en may 2026) | ídem | ídem |
| Rezago de publicación | el registro de 23:50 del 26 sep estaba publicado a la 1:17 a. m. del 27 | 2026 | alta (frente 12b) |

Lectura: el choque es frecuente, casi siempre de un solo día, y se concentra en dos temporadas. Un puente de 1 a 3 días cubre todas las rachas observadas.

## 2. Mecanismo E. "El puente del fiado"

### 2.1 En una frase

Cuando la estación del IDEAM marca día de lluvia, el vendedor que ya tiene historial con su minorista paga el fiado de ese día en los tres días de venta siguientes, sin recargo; el minorista corre en la misma medida su pago al mayorista, y el mayorista carga ese plazo porque le conviene no perder vendedores. Nosotros ponemos el disparador, la regla y el registro, y le cobramos al mayorista. Nunca le prestamos al vendedor ni recibimos su plata.

### 2.2 Paso a paso (quién, qué, cuándo, con qué, dónde está la plata)

| Momento | Quién | Qué hace | Con qué | Dónde está la plata |
|---|---|---|---|---|
| Semana 0 | Nosotros | SAS con objeto de servicios de información y, para la variante E2, crédito comercial con recursos propios. Programa que lee cada noche la API del IDEAM (estación Universidad del Valle y, de respaldo, Base Aérea Marco Fidel Suárez) y calcula el disparador. Bot de WhatsApp para minoristas. Un abogado revisa la cláusula | SAS (Ley 1258), script sobre datos.gov.co, WhatsApp | Capital propio en la cuenta de la SAS; no se mueve |
| Semana 1 | Nosotros y un mayorista | Le proponemos una "cláusula de lluvia" en su acuerdo con los minoristas: en día de disparo, el pago del minorista por lo que fió a sus vendedores ese día se corre hasta 3 días de venta. Él paga una tarifa mensual por vendedor activo. Le mostramos el dato con el que se activa (público, lo puede revisar él mismo) | Conversación, una página de acuerdo comercial | Nada se mueve |
| Semana 1 | Mayorista y 2 o 3 de sus minoristas | El mayorista les ofrece la cláusula; cada minorista elige a los vendedores que entran (los que ya le fían hace al menos 4 semanas **[S]**) y se lo dice a cada uno de palabra, con una tarjeta: "Si el IDEAM marca lluvia, lo de ese día me lo paga en los 3 días siguientes, sin recargo" | Su palabra, tarjeta física | Nada se mueve |
| Día normal, 5 a 7 a. m. | Vendedor y minorista | Igual que hoy: el vendedor saca su mercancía fiada | Mercancía, cuaderno del minorista | Mercancía del minorista en el carrito |
| Día normal, tarde | Vendedor y minorista | Igual que hoy: el vendedor paga lo del día | Efectivo o Nequi | Bolsillo del vendedor → caja del minorista → pago al mayorista en su plazo de siempre |
| Día de lluvia, 7:00 p. m. a 9:00 p. m. | Nuestro programa | Con el dato publicado (rezago observado de cerca de 1,5 horas), calcula si hubo 5 mm o más entre 7 a. m. y 7 p. m. **[S: umbral a calibrar]**. Si sí, avisa al minorista y al mayorista: "Hoy fue día de lluvia (Univalle, 12 mm). Rige la cláusula" | API del IDEAM, WhatsApp | Nada se mueve |
| Esa misma noche | Minorista | Responde al bot con los vendedores que no pudieron pagar y el monto ("Pedro 45"). Es lo único que registra, unas 2 veces al mes | WhatsApp | La deuda del vendedor con el minorista queda como está: es la misma de siempre, con otra fecha |
| Esa misma noche | Bot | Le manda al mayorista el total aplazado por minorista y el calendario ("su pago de mañana baja en $135.000; se completa en 3 días de venta") | WhatsApp o una hoja compartida | La cuenta por pagar del minorista con el mayorista se corre; el mayorista carga el plazo |
| Días de venta 1 a 3 siguientes | Vendedor | Saca su fiado del día como siempre y paga lo del día más un tercio de lo aplazado | Efectivo o Nequi | Bolsillo del vendedor → caja del minorista |
| Días de venta 1 a 3 siguientes | Minorista y bot | El minorista paga al mayorista lo corriente más la parte aplazada; el bot concilia y confirma "puente cerrado" | WhatsApp | Caja del minorista → mayorista |
| Si llueve de nuevo dentro del puente | Programa | Suma el nuevo día, con tope de 3 días de disparo seguidos y saldo aplazado de 2 fiados por vendedor **[S]** | | El mayorista carga como máximo 2 fiados por vendedor inscrito |
| Si no hay dato de la estación | Programa y minorista | Se usa la estación de respaldo. Si tampoco hay dato, el minorista puede declarar el día, como máximo una vez al mes, y se revisa contra el dato cuando llegue | | Igual |
| Si el vendedor no cierra el puente en 5 días de venta | Minorista | Decide él, como hoy con su fiado. Nosotros solo lo marcamos como no elegible para el siguiente día de lluvia. Nunca cobramos, nunca llamamos al vendedor | | La pérdida, si la hay, es del minorista o del mayorista según la cláusula |
| Fin de mes | Mayorista | Paga la tarifa por vendedor activo | Transferencia | Mayorista → cuenta de la SAS |

**Variante E2 (solo si el minorista compra de contado y no hay un mayorista que acepte correr el plazo):** esa noche prestamos al minorista, con capital propio, el total aplazado, por hasta 5 días de venta, como crédito comercial entre empresas y con interés por debajo de la usura de crédito ordinario (29,24% E.A. en sep 2026). La plata va de la cuenta de la SAS al proveedor del minorista o al minorista, y vuelve del minorista a la SAS. **Seguimos sin prestarle al vendedor:** el deudor es el minorista, un comercio conocido con varios vendedores.

### 2.3 Reglas y límites

- **Solo lluvia pública, nunca la palabra del deudor.** La flexibilidad dada a clientes nuevos subió el impago en Barranquilla y Cartagena (Brune, Giné y Karlan 2025) y la dada a clientes con historial lo bajó (Battaglia et al. 2023). El disparador externo y el requisito de historial son la regla que sale de ahí.
- **Tope de 3 días de disparo seguidos** (cubre todas las rachas observadas) y **saldo aplazado máximo de 2 fiados** por vendedor **[S]**.
- **Sin recargo para el vendedor, siempre.** Cobrarle algo al vendedor a cambio de que se active con la lluvia se parecería a un seguro sin licencia (frente 12b, pregunta abierta 2).
- **No cubre** vacaciones, paros ni enfermedad. Las vacaciones universitarias son predecibles y se manejan bajando el volumen de fiado, no aplazando (12a, hipótesis 3.2). El choque de salud o familiar (informante, 06 hallazgo 10) queda fuera y hay que decirlo.
- **No cubre la pérdida por mercancía dañada:** si se pudre, el vendedor sigue debiéndola, pero la paga en 3 días a 0% en lugar de con un gota a gota a 20%.

### 2.4 Quién paga y forma legal

| Actor | Qué pone | Qué gana | Forma legal |
|---|---|---|---|
| Vendedor | Nada nuevo | No pierde el fiado de mañana el día que no vendió; no necesita el gota a gota para eso | Sigue siendo el fiado verbal sin interés que ya tiene |
| Minorista | Registra 2 veces al mes quién no pagó | Conserva a sus vendedores y no tiene que escoger entre fiarle a un vendedor endeudado o perderlo | Sigue siendo acreedor de su fiado; su plazo con el mayorista se corre por cláusula |
| Mayorista | Carga el plazo (unos $2.000 por vendedor al año de costo del dinero) y el impago adicional; paga la tarifa | Protege el volumen de su red de carritos | Crédito comercial entre comerciantes, sin licencia (frente 07, estructura 9; Código de Comercio). Sin interés, así que sin tema de usura |
| Nosotros | Disparador, regla, registro, conciliación | Tarifa por vendedor activo | Servicio de información y software. En E1 no hay crédito nuestro ni plata de terceros en nuestra cuenta. En E2, crédito comercial con capital propio a pocos comercios identificados (frente 07, estructura 7), por debajo de la usura, sin captar (Decreto 1981 de 1988) |

**Por qué el mayorista y no el minorista paga la tarifa:** el minorista es un deudor más de la cadena y, según WIEGO (Accra), el proveedor que fía también debe. El que tiene balance y volumen es el de arriba. Si no hay un mayorista dispuesto, la tarifa la paga el minorista (y entonces hay que mirar si le alcanza) o se usa E2.

Pregunta para el abogado: en E2, que el mayorista nos pague una tarifa mientras nosotros le prestamos al minorista ¿se suma al interés para efectos de usura? (Ley 2439 de 2024 reputa como interés los cargos de tecnología en créditos por medios electrónicos; hay que ver si aplica entre comerciantes y si aplica a un pago de un tercero).

### 2.5 Cómo un solo mecanismo resuelve las tres restricciones

El mecanismo es uno: **un dato público de lluvia que corre las fechas de pago de una cadena de fiado que ya existe**. De esa misma pieza salen las tres respuestas.

- **No soy entidad vigilada:** no presto ni aseguro. El crédito ya existe (el fiado) y lo dan comerciantes a comerciantes. Nosotros solo le cambiamos la fecha con una regla pactada. No hay prima ni indemnización (por eso no es seguro) y no hay desembolso al vendedor (por eso no es crédito nuestro). La plata del vendedor nunca pasa por nosotros.
- **Ingreso diario sin ahorro:** el mecanismo existe solo para el día en que no hubo ingreso, que es justo cuando la falta de ahorro obliga a pedir prestado. Después, la devolución se reparte en el ritual que ya tiene (pagar al minorista cada tarde), sin cuota nueva ni calendario mensual.
- **Desconocido de 22 años:** el vendedor no tiene que confiar en nosotros. Ni siquiera nos conoce: su trato sigue siendo con el minorista de siempre. Entramos por arriba: hay que ganarse a un mayorista y a unos pocos minoristas, no a miles de vendedores. Y a ellos no les pedimos que nos crean: el disparador es un número del IDEAM que pueden revisar solos.

Extra que conecta con el diagnóstico: E no compite por el lugar en la fila de pago (riesgo principal de A, 07 hallazgo 7). No agrega un acreedor: el vendedor le sigue debiendo a la misma persona.

### 2.6 A qué respuesta predecible se parece y qué la hace distinta

**Se parece a la 6 (crédito de proveedor o BNPL para inventario)**, y el evaluador lo va a pensar. Hay casos en el mercado: Tienda Pago ("págalo en 7 días") y el plazo de BEES. También se parece al mecanismo D de la síntesis y a las cuotas aplazables de las microfinancieras.

Lo distinto está en el mecanismo, no en el nombre:
1. **No crea crédito.** El crédito ya existe, es gratis y lo da otro. La 6 agrega una línea o alarga el plazo estándar. E deja el plazo normal en cero días y solo lo abre cuando pasa un evento.
2. **Se activa con un dato público, no con una solicitud.** Nadie pide nada. La decisión de crédito la toma la lluvia.
3. **El que carga el plazo es el de arriba**, que hoy le traslada el choque al vendedor (vía gota a gota), y no un financiador nuevo que le presta al de abajo.
4. **Ataca el momento en que nace el gota a gota** (la tarde del día malo), no la necesidad de crecer el inventario.
5. **No hay nada que pagar por el servicio del lado del usuario.** En la 6 el usuario paga el financiamiento.

Prueba honesta para el anexo: pegar el enunciado del caso más el hallazgo de campo en tres modelos y ver si alguno propone "aplazamiento del fiado atado a un índice de lluvia, financiado por el mayorista". Si alguno lo propone, la originalidad está en el hallazgo, no en el mecanismo, y hay que decirlo.

### 2.7 Trazabilidad hallazgo → decisión

| Hallazgo | Fuente | Decisión de diseño |
|---|---|---|
| El vendedor saca fiado sin interés cada mañana al minorista | Campo (09, hallazgo 1); WIEGO 2014 ("I take stock on credit every morning") | No crear crédito; el nodo es el minorista que fía, no el tendero de barrio |
| Cadena mayorista, minorista, vendedor; el proveedor que fía también debe | Campo (09, hallazgo 2); WIEGO 2014 (Accra) | El plazo lo carga el mayorista; el minorista solo pasa el aplazamiento hacia arriba |
| El gota a gota entra el día de lluvia, cuando no puede pagar el fiado | Campo (09, hallazgo 3) | El mecanismo solo se activa ese día; los días normales no cambia nada |
| La sanción del fiado es la exclusión ("que no vuelva por acá") | Martínez Benavides 2021 | El aplazamiento se pacta antes, para que no pagar el día de lluvia no cuente como "quedar mal" |
| Un gota a gota paga otro; "para pagarle a uno, se meten en otro" | Campo (09, hallazgo 4); informante (06, hallazgo 4); El País 2018 | Actuar antes del primer préstamo; no refinanciar deudas del gota a gota (Karlan, Mullainathan y Roth 2019: pagarlas no saca de la trampa) |
| 26 de 294 días de venta con disparo; 21 rachas de 1 día y 3 de 2 | Cálculo propio, IDEAM (datos.gov.co) | Tope de 3 días; devolución en 3 días de venta |
| El dato se publica con cerca de 1,5 horas de rezago; hay huecos y un marzo sospechoso | Frente 12b | Aviso la misma noche; estación de respaldo; día declarado con tope de 1 al mes |
| Flexibilidad a clientes nuevos sube el impago; a clientes con historial lo baja | Brune, Giné y Karlan 2025; Battaglia et al. 2023 | Solo vendedores con historial con su minorista; disparador externo, no la palabra del deudor |
| El problema del pobre con el seguro es el momento del pago, no el estado | Casaburi y Willis 2018 | Mover el pago en el tiempo en vez de indemnizar |
| El mercado ya vende este puente: "diario anticipado" a 10% en el día; crédito de horas en Corabastos | Pérez Cruz 2025; La República 2019 | Hay demanda y precio de referencia; nosotros lo hacemos gratis para el vendedor |
| El crédito sobre mercancía que rota se paga muy bien | AB InBev 20-F 2025 (93,6% al día) | Hipótesis de impago bajo del aplazamiento; se mide en el piloto |
| Quien recomienda no quiere ser cobrador | Informante (07, hallazgo 2) | Nosotros nunca cobramos ni contactamos al vendedor; el minorista sigue siendo el acreedor de siempre, sin papel nuevo |
| Al gota a gota se le paga primero porque amenaza | Informante (07, hallazgo 7), hipótesis | E no entra a la fila de pago: el vendedor le debe a la misma persona que antes |
| No se formalizan; no quieren rastro para la DIAN | Campo (09, hallazgo 5); EMICRON 2025 (93,3% sin RUT) | El vendedor no se inscribe en nada, no da cédula ni usa app; el minorista lo anota con su nombre de pila |
| En Cali el crédito de proveedores es 11,6% de los micronegocios que pidieron crédito, frente a 3,0% en 24 ciudades | Cálculo propio sobre EMICRON 2025, Cuadro H.4_24C | Piloto en Cali, alrededor de una cadena de carritos |
| Los proveedores de tiendas se están endureciendo | Fenalco 2026 (39,55% más restricciones; 20,91% exige contado) | Riesgo nombrado: el mayorista puede no querer más riesgo; variante E2 para ese caso |
| Captar de más de 20 personas es delito | Decreto 1981 de 1988; Código Penal art. 316 | La plata del vendedor nunca pasa por la SAS |
| Un choque hundió a la vendedora de arepas | Informante (06, hallazgo 10) | El producto existe para el choque; la regla es estirar el plazo, nunca subir el saldo |

### 2.8 Soluciones parecidas y lo que enseñan

| Solución | Qué hace | Lección para E |
|---|---|---|
| Tienda Pago (Perú y México) | Financia a bodegas el pago al distribuidor a 7 días, con alianzas con Heineken y Arca Continental (tiendapago.com, consultado el 26 sep 2026; media) | Los distribuidores sí financian a su canal. Pero es un plazo fijo que invita a saldos que crecen; E es contingente y de 1 a 3 días |
| BEES y AB InBev | Plazo sobre su propia mercancía; muy poco préstamo en efectivo (US$58 millones frente a US$4.261 millones de cuentas por cobrar, 93,6% al día; 20-F 2025; alta) | El crédito atado a mercancía que rota se paga. El plazo debe quedar atado al fiado, no volverse caja libre |
| "Diario anticipado" y crédito de horas en Corabastos | 10% en el día (Pérez Cruz 2025; alta) y 0,5% a 1% por noche (La República 2019; media) | La necesidad de un puente de horas o días existe y se paga cara. Nadie la resuelve desde la cadena |
| Cuotas aplazables de BRAC (Bangladesh) | Aplazar 2 cuotas funcionó como seguro y bajó el impago en clientes con historial (Battaglia et al. 2023; alta en resumen) | El aplazamiento es la forma barata de asegurar el choque de liquidez |
| "Pases" a clientes nuevos (Colombia) | Subieron el impago 3 y 2 puntos en Barranquilla y Cartagena (Brune, Giné y Karlan 2025; alta) | Solo con historial; nunca a pedido del deudor |
| Seguro pagado en la cosecha (Kenia) | 72% de adopción frente a 5% del que se paga por adelantado (Casaburi y Willis 2018; alta) | Mover el pago en el tiempo vale más que la indemnización |

No se encontró (búsqueda limitada) un mayorista que aplace el cobro por clima ni un producto que ate un plazo comercial a un índice de lluvia urbano (frente 12b, 6.3). Es un hueco y, a la vez, la parte original.

### 2.9 Riesgo real principal

**Al de arriba hoy no le duele el día de lluvia.** El vendedor toma el gota a gota y le paga al minorista, y el minorista le paga al mayorista. El choque lo absorbe el vendedor a 20%, fuera de la cadena. Con E, el mayorista pasa a cargar un plazo y un impago que hoy no carga, a cambio de algo diferido y difícil de ver: que sus vendedores no se hundan en deudas y dejen de trabajar (como la vendedora de arepas, que "ni volvió a sacar el negocio"). Además los proveedores se están endureciendo (Fenalco 2026). Si el mayorista no ve la pérdida, no firma.

Cómo se vuelve visible: preguntar al minorista cuántos vendedores perdió en el último año y por qué (pregunta de campo E2 abajo), y medir en el piloto la retención de vendedores con y sin cláusula.

Riesgos secundarios:
- **Que el minorista ya espere.** Si hoy el minorista le da un día más al vendedor, E no agrega nada y el hallazgo apunta a otra cosa (la pérdida por mercancía dañada o la necesidad del hogar).
- **Riesgo de base del disparador.** Llueve en Meléndez y no en el carrito, o llueve a las 6 p. m. después de vender. En contra del vendedor si no se activa cuando debía; en contra del mayorista si se activa de más. Es menor que en el agro porque la zona es pequeña, pero no está medido.
- **Impago del aplazamiento.** Sin dato. Es el número que decide la economía (sección 2.10).
- **Riesgo moral:** el vendedor que sí vendió un día de disparo aplaza igual. Solo cuesta el valor del dinero (decenas de pesos), porque la deuda no se perdona. Importa solo si termina en impago.
- **Mercancía perecedera:** E corre la deuda pero no la achica.
- **Legal:** bajo en E1 (no movemos plata ni damos crédito). Medio en E2 (crédito comercial con capital propio, usura ordinaria, pregunta de la tarifa del tercero).

### 2.10 Economía unitaria aproximada

Guion: `models/bad_day_mechanisms.py` (mismas convenciones que `models/unit_economics.py`: costo fijo de $10 millones al mes y fondeo de 12% E.A.).

**Supuestos:** fiado diario de $62.000 como cota superior (ventas diarias de un ambulante, unos $95.000, menos ingreso mixto, unos $33.000; DANE vía frentes 01 y 08; media; no medido para carritos) y $30.000 **[S]**; parte del fiado que no se alcanza a pagar el día de disparo: 50% **[S]** o 100% (cota); 26 días de disparo al año (cálculo propio); plazo promedio del puente de 2,5 días **[S]** (devolución en 3 tercios más fines de semana); costo del dinero del mayorista 20% E.A. **[S]**; impago del aplazado de 2%, 5% o 10% **[S]**, sin dato colombiano para este producto (referencias: mora del microcrédito 6,9% en jul 2026; AB InBev 93,6% al día en 2025).

**Costo por vendedor al año para la cadena (E1):**

| Fiado | No pagado el día de lluvia | Monto aplazado al año | Costo del dinero | Impago 2% | Impago 5% | Impago 10% | Lo que cobraría el "diario anticipado" (10% por un día) |
|---|---|---|---|---|---|---|---|
| $30.000 | 50% | $390.000 | $487 | $7.800 | $19.500 | $39.000 | $39.000 |
| $62.000 | 50% | $806.000 | $1.007 | $16.120 | $40.300 | $80.600 | $80.600 |
| $62.000 | 100% | $1.612.000 | $2.014 | $32.240 | $80.600 | $161.200 | $161.200 |

Lectura:
- El costo del plazo es casi cero (unos $2.000 al año por vendedor). Lo que pesa es el impago.
- **Mientras el impago del aplazado quede por debajo de 10%, la cadena carga el choque más barato de lo que cobra el puente informal más barato conocido** (10% por un día; el gota a gota a 20% por préstamo es más caro).
- Para el mayorista, con impago de 2% a 5% y fiado de $62.000, son $32.000 a $81.000 al año por vendedor, entre 0,2% y 0,4% de lo que ese vendedor compra en el año (unos $18,6 millones con 300 días de venta **[S]**). Con un margen bruto de 10% a 20% **[S]** sobre esas compras, la cláusula cuesta de 1% a 4% del margen que deja cada vendedor. Si un vendedor que cae en la cadena de gota a gota deja de trabajar, perderlo cuesta el margen completo.

**Ingreso nuestro (E1):** tarifa al mayorista por vendedor activo al mes **[S]**, sin precedente de precio.

| Tarifa por vendedor al mes | Vendedores activos para cubrir $10 millones de costo fijo |
|---|---|
| $2.000 | 5.000 |
| $4.000 | 2.500 |
| $6.000 | 1.667 |

$4.000 al mes es 0,26% de las compras mensuales de un vendedor con fiado de $62.000. 2.500 vendedores son, por ejemplo, 125 minoristas con 20 vendedores cada uno **[S]**. Como orden de magnitud, el DANE cuenta 286.061 ambulantes en 2025 (EMICRON vendedores ambulantes, Cuadro 13; alta), pero no se sabe cuántos sacan fiado ni cuántos venden en carrito.

**E2 (prestamos el plazo al minorista a la usura ordinaria):** por vendedor al año, interés de $2.835, fondeo de $1.252; con impago del minorista de 0%, neto de $1.583; con 1%, neto de -$14.537; con 3%, -$46.777. **E2 no es negocio.** Solo sirve para arrancar donde no hay mayorista dispuesto, con una exposición tope de capital propio (por ejemplo $5 millones **[S]**), mientras se consigue quién cargue el plazo.

**Conclusión honesta:** E1 no necesita capital de préstamo y su costo real es pequeño, pero todo el ingreso depende de que un mayorista pague por algo que hoy no le duele. Si el modelo no cierra, es por ese precio, no por el riesgo.

### 2.11 Tres preguntas de campo que lo confirman o lo matan

Hoy es domingo 27 sep: puede que los carritos de universidades no estén. Si el colaborador tiene cómo volver a hablar con los vendedores de ayer, estas son las tres. Van en pasado concreto, no en hipotético.

| # | A quién | Pregunta | Lo confirma si... | Lo mata si... |
|---|---|---|---|---|
| E1 | Vendedor | "La última vez que llovió y no vendió, ¿qué le dijo el que le fía cuando no le pudo pagar esa tarde? ¿Le esperó al otro día o le exigió ese mismo día? ¿Y al otro día le fió?" | El minorista exige ese mismo día o corta el fiado de mañana (el plazo es lo que falta) | El minorista ya espera un día sin problema: entonces el gota a gota se toma por otra cosa (pérdida, hogar) |
| E2 | Minorista (es un comerciante, no un prestamista) | "¿Usted le paga al que le vende a usted de contado cada día o le da plazo? Cuando llueve y sus vendedores no le pagan, ¿qué hace usted esa noche? ¿Cuántos vendedores ha perdido este año por deudas?" | Paga de contado o a diario y ha perdido vendedores por deudas (el choque sube por la cadena y le cuesta) | Tiene plazo holgado con su proveedor y no pierde vendedores: el problema no está en la cadena y al de arriba no le importa |
| E3 | Vendedor | "Lo que no vendió ese día de lluvia, ¿se le dañó o lo vendió al otro día? ¿Cuánto saca fiado en un día normal, más o menos?" | La mayor parte no se daña (choque de tiempo) y el fiado está en el rango de decenas de miles | La mayor parte se daña: E solo corre una pérdida y F (o la devolución de lo no vendido) pasa adelante |

Umbral mínimo para decirlo en el PDF **[S]**: que 4 de 6 vendedores describan la exigencia del mismo día y que el minorista describa su propio pago diario hacia arriba.

## 3. Mecanismo F. "El día de lluvia pagado"

### 3.1 En una frase

Una prima diaria pequeña, cobrada junto con el pago del fiado en los días buenos, compra una póliza de una aseguradora vigilada que, cuando la estación del IDEAM marca día de lluvia, le paga directamente al minorista el fiado de ese día (o una parte fija); el minorista es el canal de venta y nosotros el canal tecnológico y el disparador.

### 3.2 Paso a paso (en su mejor versión)

| Momento | Quién | Qué hace | Con qué | Dónde está la plata |
|---|---|---|---|---|
| Antes de empezar | Nosotros y una aseguradora | Diseñamos con la aseguradora un seguro colectivo paramétrico: tomador el minorista (o el mayorista), asegurados sus vendedores; nosotros como canal (uso de red o agencia, reglas del Decreto 1692 de 2020 no verificadas) | Contrato con la aseguradora | Nada se mueve |
| Inscripción, una vez al año (no por temporada) | Minorista y vendedor | El vendedor entra con nombre y cédula (la póliza lo exige **[S]**); la prima corre todo el año para evitar que solo se inscriba en temporada de lluvias | Formulario por WhatsApp | Nada se mueve |
| Cada día de venta | Vendedor y minorista | El vendedor paga su fiado del día más la prima (por ejemplo $500 **[S]**), cobrada en el día bueno como en Casaburi y Willis | Efectivo o Nequi | Bolsillo del vendedor → caja del minorista |
| Cada semana | Minorista | Transfiere las primas recaudadas a la aseguradora | Transferencia | Caja del minorista → aseguradora (el riesgo es de ella) |
| Día de lluvia, noche | Nuestro programa | Calcula el disparador y lo reporta a la aseguradora | API del IDEAM | Nada se mueve |
| Día siguiente | Aseguradora | Paga al minorista el valor pactado por cada vendedor asegurado | Transferencia | Aseguradora → minorista; la deuda del vendedor queda saldada hasta ese valor |
| Cada mes | Aseguradora | Paga comisión de canal (en microseguros, los gastos de comercialización fueron 24,3% de las primas en 2025) | Transferencia | Aseguradora → minorista y nosotros |

### 3.3 Cómo resuelve las tres restricciones (y dónde se rompe)

- **No soy entidad vigilada:** el riesgo lo asume una aseguradora vigilada; nosotros somos canal. Se rompe si no conseguimos aseguradora: sin ella, cobrar una suma a cambio de pagar cuando llueve es asegurar sin licencia (frente 12b, 5).
- **Ingreso diario sin ahorro:** la prima es diaria y se cobra en el día bueno; el pago llega el día malo, al acreedor, sin que el vendedor tenga que tener nada guardado. Se rompe en el precio: para que el pago valga algo, la prima diaria es una fracción grande del ingreso (3.7).
- **Desconocido de 22 años:** el vendedor paga la prima a su minorista de siempre y ve el resultado ("hoy no me cobraron"). Pero ahora sí tiene que creer en algo nuevo: que un tercero va a pagar cuando llueva. La evidencia dice que esa confianza es justo lo que frena el seguro de lluvia (Cole et al. 2013). Y la póliza pide cédula, contra el hallazgo de campo de no dejar rastro (09, hallazgo 5).

Es un solo mecanismo en la forma, pero dos de las tres respuestas dependen de piezas externas (aseguradora y precio).

### 3.4 A qué respuesta predecible se parece y qué la hace distinta

No está entre las 10, pero **el microseguro paramétrico es una categoría conocida** (seguros índice de lluvia en el agro; SEWA en India para calor extremo desde 2024, fuente con "cita requerida", baja). Un evaluador lo leerá como "seguro paramétrico para informales". Por canal se acerca a la 6 (lo vende el proveedor). Lo único distinto es que asegura el fiado y le paga al proveedor, no a la persona. Es una diferencia de destino del pago, no de mecanismo.

### 3.5 Trazabilidad hallazgo → decisión

| Hallazgo | Fuente | Decisión |
|---|---|---|
| El día de lluvia rompe el pago del fiado | Campo (09, hallazgo 3) | El seguro paga el fiado del día, directo al minorista |
| La lluvia es pública y medible cada 10 minutos | IDEAM, datos.gov.co; cálculo propio | Disparador paramétrico: sin reclamo ni verificación de ventas |
| La prima pagada en la cosecha multiplica la adopción | Casaburi y Willis 2018 | Prima cobrada con el pago del fiado en el día bueno |
| La demanda de seguro de lluvia es baja aun con buen precio (confianza, liquidez, saliencia) | Cole et al. 2013 | Seguro colectivo con el minorista como tomador, no venta individual |
| Microseguros: siniestralidad 32,3%, comercialización 24,3%; "uso de red" y agencias son canales principales | RIF 2025 | Canal por red del minorista; precio calculado con esa siniestralidad |
| La startup no puede asumir el riesgo | Frente 12b (hipótesis para el abogado) | Aseguradora vigilada como tomadora del riesgo |
| Inscripción por temporada invita a la selección adversa | Inferencia propia sobre la estacionalidad medida (oct y may con 7 días) | Inscripción anual con prima todo el año |

### 3.6 Soluciones parecidas y lo que enseñan

| Solución | Lección |
|---|---|
| SEWA, seguro por calor extremo (India, desde jun 2024; Wikipedia con "cita requerida"; baja) | Existe el precedente urbano informal; no se verificaron prima, umbral ni renovación |
| Seguro de lluvia en India (Cole et al. 2013; alta) | Poca adopción aun a buen precio: el problema es confianza y liquidez |
| Seguro con prima al vender la cosecha (Casaburi y Willis 2018; alta) | Cobrar en el momento de liquidez sube mucho la adopción. Es lo mejor que F puede copiar |
| Microseguros en Colombia (RIF 2025; alta) | 32,3% de siniestralidad: el asegurado recibe en promedio un tercio de lo que paga. Para un evento frecuente eso es demasiado caro |
| Seguros paramétricos colombianos de 2026 (titulares, URL original no resuelta; baja) | Son agropecuarios; no se encontró ninguno para vendedores urbanos |

### 3.7 Economía unitaria aproximada

**Supuestos:** 26 días de disparo al año y 300 días de venta **[S]**; siniestralidad de 32,3% (microseguros 2025, RIF; alta) como relación entre pagos y prima comercial; ingreso mixto de unos $38.000 por día de venta (convención de 26 días, síntesis 10.3 #19; media); comisión de canal igual a los gastos de comercialización (24,3% de las primas; RIF 2025; es una aproximación, media).

| Qué paga | Eventos al año | Prima pura por día de venta | Prima comercial por día de venta | Parte del ingreso mixto diario | Nuestra comisión por vendedor al mes | Vendedores para cubrir $10 millones |
|---|---|---|---|---|---|---|
| El fiado entero ($62.000) cada día de disparo | 26 | $5.373 | $16.636 | 43,8% | $101.062 | 99 |
| Solo una pérdida de $15.000 **[S]** cada día de disparo | 26 | $1.300 | $4.025 | 10,6% | $24.450 | 409 |
| Capa "mes malo": $30.000 desde el cuarto disparo del mes | 8 | $800 | $2.477 | 6,5% | $15.046 | 665 |

Al revés: **una prima de $500 diarios compra un pago de unos $1.863 por día de disparo.** No alcanza ni para un tercio de la pérdida supuesta de $15.000.

Lectura:
- F parece mejor negocio para nosotros que E (menos de 700 vendedores para cubrir costos) justo porque le saca al vendedor entre 6% y 44% de su ingreso diario. **Esa es la señal de que está mal diseñado para el usuario.**
- Para la cadena, F cuesta entre 15 y 40 veces más que E por vendedor al año. Con la pérdida de $15.000, la prima comercial suma unos $1,2 millones al año por vendedor, frente a $32.000 a $81.000 de impago esperado en E con fiado de $62.000 e impago de 2% a 5%. Las pérdidas frecuentes y pequeñas conviene retenerlas y suavizarlas (plazo); se aseguran las raras y grandes (inferencia propia, estándar en gestión de riesgo).
- La capa "mes malo" es la única versión con lógica de seguro (8 eventos al año, concentrados en octubre y mayo). Pero con solo dos años de serie limpia en la estación, ninguna aseguradora la tarifaría sin cargar mucho la prima (inferencia).

### 3.8 Riesgo real principal

**El precio, que viene de la frecuencia.** Un evento que pasa 2 veces al mes no se puede asegurar barato. Ningún diseño de canal arregla eso. Siguen:
- **Adopción** baja aun a buen precio (Cole et al. 2013).
- **Riesgo de base** (llueve en la estación y no en el carrito); en un seguro pesa más que en E, porque aquí el pago es definitivo y no un simple aplazamiento.
- **Selección adversa** por temporada.
- **Legal:** necesitamos una aseguradora que quiera diseñar un producto nuevo para montos diminutos, y no verificamos qué exige el Decreto 1692 al canal.
- **El minorista como recaudador de primas** asume trabajo y responsabilidad frente a una aseguradora.
- **Rastro formal:** la póliza pide identificar al asegurado, contra lo que dijeron los vendedores sobre la DIAN (09, hallazgo 5).

### 3.9 Tres preguntas de campo que lo confirman o lo matan

| # | A quién | Pregunta | Lo confirma si... | Lo mata si... |
|---|---|---|---|---|
| F1 | Vendedor | La misma E3: "Lo que no vendió ese día de lluvia, ¿se le dañó? ¿Cuánto perdió?" | La mayor parte se daña y la pérdida es grande (hay una pérdida que asegurar) | No se daña: no hay nada que indemnizar, solo tiempo (gana E) |
| F2 | Vendedor | "¿Qué día fue la última vez que la lluvia le dañó la venta? ¿A qué hora empezó a llover?" (luego se compara con la estación del IDEAM para esa fecha) | Los días que nombran coinciden con los días de disparo de la estación | Nombran días en que la estación marca seco, o la estación marca lluvia en días que ellos no recuerdan: el riesgo de base mata el disparador (esto también golpea a E, aunque menos) |
| F3 | Vendedor | "¿Hoy paga algo diario o semanal para cubrirse de algo: funeraria, cadena, natillera? ¿Cuánto y a quién?" | Ya paga pequeñas sumas periódicas por protección a alguien que conoce | No paga nada de eso: vender una prima diaria es empezar de cero con la confianza |

## 4. E frente a F, y frente a A a D

| Criterio | E "El puente del fiado" | F "El día de lluvia pagado" |
|---|---|---|
| Qué resuelve | Tiempo (liquidez del día sin venta) | Estado (pérdida del día) |
| Qué le cuesta al vendedor | Nada | $2.500 a $16.600 por día de venta (6% a 44% del ingreso) |
| Quién carga el riesgo | El mayorista (E1) o nosotros como prestamistas del minorista (E2) | Una aseguradora vigilada |
| Licencia | No hace falta en E1 | Hace falta una aseguradora; nosotros canal |
| Confianza del vendedor | No la necesita: no nos conoce | La necesita: cree en un pago futuro de un tercero |
| Qué pide al vendedor | Nada (el minorista anota su nombre de pila) | Cédula e inscripción |
| Parecido con las 10 predecibles | La 6, con diferencias de mecanismo (contingente, sin crédito nuevo, lo carga el de arriba) | Ninguna tal cual, pero "seguro paramétrico" es una categoría conocida |
| Riesgo que lo mata | El mayorista no paga porque hoy no le duele | El precio, por la frecuencia del evento |
| Uso en el PDF | Candidato a mecanismo principal si E1 y E2 se confirman en campo | Descarte con números propios, o capa futura de "mes malo" |

**Relación con los mecanismos de la síntesis.**
- E responde a la crítica más dura a A (10.4.1 y 10.6.3: prestar montos de ambulante a precio legal no deja plata). E no presta.
- E también esquiva el riesgo de seguridad del nodo (6.1), porque no hay cobro ni efectivo acumulado en ninguna tienda.
- Se parece a D (consignación) en que vive en la cadena de mercancía. La diferencia es que en D el riesgo de no vender pasa al proveedor todos los días, y en E solo se corre el plazo el día de disparo.
- La devolución de lo no vendido el día de lluvia (contrato estimatorio, frente 12b, 6.2) es un complemento natural de E para mercancía que no se daña. No es otro mecanismo.

## 5. Supuestos a la vista

| Supuesto | Valor | De dónde sale | Qué pasa si está mal |
|---|---|---|---|
| Umbral de lluvia que tumba la venta | 5 mm entre 7 a. m. y 7 p. m. | Convención del frente 12b; sin dato de ventas | Cambia la frecuencia: con 10 mm son 15 días en 12 meses en vez de 26 |
| Fiado diario de un carrito | $62.000 (cota) y $30.000 | Ventas menos ingreso mixto de ambulantes (DANE; media) y supuesto puro | Escala lineal todos los costos |
| Parte del fiado no pagada el día de disparo | 50% o 100% | Supuesto | Escala lineal |
| Plazo promedio del puente | 2,5 días | Devolución en 3 tercios más fines de semana | Irrelevante para el costo (el dinero cuesta decenas de pesos) |
| Costo del dinero del mayorista | 20% E.A. | Supuesto | Irrelevante por lo mismo |
| Impago del aplazado | 2%, 5%, 10% | Sin dato; referencias: mora del microcrédito 6,9% (jul 2026), AB InBev 93,6% al día | Es el número que decide E |
| Historial mínimo | 4 semanas con el minorista | Supuesto, en la lógica de Brune et al. y Battaglia et al. | Más corto sube el impago; más largo deja fuera a los nuevos |
| Tope de saldo aplazado | 2 fiados por vendedor | Supuesto | Limita la pérdida máxima del mayorista |
| Días de venta al año | 300 | Lunes a sábado menos festivos, redondeado | Cambia poco |
| Margen bruto del minorista | 10% a 20% | Supuesto sin fuente | Cambia el argumento de venta al mayorista, no el mecanismo |
| Tarifa de E | $2.000 a $6.000 por vendedor activo al mes | Supuesto sin precedente | Cambia el punto de equilibrio (1.667 a 5.000 vendedores) |
| Costo fijo | $10 millones al mes | Convención de `models/unit_economics.py` | Escala lineal el punto de equilibrio |
| Siniestralidad de F | 32,3% | RIF 2025 (microseguros, alta) | Un producto nuevo y pequeño probablemente tendría menos, es decir, más caro |

## 6. Tabla de datos clave

| Dato | Cifra | Lugar | Año | Fuente | URL | Confianza |
|---|---|---|---|---|---|---|
| Días de venta con 5 mm o más diurnos | 26 de 294 (8,8%); rachas: 21 de 1 día y 3 de 2 | Cali, estación 0026055120 | sep 2025 a sep 2026 | Cálculo propio sobre IDEAM, "Precipitación" | https://www.datos.gov.co/resource/s54a-sgyg.json | alta en el método; media en el dato |
| Igual, 2025 | 23 de 307 (7,5%) | ídem | 2025 | Frente 12b sobre IDEAM | ídem | ídem |
| Fiado de mercancía de mañana a tarde; crédito del proveedor "muy importante" | 38% de ambulantes (19% de plaza) | 5 ciudades (Kenia, Ghana, India, Sudáfrica, Perú) | 2012, pub. 2014 | Roever, WIEGO IEMS Street Vendors, p. 39 | https://www.wiego.org/sites/default/files/publications/files/IEMS-Sector-Full-Report-Street-Vendors.pdf | alta |
| Reglas del fiado en Cali: sin interés, exclusión al que no paga | cualitativo | Cali (Aguablanca) | 2017, pub. 2021 | Martínez Benavides, Estudios Sociológicos 116 | https://www.redalyc.org/journal/598/59868383004/html/ | alta |
| Crédito de proveedores entre micronegocios que pidieron crédito | Cali 11,6% frente a 3,0% en 24 ciudades (CV 16,6% en Cali) | Colombia | 2025 | Cálculo propio sobre DANE EMICRON 24 ciudades, Cuadro H.4_24C | https://www.dane.gov.co/index.php/estadisticas-por-tema/mercado-laboral/micronegocios | media |
| Ambulantes sin RUT | 93,3% (19.145 de 286.061 lo tienen) | Colombia | 2025 | DANE EMICRON vendedores ambulantes, Cuadros 13 y 13.1 | https://www.dane.gov.co/files/operaciones/EMICRON/anex-EMICRONVendedoresAmbulantes-2025.xlsx | alta |
| "Diario anticipado" | 10% en el día | Bogotá (Corabastos) | 2025 | Pérez Cruz, Working Paper vol. 6 núm. 6, p. 7 | https://revistas.poligran.edu.co/index.php/ngs/article/download/4812/5088 | alta |
| Crédito de horas | 0,5% a 1% por noche | Bogotá (Corabastos) | 2019 | La República | https://www.larepublica.co/finanzas/gota-a-gota-corabastos-2829008 | media (dato viejo) |
| "Acudir a un gota a gota para pagarle a otro" | cita | Cali | 2018 | El País Cali | https://www.elpais.com.co/judicial/prestamos-gota-a-gota-una-pesadilla-que-no-deja-en-paz-a-calenos-de-todos-los-estratos.html | media |
| Pagar la deuda del prestamista no saca de la trampa | la mayoría vuelve a deber en seis semanas | India y Filipinas | 2019 | Karlan, Mullainathan y Roth, AER: Insights | https://poverty-action.org/sites/default/files/publications/Debt%20Trap.pdf | alta |
| Seguro con prima en la cosecha | 72% frente a 5% de adopción; aplazar un mes la prima suma 21 puntos | Kenia | 2018 | Casaburi y Willis, AER 108(12) | https://www.aeaweb.org/articles?id=10.1257/aer.20171526 | alta |
| Seguro de lluvia | demanda sensible al precio; frenos de confianza, liquidez y saliencia | India | 2013 | Cole et al., AEJ Applied 5(1) | https://www.aeaweb.org/articles?id=10.1257/app.5.1.104 | alta |
| Aplazar 2 cuotas con historial | mejor negocio y menos impago | Bangladesh | 2023 | Battaglia, Gulesci y Madestam, ReStud | https://doi.org/10.1093/restud/rdad107 | alta en resumen |
| "Pases" a clientes nuevos | +3 y +2 puntos de impago | Barranquilla y Cartagena | 2022, rev. 2025 | Brune, Giné y Karlan, NBER WP 30634 | https://www.nber.org/system/files/working_papers/w30634/w30634.pdf | alta |
| Microseguros: siniestralidad y comercialización | 32,3% y 24,3% de las primas | Colombia | 2025 | RIF 2025 (Banca de las Oportunidades y SFC), p. 172 | https://www.superfinanciera.gov.co/publicaciones/10116222/reporte-de-inclusion-financiera-2025-avances-en-depositos-credito-cobertura-y-transacciones/ | alta |
| Crédito comercial de AB InBev | US$58 millones de préstamos frente a US$4.261 millones de cuentas por cobrar, 93,6% al día | global | 2025 | AB InBev 20-F 2025, nota 19 | https://www.sec.gov/Archives/edgar/data/1668717/000119312526088105/d65314d20f.htm | alta |
| Proveedores más duros con tiendas | 39,55% más restricciones; 20,91% exige contado | Colombia | 2026 | Fenalco, comunicado | https://www.fenalco.com.co/blog/noticias-10/la-mayoria-de-tiendas-de-barrio-operan-en-modo-supervivencia-ante-caida-de-ingresos-y-presion-de-costos-en-2026-fenalco-8830 | media (sin metodología) |
| Usura de crédito ordinario | 29,24% E.A. | Colombia | sep 2026 | SFC, Resolución 1260 de 2026 | https://www.superfinanciera.gov.co/loader.php?lServicio=Tools2&lTipo=descargas&lFuncion=descargar&idFile=1083364 | alta |
| Captación masiva | más de 20 personas o 50 obligaciones, más otras condiciones | Colombia | vigente | Decreto 1981 de 1988 | https://www.funcionpublica.gov.co/eva/gestornormativo/norma.php?i=75473 | alta |
| Contrato estimatorio | paga lo vendido o devuelve lo no vendido | Colombia | vigente | Código de Comercio arts. 1377 a 1379 | https://www.funcionpublica.gov.co/eva/gestornormativo/norma.php?i=41102 | alta |
| Tienda Pago | "págalo en 7 días", con Heineken y Arca Continental | Perú y México | consulta del 26 sep 2026 | Sitio de la empresa (vía síntesis 10.2) | https://tiendapago.com | media (fuente interesada) |
| SEWA, calor extremo | pagos desde jun 2024 | India | 2024 | Wikipedia (cita requerida) | https://en.wikipedia.org/wiki/Self-Employed_Women%27s_Association | baja |

Fuentes de campo: `docs/09-resumen-entrevistas-carritos.md` (resumen oral de un colaborador, 26 sep 2026; sin número exacto de vendedores ni citas textuales por vendedor) y la informante clave de Cali (`docs/06` y `docs/07`, segunda mano). Se citan como tales y nunca como medición.

## 7. Huecos

1. No hay un solo dato del monto del fiado de un carrito, de la parte que se daña ni de a qué hora cobra el minorista. Todo el tamaño de E y F cuelga de eso (preguntas E3 y F1).
2. No se sabe si el minorista le paga al mayorista de contado o a plazo, ni si en Cali hay un mayorista con red de carritos que quiera pagar una tarifa (E2). Nada publicado sobre crédito en Cavasa o Santa Elena (frente 12a).
3. El impago de un aplazamiento pactado no tiene referencia en Colombia.
4. No se validó con ventas reales el umbral de 5 mm, ni el riesgo de base entre la estación de Meléndez y la estación Universidades del MIO (pregunta F2). La distancia entre las dos no se midió en esta sesión.
5. Decreto 1692 de 2020 y reglas de canales de seguros: no leídos (afecta solo a F).
6. Pregunta al abogado para E2: tarifa pagada por un tercero y usura; aplicación de la Ley 2439 entre comerciantes.
7. El hallazgo de campo es un resumen oral de segunda mano: la frase "no le puedo pagar, y ahí entra el gota a gota" necesita al menos un vendedor que lo cuente en primera persona antes de ponerlo como hallazgo central del PDF.

## Revisión adversarial

Revisión hecha el 27 sep 2026 desde el lado del evaluador del Builder Case, con la rúbrica de `docs/02-criterios-evaluacion.md` y la misma escala de la sección 10.2 de `00-sintesis.md` (1 muy débil, 3 aceptable, 5 sobresaliente frente a más de cien propuestas). Base: este archivo, los frentes `12a` y `12b`, `docs/09-resumen-entrevistas-carritos.md`, la informante (`docs/06` y `docs/07`) y las secciones 2, 3, 6, 7, 10 y 11 de la síntesis.

Método: el buscador web de la sesión está agotado (200 de 200) y cuatro lecturas directas intentadas en esta pasada devolvieron 404, así que no hay fuente nueva. Se corrió `models/bad_day_mechanisms.py` y sus salidas coinciden con las tablas de 2.10 y 3.7. Los cálculos nuevos de esta sección se marcan como propios y usan los supuestos ya declarados en la sección 5. No se contactó a nadie ni se buscó a ningún prestamista.

### R.1 Veredicto corto

1. **E puntúa 27 de 40, empatado con A, y es el que tiene la subida más barata de confirmar (a 30 con tres respuestas de campo y la prueba de las IA).** Lo que A no tiene y E sí: nace de un hallazgo propio de campo, resuelve las tres restricciones con una sola pieza (en su versión E1) y responde a la crítica más dura de A (prestar montos de ambulante a precio legal no deja plata). Lo que le cuesta puntos: su premisa central no está confirmada y choca con la única etnografía del fiado en Cali.
2. **F puntúa 21 de 40, igual que B.** Es la respuesta que cualquier IA da cuando oye "lluvia", ya existe en el agro y los propios números del archivo la matan. Vale más como descarte que como propuesta.
3. **La premisa de la que cuelga E no es la lluvia, es la exigencia del mismo día.** Si el minorista ya espera uno o dos días (como describe Martínez Benavides 2021 para el fiado de Aguablanca: sin fecha fija, "en los próximos días"), E no agrega nada y el gota a gota del día malo se toma por otra razón (el hogar o la mercancía perdida).
4. **E cubre bien el caso en que el problema es más chico y mal el caso en que es más grande.** Con mercancía que no se daña, el vendedor todavía tiene el producto y el choque es pequeño. Con mercancía perecedera, E le hace pagar la pérdida en 3 días, entre 26% y 54% de su ingreso diario (cálculo propio abajo), que es justo cuando el gota a gota sigue siendo la salida.

### R.2 Puntajes

#### Mecanismo E. "El puente del fiado" (27 de 40)

| # | Criterio | Puntaje | Justificación |
|---|---|---|---|
| 01 | Efectividad | 3 | Ataca el momento en que, según el campo, nace el gota a gota, y E1 resuelve licencia, flujo diario y confianza con la misma pieza; pero la premisa (el minorista exige el mismo día) no está confirmada, no cubre el hogar del día sin venta (entre los ambulantes, 28,9% del crédito va a gasto personal y 20,5% a negocio y hogar; DANE 2025, Cuadro 21.1) y con perecederos solo reparte una pérdida. Sube a 4 si el campo confirma la exigencia del mismo día. |
| 02 | Especificidad | 4 | La tabla de 2.2 dice quién, qué, cuándo, con qué y dónde está la plata, con casos borde (sin dato, lluvia dentro del puente, puente sin cerrar); falta resolver que el vendedor paga en la tarde y el disparador se calcula entre 7 y 9 p. m. (a la hora de decidir nadie sabe si rige la cláusula), el minorista que compra a varios mayoristas y el minorista que declara el día sin dato. |
| 03 | Creatividad | 3 | No es ninguna de las 10 predecibles tal cual y no se encontró en el mercado la combinación (plazo contingente a un índice público, en la base de una cadena informal, pagado por el de arriba, sin tocar la plata); pero cada pieza tiene dueño (crédito de proveedor como la respuesta 6, aplazamiento de cuotas, disparador paramétrico) y es el mecanismo de C aplicado al fiado. Sube a 4 si la prueba de las tres IA del anexo no lo produce. |
| 04 | Diagnóstico | 3 | La tesis "el gota a gota entra el día que un choque rompe un fiado que funciona, y se paga 20% para proteger la relación" es propia y refutable; pero sale de un resumen oral de segunda mano sin número de vendedores ni una sola cita en primera persona, y la parte "por la relación, no por la plata" es inferencia. |
| 05 | Fuentes | 3 | Serie propia del IDEAM, WIEGO, Casaburi y Willis, Brune, Giné y Karlan y RIF 2025 son sólidas; el hallazgo central es oral, el monto del fiado es derivado, el 11,6% de Cali es de todos los micronegocios (no de ambulantes) con CV de 16,6%, y Battaglia et al. se usa como "bajó el impago" cuando 10.3 #8 dejó eso sin verificación independiente. |
| 06 | Trazabilidad | 4 | La tabla 2.7 es la mejor del proyecto; quedan sin hallazgo el mayorista como pagador (la única fuente, WIEGO Accra, dice que el de arriba también debe, que es lo contrario de "tiene balance"), la tarifa y el historial de 4 semanas. |
| 07 | Juicio cuantitativo | 3 | Separa bien el costo del plazo (casi cero) del impago (lo que decide), dice que E2 no es negocio y que si no cierra es por el precio; pero el universo de carritos es desconocido frente a los 2.500 vendedores del equilibrio, la tarifa no tiene precedente, el argumento del margen omite nuestra propia tarifa y usa el margen del minorista para una decisión del mayorista, y el ingreso diario cambia de convención entre 12b ($33.000) y este archivo ($38.000). |
| 08 | Descartes y autocrítica | 4 | Nombra el riesgo real (al de arriba no le duele) y deja preguntas que lo matan con criterio de refutación; F es un descarte con números propios. Resta que trata como secundario lo que es la premisa ("que el minorista ya espere") y que no nombra el hueco del hogar. |

#### Mecanismo F. "El día de lluvia pagado" (21 de 40)

| # | Criterio | Puntaje | Justificación |
|---|---|---|---|
| 01 | Efectividad | 2 | Paga el día malo, pero la prima se come entre 6% y 44% del ingreso diario, que empeora la restricción del ingreso sin ahorro; la licencia la resuelve una aseguradora que no está y la confianza exige creer en un pago futuro de un tercero y dar cédula. |
| 02 | Especificidad | 3 | Pasos claros en su mejor versión; sin aseguradora, sin leer el Decreto 1692 de 2020, sin regla para la prima de los días que no se vende y con el minorista como recaudador sin nada a cambio definido. |
| 03 | Creatividad | 2 | Microseguro paramétrico es una categoría conocida; el diseño de "el comprador vende el seguro y cobra la prima en el momento de liquidez" es literalmente el de Casaburi y Willis (2018). Pagarle al acreedor cambia el destino del pago, no el mecanismo. |
| 04 | Diagnóstico | 2 | Supone que el día de lluvia es pérdida, y el propio archivo muestra que casi siempre es tiempo; la pérdida no está medida (pregunta F1). |
| 05 | Fuentes | 3 | RIF 2025, Casaburi y Willis y Cole et al. son altas; SEWA es Wikipedia con "cita requerida", los paramétricos colombianos de 2026 son titulares sin URL y el decreto no se leyó. |
| 06 | Trazabilidad | 3 | Tabla completa, pero el monto asegurado ($15.000) y la prima de $500 no salen de ningún hallazgo. |
| 07 | Juicio cuantitativo | 3 | Los números muestran con honestidad que no cierra para el usuario; pero aplicar la siniestralidad de todos los microseguros (32,3%) a un producto nuevo es un supuesto fuerte y la comparación "15 a 40 veces más que E" mezcla una indemnización con un aplazamiento (ver R.5). |
| 08 | Descartes y autocrítica | 3 | Se critica a sí mismo mejor que nadie; como propuesta, su riesgo real (el precio por la frecuencia) no tiene salida. |

#### Resumen de puntajes (misma escala que 10.2)

| Criterio | A | C | E | B | F | D |
|---|---|---|---|---|---|---|
| 01 Efectividad | 3 | 3 | 3 | 2 | 2 | 2 |
| 02 Especificidad | 4 | 3 | 4 | 3 | 3 | 2 |
| 03 Creatividad | 2 | 3 | 3 | 2 | 2 | 1 |
| 04 Diagnóstico | 4 | 3 | 3 | 3 | 2 | 2 |
| 05 Fuentes | 4 | 3 | 3 | 3 | 3 | 2 |
| 06 Trazabilidad | 4 | 3 | 4 | 3 | 3 | 2 |
| 07 Juicio cuantitativo | 3 | 2 | 3 | 2 | 3 | 1 |
| 08 Descartes y autocrítica | 3 | 3 | 4 | 3 | 3 | 3 |
| **Total (de 40)** | **27** | **23** | **27** | **21** | **21** | **15** |

Lectura: E empata con A hoy, pero sus puntos están en los criterios del bloque 1 que "más importan" (creatividad y efectividad, ambos con techo de 4 si el campo confirma) y no depende de la usura de una SAS ni del tendero con efectivo (10.3 #4 y #16). Con la exigencia del mismo día confirmada y la prueba de las IA limpia, E llega a 30 (01, 03 y 04 suben a 4). A no tiene una subida equivalente disponible hoy: su hallazgo de originalidad (el desbalance del tendero, 10.5) sigue sin dato.

### R.3 ¿Primera respuesta de una IA, ya existe, un mecanismo?

| | E "El puente del fiado" | F "El día de lluvia pagado" |
|---|---|---|
| ¿Primera respuesta de una IA? | Sin el hallazgo de campo en el prompt, no. Con el hallazgo pegado, lo primero que sale es seguro paramétrico, fondo de emergencia o crédito puente; "periodo de gracia por lluvia" puede aparecer en la lista, pero "que el mayorista cargue el plazo, disparado por el IDEAM, sin que nosotros toquemos la plata" es menos probable. Juicio del evaluador, no medición: hacer la prueba de 2.6 antes de escribir | Sí, casi seguro, en cuanto el prompt dice "lluvia" |
| ¿Ya existe? | No se encontró la combinación completa (búsqueda limitada). Existen las piezas: plazo de proveedor (Tienda Pago, BEES de AB InBev), opción de aplazar cuotas (BRAC en Battaglia et al. 2023) y, como conocimiento general no verificado en esta sesión (baja, no citar sin abrir la fuente), cláusulas de deuda soberana que suspenden pagos tras un huracán o desastre medido (Granada, Barbados, y las "climate resilient debt clauses" de UK Export Finance). Un evaluador que conozca estas últimas leerá E como "cláusula de huracán llevada al carrito" | Sí. El diseño con canal comprador y prima cobrada al vender es el experimento de Casaburi y Willis 2018 (Kenia; alta). Seguros índice vendidos por proveedores de insumos en el agro africano, como Kilimo Salama o ACRE en Kenia (conocimiento general no verificado en esta sesión; baja). SEWA por calor en India (baja) |
| ¿Un mecanismo para las tres restricciones? | Sí en E1: el mismo dato público que corre fechas de un crédito ajeno resuelve licencia (no prestamos ni aseguramos), flujo diario (actúa el día sin ingreso y devuelve en el ritual diario) y confianza (el vendedor no nos conoce). Matiz: la confianza no se resuelve, se traslada a una venta B2B a un mayorista, que también es un desconocido para un joven de 22 años, aunque con un dato que él mismo revisa. No en E2: ahí somos prestamistas del minorista y E se vuelve la respuesta 6 | No: la licencia depende de una aseguradora externa, la prima empeora el flujo diario y la confianza exige creer en un tercero y dar cédula |

### R.4 Afirmaciones sin respaldo verificado

| # | Afirmación | Dónde | Problema | Qué hacer antes del PDF |
|---|---|---|---|---|
| 1 | El minorista exige el pago el mismo día y, si no, corta el fiado de mañana | Premisa de todo E (sección 1, inferencia propia) | El campo solo dice "no le puedo pagar"; la única etnografía del fiado en Cali dice lo contrario: sin fecha fija, "en los próximos días" (Martínez Benavides 2021; alta en lo que dice, aunque es una tienda de ropa, no un surtidor de carritos) | Pregunta E1 de campo; si no se confirma, no afirmarlo |
| 2 | "El vendedor no toma el gota a gota por la plata, sino para proteger la relación" | Sección 1 | Inferencia propia. La alternativa con dato es el hogar: el día sin venta tampoco hay ingreso para comer, y la mitad del crédito de los ambulantes va a gasto personal o mixto (28,9% y 20,5%; DANE, EMICRON vendedores ambulantes 2025, Cuadro 21.1; https://www.dane.gov.co/files/operaciones/EMICRON/anex-EMICRONVendedoresAmbulantes-2025.xlsx; alta) | Preguntar en qué se fue la plata del gota a gota del día malo |
| 3 | "El gota a gota le vende ese plazo a 20% por préstamo", "paga 20% por un plazo que vale decenas de pesos" | Secciones 0 y 1 | Un gota a gota no presta a un día: presta a unas semanas en cuotas diarias. No se sabe el monto ni el plazo del préstamo del día malo; si es mayor que el fiado, parte va al hogar | Decirlo como retórica marcada o reemplazar por "el plazo cuesta decenas de pesos y el vendedor lo compra en un préstamo de semanas a 20%" |
| 4 | "El mayorista carga el plazo porque le conviene no perder vendedores"; "el que tiene balance y volumen es el de arriba" | 2.1, 2.4 | Sin fuente. WIEGO (Accra) dice que el proveedor que fía también debe, y Fenalco 2026 que los proveedores se endurecen. Tampoco se sabe si el minorista compra a crédito | Pregunta E2; nombrarlo como el supuesto que decide el modelo |
| 5 | "Eso les pasa a muchos de ellos" | 09 | Resumen oral de un colaborador; sin número de vendedores ni cita en primera persona (el propio archivo lo dice en 7.7) | En el PDF: "conversaciones con vendedores (n = x), resumen de un colaborador"; poner el n |
| 6 | 11,6% de crédito de proveedores en Cali como razón para pilotear en Cali | 2.7 | Es de todos los micronegocios que pidieron crédito, CV 16,6%; en ambulantes, nacional, es 1,8% (Cuadro 18.1) | Usarlo como contexto, no como prueba de que el fiado de carritos es mayor en Cali |
| 7 | Fiado diario de $62.000 | 2.10 | Es ventas menos ingreso mixto: todos los costos, no solo la mercancía fiada | Rotularlo "cota superior" en cada uso (ya está en 2.10; falta en 3.7 y 4) |
| 8 | Battaglia et al.: el aplazamiento "bajó el impago" | 2.3, 2.8 | 10.3 #8 lo dejó sin verificación independiente; J-PAL solo confirmó el efecto en ingreso | Abrir el resumen o citar solo el efecto en el negocio |
| 9 | Tarifa de $2.000 a $6.000 por vendedor al mes | 2.10 | Sin precedente de precio | Decirlo como la incógnita del modelo, igual que en C |
| 10 | "La estación queda cerca de los carritos" | 12b, hallazgo 1 | Distancia no medida (hueco 7.4); riesgo de base sin medir | Medir en mapa y ponerlo en el anexo |

### R.5 Contradicciones internas

1. **El caso fuerte y el caso débil están al revés.** Si la mercancía no se daña, el vendedor la tiene en el carrito: el choque es pequeño, la devolución o el arrastre al día siguiente lo resuelven sin nosotros, y E aporta poco. Si se daña, E corre la pérdida a 3 días: con fiado de $62.000 no pagado, son unos $20.700 diarios, 54% del ingreso mixto de $38.600; con $31.000, unos $10.300, 27% (cálculo propio con los supuestos de la sección 5). Un vendedor sin ahorro que paga la mitad de su ingreso tres días seguidos puede volver al gota a gota igual. El veredicto 0.1 ("E responde al tiempo, F a la pérdida") es correcto, pero el archivo no saca la consecuencia: el caso donde el gota a gota es más probable es el que E cubre peor.
2. **La hora del disparo llega después de la decisión.** En 2.2 el vendedor paga "en la tarde" y el programa calcula el disparo entre 7 y 9 p. m. El vendedor y el minorista deciden antes de saber si la estación marcará 5 mm. O el minorista aplica la cláusula a ojo y carga el riesgo de base, o el vendedor no sabe esa tarde si está cubierto y el gota a gota sigue siendo la salida segura. Hay que decir cuál.
3. **"Solo lluvia pública, nunca la palabra del deudor" frente a "el minorista puede declarar el día".** El minorista no es el deudor final, pero sí es deudor del mayorista y el aplazamiento le da plazo gratis: tiene incentivo a declarar. Tope de una vez al mes ya está; falta decir quién pierde si el dato posterior lo desmiente.
4. **El argumento del margen omite nuestra tarifa y mezcla eslabones.** Con $4.000 al mes, el mayorista paga $48.000 al año por vendedor además de $34.000 a $83.000 de impago y plazo (fiado de $62.000, 100% no pagado, impago de 2% a 5%): $82.000 a $131.000, 0,44% a 0,70% de las compras del vendedor, es decir 2,2% a 7,0% de un margen de 10% a 20% (cálculo propio), no "1% a 4%". Y el margen de 10% a 20% es del minorista (sección 5), mientras que quien decide y paga es el mayorista, cuyo margen no se conoce.
5. **"Un solo mecanismo" solo vale para E1.** E2 nos vuelve prestamistas del minorista con capital propio, con la pregunta de usura abierta, y el propio archivo dice que no es negocio. Si en Cali no aparece un mayorista, lo que queda es una versión pequeña de Tienda Pago.
6. **F frente a E compara cosas distintas.** "F cuesta 15 a 40 veces más que E" pone una prima que devuelve al vendedor una indemnización esperada (unos $390.000 al año con la pérdida de $15.000) contra un impago que no le devuelve nada. La comparación justa es el recargo (prima menos pago esperado, unos $818.000 al año) contra el impago de E. La conclusión sobrevive, pero el número no se puede usar así. En 12b, "más de 200 veces" compara prima por día de venta con plazo por evento e ignora el impago: no usar.
7. **Ingreso diario con tres convenciones.** 12b usa $33.000 (14%), este archivo $38.000 (44%) y la síntesis 10.3 #19 pide $38.600. El PDF necesita una sola.
8. **Geografía.** El diagnóstico de la síntesis empuja al Caribe (80,1% de concentración, 10.4.3); E y su disparador están calibrados en Cali, igual que el campo y la informante. Si E lidera, el usuario es el vendedor de carrito de Cali y el Caribe pasa a contexto, no al revés.
9. **E es C con otro acreedor, y eso es bueno si se dice.** C era "cambiar el calendario de pago y que lo pague el acreedor" y fallaba porque el ambulante casi no tiene deuda formal mensual (10.2, C, criterio 01). E aplica el mismo principio al crédito que el ambulante sí tiene. Presentarlo como hallazgo nuevo sin mencionar C haría que un evaluador atento lo lea como el mismo mecanismo con otro nombre.

### R.6 Recomendación

**Debe liderar E1, contado como la evolución de C sobre el crédito que el ambulante sí tiene, con A y F como los dos descartes.** La historia que el PDF puede contar y nadie más tiene es un cambio de pregunta con dato propio: empezamos diseñando un préstamo más barato (A), vimos que en pesos por día es solo 14% más barato, que no llega al equilibrio con montos de ambulante y que depende de una usura que quizá no aplica; el campo mostró que el vendedor ya tiene un crédito diario gratis y que el gota a gota entra el día que la lluvia lo rompe; probamos asegurar ese día (F) y nuestra serie del IDEAM mostró que un evento de dos veces al mes no se asegura barato; lo que queda es mover la fecha, que cuesta decenas de pesos, y hacer que la cargue el de arriba. Eso sube creatividad, trazabilidad y descartes a la vez, y el riesgo real queda nombrado (al mayorista hoy no le duele). A no desaparece: su escalera y su diagnóstico quedan en la sección de alternativas con sus números. C se menciona en una línea como el principio que E aplica. Si el campo no confirma las condiciones de R.7, lidera A como estaba, con el hallazgo del día malo en el diagnóstico y E como riesgo abierto, no como propuesta.

### R.7 Qué tiene que confirmar el campo antes de las 9:30 a. m. del 27 sep (cierre a las 12:00)

Es domingo: lo realista es que el colaborador vuelva a hablar, por teléfono o en persona, con los mismos vendedores del 26 sep y con al menos un minorista que les fía. Preguntas en pasado concreto (E1 a E3 y F2 de este archivo). Los umbrales son supuestos del evaluador **[S]**, fijados antes de oír las respuestas.

| # | Qué confirmar | Umbral para que E lidere | Si no se cumple |
|---|---|---|---|
| 1 | El minorista exige el pago el mismo día o corta o baja el fiado de mañana | 4 de 6 vendedores lo describen con un caso concreto (fecha aproximada, qué dijo el minorista) | Si 3 o más de 6 dicen que el minorista espera sin problema, E muere: lidera A |
| 2 | La plata del gota a gota del día malo fue a pagarle al que fía | Al menos 3 de 6 nombran un caso (propio o de un compañero) en que el préstamo fue para pagarle al minorista, y al menos 2 lo cuentan en primera persona | Si el uso que nombran es el hogar (comida, arriendo), E cubre la mitad del problema: E lidera solo si se cumple 1 y se dice el hueco |
| 3 | Lo que no se vende el día de lluvia no se daña | 4 de 6 dicen que la mayor parte se vende al otro día | Si la mayoría se daña, E solo reparte una pérdida (27% a 54% del ingreso por 3 días): E baja a complemento y A lidera |
| 4 | El monto del fiado diario | Mediana entre $20.000 y $80.000 | Por encima de $100.000, recalcular la economía antes de escribir |
| 5 | El choque sube por la cadena | El minorista paga a su proveedor de contado o a menos de una semana, y perdió al menos 1 vendedor por deudas en el último año | Si tiene plazo holgado y no pierde vendedores, no hay quién pague E1: presentarlo con el pagador como riesgo principal, sin tarifa en el modelo base |
| 6 | La lluvia es el día malo y coincide con la estación | Los vendedores dicen entre 1 y 4 días malos al mes y al menos 2 fechas nombradas coinciden con días de disparo del IDEAM | Si el día malo principal es vacaciones, paro o enfermedad, el disparador de lluvia no es el correcto |

Además, antes de las 9:30 y sin campo: la prueba de 2.6 (enunciado más hallazgo en tres modelos, respuestas guardadas para el anexo). Si alguno propone el aplazamiento pagado por el mayorista, la originalidad se declara en el hallazgo y no en el mecanismo.

Regla de decisión: E lidera si se cumplen 1 y 3, y al menos uno de 2 o 5. Con solo 1 cumplido, E va como mecanismo con el hueco nombrado y A como plan B en alternativas. Con 1 fallado, lidera A.
