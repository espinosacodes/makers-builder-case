# Brief final del editor

Fecha: 27 sep 2026, madrugada. Entrega: hoy a las 12:00 (hora Colombia). Archivo: `report/MAKERS_SANTIAGO_ESPINOSA_CALI.pdf` (nombre exacto, carta, cuerpo de máximo 5 páginas, "ANEXOS" en página nueva).

Este brief reemplaza a `brief-evaluator.md`, `brief-field.md` y `brief-viability.md`. Donde se contradigan, manda este. Se leyó además `docs/research/12-mecanismos-dia-malo.md` completo (con su revisión adversarial) y la sección 11.7 de la síntesis, que ya existen, y se verificaron contra el anexo del DANE las cifras de Cali que el brief de campo marcó como nuevas (resultado en la sección 7, hechos N1 a N3).

Convenciones de este documento: F1 a F40, P1 a P12, C1 a C20 y R1 a R58 son los ids de `report/fact-pack.md`. N1 a N12 son hechos o cálculos nuevos definidos en la sección 7. [S] marca un supuesto propio sin dato.

---

## 0. Decisión en corto

**Mecanismo elegido: E1 del frente 12, refinado, con el nombre "Cláusula de lluvia del fiado".** Cuando la estación del IDEAM marca día de lluvia, lo que el vendedor de carrito no alcanzó a pagar de su fiado ese día se paga en tercios en sus tres días de venta siguientes, sin recargo, y al otro día recibe fiado como siempre. Quien fía carga ese plazo y paga una tarifa por vendedor inscrito. Yo pongo el dato, la regla escrita y el registro. No presto, no aseguro y la plata del vendedor nunca pasa por mi empresa.

Por qué este y no otro:
- Es el único que nace del hallazgo de campo y ataca el momento en que, según ese hallazgo, entra el gota a gota (la tarde del día sin ventas). Eso es lo que el bloque 1 premia: causa raíz y un solo mecanismo para los cuatro puntos.
- Es el único que resuelve "no soy entidad financiera" sin pedirle nada a nadie con licencia: no hay crédito nuevo, ni prima, ni plata de terceros.
- Es viable el día 1 con una persona: el primer cliente es el minorista que surte a los carritos de la estación Universidades, al que se llega por los mismos vendedores; no hace falta un mayorista para arrancar.
- Honestidad: la premisa (el minorista exige el pago el mismo día y el gota a gota se toma para pagarle) viene de un resumen oral de segunda mano y choca con la única etnografía del fiado en Cali. El PDF la presenta como hipótesis, nombra la contradicción y dice cuál es la primera prueba que la mata.

Puntaje de juez (1 a 5 por criterio, misma escala que la síntesis 10.2):

| Criterio | Cláusula (E final) | A ventanilla del tendero | C cuota diaria de la deuda mensual | F día de lluvia pagado |
|---|---|---|---|---|
| 01 Efectividad | 3 | 3 | 3 | 2 |
| 02 Especificidad | 4 | 4 | 3 | 3 |
| 03 Creatividad | 4 | 2 | 3 | 2 |
| 04 Diagnóstico | 3 | 4 | 3 | 2 |
| 05 Fuentes | 4 | 4 | 3 | 3 |
| 06 Trazabilidad | 4 | 4 | 3 | 3 |
| 07 Juicio cuantitativo | 4 | 3 | 2 | 3 |
| 08 Descartes y autocrítica | 4 | 3 | 3 | 3 |
| **Total (de 40)** | **30** | **27** | **23** | **21** |

01 y 04 se quedan en 3 porque la premisa no está confirmada en primera persona. Sube respecto del 27 de la revisión adversarial de `12` porque este brief corrige lo que esa revisión marcó: la hora del disparo frente a la hora del pago, quién paga, E2 fuera del plan, el argumento del margen con nuestra tarifa, la línea de C declarada, una sola convención de ingreso y el riesgo de la premisa puesto al frente.

Qué tomé de cada brief:
- **Evaluador:** la estructura "la lluvia decide la fecha", las cinco diferencias con la respuesta predecible 6, la tabla de validación con criterios de muerte, la idea de no agregarle piezas al mecanismo.
- **Campo:** el pagador que arranca en el minorista y sube al mayorista, el minorista que decide quién entra pero no cobra por nadie, "cero rastro" para el vendedor, la contradicción con Palmira dicha en el cuerpo, y la lectura del DANE por ciudad (verificada y corregida aquí).
- **Viabilidad:** la base de costos de una persona, el modelo `models/fiado_bridge_viability.py`, el bot que nunca le escribe al vendedor, la vista del que paga ("se paga sola si evita perder 1 de cada 20 vendedores"), el primer mes gratis y los criterios de muerte por mes.

---

## 1. Tesis

**Una frase (va en negrita debajo del título):**
"El gota a gota no le gana al sistema formal principalmente por precio ni por requisitos, sino porque aparece la tarde en que un día sin ventas rompe el crédito que el vendedor ya tiene, el fiado diario sin interés de su minorista; el formal no compite ahí porque vende plata a meses a alguien a quien le faltan uno o dos días."

**Cierre del diagnóstico (una línea):** "Al vendedor no le falta crédito. Le falta que un día de lluvia no cuente como quedar mal."

Qué la sostiene:
- No es precio: en cuota diaria, el préstamo legal más caro permitido se ve apenas 12 a 15% más barato que el gota a gota ($3.436 frente a $4.000 diarios por cada $100.000 en 30 cuotas; P1, P2). La usura del popular productivo subió de 52,89% a 88,13% E.A. y la SFC no vio más acceso (F17). Solo 6,5% de los micronegocios que no piden crédito dice que es por la tasa (F15).
- No es sobre todo requisitos: 14,6% no pide por requisitos y 42,5% por miedo a endeudarse; a quien pide le aprueban 92,9% (F15). La informante sí menciona requisitos (C4): decir que las dos cosas se mezclan.
- Es la forma: 87,2% del crédito formal se paga en cuota mensual (F20) y originar un microcrédito cuesta $1.117.131 fijos (F18).
- El crédito diario ya existe (C15, C16; WIEGO F13) y el choque es de uno o dos días (N4).

Qué la refutaría (va en la página 2, dicho por Santiago):
- Que el minorista de carritos ya espere uno o dos días sin problema. La única etnografía del fiado en Cali describe un fiado sin fecha fija, que "debe saldarse en los próximos días" (Martínez Benavides 2021, R52; es una tienda de ropa en Aguablanca, no un surtidor de carritos).
- Que la plata del gota a gota del día malo se vaya sobre todo al hogar y no a pagarle al que fía (entre los ambulantes, 28,9% del crédito va a gasto personal y 20,5% a negocio y hogar; F9).

---

## 2. El mecanismo

### 2.1 Nombre y frase

Nombre (simple, sin marca): **Cláusula de lluvia del fiado.**

Frase para el PDF: "Cuando la estación del IDEAM en la Universidad del Valle registra 5 mm o más de lluvia entre 7 a. m. y 7 p. m., lo que el vendedor no alcanzó a pagar de su fiado ese día se paga en tercios en sus tres días de venta siguientes, sin recargo, y al otro día recibe fiado como siempre. Quien fía carga ese plazo y me paga $4.000 al mes por vendedor inscrito. Yo pongo el dato, la regla escrita y el registro. No le presto a nadie, no aseguro a nadie y la plata del vendedor nunca pasa por mí."

Línea de origen, obligatoria (revisión adversarial de `12`, R.5 punto 9): "La idea de fondo ya estaba en una de mis opciones anteriores: cambiar el calendario de una deuda y que lo pague el acreedor (C). Fallaba porque el ambulante casi no tiene deuda formal mensual: solo 22,5% de los que piden crédito va a una entidad regulada (F7). Aquí la aplico al crédito que sí tiene."

### 2.2 Paso a paso (tabla para la página 3; copiar tal cual o recortar palabras, no filas)

| Momento | Quién | Qué hace | Con qué | Dónde está la plata |
|---|---|---|---|---|
| Semana 0 | Yo | Constituyo una SAS de servicios de información (Ley 1258 de 2008). Dejo corriendo el programa que lee cada 30 minutos la estación 0026055120 del IDEAM. Un abogado revisa la cláusula de una página | SAS, API de datos.gov.co, WhatsApp Business | Capital propio en la cuenta de la SAS |
| Semana 1 | Yo y un minorista que fía a carritos cerca de la estación Universidades del MIO | Le propongo la cláusula: si el IDEAM marca 5 mm o más entre 7 a. m. y 7 p. m., lo que sus vendedores no alcanzaron a pagar ese día se paga en tercios en los 3 días de venta siguientes, sin recargo, y al otro día hay fiado. Primer mes gratis; después, $4.000 al mes por vendedor inscrito | Una hoja impresa; el dato, que él puede revisar solo | Nada se mueve |
| Semana 1 | Minorista | Escoge qué vendedores entran (los que le sacan fiado hace 4 semanas o más) y les explica la regla con una tarjeta | Su palabra y una tarjeta física. Al vendedor no se le pide cédula, RUT, celular ni app | Nada se mueve |
| Día normal | Vendedor y minorista | Igual que hoy: fiado en la mañana, pago en la tarde | Mercancía y efectivo | Del bolsillo del vendedor a la caja del minorista |
| Día de lluvia, apenas el acumulado pasa 5 mm | Programa | Le escribe al minorista: "Hoy es día de lluvia (Univalle, 6 mm a las 2:30 p. m.). Rige la cláusula." Si la lluvia llega tarde, el aviso sale hacia las 8:30 p. m., con el dato del día completo | API del IDEAM (el dato se publica con cerca de 1,5 horas de rezago), WhatsApp | Nada se mueve |
| Esa noche | Minorista | Responde quién no alcanzó a pagar y cuánto ("vendedor 3: 45"). Decide el fiado de mañana después del aviso, no antes | WhatsApp | La deuda sigue siendo con él, con otra fecha |
| Días de venta 1 a 3 | Vendedor y minorista | El vendedor saca fiado como siempre y paga lo del día más un tercio de lo aplazado. El programa le confirma al minorista "puente cerrado" | Efectivo; WhatsApp solo con el minorista | Del vendedor al minorista |
| Si el minorista le paga a diario a su proveedor | Mayorista | La misma cláusula sube un eslabón: corre en igual monto el cobro al minorista y pasa a ser quien paga la tarifa | Anexo de una página a su acuerdo con el minorista | Cuenta por cobrar del mayorista |
| Si no cierra en 5 días de venta | Minorista | Decide él, como hoy con su fiado. El programa marca al vendedor como no elegible para el siguiente día de lluvia. Yo nunca cobro ni contacto al vendedor | Nada nuevo | La pérdida es de quien fía, igual que hoy |
| Fin de mes | Quien carga el plazo | Paga la tarifa | Nequi o transferencia | Única entrada de la SAS |

Reglas debajo de la tabla (una línea cada una):
- Tope de 3 días de disparo seguidos y de 2 fiados aplazados por vendedor [S]. Cubre todas las rachas de los últimos 12 meses: 21 de un día y 3 de dos, ninguna de tres (N4).
- Si ninguna estación tiene dato, el minorista puede declarar el día, como máximo una vez al mes; cuando llega el dato se revisa y, si no hubo lluvia, esa declaración cuenta como la del mes. El costo de equivocarse es el valor del dinero de un día, porque la deuda no se perdona.
- Nunca hay recargo para el vendedor. Cobrarle algo a cambio de que la regla se active con la lluvia se parecería a un seguro sin licencia (frente 12b).
- El programa solo habla con el minorista (y con el mayorista si entra). Al vendedor no le llega ningún mensaje: 48,4% de los ambulantes usa celular en el negocio (F8), y un mensaje sobre lo que debe podría leerse como cobranza (Ley 2300, F29).

### 2.3 Lo que no cubre (va en la página 3, unas 60 palabras)

- Enfermedad, choque familiar, vacaciones universitarias o paros. El caso de la vendedora de arepas de la informante (C7) queda fuera y se dice.
- Mercancía que se daña: la cláusula corre la deuda, no la achica. Pagar el fiado entero en tercios cuesta de 27% a 54% del ingreso de cada uno de esos tres días (N6). Ahí el gota a gota puede seguir siendo la salida.
- El ingreso que no hubo: la cláusula deja lo poco que se vendió ese día para la casa, pero no lo reemplaza.

Extensión que NO entra al plan base: un día malo "ganado" al mes para vendedores con 8 semanas limpias. Si se menciona, una sola línea: "la probaría después del mes 4 y solo si el impago de lo aplazado queda bajo 3%, porque en Barranquilla y Cartagena la flexibilidad a pedido del deudor subió el impago (F39)".

### 2.4 Lo que se saca del mecanismo

- **E2 (prestarle yo el plazo al minorista) sale del plan.** Con 1% de impago del minorista pierdo $14.537 por vendedor al año (P10) y me vuelve prestamista, que rompe el punto 1. Solo una línea en el Anexo E.
- **No hay reserva de capital para prestar** en la inversión inicial.
- **Nada de seguro encima.** F es el descarte 2.

---

## 3. Cómo una sola pieza resuelve los cuatro puntos (página 4, unas 250 palabras)

La pieza: **un dato público de lluvia que corre la fecha de pago de un crédito que ya existe entre comerciantes que ya se conocen.**

1. **No soy entidad financiera.** No presto ni aseguro. El crédito (el fiado) ya existe y lo dan comerciantes a comerciantes, sin interés, así que no hay usura que calcular. No hay prima ni indemnización, así que no es seguro. La plata del vendedor nunca pasa por mi cuenta, así que no hay captación (F31). Vendo un servicio de información desde una SAS, desde el día 1. Pregunta abierta para el abogado: si una regla de aplazamiento pagada por quien fía puede leerse como seguro; la respuesta prudente ya está en el diseño (el vendedor no paga nada y yo no indemnizo a nadie).
2. **Ingreso diario sin ahorro.** La regla solo actúa el día en que no hubo ingreso, que es cuando la falta de ahorro obliga a pedir (49,9% de los adultos no podría reunir fondos de emergencia en 30 días o le sería muy difícil; F16). La devolución va en tercios dentro del ritual que ya tiene, pagar cada tarde, en días de venta y nunca en domingo, como cobra el propio informal (C6, F23).
3. **Soy un desconocido de 22 años.** El vendedor no tiene que confiar en mí: no me conoce ni me entrega nada, y su trato sigue con el minorista de siempre. Honestidad obligatoria: la confianza no desaparece, se mueve a una venta a pocos minoristas, que tampoco me conocen. A ellos no les pido plata ni que me crean: el disparador es un número del IDEAM que pueden revisar solos, el primer mes es gratis y les doy algo que hoy no tienen, una razón externa para esperar sin tener que juzgar si el vendedor miente. La paciencia que hoy se consigue como favor personal (C9) se vuelve una regla. Confianza en desconocidos: 5,6% (F14).
4. **El problema ya tiene soluciones.** Todas venden plata con calendario mensual o de 30 días (bancos y microfinancieras con ticket promedio de $8,43 a $9,96 millones, F19; Nequi con promedio de $2,3 millones, F35; Bogotá con Monet a 30 días, F34; CREO, F33) o aseguran estados del mundo, en el agro. El mercado ya vende este puente, caro: el "diario anticipado" de Corabastos cobra 10% en el día (F24). No encontré a nadie que corra la fecha de un crédito que ya existe con un dato público (búsqueda limitada; decir "no encontré"). Lo que aprendí y usé: mover el pago en el tiempo pesa más que indemnizar (72% frente a 5% de adopción; Casaburi y Willis, F40); la flexibilidad solo con historial y sin que la pida el deudor (F39); el crédito atado a mercancía que rota se paga (AB InBev: 93,6% de sus cuentas por cobrar al día, reserva del fact pack, R56); pagarle la deuda al prestamista no rompe el ciclo, hay que llegar antes del primer préstamo (F38).

Frase de cierre de la sección (opcional): "El mismo dato que le quita la licencia al problema le quita la desconfianza: nadie tiene que creerle a nadie que llovió."

## 4. Parecido con las respuestas predecibles y con el mercado (página 4, unas 110 palabras)

Nombrarlo antes que el evaluador: se parece a la **6** (crédito de proveedor o BNPL para inventario) y un poco a la **9** (cuaderno de fiado digital). En el mercado, a Tienda Pago y al plazo de BEES (citar Tienda Pago sin cifras, "según su sitio"). Diferencias de mecanismo, no de nombre:
1. No crea crédito ni alarga el plazo normal: el plazo sigue en cero días y solo se abre cuando pasa un evento.
2. Lo activa un dato público, no una solicitud ni una evaluación.
3. Carga el plazo quien hoy le pasa el choque al vendedor, no un financiador nuevo.
4. Actúa la tarde del día malo, no cuando el negocio quiere crecer.
5. El vendedor no paga nada ni se inscribe; el registro no es el producto, existe solo para cerrar el puente unas dos veces al mes.

Prueba de originalidad con IA (pegar el caso más el hallazgo en tres modelos y ver si alguno propone esto): solo se menciona si se hizo antes de entregar, con el resultado tal cual en el Anexo C. Si no se hizo, no se menciona.

---

## 5. Usuario exacto, cliente que paga y alcance

**Usuario.** Vendedor de carrito que cada mañana saca fiada, sin interés, la mercancía del día a un minorista que le surte, y se la paga esa tarde con lo que vendió. Trabaja a la intemperie, opera como persona natural, sin RUT. Entra quien lleva 4 semanas o más sacando fiado con ese minorista [S].

**Dónde empieza.** Los carritos alrededor de la estación Universidades del MIO, en el sur de Cali, donde el colaborador conversó con vendedores el 26 sep 2026. El disparador es la estación IDEAM 0026055120 (Universidad del Valle, Meléndez). La distancia entre la estación y los carritos no está medida: decirlo, o medirla con coordenadas y ponerla en el Anexo F.

**Cliente que paga.** Quien carga el plazo: en el piloto, el minorista; si él le paga a diario a su proveedor, el mayorista.

**Cuántos, con fuente:**
- 286.061 micronegocios ambulantes en 24 ciudades; 15,4% pidió crédito (F8). De los que pidieron, 61,8% fue a un gota a gota, frente a 11,3% en tiendas de barrio (F7).
- En Cali A.M., 17.745 micronegocios ambulantes, 8,0% de los micronegocios de la ciudad (N1, CV 8,4%).
- En Cali, 51,3% de la deuda de los ambulantes del centro y la galería Santa Elena era con gota a gota, a 20,4% mensual en promedio (F12; datos de 2016, decir el año).
- 93,3% de los ambulantes no tiene RUT (F10).
- **Lo que no se sabe y hay que decir:** cuántos ambulantes de Cali sacan fiado diario de mercancía. El DANE casi no lo ve: entre los ambulantes que pidieron crédito, solo 1,8% se lo pidió a un proveedor (F7), probablemente porque nadie llama "crédito" a la mercancía del día (inferencia del frente 12a). Es el primer dato que mide el piloto.
- Alcance del plan: 40 vendedores en el mes 3, 144 en el mes 6, 468 en el mes 12; equilibrio con unos 900, que serían 5% de los ambulantes de Cali A.M. si todos sacaran fiado, y no sé cuántos lo hacen (N12). Si funciona en un corredor, crece por mayorista, no vendedor por vendedor.
- Geografía, una línea: el gota a gota de micronegocios se concentra en el Caribe (P12), pero mi campo, mi informante y mi disparador están en Cali; la cláusula se calibra estación por estación.

---

## 6. Contradicciones entre briefs y cómo quedan

| Tema | Evaluador | Campo | Viabilidad | Decisión final |
|---|---|---|---|---|
| Quién paga | Mayorista desde la semana 1 | Minorista (fase 1), mayorista (fase 2) | Quien cargue el plazo | Paga quien carga el plazo. Piloto con el minorista; la cláusula sube al mayorista si el minorista paga a diario hacia arriba. Una sola tarifa: $4.000 |
| Base de costos | $4 millones y luego $10 millones | $1,2 y luego $6 millones | $2,53 millones | $2,53 millones al mes (una persona con 1 SMMLV). $10 millones solo como escenario del Anexo E |
| E2 | Arranque con tope de $5 millones | Descartado | Fuera del plan base | Fuera. Una línea en el Anexo E |
| Comodín de día no lluvioso | No | Sí, desde la semana 8 | Extensión futura | Fuera del plan base; como mucho una línea |
| Mensajes al vendedor | Solo minorista | Minorista y vendedores | Solo minorista y mayorista | Solo minorista y mayorista |
| Hora del disparo frente a hora del pago | Noche | Noche | Noche | Aviso apenas el acumulado pasa 5 mm; si no, confirmación hacia las 8:30 p. m.; el minorista decide el fiado de mañana después del aviso |
| Rachas de lluvia | 12 meses | 2025 | Usar 12 meses | Serie de 12 meses (N4). La de 2025 solo en el Anexo F |
| Ingreso diario | $38.000 | $38.000 | $38.000 | $38.600 por día de venta (unos $1,0 millón al mes en 26 días; F11). Recalcular todo con esta cifra |
| Argumento del margen | 1% a 4% del margen | No | Con tarifa: 1 de cada 20 vendedores | Con tarifa incluida (N7). "1% a 4%" no se usa |
| Cifras "[NUEVO]" de Cali | No | En el cuerpo | En anexo | 17.745 en el cuerpo con CV (N1, verificado). Móvil y estacionario, nunca (N3). 11,6% y 8,8% solo en el Anexo G (N2) |
| Battaglia et al. | "bajó el impago" | Sí | Sí | Fuera del PDF (síntesis 10.3, punto 8: sin verificación independiente) |
| Nombre | "El puente del fiado" | "La regla del día de lluvia" | "Puente del fiado" | "Cláusula de lluvia del fiado" |
| Riesgo principal | Al de arriba no le duele | El hueco sube un eslabón | Al de arriba no le duele | Dos capas: primero el riesgo de la premisa (que el hueco no exista), después el riesgo del negocio (que nadie quiera cargarlo). Sección 10 |

---

## 7. Hechos nuevos (N1 a N12) que no están en el fact pack

| Id | Hecho | Fuente y cómo se obtuvo | Uso |
|---|---|---|---|
| N1 | Cali A.M. tiene 17.745 micronegocios ambulantes ("ambulante, sitio al descubierto"), 8,0% de los micronegocios de la ciudad | DANE, EMICRON 24 ciudades 2025, Cuadro D.1_24C (R3). Verificado por el editor en el archivo del anexo el 27 sep; CV 8,4% (conteo) y 8,0% (porcentaje), precisión aceptable | Cuerpo, página 3, con cuadro y CV; tabla en el Anexo G |
| N2 | Entre los micronegocios de Cali A.M. que pidieron crédito (35.496): crédito de proveedores 11,6% (4.105; CV 15,2%) y gota a gota 8,8% (3.130; CV 17,1%); institución regulada 64,4%. En las 24 ciudades: 3,0% y 35,6% | Mismo anexo, Cuadro H.4_24C. Verificado por el editor | Solo Anexo G, con la advertencia de precisión baja (CV mayor a 15%) y de que es de todos los micronegocios, no de ambulantes |
| N3 | El Cuadro D.5_24C parte a los ambulantes de Cali en "móvil" (7.993) y "estacionario" (9.752), pero la nota del DANE define "estacionario" como quien "se desplaza en el espacio y porta los bienes sobre sí" | Mismo anexo, nota del Cuadro D.5_24C | No usar en ninguna parte. El brief de campo lo leyó al revés |
| N4 | Últimos 12 meses (27 sep 2025 a 26 sep 2026): 26 de 294 días de venta con 5 mm o más entre 7:00 y 18:59 (8,8%); en todos los días, 27 de 340. Rachas: 21 de un día y 3 de dos, ninguna de tres o más. Octubre de 2025 y mayo de 2026, 7 días cada uno | `12-mecanismos-dia-malo.md`, sección 1 (cálculo propio sobre IDEAM, R51) | Cuerpo, páginas 2 y 3 |
| N5 | El dato del IDEAM se publica con cerca de 1,5 horas de rezago (el registro de las 23:50 del 26 sep estaba publicado a la 1:17 a. m. del 27) | Frente 12b | Tabla de paso a paso y Anexo F |
| N6 | Con mercancía que se daña, pagar el fiado en tercios cuesta 27% ($31.000) a 54% ($62.000) del ingreso de cada uno de esos tres días ($38.600) | Cálculo propio (`12`, R.5 punto 1) | Página 3, "lo que no cubre" |
| N7 | Para quien carga el plazo, por vendedor al año: tarifa $48.000 + costo del dinero unos $2.000 + impago de lo aplazado. Con fiado de $62.000, 3% de impago y margen bruto de 10% [S], la cláusula se paga sola si le evita perder 5,1% de sus vendedores al año (1 de cada 20); con fiado de $30.000, 7,7% | Cálculo propio, `models/fiado_bridge_viability.py`, función `retailer_view` | Página 4 o 5, una línea; tabla en el Anexo E |
| N8 | Para el vendedor, cubrir el fiado de un día de lluvia con un préstamo de gota a gota a 20% cuesta $6.000 ($30.000) a $12.400 ($62.000), 16% a 32% del ingreso de un día; con el "diario anticipado" a 10%, la mitad. Con la cláusula, $0 | Cálculo propio sobre F24 y el enunciado del caso | Página 4, una línea |
| N9 | Plan de negocio: inversión $3,9 millones; costo fijo $2.530.905 al mes; $2.800 por vendedor al mes; equilibrio con 904 vendedores en el mes 22; caja necesaria $34,5 millones (con salario) u $8,5 millones sin salario (equilibrio en el mes 10) | `models/fiado_bridge_viability.py` (corrido por el editor) | Tabla de números, página 4 |
| N10 | Prima de F recalculada con $38.600: fiado entero cada día de lluvia $16.636 por día de venta (43% del ingreso); pérdida de $15.000, $4.025 (10%); capa de mes malo $2.477 (6%); una prima de $500 diarios compra un pago de unos $1.863 | `models/bad_day_mechanisms.py` (P9, P11) con el ingreso de la convención | Descarte 2 |
| N11 | Economía de A sin la convención de $10 millones: con pérdidas de 1,5% o más por ciclo, el neto por usuario ya es negativo (P6), así que ningún volumen de usuarios lo salva | Lectura de P6 | Descarte 1 |
| N12 | 904 vendedores equivalen a 5,1% de los 17.745 ambulantes de Cali A.M. | Cálculo propio sobre N1 y N9 | Página 3, alcance, con la advertencia de que no se sabe cuántos fían |

---

## 8. Esquema página por página

Presupuesto del cuerpo: unas 2.350 palabras y 3 tablas. Con `style.css` (Charter 9,8 pt, márgenes de 1,5 cm) caben unas 800 palabras de prosa por página; una tabla de 9 a 10 filas en 8,5 pt ocupa cerca de 40% de una página. Medir después del primer render y recortar prosa, nunca filas de la tabla del paso a paso ni de los números.

Título: "Cláusula de lluvia del fiado". Línea de autor: "Santiago Espinosa · Cali, Colombia · Builder Case, Makers Fellowship · 27 de septiembre de 2026". Debajo, la tesis en negrita.

Citas en el texto: cortas, "(DANE, EMICRON ambulantes 2025, C. 18.1)", "(Karlan, Mullainathan y Roth 2019)", "(cálculo propio, Anexo E)". Referencias completas con URL en el Anexo B.

### Página 1. Diagnóstico: el crédito que ya existe y el día que se rompe (unas 560 palabras, sin tabla)

- **Tesis** (50 palabras): la frase de la sección 1.
- **Tamaño** (140 palabras). F1 (5.297.252 micronegocios); F3 (14,2% pidió crédito, 22,9% de ellos fue a un gota a gota, 160.724 negocios: piso oficial); F4 (35,6% en las 24 ciudades); F7 (61,8% de los ambulantes que piden frente a 11,3% en tiendas: el usuario central no es el del mostrador); F12 (Cali, 51,3% de la deuda de los ambulantes, datos de 2016).
- **Consecuencias** (120 palabras). F5 (el gota a gota es 17,7% de la deuda de los hogares con ingreso de hasta 1 SMMLV); deuda que paga deuda (C2: "para pagarle a uno, se meten en otro"; C18, palabras del colaborador: "un gota a gota con otro gota a gota"; F21: 36% pide para pagar otras deudas, Perú); F38 (pagarle al prestamista no saca de la trampa); amenaza como forma principal de cobro (F26, Costa Rica, decirlo) y como lo primero que aparece en los casos de Cali (C1); C7 (la vendedora de arepas que "ni volvió a sacar el negocio", como ilustración de segunda mano).
- **Por qué falla el formal** (150 palabras). No es el precio: P1 y P2 (12 a 15% más barato por día, cálculo propio), F17. No es falta de cuentas: F16 (96,5% con depósito, 8,0% pidió a un banco). Es la forma: F20 (87,2% en cuota mensual), F18 ($1.117.131 fijos; un crédito de 1 SMMLV cuesta 100,3% de lo prestado), F19 (ticket promedio de $8,43 a $9,96 millones). Y el usuario no pide: F15 (42,5% miedo, 14,6% requisitos, 6,5% tasa; aprobación de 92,9%).
- **Qué hace bien el informal** (100 palabras). Dos piezas. El fiado: diario, sin interés, basado en conocer a la persona, con la exclusión como sanción (R52: "Que no pague entonces, pero que no vuelva por acá"; F13). El gota a gota: llega esa tarde, sin papeles, cobra en los días de venta (C6, F23), renueva al que paga (F21: 93% paga, 82% llega por recomendación). La amenaza castiga al que se atrasa.
- **Cierre** (una línea): "Al vendedor no le falta crédito. Le falta que un día de lluvia no cuente como quedar mal."
- No usar aquí: F25 (31 cobradiarios), el "atentado", "3 a 4 veces lo que sacan", ninguna cifra de la lista 1.4.

### Página 2. Lo que encontré: el día de lluvia rompe un fiado que funciona (unas 420 palabras y Tabla 1)

- **Método, honesto** (80 palabras), casi textual: "Conversaciones con vendedores de carrito en la estación Universidades del MIO (Cali), hechas por un colaborador en mi nombre en la mañana del 26 sep 2026; tengo su resumen oral, no el número de vendedores ni citas de cada uno. Una informante de Cali que conoce varios casos de amigos y familiares (dos notas de voz, 27 sep 2026; segunda mano, sin muestreo). Yo no entrevisté vendedores en persona y nadie contactó prestamistas. Sirve para encontrar mecanismos, no para medir; por eso cruzo cada hallazgo con un dato oficial o un estudio."
- **Hallazgo central** (110 palabras). C15, C16, C17 (citar: "hay días en que, no sé, llovió, entonces nadie va [...] No le puedo pagar. Y ahí es cuando entran con un gota a gota", como palabras del colaborador, cortando antes de "eso les pasa a muchos de ellos"), C18, C19. Una línea: "No encontré publicado el paso 'tomo un gota a gota para no perder el fiado de mañana' (búsqueda limitada). Lo trato como hipótesis de trabajo."
- **El número propio** (80 palabras). N4: 26 de 294 días de venta, unos dos al mes, 21 rachas de un día y 3 de dos, ninguna de tres; octubre y mayo. Lectura: el choque es frecuente y corto; cuando la mercancía no se daña, lo que falta ese día es tiempo, no plata.
- **Lo que no cuadra, dicho** (90 palabras). (1) Martínez Benavides 2021: el fiado de Aguablanca no tiene fecha fija; si el minorista de carritos ya espera, mi mecanismo no agrega nada, y es lo primero que pruebo. (2) Palmira frente a Cali: el prestamista de Palmira castiga negando el siguiente préstamo (F23) y en los casos de Cali lo primero es la amenaza (C1). Lectura: la renovación premia al que paga y la amenaza castiga al que se atrasa.
- **La pregunta que cambió** (40 palabras): de "¿cómo le presto más barato?" a "¿cómo evito que un día de lluvia rompa un fiado que ya funciona?".
- **Tabla 1. Hallazgo, qué lo respalda, qué decidí** (8 filas, frases cortas):

| Hallazgo | Qué lo respalda | Qué decidí |
|---|---|---|
| El vendedor saca fiado sin interés cada mañana (C15, C16) | WIEGO: "I take stock on credit every morning then pay back in the evening" (F13) | No crear crédito: trabajar dentro del fiado |
| La lluvia rompe el pago y entra el gota a gota (C17) | IDEAM: 26 de 294 días de venta, rachas de 1 a 2 días (N4) | Solo se activa ese día; 3 días para pagar, en tercios |
| Un gota a gota paga otro (C18, C2) | Karlan, Mullainathan y Roth (F38); IPE, 36% (F21) | Llegar antes del primer préstamo; no refinanciar ni prestar |
| El que fía no puede saber si fue un mal día o un mal pagador; la sanción es la exclusión (R52) | La flexibilidad a pedido del deudor nuevo subió el impago (F39) | Decide un dato público, no la palabra del deudor; solo con 4 semanas de historial |
| La recomendación compra paciencia y quien recomienda no quiere cobrar (C9, C10) | IPE: 82% llega por recomendación (F21) | El minorista escoge quién entra; nadie asume un papel nuevo de cobrador; yo nunca cobro |
| Al que amenaza se le paga primero (C11, C12; hipótesis) | UNODC, Costa Rica (F26) | No agrego un acreedor: lo aplazado sigue siendo fiado con la misma persona |
| No se formalizan y no quieren rastro (C19) | 93,3% sin RUT; 48,4% usa celular en el negocio (F10, F8) | Al vendedor no se le pide nada: tarjeta y palabra del minorista |
| El cobro informal sigue los días de venta (C6) | Palmira: no cobra domingos ni festivos (F23) | Devolución solo en días de venta |

### Página 3. La propuesta (unas 380 palabras y Tabla 2)

- **Nombre y frase** (80 palabras): sección 2.1, más la línea de origen en C (40 palabras).
- **Usuario, cliente y cuántos** (110 palabras): sección 5, con F8, F7, N1, F12, F10, F7 (1,8%) y N12. Frase obligatoria: "No sé cuántos carritos de Cali sacan fiado diario; es el primer dato que mide el piloto."
- **Tabla 2. Paso a paso**: la de la sección 2.2.
- **Reglas** (60 palabras): las cuatro líneas debajo de la tabla de 2.2.
- **Lo que no cubre** (60 palabras): sección 2.3, con N6.

### Página 4. Por qué debería funcionar y los números (unas 360 palabras y Tabla 3)

- **Los cuatro puntos con una pieza** (250 palabras): sección 3, apretada. Datos: F31, F16, C6, F23, C9, F14, F19, F35, F34, F33, F24, F40, F39, R56, F38.
- **Parecido y diferencias** (110 palabras): sección 4.
- **Tabla 3. Los números**: la de la sección 9.1, versión corta (pregunta, respuesta, supuesto y fuente).

### Página 5. Si cierra, lo que descarté, el riesgo y cómo sé si me equivoqué (unas 600 palabras)

- **¿Cierra?** (120 palabras): sección 9.4, con N7 y N8 en una línea cada uno.
- **Descarte 1, A** (140 palabras): sección 10.1.
- **Descarte 2, F** (120 palabras): sección 10.2.
- **Una línea**: "También consideré C, B, D, refinanciar la deuda del gota a gota, una app de préstamo y una guía de préstamos; están en el Anexo H con la razón de cada descarte."
- **Riesgo real** (130 palabras): sección 11.1.
- **Cómo sé si me equivoqué** (90 palabras): los criterios de muerte de la sección 11.3, en prosa o en una tabla de 4 filas si cabe.

---

## 9. Especificación de números

Modelo base: `models/fiado_bridge_viability.py` (ya existe, en inglés, corre con `python3`). Extenderlo en el mismo archivo, sin crear otro script salvo que haga falta, para que imprima también: el escenario de $10 millones, el de incorporación lenta, el de 5 vendedores por minorista, la vista del vendedor con el ingreso de $38.600 (N8), la carga con mercancía que se daña (N6) y las primas de F como porcentaje de $38.600 (N10). Cada supuesto con su fuente en un comentario. El Anexo E reproduce las tablas con el comando que las genera.

### 9.1 Las seis respuestas (Tabla 3 del cuerpo)

| # | Pregunta del caso | Respuesta | Supuesto y fuente |
|---|---|---|---|
| 1 | Inversión inicial | $3,9 millones | Registro de la SAS $0,6 millones [S, sin cotización]; concepto de un abogado sobre 5 preguntas $3 millones [S, cotización pendiente]; tarjetas y material $0,3 millones [S]. El programa y el bot los hago yo: $0 en efectivo. No hay capital para prestar porque no presto |
| 2 | Costos mensuales | $2,53 millones | Mi salario, 1 SMMLV de 2026: $1.750.905 (frente 07, confirmado); transporte y campo $200.000; celular y datos $80.000; WhatsApp Business, servidor y herramientas $150.000; contador $350.000 (todo [S] salvo el salario) |
| 3 | Cuánto deja cada usuario | $2.800 por vendedor inscrito al mes | Tarifa de $4.000 [S, sin precedente de precio; rango probado $2.000 a $6.000] por 90% cobrado [S] menos $800 de mensajes y tarjeta [S; verificar el precio de WhatsApp Business en Colombia]. No presto, así que no tengo cartera. El impago de lo aplazado lo carga quien fía: 1%, 3% o 10% de $1,61 millones aplazados al año por vendedor son $16.120, $48.360 o $161.200 (fiado de $62.000, cota superior, P9) [S]; referencia: mora del microcrédito formal 6,9% (R58) |
| 4 | Usuarios e ingresos | Mes 3: 40 vendedores (27 pagando), $108.000 facturados y $76.000 de contribución al mes. Mes 6: 144 (108), $432.000 y $302.000. Mes 12: 468 (416), $1,66 millones y $1,16 millones | 4, 12 y 36 minoristas con 10, 12 y 13 vendedores cada uno [S]; 4 minoristas nuevos al mes desde el mes 7 [S]; primer mes gratis por minorista. Entrada por los vendedores de la estación Universidades y luego por minoristas que le compran al mismo mayorista |
| 5 | Break-even | 904 vendedores, mes 22 | $2.530.905 / $2.800. Con el ritmo de la fila 4 |
| 6 | Cuánto necesito para sobrevivir | $34,5 millones con mi salario; $8,5 millones si trabajo sin salario hasta el equilibrio (mes 10, 279 vendedores) | Inversión más pérdidas acumuladas hasta el punto más bajo. De dónde: [confirmar con Santiago antes de escribir] ahorro propio y aportes de capital de mi familia a la SAS, como socios y no como préstamos, para no acercarme a la captación; la diferencia hasta $34,5 millones sería capital semilla que hoy no tengo. No cuento con el fellowship como fuente de plata |

### 9.2 Supuestos clave (para el Anexo E, con qué pasa si están mal)

| Supuesto | Valor | Fuente o razón | Qué pasa si está mal |
|---|---|---|---|
| Días de disparo | 26 al año | N4 | Con 10 mm son unos 15 días en 12 meses: menos costo para la cadena, menos cobertura |
| Umbral | 5 mm entre 7 a. m. y 7 p. m. | Convención del frente 12b [S]; sin calibrar con ventas | Se calibra en el piloto contra los días que los vendedores recuerdan como malos |
| Fiado diario | $30.000 [S] a $62.000 (cota) | $62.000 = ventas diarias de un ambulante menos su ingreso mixto (P9); no medido para carritos | Escala el costo de la cadena, no mi margen |
| Parte no pagada el día de lluvia | 50% a 100% [S] | Sin dato | Escala lineal |
| Plazo promedio | 2,5 días [S] | Tercios más domingos | Irrelevante: el dinero cuesta unos $2.000 al año por vendedor |
| Impago de lo aplazado | 1%, 3%, 10% [S] | Sin dato colombiano; R58 como referencia | Es lo que decide si quien fía acepta |
| Tarifa | $4.000 [S] | Sin precedente | Mueve el equilibrio de 550 a 2.531 vendedores |
| Vendedores por minorista | 10 a 13 [S] | Sin dato; pregunta de campo | Con 5, el equilibrio pide más del doble de minoristas |
| Ritmo | 4 minoristas nuevos al mes desde el mes 7 [S] | Capacidad de una persona | Con 2 al mes, recalcular (el brief de viabilidad estimó mes 39 y unos $55 millones: verificar con el script) |
| Margen bruto de quien fía | 10% [S] | Sin fuente | Solo mueve el argumento de venta (N7) |
| Ingreso del vendedor | $38.600 por día de venta | F11, 26 días al mes | Única convención del PDF |

### 9.3 Escenarios (salida del script, van en el Anexo E; en el cuerpo, una línea)

| Tarifa al mes | Con mi salario | Sin salario |
|---|---|---|
| $2.000 | 2.531 vendedores; no llega en 36 meses; caja de $67,5 millones | 780; mes 19; $12,4 millones |
| $4.000 (base) | 904; mes 22; $34,5 millones | 279; mes 10; $8,5 millones |
| $6.000 | 550; mes 15; $25,8 millones | 170; mes 8; $7,5 millones |

Más: equipo de $10 millones al mes, unos 3.570 vendedores para el equilibrio (10.000.000 / 2.800); incorporación lenta y 5 vendedores por minorista, recalcular.

### 9.4 ¿Cierra? (texto casi literal para la página 5)

"Con mi salario, el modelo no cierra en los primeros 12 meses: en el mes 12 pierdo unos $1,4 millones al mes y llego al equilibrio en el mes 22, con unos 900 vendedores. Sin salario llego en el mes 10. Si no cierra, será por la tarifa, que nadie ha pagado todavía, y no por riesgo de crédito, porque no presto. Por eso el piloto cobra desde el segundo mes y el mes 3 me dice si sigo."

Una línea de la vista del que paga (N7): "Para el minorista, la cláusula se paga sola si le evita perder 1 de cada 20 vendedores al año (fiado de $62.000, 3% de impago, margen supuesto de 10%)."

Una línea de la vista del vendedor (N8): "Para el vendedor, cubrir ese día con un gota a gota del tamaño del fiado cuesta de $6.000 a $12.400, hasta un tercio de lo que gana en un día; con la cláusula, nada."

---

## 10. Los dos descartes

### 10.1 Descarte 1: A, "la ventanilla del tendero" (préstamo diario escalonado cobrado en la tienda)

- **Por qué parecía buena.** Fue mi mejor opción antes del campo (27 de 40 en mi propia revisión adversarial). Iba al usuario con más gota a gota (F7), copiaba lo que el informal hace bien (cuota diaria, renovación como premio, recomendación; F21, F23) y usaba la tienda como punto de pago sin visitas de cobro (F29).
- **Qué la mató.** (1) Mis números: a precio legal (P1) y con montos de ambulante, el neto por usuario va de -$26.143 a +$5.857 al año según la pérdida por ciclo, y con 1,5% o más ya es negativo, así que ningún volumen lo salva (P6, N11). (2) La fila de pago: en los casos que conoce la informante, al que amenaza se le paga primero y al banco se le deja de pagar porque al final negocia (C11, C12; hipótesis de segunda mano, decirlo). Un prestamista legal sin amenaza queda de último. (3) El campo movió el nodo y la pregunta: el vendedor de carrito ya tiene crédito diario gratis con su minorista (C15). No le falta un préstamo; le falta que el fiado aguante un día. (4) Se lee como las respuestas predecibles 3 y 7.

### 10.2 Descarte 2: F, "el día de lluvia pagado" (seguro paramétrico del fiado vía una aseguradora)

- **Por qué parecía buena.** Salió del mismo hallazgo, usa el mismo dato público, no pide reclamos ni verificar ventas, y el riesgo lo cargaría una aseguradora vigilada, así que resolvía la licencia. Casaburi y Willis dicen cómo venderlo: cobrar la prima en el día bueno (F40).
- **Qué la mató.** La frecuencia. Con 26 días de disparo al año, pagar el fiado entero cada día de lluvia exige una prima comercial de unos $16.600 por día de venta, 43% del ingreso diario; cubrir solo una pérdida de $15.000 cuesta unos $4.000 diarios, 10% (N10, con la siniestralidad de 32,3% de los microseguros colombianos, F40). Una prima de $500 diarios compra un pago de unos $1.863. Además la demanda de seguro de lluvia es baja aun a buen precio (Cole et al., F40), la póliza pide cédula, contra lo que dijeron los vendedores (C19), y un evaluador lo lee como lo primero que dice una IA al oír "lluvia". Lo que me llevé: las pérdidas pequeñas y frecuentes se suavizan con plazo; se aseguran las raras.

No usar la comparación "F cuesta 15 a 40 veces más que E" ni "más de 200 veces" (R.5 punto 6 de `12`).

---

## 11. Riesgo real, mitigación y cómo sé si me equivoqué

### 11.1 Riesgo real (página 5, unas 130 palabras)

Dos capas, en este orden:
1. **Que el hueco no esté donde creo.** Si el minorista ya espera uno o dos días (como en el fiado de Aguablanca, R52), o si la plata del gota a gota del día malo se va al hogar (F9), la cláusula no cambia nada. Todo el hallazgo viene de un resumen oral de segunda mano. Mitigación: es lo primero que pruebo, con umbrales fijados antes de oír las respuestas (11.3), y no firmo con nadie antes.
2. **Que nadie quiera cargar el día de lluvia, porque hoy no le duele.** Hoy el vendedor toma el gota a gota y le paga al minorista, y el minorista le paga al mayorista: el choque lo absorbe el vendedor a 20%, fuera de la cadena. Con la cláusula, quien fía carga un plazo y un impago que hoy no carga, a cambio de algo diferido: que sus vendedores no se hundan y dejen de trabajar. Y si el minorista vive al día y le paga de contado a su proveedor, solo muevo el hueco un eslabón arriba. Mitigación: preguntarle cuántos vendedores perdió este año por deudas y a quién le paga él y cuándo; primer mes gratis; mostrar que se paga sola si evita perder 1 de cada 20 vendedores (N7); si el minorista no puede esperar, ir al mayorista antes de inscribir a un solo vendedor; medir en el piloto la permanencia de los vendedores con y sin cláusula.

Riesgos secundarios, una línea cada uno: llueve en Meléndez y no en el carrito, o al revés (distancia no medida); impago de lo aplazado sin dato; mercancía que se daña (N6); que el abogado lea la cláusula como seguro; cómo facturarle a un minorista sin RUT.

### 11.2 Validación antes de firmar (preguntas en pasado concreto, a vendedores y a un minorista; ninguna a prestamistas)

Salen de `12`, sección 2.11 y R.7. Los umbrales son supuestos fijados antes de oír las respuestas.

| Pregunta | A quién | Sigo si | Lo paro o lo cambio si |
|---|---|---|---|
| "La última vez que llovió y no vendió, ¿qué le dijo el que le fía esa tarde? ¿Le esperó o le exigió? ¿Al otro día le fió?" | 6 vendedores | 4 de 6 describen que se exige el mismo día o se corta el fiado | 3 o más de 6 dicen que el minorista espera: la cláusula no agrega nada |
| "Lo que no vendió ese día, ¿se le dañó o lo vendió al otro día? ¿Cuánto saca fiado en un día normal?" | Vendedores | 4 de 6 dicen que casi todo se vende al otro día; fiado entre $20.000 y $80.000 | La mayoría se daña: la cláusula solo reparte una pérdida (N6) |
| "Esa plata del gota a gota, ¿en qué se fue?" | Vendedores | Al menos 3 casos para pagarle al que fía, 2 contados en primera persona | Se fue al hogar: la cláusula cubre la mitad del problema y lo digo |
| "¿Usted le paga a su proveedor de contado o a plazo? ¿Cuántos vendedores perdió este año por deudas?" | Minorista (comerciante, no prestamista) | Paga a diario o a menos de una semana y perdió al menos 1 vendedor | Tiene plazo holgado y no pierde vendedores: no hay quién pague |

### 11.3 Criterios del piloto (en la página 5, en prosa)

- Mes 1: de 5 minoristas a los que les ofrezco la cláusula gratis, al menos 1 acepta. Si ninguno, paro.
- Meses 2 y 3: al menos 90% de los puentes se cierran en 5 días de venta y el impago de lo aplazado queda bajo 5%. Si no, subo el historial exigido o paro.
- Mes 3: al menos la mitad de los minoristas paga los $4.000. Si no, pruebo $2.000 con el mayorista; si tampoco, el modelo no cierra y lo digo.
- Todo el piloto: que los días de disparo coincidan con los días que los vendedores recuerdan como malos.

---

## 12. Anexos (desde una página nueva con el título "ANEXOS")

| Anexo | Contenido |
|---|---|
| **A. Prototipo** | Lo que existe antes del mediodía: (1) un script en inglés, `models/rain_trigger.py`, que consulta la API de datos.gov.co (dataset s54a-sgyg, estación 0026055120), quita registros duplicados, suma la lluvia entre 7:00 y 18:59, exige 60 de 72 registros para el cierre del día, dispara el aviso apenas el acumulado pasa 5 mm y escribe el mensaje en español para el minorista; con una opción de prueba histórica que reproduzca 26 de 294 y las rachas de N4, y una función que reparte lo aplazado en tercios redondeados a $100. El `rain_cali.py` del scratchpad es la base, pero su CSV ya no está: el script nuevo descarga el dato. (2) Captura de la salida para un día real de disparo de octubre de 2025. (3) Maquetas en texto: el mensaje al minorista, la tarjeta del vendedor ("Si el IDEAM marca lluvia, lo de ese día me lo paga en los 3 días siguientes, sin recargo. Mañana hay mercancía") y la cláusula de una página. Formato del caso: qué hace hoy, qué no hace (no envía WhatsApp real, no tiene estación de respaldo, no lleva el registro de un minorista real), cuánto tomó, con qué herramientas (Python, API de datos.gov.co, Claude Code), y la verdad: no se lo mostré a ningún vendedor ni minorista. Nada de Artifacts ni páginas publicadas: todo va como capturas o texto en el PDF |
| **B. Referencias** | Lista completa con URL y fecha de consulta, en este orden: datos oficiales y normas (DANE R1 a R7, Banca de las Oportunidades y SFC R8 a R13, IDEAM R51, leyes y decretos R31 a R40); estudios (R14, R17 a R23, R46 a R50, R52); prensa y empresas, marcadas como tales (R24 a R28, R41 a R45, R54 a R58). Solo las citadas en el PDF |
| **C. Método y uso de IA** | Sin adornos: usé Claude Code con agentes para investigar por frentes, cada uno con una tabla de verificación de cifras; una revisión adversarial con la rúbrica que puntuó mis mecanismos y marcó 19 afirmaciones sin respaldo, que corregí o saqué; los cálculos en Python sobre datos abiertos; y borradores de texto. Transcribí las notas de voz en local con Whisper. Lo que decidí yo: organizar el campo con el colaborador y la informante, cambiar de A a la cláusula después del campo, descartar F con mis números, qué cifras no usar. Cómo cambié de idea (A, el hallazgo, F, la cláusula). El error del boletín EMICRON 2024 (F6) y cómo lo evité leyendo el anexo. Tabla resumida de cifras que circulan y no usé (síntesis 1.4). La prueba de las tres IA solo si se hizo, con el resultado tal cual |
| **D. Notas de campo** | Informante: hallazgos anonimizados de las dos notas de voz (C1 a C14, C20), cómo citarla y sus límites (segunda mano, sin muestreo, sesgo a los casos que salieron mal). Colaborador: transcripción del resumen oral (las dos notas) y sus cinco hallazgos (C15 a C19), con la advertencia de que no hay número de vendedores ni citas por persona. Reglas cumplidas: nadie contactó prestamistas, nadie grabó ni fotografió a nadie sin permiso. Preguntas que faltan (sección 11.2). Sin nombres, barrios, oficios identificables ni el parentesco. No citar la tercera ronda de preguntas (no fue respondida) |
| **E. Números** | Salida completa de `fiado_bridge_viability.py` (seis respuestas, mes a mes hasta el 24, escenarios de 9.3, vista del que paga, vista del vendedor, escenario de $10 millones); tabla de supuestos 9.2; tabla de `bad_day_mechanisms.py` (costo para la cadena con impago de 2%, 5% y 10%; E2 en una línea: "no es negocio"; primas de F con N10); tabla de `usury_cap.py` (P1 a P4); economía de A de `unit_economics.py` (P6). Cada tabla con el comando que la genera |
| **F. Datos de lluvia** | Estación, periodo, umbral, regla de cobertura (60 de 72), huecos (58 días de 2025 sin cobertura diurna completa, febrero de 2025 casi sin datos, marzo de 2026 con 2,6 mm sospechoso, duplicados), tabla mensual de disparos de los últimos 12 meses, rachas (N4), rezago (N5), la serie de 2025 del frente 12b (18 episodios de un día, 1 de dos y 1 de tres) explicando por qué difiere, estaciones de respaldo con datos al día (Base Aérea Marco Fidel Suárez 0026085170 y Farallones 0026055100) y la distancia a la estación Universidades del MIO, medida o "no medida" |
| **G. El DANE para Cali** | N1 con cuadro y CV; N2 con la advertencia de precisión baja; por qué no uso la partición móvil y estacionario (N3); P12 (concentración en el Caribe) como contexto |
| **H. Mecanismos considerados** | A a F, una línea cada uno, con puntaje de 8 criterios y razón de descarte; los descartes de la síntesis 7 (adelanto por QR, refinanciar al gota a gota, app de préstamo) y la "guía de préstamos" (se parece a la respuesta predecible 5) |
| **I. Preguntas para el abogado y el contador** | (1) ¿Una regla de aplazamiento atada a la lluvia y pagada por quien fía puede leerse como actividad aseguradora si el vendedor no paga nada? (2) ¿Un aviso al minorista sobre montos que le deben sus vendedores cuenta como gestión de cobranza bajo la Ley 2300? (3) Datos mínimos y Ley 1581 (apodo del vendedor, teléfono del minorista). (4) ¿Cómo facturarle a un minorista sin RUT? |
| **J. Trazabilidad completa** | La tabla de `12`, sección 2.7, recortada a los rasgos que quedaron en la cláusula, sin las filas de E2, Fenalco ni Battaglia |

---

## 13. Lo que NO puede aparecer (ni en el cuerpo ni en los anexos, salvo que se diga otra cosa)

Aplica completa la sección 4 del fact pack (puntos 1 a 66). Además:

67. Que yo (Santiago) entrevisté vendedores, o "mis entrevistas" para lo del MIO. Es "conversaciones de un colaborador en mi nombre".
68. Cualquier número de vendedores conversados, "muchos vendedores", o la frase del colaborador "eso les pasa a muchos de ellos".
69. "Mamá", el parentesco con la informante o cualquier nombre, incluso de ejemplo en las maquetas ("Pedro 45" pasa a "vendedor 3: 45").
70. Battaglia et al. 2023 con "bajó el impago", y BRAC como prueba de que aplazar baja el impago.
71. "El gota a gota le vende un día de plazo a 20%" o "paga 20% por un plazo que vale decenas de pesos" como hecho. Correcto: "el plazo cuesta decenas de pesos y hoy se compra con un préstamo de semanas a 20%".
72. "El minorista exige el pago el mismo día" como hecho. Es la premisa por confirmar.
73. "El vendedor toma el gota a gota para proteger la relación, no por la plata" como hecho. Es inferencia.
74. "El mayorista tiene balance" o "le conviene cargar el plazo" como hecho.
75. "La estación queda cerca de los carritos" sin haber medido la distancia.
76. E2, la reserva de $5 millones para prestar, o cualquier frase donde yo le preste a alguien.
77. "F cuesta 15 a 40 veces más que E" y "más de 200 veces".
78. "La cláusula le cuesta 1% a 4% del margen".
79. Ingresos diarios de $33.000 o $38.000, y el 43,8% o el 44%. Solo $38.600 y 43%.
80. Los 9.752 "estacionarios", los 7.993 "móviles" y el "30 a 40% de los estacionarios" (N3).
81. El 11,6% de crédito de proveedores y el 8,8% de gota a gota de Cali en el cuerpo (solo Anexo G, con advertencia).
82. Los 31 cobradiarios (F25) en el cuerpo.
83. Fenalco 2026 (39,55%, 20,91%) y Fenaltiendas (94,4%): sin metodología, fuera del PDF.
84. El "págalo en 7 días" de Tienda Pago y cualquier cifra de la empresa.
85. La fianza de Nequi ("$1 millón queda en $1.119.000") y "OkCredit y Treinta murieron": no están verificadas en el fact pack.
86. El País Cali 2018 como fuente del cuerpo (media); bastan C2, C18 y F21.
87. "No existe ningún producto que..." en vez de "no encontré".
88. Que el prototipo se le mostró a alguien, o resultados de la prueba de las tres IA si no se hizo.
89. La tercera ronda de preguntas a la informante (`docs/08`).
90. El caso del cobrador que era policía en el cuerpo (C14 solo en el Anexo D, como explicación, sin detalles).
91. "Decreto 1469 de 2025" como norma vigente del salario mínimo (fue suspendido): decir "salario mínimo de 2026, $1.750.905".
92. El comodín de día no lluvioso como parte del plan.
93. Afirmar que el fellowship financia la operación, o la fuente de la plata propia sin que Santiago la confirme.

---

## 14. Notas de redacción y cierre

- Primera persona singular. "Mi empresa" o "la SAS", nunca "nosotros".
- Español directo. Sin relleno, sin palabras de moda, sin tríadas retóricas, sin preguntas retóricas en cadena. Frases cortas.
- Ni raya ni semirraya en ningún lado, tampoco guion con espacios. Rangos con "a" (20 a 30%). Negativos pegados (-$26.143).
- Cada cifra con fuente o con "cálculo propio" y el anexo. Cada tope de usura con "septiembre de 2026" (cambia el 1 de octubre).
- La informante siempre así: "una informante de Cali que conoce varios casos de amigos y familiares (notas de voz, 27 sep 2026)". Nunca como dato.
- El colaborador siempre así: "conversaciones con vendedores de carrito en la estación Universidades del MIO (Cali), hechas por un colaborador en mi nombre el 26 sep 2026; resumen oral".
- Antes de entregar: `python3 report/check.py` (necesita `pypdf`, que hoy no está instalado en el Python del sistema: usar el venv del scratchpad o instalarlo), revisar que el cuerpo tenga 5 páginas o menos, que "ANEXOS" abra página, que no haya nombres y que el archivo se llame exactamente `MAKERS_SANTIAGO_ESPINOSA_CALI.pdf`.
