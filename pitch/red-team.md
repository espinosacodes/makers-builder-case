# Red team: la defensa vista por el entrevistador 2

Leí `guion.md` y `slides.md` como si Santiago estuviera presentando ahora, y lo crucé contra `report/docs/informe-docs.md` (la fuente de verdad), `preguntas.md`, `report/ENTREGA.md`, `report/docs/review-rubric-final.md`, `docs/research/12-mecanismos-dia-malo.md` (revisión adversarial), la síntesis 10.4 a 11.7 y las notas de campo `docs/09`.

## Veredicto corto

1. **La honestidad está muy bien.** Lo del colaborador, "no sé cuántos fueron" y "hipótesis de trabajo" quedan dichos de frente y a tiempo. Hay cuatro frases que dicen más de lo que dice el informe, o que se oyen mal (sección 3).
2. **El top-down está a medias.** A los 40 segundos puedo repetir la regla (lluvia, $15.000, tercios, $4.000), pero no sé qué problema resuelve: la palabra "gota a gota" no aparece hasta el segundo 47. Hay que reescribir la apertura (arreglo 1).
3. **El tiempo está justo, sin margen real.** 889 palabras dan 6:35 a 135 palabras por minuto, pero el guion mismo pide unos 8 segundos de pausas marcadas y hay 9 cambios de diapositiva. Eso da unos 6:55 a 135 y unos 7:10 a 130: se pasa. Con los cinco arreglos, el guion baja a 859 palabras (6:22 sin pausas; unos 6:40 con ellas).
4. **Falta el hueco más obvio del mecanismo.** La lluvia le cae el mismo día a todos los vendedores de un minorista y el pitch no lo dice. Es lo primero que yo preguntaría, y el informe ya tiene la cifra ($562.000 con 12 vendedores).
5. **Mi primera pregunta no está en `preguntas.md`:** "Tu prueba para matar la idea cuesta una tarde en tu ciudad. Entregaste el 27. ¿Ya la hiciste?"

---

## 1. Tiempos

Conteo con script sobre el texto hablado (las líneas `>` del guion), a 135 palabras por minuto. Coincide con la tabla del guion.

| Diap. | Palabras | Ventana del guion | Segundos a 135 | Pausas y carga del guion | Riesgo |
|---|---|---|---|---|---|
| 1 | 102 | 0:00 a 0:45 (45 s) | 45,3 | 1 s después de "quedar mal"; recorrer las 3 cajas con el cursor | **Se pasa** unos 2 s |
| 2 | 99 | 0:45 a 1:29 (44 s) | 44,0 | pausa antes de "Y le gana"; cifras largas ("tres mil cuatrocientos") | **Se pasa** unos 1 a 2 s |
| 3 | 103 | 1:29 a 2:15 (46 s) | 45,8 | 1 s después de "gota a gota"; cambio de voz en las citas | **Se pasa** unos 2 s |
| 4 | 91 | 2:15 a 2:55 (40 s) | 40,4 | pausa antes de "falta tiempo"; "veintiséis de doscientos noventa y cuatro" se dice lento | **Se pasa** unos 2 a 3 s |
| 5 | 103 | 2:55 a 3:41 (46 s) | 45,8 | "la lección se dice lento" y mirada a cámara | **Se pasa** unos 2 a 3 s |
| 6 | 71 | 3:41 a 4:12 (31 s) | 31,6 | ninguna | En el borde |
| 7 | 133 | 4:12 a 5:12 (60 s) | 59,1 | la más densa en cifras: 7 números seguidos | **Se pasa** unos 3 s por las cifras |
| 8 | 90 | 5:12 a 5:52 (40 s) | 40,0 | se pide ir más rápido | Bien |
| 9 | 58 | 5:52 a 6:17 (25 s) | 25,8 | ninguna | En el borde |
| 10 | 39 | 6:17 a 6:35 (18 s) | 17,3 | 1 s antes de "Al vendedor" y la última frase lenta | **Se pasa** unos 2 s |
| **Total** | **889** | **6:35** | **395 s** | | |

Cuenta real: 6:35 de texto, más unos 8 s de pausas marcadas, más 9 cambios de diapositiva (1 s cada uno si hace clic sin dejar de hablar, más si se detiene), más unos 5 s por las cifras largas que se dicen despacio. **Eso da de 6:55 a 7:00 a 135 y de 7:10 a 7:15 a 130.** Con los nervios uno suele acelerar, pero este guion le pide lo contrario (pausas y frases lentas). El margen de 25 segundos que dice el guion no existe: se lo comen sus propias indicaciones.

Otros puntos de tiempo:
- **El reloj arranca a las 12:00 en punto.** Compartir pantalla en Meet toma de 5 a 15 segundos. Conectarse a las 11:58 con la presentación ya abierta en modo presentador y preguntar al entrar si puede compartir de una vez.
- **Diapositiva 1 dice "a los 0:37 ya está dicha la solución completa".** Es cierto a 135. Pero lo que falta ahí es el problema, no la solución (sección 2).
- Con los arreglos de la sección 5, el texto queda así:

| Diap. | Palabras | Ventana nueva a 135 |
|---|---|---|
| 1 | 123 | 0:00 a 0:55 |
| 2 | 81 | 0:55 a 1:31 |
| 3 | 90 | 1:31 a 2:11 |
| 4 | 81 | 2:11 a 2:47 |
| 5 | 97 | 2:47 a 3:30 |
| 6 | 72 | 3:30 a 4:02 |
| 7 | 112 | 4:02 a 4:52 |
| 8 | 96 | 4:52 a 5:34 |
| 9 | 68 | 5:34 a 6:04 |
| 10 | 39 | 6:04 a 6:22 |
| **Total** | **859** | **6:22** (6:36 a 130; unos 6:40 a 6:55 con pausas y cambios) |

Puntos de control nuevos: **2:10** entrando a la 4; **4:00** entrando a la 7; **5:35** entrando a la 9.

---

## 2. Top-down: ¿puedo decir su propuesta a los 40 segundos?

**Con el guion actual, a los 40 segundos (unas 90 palabras) sé esto:** "Una cláusula de lluvia del fiado: si el IDEAM marca lluvia, el vendedor se queda con hasta $15.000, abona el resto y paga lo que falte en tercios en tres días, sin recargo". Eso es la regla.

**Lo que no sé a los 40 segundos:**
- **Qué problema resuelve.** El caso es sobre el gota a gota y la palabra no aparece hasta el segundo 47 (diapositiva 2). La tesis que conecta todo ("el gota a gota entra la tarde en que la lluvia rompe el fiado") llega hacia la 1:21, al final de la diapositiva 2.
- **Qué es "el fiado" y quién es "quien le fía".** Un jurado que no leyó el informe esa mañana oye "abona el resto a quien le fía" sin saber que el vendedor saca la mercancía fiada en la mañana y la paga en la tarde. Sin esa frase, "tercios" y "abona el resto" no se entienden.
- **"Le falta que un día de lluvia no cuente como quedar mal"** es una buena frase para el cierre, pero en la apertura llega antes de que yo sepa qué es quedar mal con quién. Funciona si la sigue de inmediato el contexto.

**Veredicto:** puedo repetir el mecanismo, pero no la propuesta, porque no sé qué problema resuelve. La reescritura está en el arreglo 1. Con ella, a los 15 s tengo el mensaje, a los 28 s el problema y la hipótesis, y a los 45 s la regla completa.

---

## 3. Honestidad contra el informe y las reglas

| Tema | Qué dice el guion | Qué dice el informe | Estado |
|---|---|---|---|
| Colaborador | "Yo no entrevisté vendedores en persona. Un colaborador habló en mi nombre... no sé cuántos fueron" | Sección 1 y Anexo C, igual | **Bien.** Es lo mejor del pitch |
| Citas del colaborador | "Pero 'hay días en que...'" | Son palabras del colaborador, no de un vendedor | **Arreglar.** Dicho en voz alta no se oyen las comillas: suena a que habla un vendedor. Decir "En sus palabras:" antes de la cita |
| Paráfrasis | "lo que necesitan ese día se lo piden **fiado**" | Cita: "se lo piden **prestado** al minorista" | Menor. Con el arreglo 1 la frase sale del todo (ya queda dicho en la apertura como definición del usuario) |
| Informante | No aparece | "una informante de Cali" | **Bien.** Si sale en preguntas, `preguntas.md` ya tiene la fórmula |
| Hipótesis | Diap. 3: "hipótesis de trabajo, con umbrales para matarla" | Igual | **Bien** |
| "Por eso la crucé con datos" | Diap. 4, antes del DANE y la lluvia | Ninguno de los dos datos prueba que la lluvia rompa el fiado: uno muestra que el ambulante va al gota a gota y el otro que la lluvia es frecuente y corta | **Arreglar (arreglo 4).** Suena a que los datos confirman el paso, y un jurado lo nota |
| 26 de 294 "días" | "en veintiséis de doscientos noventa y cuatro días" | "26 de 294 días **de venta**", contando solo días con dato | Menor. Si no dice "de venta", alguien piensa "¿un año no tiene 365?" |
| "La medí yo" | Con énfasis | "Los cálculos son míos... la IA me ayudó con el código" (Anexo C) | **Bien, con condición.** Solo si puede explicar el método en 20 segundos sin notas (pregunta de reserva en la sección 4) |
| Descarte 1 | "en el peor caso perdía unos veintiséis mil" | "de $5.857 a -$26.143 al año" | **Arreglar (arreglo 3).** Dar solo el peor caso suena a escoger el número que conviene |
| Descarte 2 | "la prima sería el cuarenta y tres por ciento de lo que gana en un día" | "$16.600 **por día de venta**, 43% del ingreso diario" | **Arreglar (arreglo 3).** Así dicho se oye como un pago único de 43% de un día, que sería barato. Falta "cada día de venta", que es justo lo que mata la idea |
| Lo que ya existe | "lo que ya existe vende plata a treinta días o más" | "**Las que encontré** venden plata a 30 días o más" y, en el mismo párrafo, el "diario anticipado" de Corabastos cobra 10% **en el día** | **Arreglar (arreglo 3).** El informe mismo lo contradice. Si el jurado leyó ese párrafo, lo ve |
| Licencia | "No soy entidad financiera" | Igual, más "Queda para el abogado si una regla pagada por quien fía puede leerse como seguro" | Aceptable en 7 minutos. P18 de `preguntas.md` ya nombra la pregunta abierta; no decir "es 100% legal" |
| 2,5% y 1 de cada 20 | Dichos como hechos | $161.200 sale de supuestos [S]; "1 de 20" es cálculo propio con 3% de impago [S] | **Arreglar (en el arreglo 5, 3 palabras):** "con mis supuestos" |
| Riesgo | Solo "que el minorista ya espere" | Tres capas: la premisa (y el hogar), la caja de quien fía, la copia | **Arreglar (arreglo 2).** Falta la capa que un jurado ve primero |
| IA | No va en el guion | Anexo C | **Bien.** P7 está lista. El caso permite IA y el informe lo dice |
| Cifras viejas del pitch de 3 min | No aparecen | | **Bien** |
| Rayas | 0 en guion y slides | | **Bien** |

---

## 4. Mis 3 preguntas después de sus 7 minutos

Elegí las que salen de lo que dijo y de lo que no dijo, no las del banco.

### Pregunta 1. "Tu prueba para matar la idea son seis vendedores y un minorista en tu ciudad, una tarde. Entregaste el 27 y hoy es 30. ¿Ya la hiciste? ¿Qué te dijeron? Y si no, ¿por qué no?"

**Por qué la hago:** la diapositiva 9 pone el "3 de 6" en 140 pt y dice "no firmo antes de probarlo". Una prueba tan barata y tan clara invita a preguntar por qué no está hecha. Es la pregunta que separa "sé qué pregunta mata la idea" de "la hice".

**¿La contesta `preguntas.md`?** No. P20 ("¿qué haces la primera semana?") termina con "lo que haría distinto: hacer esas conversaciones yo mismo antes de entregar", que reconoce el hueco pero no contesta el "ya pasaron tres días".

**Respuesta sugerida (se escoge la que sea verdad, sin adornar):**
- *Si la hizo antes de la entrevista (él, en persona, sin contactar prestamistas, sin nombres, en pasado concreto):* "Sí, el [fecha], con [n] vendedores y [n] minorista en [lugar]. [Lo que dijeron, contra los umbrales ya fijados, aunque la debilite]. No está en el informe porque fue después de entregar." Si el resultado toca el umbral, decirlo: es justo lo que prometió.
- *Si no la hizo:* "No, todavía no. [La razón real, en una frase y sin disculpas]. Las preguntas están escritas y los umbrales los fijé antes de oír respuestas: si 3 de 6 dicen que el minorista espera, paro. La hago esta semana." No inventar una razón ni sugerir que ya hay respuestas.

### Pregunta 2. "Dijiste 'no presto'. Pero llueve para todos los vendedores del minorista el mismo día. ¿Con qué plata se surte él al otro día? ¿No le pasaste el gota a gota al minorista? ¿Y por qué lo aceptaría el mayorista?"

**Por qué la hago:** es el hueco más visible del mecanismo y el guion actual no lo menciona. "No por riesgo de crédito, porque no presto" es cierto para él, pero el riesgo existe: lo carga quien fía, y todo junto el mismo día.

**¿La contesta `preguntas.md`?** A medias. P3 tiene la cifra correcta ($562.000 con 12 vendedores) y el "sube al mayorista". Dos problemas:
1. P3 abre con "Es mi riesgo más grande", y la diapositiva 9 dice que el riesgo real es otro (que el minorista ya espere). Dos "riesgos más grandes" en 10 minutos suenan a respuesta armada.
2. "Si no los tiene, sube al mayorista" queda como afirmación. La repregunta obvia ("¿y por qué aceptaría el mayorista?") no tiene respuesta.

**Respuesta mejorada (todo sale del informe):**
> No lo pierde: le llega en tercios en tres días. Pero esa tarde le faltan unos $562.000 si tiene 12 vendedores, y esa es la segunda cara del riesgo que nombré. Si no tiene la caja, el plazo tiene que subir al mayorista. Si el mayorista aceptaría, no lo sé. Por eso una de las preguntas al minorista es si le paga a su proveedor de contado o a plazo. Si paga de contado y no tiene la caja, la cláusula no se sostiene, y lo digo.

(Respaldo: Sección 3, "Para quien paga"; Sección 4, segunda capa; Tabla 2, fila "Fin de mes"; Anexo C, "Preguntas que faltan".)

### Pregunta 3. "Dijiste 'si la mercancía no se daña, falta tiempo, no plata'. ¿Qué venden los carritos de Universidades? Si es comida o fruta, el día de lluvia sí se pierde plata, y tu cláusula solo reparte esa pérdida en tres días. ¿No es justo el caso donde el gota a gota es más probable?"

**Por qué la hago:** la frase "si la mercancía no se daña" es un condicional que sostiene todo el argumento de plazo contra seguro, y lo dijo rápido. La revisión adversarial (`12-mecanismos-dia-malo.md`, R.5.1) lo marca: con mercancía perecedera, pagar lo perdido en tres días se come una parte grande del ingreso diario, justo cuando el gota a gota sigue siendo la salida.

**¿La contesta `preguntas.md`?** No como pregunta propia. Solo aparece dentro de P5 ("o si la mayoría dice que la mercancía se daña").

**Respuesta sugerida (dentro del informe):**
> Tiene razón, y el informe lo deja fuera a propósito: la mercancía que se daña no tiene dato público. Por eso está en el umbral: si la mayoría de los seis dice que lo que no vendió se dañó, la cláusula no sirve. No sé qué venden esos carritos: el resumen del colaborador no lo dice, y es una de las primeras preguntas: "lo que no vendió ese día, ¿se dañó o lo vendió al otro día?".

(Respaldo: Sección 2, "Reglas y límites"; Sección 4, "Cómo sé si me equivoqué"; Anexo B, "no modela la mercancía que se daña"; Anexo C, "Preguntas que faltan".)

### Reserva, si queda tiempo

- **"¿Cómo mediste la lluvia? ¿Lo hiciste tú o un agente?"** No hay respuesta de método en `preguntas.md`, y el guion subraya "la medí yo". Respuesta de 20 s, todo del Anexo C: "Estación del IDEAM 0026055120 en Univalle, registros cada 10 minutos. Sumo la lluvia de 7:00 a 18:59 y solo cuento días con al menos 60 de 72 registros. Del 27 de septiembre de 2025 al 26 de septiembre de 2026: 26 de 294 días de venta con 5 mm o más, 3 rachas de dos días, ninguna de tres. El código lo escribí con ayuda de IA y el cálculo lo corrí yo. El umbral no está calibrado contra ventas y no medí la distancia a los carritos."
- **"¿Qué vendedor te abre la puerta del minorista en la semana 1?"** El plan dice "llego con un vendedor que ya le compra", y hoy no tiene contacto propio con ninguno. Respuesta honesta: "Todavía ninguno. Es parte de la misma salida de campo: los seis vendedores de la prueba son los primeros candidatos."

---

## 5. Los 5 arreglos obligatorios, con el texto exacto

Los cinco juntos dejan el guion en **859 palabras**. Cada bloque da el texto actual y el nuevo, listos para pegar en `guion.md` y en las notas del orador de `slides.md`.

### Arreglo 1. La apertura tiene que decir qué problema resuelve (diapositivas 1 y 2)

**Diapositiva 1, actual (102 palabras):**
> Buenas. Soy Santiago Espinosa, de Cali.
>
> Al vendedor de carrito no le falta crédito. Le falta que un día de lluvia no cuente como quedar mal.
>
> Propongo la cláusula de lluvia del fiado. Cuando el IDEAM marca lluvia, el vendedor se queda hasta con quince mil pesos para la casa, abona el resto a quien le fía y lo que falte lo paga en tercios, en sus tres días de venta siguientes. Sin recargo. Al otro día le siguen fiando.
>
> Quien fía me paga cuatro mil pesos al mes por vendedor. No presto, no aseguro, y la plata nunca pasa por mí.

**Diapositiva 1, nueva (123 palabras, 0:00 a 0:55):**
> Buenas. Soy Santiago Espinosa, de Cali, y propongo la cláusula de lluvia del fiado.
>
> Al vendedor de carrito no le falta crédito. Le falta que un día de lluvia no cuente como quedar mal.
>
> Mi usuario saca fiada la mercancía del día y la paga esa tarde, sin interés. Mi hipótesis: el día que llueve no alcanza, y ahí entra el gota a gota.
>
> La cláusula: si el IDEAM marca lluvia, se queda hasta con quince mil pesos para la casa, abona el resto y lo que falte lo paga en tercios, en sus tres días de venta siguientes. Sin recargo.
>
> Quien fía me paga cuatro mil pesos al mes por vendedor. No presto, no aseguro, y la plata nunca pasa por mí.

Marcas: nombre de la propuesta a los 6 s, mensaje a los 15 s, problema e hipótesis a los 28 s, regla completa a los 45 s. "Mi usuario saca fiada..." es la definición de usuario del informe (Sección 2, "Usuario y alcance"), no una observación de campo. "Mi hipótesis" deja clara la calidad de la evidencia desde el primer medio minuto.

**Diapositiva 2: quitar la última frase**, porque ya quedó dicha en la apertura (menos 18 palabras):
> ~~Y le gana en un momento preciso: la tarde en que un día sin ventas rompe el fiado.~~

La diapositiva 2 queda en 81 palabras y termina en "Vende plata a meses a quien le faltan uno o dos días." Quitar también la indicación "Pausa corta antes de 'Y le gana...'".

**En pantalla (slides.md, diapositiva 1):** sin cambios en las cajas. Cambiar la línea superior de 12 pt a: `Cláusula de lluvia del fiado · Santiago Espinosa · Cali · Hipótesis: el gota a gota entra el día que llueve`.

### Arreglo 2. Primero la prueba que mata la idea, y nombrar la caja del minorista (diapositivas 8 y 9)

Hoy el pitch tiene tres "primero": la semana 0 (programa), "lo primero es contar" (40 vendedores) y "no firmo antes de probarlo" (6 vendedores). Y el riesgo que más se ve (la lluvia le cae a todos el mismo día) no está.

**Diapositiva 8, nueva (96 palabras, 4:52 a 5:34):**
> ¿Cómo lo llevo a cabo? Antes de firmar con nadie, le pregunto a seis vendedores y a un minorista por la última vez que llovió.
>
> Si pasa, un programa lee la estación cada treinta minutos. Llego al minorista con un vendedor que ya le compra, y el primer mes es gratis. El día de lluvia le llega un WhatsApp: "Rige la cláusula". Tres días de fiado normal más un tercio. A fin de mes me paga por Nequi.
>
> Y cuento: si con cinco minoristas no llego a cuarenta vendedores con fiado diario, el modelo no cierra.

**Diapositiva 9, nueva (68 palabras, 5:34 a 6:04):**
> El riesgo real tiene dos caras. Una: que el minorista ya espere cuando llueve. Si tres o más de seis vendedores lo dicen, la cláusula no sirve, y lo digo.
>
> Otra: la lluvia le cae a todos sus vendedores el mismo día. Con doce, le quedan unos quinientos sesenta mil pesos sin cobrar. Si no los tiene, el plazo sube al mayorista, y eso no lo he probado.

Respaldo: Sección 3, "Para quien paga" ($562.000 con 12 vendedores; "si no los tiene, sube al mayorista") y Sección 4, segunda capa del riesgo.

**En pantalla (slides.md):**
- Diapositiva 8, texto nuevo (13 palabras): `Antes: 6 vendedores` · `Semana 1: gratis` · `Lluvia: WhatsApp` · `3 días: tercios` · `Mes: Nequi`. El primer punto va en acento junto con el de lluvia. Título: "Primero la pregunta que la mata; después, un día de lluvia paso a paso".
- Diapositiva 9, texto nuevo (14 palabras): `3 de 6` (140 pt, acento) y, debajo en 24 pt, `Caja del minorista un día de lluvia: $562.000 con 12 vendedores`. Línea de fuente: "Umbral fijado antes de oír respuestas, sección 4 · Caja: sección 3, cálculo propio con supuestos [S]".

**En `preguntas.md`, P3:** cambiar "Es mi riesgo más grande." por "Es la segunda cara del riesgo que nombré." y agregar al final: "Si el mayorista aceptaría, no lo sé: por eso le pregunto al minorista si le paga a su proveedor de contado o a plazo."

### Arreglo 3. Tres frases que se oyen distinto de lo que dice el informe (diapositivas 5 y 6)

**Diapositiva 5, actual:**
> Antes maté dos soluciones reales con números.
>
> Un préstamo diario legal, cobrado en la tienda: con montos de ambulante, en el peor caso perdía unos veintiséis mil pesos por usuario al año. Y el vendedor ya tiene crédito diario sin interés.
>
> Un seguro del día de lluvia: con veintiséis días al año, la prima sería el cuarenta y tres por ciento de lo que gana en un día.

**Diapositiva 5, nueva (97 palabras en total con la lección, que no cambia):**
> Maté dos soluciones reales con números.
>
> Un préstamo diario legal, cobrado en la tienda: con montos de ambulante, iba de ganar unos seis mil pesos a perder veintiséis mil por usuario al año.
>
> Un seguro del día de lluvia: con veintiséis días al año, la prima se comería el cuarenta y tres por ciento de lo que gana, cada día de venta.

(Sale "Y el vendedor ya tiene crédito diario sin interés": ya está dicho en la apertura.) Respaldo: Sección 4, Descarte 1 ($5.857 a -$26.143) y Descarte 2 ($16.600 por día de venta, 43%).

**En pantalla, diapositiva 5 (15 palabras):** fila 1 `Préstamo diario` y `$5.857 a -$26.143 al año`; fila 2 `Seguro de lluvia` y `43% del ingreso, cada día`.

**Diapositiva 6, actual:**
> Y lo que ya existe vende plata a treinta días o más.

**Diapositiva 6, nueva:**
> Y las soluciones formales que encontré venden plata a treinta días o más.

Por qué: el informe dice "las que encontré" y en el mismo párrafo cita el "diario anticipado" de Corabastos, que cobra 10% en el día. "Lo que ya existe" en general es falso según el propio informe. Si preguntan por Corabastos, la respuesta está en el informe: el puente de un día ya se vende, y caro.

### Arreglo 4. Los datos no confirman el paso: decirlo (diapositiva 4)

**Actual:**
> Por eso la crucé con datos. Del DANE: de los ambulantes que pidieron crédito, casi sesenta y dos por ciento fue a un gota a gota. En tiendas de barrio, once. Mi usuario es el carrito, no el tendero.
>
> Y la lluvia la medí yo. En doce meses, la estación del IDEAM en Univalle marcó cinco milímetros o más en horario de venta en veintiséis de doscientos noventa y cuatro días. Nunca tres seguidos, en los días con dato. Si la mercancía no se daña, ese día falta tiempo, no plata.

**Nueva (81 palabras, 2:11 a 2:47):**
> Los datos no prueban ese paso. Muestran el contexto. Del DANE: de los ambulantes que pidieron crédito, casi sesenta y dos por ciento fue a un gota a gota.
>
> Y la lluvia la medí yo, con datos abiertos del IDEAM. En doce meses, la estación de Univalle marcó cinco milímetros o más en horario de venta en veintiséis de doscientos noventa y cuatro días de venta. Nunca tres seguidos. Si la mercancía no se daña, ese día falta tiempo, no plata.

Por qué: "la crucé con datos" le hace creer al jurado que el DANE y el IDEAM confirman que la lluvia rompe el fiado, y no lo hacen. Decirlo primero es coherente con "empiezo por la más débil" y es difícil de atacar. "Días de venta" evita la pregunta del 365. Salen "En tiendas de barrio, once" y "Mi usuario es el carrito, no el tendero" porque la apertura ya define al usuario.

**En pantalla, diapositiva 4:** quitar `Tiendas: 11,3%` y poner `días de venta con lluvia` debajo de `26 de 294`. El título queda: "El ambulante va al gota a gota, y la lluvia es frecuente y corta". La línea de fuente pierde "tiendas (R3)".

### Arreglo 5. Diapositiva 7: menos cifras seguidas y los supuestos a la vista

**Actual (133 palabras):**
> ¿Qué impacto tiene? Para el vendedor, cubrir ese día con un gota a gota le costaría de dieciséis a treinta y dos por ciento de lo que gana. En mi prototipo, con tres días de lluvia simulados, el gota a gota termina en tres préstamos. Con la cláusula, nada queda pendiente.
>
> Para quien fía, mis cuatro mil pesos son el dos coma cinco por ciento del margen que le deja cada vendedor. Se paga sola si le evita perder uno de cada veinte vendedores al año.
>
> Para el negocio: sin salario, cierra en el mes diez, con doscientos setenta y nueve vendedores que pagan. Con salario, en el mes veintidós. Si no cierra, será por volumen y por una tarifa que nadie ha pagado todavía. No por riesgo de crédito, porque no presto.

**Nueva (112 palabras, 4:02 a 4:52):**
> ¿Qué impacto tiene? Para el vendedor: en mi prototipo, con tres días de lluvia simulados, el gota a gota termina en tres préstamos, dos para pagar cuotas del anterior. Con la cláusula, nada queda pendiente.
>
> Para quien fía, con mis supuestos, mis cuatro mil pesos son el dos coma cinco por ciento del margen que le deja cada vendedor. Se paga sola si le evita perder uno de cada veinte vendedores al año.
>
> Para el negocio: sin salario, cierra en el mes diez. Con salario, en el mes veintidós. Si no cierra, será por volumen y por una tarifa que nadie ha pagado todavía. No por riesgo de crédito, porque no presto.

Por qué: era el segmento más cargado de cifras (7 seguidas) y el que más se iba a alargar. "Dos para pagar cuotas del anterior" (Anexo B) conecta con "un gota a gota paga otro" del campo, y vale más que el 16% a 32%, que queda para P16. "Con mis supuestos" marca que $161.200 y el 1 de cada 20 salen de supuestos [S]. El 279 queda para P4 y P11 (y evita abrir en el pitch la pregunta de los 50 del DANE).

**En pantalla, diapositiva 7:** sin cambios en las tres columnas. En la línea de fuente, quitar "279 vendedores que pagan".

---

## 6. Guion completo con los cinco arreglos (859 palabras)

Para ensayar con cronómetro. Diapositivas 2, 3, 6 y 10 con cambios mínimos o ninguno.

**1 · 0:00 a 0:55 (123)**
> Buenas. Soy Santiago Espinosa, de Cali, y propongo la cláusula de lluvia del fiado. Al vendedor de carrito no le falta crédito. Le falta que un día de lluvia no cuente como quedar mal. Mi usuario saca fiada la mercancía del día y la paga esa tarde, sin interés. Mi hipótesis: el día que llueve no alcanza, y ahí entra el gota a gota. La cláusula: si el IDEAM marca lluvia, se queda hasta con quince mil pesos para la casa, abona el resto y lo que falte lo paga en tercios, en sus tres días de venta siguientes. Sin recargo. Quien fía me paga cuatro mil pesos al mes por vendedor. No presto, no aseguro, y la plata nunca pasa por mí.

**2 · 0:55 a 1:31 (81)**
> ¿Por qué llegué ahí? El gota a gota no le gana al formal por precio. Con la usura de septiembre, el préstamo diario legal más caro posible cobra unos tres mil cuatrocientos pesos al día por cada cien mil. El gota a gota, cuatro mil. Solo catorce por ciento menos. Le gana por la forma. El ochenta y siete por ciento del crédito formal se paga en cuota mensual. Vende plata a meses a quien le faltan uno o dos días.

**3 · 1:31 a 2:11 (90)**
> ¿Qué evidencia tengo? Tres capas, y empiezo por la más débil. El campo. Yo no entrevisté vendedores en persona. Un colaborador habló en mi nombre con vendedores de carrito en la estación Universidades del MIO, el veintiséis de septiembre. Tengo su resumen oral y no sé cuántos fueron. En sus palabras: "hay días en que, no sé, llovió, entonces nadie va". "Y ahí es cuando entran con un gota a gota". No encontré ese paso publicado en mi búsqueda. Por eso es una hipótesis de trabajo, con umbrales para matarla.

**4 · 2:11 a 2:47 (81)**
> Los datos no prueban ese paso. Muestran el contexto. Del DANE: de los ambulantes que pidieron crédito, casi sesenta y dos por ciento fue a un gota a gota. Y la lluvia la medí yo, con datos abiertos del IDEAM. En doce meses, la estación de Univalle marcó cinco milímetros o más en horario de venta en veintiséis de doscientos noventa y cuatro días de venta. Nunca tres seguidos. Si la mercancía no se daña, ese día falta tiempo, no plata.

**5 · 2:47 a 3:30 (97)**
> Maté dos soluciones reales con números. Un préstamo diario legal, cobrado en la tienda: con montos de ambulante, iba de ganar unos seis mil pesos a perder veintiséis mil por usuario al año. Un seguro del día de lluvia: con veintiséis días al año, la prima se comería el cuarenta y tres por ciento de lo que gana, cada día de venta. Aprendí que lo frecuente se suaviza con plazo y lo raro se asegura. Así que cambié la pregunta: no cómo prestarle más barato, sino cómo evitar que la lluvia rompa un fiado que ya funciona.

**6 · 3:30 a 4:02 (72)**
> Esa sola pieza resuelve los cuatro puntos del caso. No soy entidad financiera: no hay interés, ni prima, y no capto plata. Sirve sin ahorro: actúa solo el día sin ingreso. Soy un desconocido, pero el trato sigue con el minorista de siempre. Y las soluciones formales que encontré venden plata a treinta días o más. Aquí el plazo sigue en cero y solo lo abre un dato público, nunca el deudor.

**7 · 4:02 a 4:52 (112)**
> ¿Qué impacto tiene? Para el vendedor: en mi prototipo, con tres días de lluvia simulados, el gota a gota termina en tres préstamos, dos para pagar cuotas del anterior. Con la cláusula, nada queda pendiente. Para quien fía, con mis supuestos, mis cuatro mil pesos son el dos coma cinco por ciento del margen que le deja cada vendedor. Se paga sola si le evita perder uno de cada veinte vendedores al año. Para el negocio: sin salario, cierra en el mes diez. Con salario, en el mes veintidós. Si no cierra, será por volumen y por una tarifa que nadie ha pagado todavía. No por riesgo de crédito, porque no presto.

**8 · 4:52 a 5:34 (96)**
> ¿Cómo lo llevo a cabo? Antes de firmar con nadie, le pregunto a seis vendedores y a un minorista por la última vez que llovió. Si pasa, un programa lee la estación cada treinta minutos. Llego al minorista con un vendedor que ya le compra, y el primer mes es gratis. El día de lluvia le llega un WhatsApp: "Rige la cláusula". Tres días de fiado normal más un tercio. A fin de mes me paga por Nequi. Y cuento: si con cinco minoristas no llego a cuarenta vendedores con fiado diario, el modelo no cierra.

**9 · 5:34 a 6:04 (68)**
> El riesgo real tiene dos caras. Una: que el minorista ya espere cuando llueve. Si tres o más de seis vendedores lo dicen, la cláusula no sirve, y lo digo. Otra: la lluvia le cae a todos sus vendedores el mismo día. Con doce, le quedan unos quinientos sesenta mil pesos sin cobrar. Si no los tiene, el plazo sube al mayorista, y eso no lo he probado.

**10 · 6:04 a 6:22 (39)**
> No le vendo plata a quien le faltan dos días. Le corro la fecha a un crédito que ya funciona. Al vendedor no le falta crédito. Le falta que un día de lluvia no cuente como quedar mal. Gracias.

**Recortes nuevos si va tarde**, en este orden (lo que sale queda para las preguntas):
1. Diap. 7: "Se paga sola si le evita perder uno de cada veinte vendedores al año." (14 palabras, unos 6 s)
2. Diap. 8: "Llego al minorista con un vendedor que ya le compra, y el primer mes es gratis." (16, unos 7 s)
3. Diap. 2: "Con la usura de septiembre," (5, unos 2 s)
4. Diap. 5: "Aprendí que lo frecuente se suaviza con plazo y lo raro se asegura." (13, unos 6 s; la frase "cambié la pregunta" queda)

**Nunca se recorta:** la apertura completa, "no entrevisté vendedores en persona" y "no sé cuántos fueron", "los datos no prueban ese paso", las dos caras del riesgo y el cierre.

**Actualizar en `guion.md`:** la tabla de tiempos, los puntos de control (2:10, 4:00, 5:35), la ruta "Si me conecto tarde" (la versión completa ahora dura 6:22) y la tabla de verificación de cifras (agregar $5.857, $562.000 con 12 vendedores y "2 de ellos para pagar cuotas del anterior", Anexo B; quitar 11,3% y 279 de lo que se dice).

---

## 7. Menores (no bloquean)

- **Diapositiva 6, esquina 4 "Un día, no 30":** se puede leer como que la cláusula da un día de plazo (da tres días de venta, u ocho con sextos). Mejor `Plazo por dato` (3 palabras; el total queda en 14).
- **"Esa sola pieza resuelve los cuatro puntos":** "resuelve" es fuerte con la premisa sin probar. Es defendible porque el mecanismo sí los cubre por diseño. No cambiarlo, pero no repetirlo en las preguntas.
- **"No soy entidad financiera":** bien en el pitch. En preguntas, siempre con la cola de P18: "lo que queda abierto es si se puede leer como seguro, y eso va al abogado".
- **Emergencia de 60 s:** está bien y es honesta. Agregar "el día que llueve no alcanza y ahí entra el gota a gota" después de la primera frase, para que tenga el problema.
- **Stage directions de la diapositiva 3:** "Decir 'no entrevisté vendedores en persona' tranquilo y sin disculparse" es el mejor consejo del guion. Aplica igual a "eso no lo he probado" de la nueva diapositiva 9.
