# Banco de preguntas: defensa del Builder Case

Entrevista: miércoles 30 sep, 12:00 a 12:12 (hora Colombia). Preguntas: 3 a 4 minutos, así que caben 4 o 5 respuestas de unos 30 segundos.

**Cómo responder (la misma regla del pitch, top-down):**
1. Primera frase: la respuesta directa. Sí, no, o el número.
2. Segunda: el dato que la respalda y de dónde sale.
3. Tercera: el límite honesto o cómo lo voy a probar.

Si no sé algo: "No lo medí. Lo mediría así: ...". Nunca inventar un número para tapar un hueco.

**Nunca decir:** "entrevisté", "hablé con vendedores", "está validado", "nadie lo ha hecho", "es 100% legal", "mi mamá" (salvo que yo lo decida; en el informe es "una informante de Cali").

Primero van las 2 que el red team haría de entrada (P21 y P22), porque salen directo de lo que digo en el pitch. Después, las 7 más probables del banco, marcadas con ★. Las otras 13 van por grupo, y al final dos de reserva (P23 y P24).

---

## ★★ Las que salen del pitch (red team)

### ★★ P21. La prueba que mata la idea
**"Tu prueba para matar la idea son seis vendedores y un minorista en tu ciudad, una tarde. Entregaste el 27 y hoy es 30. ¿Ya la hiciste? ¿Qué te dijeron? Y si no, ¿por qué no?"**

Esta respuesta **se escoge hoy, antes de dormir**, y se escoge la que sea verdad. No se adorna ni se improvisa en vivo.

*Si la hice antes de la entrevista (yo, en persona, sin contactar prestamistas, sin nombres):*
> Sí, el [fecha], con [n] vendedores y [n] minorista en [lugar]. [Lo que dijeron, contra los umbrales que ya había fijado, aunque la debilite]. No está en el informe porque fue después de entregar.

*Si no la hice:*
> No, todavía no. [La razón real, en una frase y sin disculpas]. Las preguntas están escritas y los umbrales los fijé antes de oír respuestas: si 3 de 6 dicen que el minorista espera, paro. La hago esta semana.

- **Respaldo:** Sección 4, "Cómo sé si me equivoqué"; Anexo C, "Preguntas que faltan".
- **Trampa a evitar:** inventar una razón, sugerir que ya hay respuestas cuando no las hay, o decir "entrevisté" si fue otra persona. Si el resultado toca el umbral, decirlo: es justo lo que prometí.

### ★★ P22. La mercancía que se daña
**"Dijiste 'si la mercancía no se daña, falta tiempo, no plata'. ¿Qué venden los carritos de Universidades? Si es comida o fruta, el día de lluvia sí se pierde plata, y tu cláusula solo reparte esa pérdida en tres días. ¿No es justo el caso donde el gota a gota es más probable?"**

> Tiene razón, y el informe lo deja fuera a propósito: la mercancía que se daña no tiene dato público. Por eso está en el umbral: si la mayoría de los seis dice que lo que no vendió se dañó, la cláusula no sirve. No sé qué venden esos carritos: el resumen del colaborador no lo dice, y es una de las primeras preguntas: lo que no vendió ese día, ¿se dañó?

- **Respaldo:** Sección 2, "Reglas y límites"; Sección 4, "Cómo sé si me equivoqué"; Anexo B, "no modela la mercancía que se daña"; Anexo C, "Preguntas que faltan".
- **Trampa a evitar:** defender que la mercancía no se daña, o inventar qué venden los carritos. El condicional es un límite declarado, no un hallazgo.

---

## ★ Las 7 más probables

### ★ P1. Evidencia y campo
**"Tu hallazgo central viene de un colaborador y ni sabes con cuántos vendedores habló. ¿Por qué deberíamos creerle?"**

> Con razón, y el informe lo dice de frente. Un colaborador conversó en mi nombre con vendedores de carrito en la estación Universidades del MIO, y no sé cuántos fueron. Por eso lo trato como hipótesis de trabajo, no como dato. Lo puse en contexto: el fiado de mañana a tarde ya está documentado en Kenia, y medí la lluvia: 26 de 294 días de venta. Y fijé cómo matarla: si 3 de 6 vendedores dicen que el minorista espera, no sirve.

- **Respaldo:** Sección 1, "Lo que encontré en campo" y Tabla 1; umbral en Sección 4, "Cómo sé si me equivoqué"; Anexo C, notas del colaborador.
- **Trampa a evitar:** decir "entrevisté" o "hablé con", dar un número de vendedores, o ponerse a la defensiva. La honestidad sobre la evidencia es el punto fuerte, no el débil.

### ★ P2. Mecanismo
**"Olvídate de las diapositivas. Cuéntame un día de lluvia, paso a paso: quién hace qué."**

> Un programa lee la estación del IDEAM en Univalle cada 30 minutos. Si pasa de 5 milímetros entre 7 de la mañana y 7 de la noche, le llega un WhatsApp al minorista: rige la cláusula. El vendedor se queda con hasta $15.000 para la casa, abona el resto, y lo que falta lo paga en tercios en sus tres días de venta siguientes, sin recargo. Al otro día recibe fiado como siempre. La plata nunca pasa por mí.

- **Respaldo:** Sección 2, primer párrafo y Tabla 2 (fila "Día de lluvia" y "Días de venta 1 a 3").
- **Trampa a evitar:** decir "le prestamos" o "le damos crédito". No se crea crédito: se corre la fecha de uno que ya existe. Tampoco perderse en la API o en el WhatsApp.

### ★ P3. Números (quien paga)
**"¿Por qué un minorista pagaría $4.000 al mes por algo que hoy no le duele? Y si llueve, llueve para todos sus vendedores. ¿Con qué caja espera?"**

> Es la segunda cara del riesgo que nombré. La tarifa es 2,5% del margen que un vendedor le deja al mes, y con mis supuestos se paga sola si le evita perder 1 de cada 20 vendedores al año. Pero no tengo un hallazgo que muestre que pierde vendedores por deudas. Y la caja es lo duro: no pierde la plata, le llega en tercios, pero con 12 vendedores esa tarde le faltan unos $562.000. Si no los tiene, el plazo tiene que subir al mayorista. Si el mayorista aceptaría, no lo sé: por eso le pregunto al minorista si le paga a su proveedor de contado o a plazo.

- **Respaldo:** Sección 3, "Para quien paga" y Tabla 3 fila 3; segunda capa del riesgo en Sección 4; Tabla 2, fila "Fin de mes"; Anexo C, "Preguntas que faltan".
- **Trampa a evitar:** insinuar que un minorista ya dijo que pagaría. No hablé con ningún minorista. Tampoco decir que el 1 de cada 20 es un dato: es un cálculo propio con 3% de impago supuesto. Y no abrir con "es mi riesgo más grande": la diapositiva 9 ya dijo que el riesgo tiene dos caras, y dos "riesgos más grandes" suenan a respuesta armada.
- **Si repreguntan "¿y por qué aceptaría el mayorista?":** "No lo sé todavía. Si el minorista paga de contado y no tiene la caja, la cláusula no se sostiene, y lo digo."

### ★ P4. Números (viabilidad)
**"Sé directo: ¿tu modelo cierra? ¿Y de dónde sale la plata para aguantar?"**

> Sin salario cierra en el mes 10, con 279 vendedores que pagan. Con mi salario, en el mes 22, con 904. En el caso conservador, con salario no cierra en 60 meses, y lo digo. Arriesgo de $3,4 a $6,4 millones de mis ahorros, nunca plata del público. Si no cierra, será por volumen y por una tarifa que nadie ha pagado todavía, no por riesgo de crédito, porque no tengo cartera.

- **Respaldo:** Tabla 3 (filas 5 y 6) y los dos párrafos debajo; Anexo B.
- **Trampa a evitar:** vender Fondo Emprender o el BID Lab como plata disponible (hoy no hay convocatoria para Cali y el BID Lab es una meta con 12 meses de datos). Tampoco esconder que el mínimo completo me lo pago solo desde el mes 22.

### ★ P5. Riesgos y descartes
**"¿Y si el minorista ya le espera al vendedor cuando llueve? Entonces tu solución no resuelve nada."**

> Exacto, y es la primera capa de mi riesgo. La única etnografía del fiado en Cali dice que se salda "en los próximos días", o sea, puede que ya espere. Por eso fijé el umbral antes de oír respuestas: si 3 o más de 6 vendedores dicen que el minorista espera, o si la mayoría dice que la mercancía se daña, la cláusula no sirve y lo digo. Prefiero matarla con una pregunta barata que con un piloto.

- **Respaldo:** Sección 4, "El riesgo real tiene tres capas" (cita de R10) y "Cómo sé si me equivoqué".
- **Trampa a evitar:** usar el resumen del colaborador como si cerrara el tema. Si insisten, sumar la otra mitad del riesgo: si la plata del gota a gota se va sobre todo al hogar (28,9% del crédito del ambulante va a gasto personal), la cláusula cambia poco.

### ★ P6. Mecanismo (originalidad)
**"Esto suena a un seguro paramétrico, o a un BNPL tipo Tienda Pago. ¿Qué es lo nuevo aquí?"**

> Se parece, y por eso probé el seguro. Lo maté con la frecuencia: con 26 días de lluvia al año, la prima sería 43% del ingreso diario. Las soluciones formales que encontré venden plata a 30 días o, como Tienda Pago, financian a bodegas. El puente de un día ya se vende, y caro: Corabastos cobra 10% en el día. Lo mío no crea crédito: el plazo normal sigue en cero días y solo lo abre un dato público, no una solicitud del deudor. No hay prima, no hay indemnización y no hay préstamo nuevo.

- **Respaldo:** Sección 2, punto "El problema ya tiene soluciones"; Descarte 2 en Sección 4.
- **Trampa a evitar:** decir "nadie lo ha hecho nunca". El informe dice "no encontré publicado ese paso (búsqueda limitada)". La diferencia se defiende con el mecanismo, no con el nombre.

### ★ P7. Uso de IA
**"¿Cuánto de esto hizo la IA y cuánto hiciste tú?"**

> Usé Claude Code con agentes que buscaban y leían fuentes en paralelo, y otro que leyó la propuesta como un jurado: marcó 19 afirmaciones sin respaldo, que corregí o saqué. Cada cifra se contrastó con el documento original. Las decisiones fueron mías: organizar el campo, cambiar de la ventanilla del tendero a la cláusula, descartar el seguro con mis números y no usar cifras sin fuente, como la de los 12 millones de colombianos.

- **Respaldo:** Anexo C, "Cómo investigué y cómo usé la IA"; repositorio público citado ahí.
- **Trampa a evitar:** minimizar la IA (el caso la permite y el informe lo dice) o sonar como si la IA hubiera decidido. Si preguntan qué hizo mal la IA, la respuesta está en el mismo anexo: 19 afirmaciones sin respaldo.

---

## Proceso y decisiones

### P8. **"¿En qué momento cambiaste de idea? ¿Por qué dejaste la ventanilla del tendero?"**

> Empecé con un préstamo diario legal cobrado en la tienda. Parecía buena: iba al usuario con más gota a gota. La maté por dos razones. A precio legal y con montos de ambulante, el neto por usuario va de $5.857 a menos $26.143 al año. Y según el resumen del colaborador, el vendedor ya tiene crédito diario sin interés. Ahí cambió la pregunta: no cómo prestarle más barato, sino cómo evitar que la lluvia rompa ese fiado.

- **Respaldo:** Descarte 1 en Sección 4; cambio de pregunta al final de "Lo que encontré en campo" (Sección 1).
- **Trampa a evitar:** decir "el campo demostró". Es "según el resumen del colaborador".

### P9. **"¿Por qué la lluvia? ¿Y la enfermedad, o una calamidad en la familia?"**

> Por dos razones. La lluvia llega después de sacar la mercancía, así que rompe justo el pago de ese día. Y tiene dato público que cualquiera revisa. La enfermedad y los choques familiares quedan fuera porque no tienen dato, y porque en Colombia el pase pedido por el deudor subió el impago. Lo reconozco en la tesis: no es la única puerta al gota a gota. Es la que un tercero puede cerrar sin prestar.

- **Respaldo:** Sección 2, "Reglas y límites" (R16); "Mi tesis" en la primera página.
- **Trampa a evitar:** prometer que después "se amplía a enfermedad". Eso rompe la pieza que hace funcionar todo: que decide un dato, no el deudor.

---

## Evidencia y campo

### P10. **"Dices que el sistema formal no falla por precio. ¿Con qué número lo sostienes?"**

> Con un cálculo mío sobre la usura de septiembre de 2026. El préstamo diario legal más caro posible cobra $3.436 diarios por cada $100.000, frente a $4.000 del gota a gota. Solo 14% menos. Falla la forma: 87,2% del crédito formal se paga en cuota mensual, y a este vendedor le faltan uno o dos días, no plata a meses. Y a quien pide le aprueban 92,9%; el que no pide, es sobre todo por miedo a endeudarse.

- **Respaldo:** Sección 1, "Por qué falla el formal" (R7, R8, R1).
- **Trampa a evitar:** decir que los requisitos no importan. La tesis dice que "explican solo una parte" (14,6% no pide por requisitos).

### P11. **"El DANE ve casi nada de fiado a ambulantes: unos 50 en Cali. Tú necesitas 279 para cerrar. ¿No se te cae el mercado?"**

> Es la contradicción que más me incomoda, y está en el informe. Con la lectura literal del DANE salen unos 50 en Cali, frente a los 279 del equilibrio. Mi lectura es que nadie llama "crédito" a la mercancía del día, pero no lo he probado. Por eso lo primero es contar: si con los 5 primeros minoristas no llego a 40 vendedores con fiado diario, el modelo no cierra y lo digo.

- **Respaldo:** Sección 2, "Usuario y alcance" (R2, C. 18.1 y 16.1; 17.745 micronegocios ambulantes en Cali y su área).
- **Trampa a evitar:** decir que el DANE está mal. Es una encuesta seria; lo honesto es que mi lectura es una hipótesis con prueba.

### P12. **"¿Por qué Cali? El problema es nacional."**

> Porque el hallazgo y el dato de lluvia son de Cali. Las conversaciones fueron en la estación Universidades del MIO y medí la estación del IDEAM en la Universidad del Valle. Y el problema aquí es fuerte: 51,3% de la deuda de 300 ambulantes del centro era con gota a gota, a 20,4% mensual. En Cali y su área hay 17.745 micronegocios ambulantes. Otras ciudades son un escenario con condiciones, no mi caso base.

- **Respaldo:** Sección 1, "Qué tan grande es" (R4); Sección 2, "Usuario y alcance" (R17); Anexo D.
- **Trampa a evitar:** vender la escala latinoamericana como plan, o decir que la estación está al lado de los carritos (no medí la distancia).

---

## Mecanismo

### P13. **"¿Qué pasa si llueve dos días seguidos?"**

> Ese es el punto débil, y lo digo en el informe. Los tercios se suman y al vendedor le quedan $2.184 para la casa. No es frecuente: en 12 meses hubo 3 rachas de dos días y ninguna de tres. Lo primero que pruebo es pagar en sextos, unos $7.800 diarios, y el puente cierra en 8 días de venta, no en 5. Además, el tope es de 2 días aplazados abiertos por vendedor.

- **Respaldo:** Sección 2, "Reglas y límites"; Anexo B (el ejemplo de $2.184); Anexo C, "Lluvia" (3 rachas de dos días).
- **Trampa a evitar:** decir que no pasa. Pasa, y ya tengo la variante.

### P14. **"¿Y si llueve en la estación y no en el carrito? ¿Y el vendedor que sí vendió ese día y aplaza igual?"**

> Primero, lo honesto: el umbral de 5 milímetros no está calibrado contra ventas y no medí la distancia a los carritos. Eso lo mido en el piloto. Sobre el que sí vendió: la deuda no se perdona, solo se corre tres días de venta, así que aprovecharse vale poco. Y hay frenos: 4 semanas de historial, máximo 2 días abiertos, y si al día 5 no cerró, decide el minorista y el vendedor queda no elegible.

- **Respaldo:** Anexo C, "Lluvia"; Tabla 2 (fila "Días de venta 1 a 3"); Sección 2, "Reglas y límites".
- **Trampa a evitar:** afirmar que la estación representa lo que pasa en el carrito.

---

## Números

### P15. **"¿De dónde salen los $4.000 y los $15.000? Suenan inventados."**

> Son supuestos, y en el informe están marcados como supuestos sin dato. Los $4.000 son 2,5% del margen de $161.200 que un vendedor le deja al mes a quien fía: $62.000 de fiado, 26 días, 10% de margen, que también es supuesto. Nadie ha pagado esa tarifa. Los $15.000 son el piso para la casa. Por eso hay umbral: en el mes 3, si menos de la mitad paga, pruebo $2.000 con el mayorista.

- **Respaldo:** Tabla 3, fila 3 (marca [S, sin precedente]); Sección 2, primer párrafo ($15.000 [S]); "Cómo sé si me equivoqué".
- **Trampa a evitar:** defender los números como precisos. El criterio 07 pide supuestos a la vista, no cifras perfectas.

### P16. **"¿Y qué gana el vendedor, en plata?"**

> Ese día, cubrir el fiado con un gota a gota a 20% le costaría de 16% a 32% de lo que gana, unos $38.600 diarios. En mi prototipo, en un mes con 3 días de lluvia, el camino del gota a gota termina en 3 préstamos, dos para pagar cuotas del anterior, con $29.231 de interés. Eso es 76% del ingreso de un día. Con la cláusula no queda nada pendiente. Aclaro: la lluvia del ejemplo es inventada.

- **Respaldo:** Sección 2, punto "Ingreso diario sin ahorro"; Anexo B.
- **Trampa a evitar:** presentar el ejemplo como un caso real. Es una simulación con supuestos.

---

## Riesgos y descartes

### P17. **"Si la regla es tan simple, ¿qué impide que el minorista la copie después del mes gratis y no te pague?"**

> Nada lo impide del todo, y es la tercera capa del riesgo. La regla es simple a propósito. Lo que cobro no es la idea: es el registro que lleva los puentes y el acuerdo con el mayorista, que puede pagar por sus minoristas. Y tengo umbral: si en el mes 3 menos de la mitad paga los $4.000, pruebo $2.000 con el mayorista, y si tampoco funciona, digo que el modelo no cierra.

- **Respaldo:** Sección 4, tercera capa del riesgo; "Cómo sé si me equivoqué"; Tabla 2, fila "Fin de mes".
- **Trampa a evitar:** inventar una barrera (patente, tecnología propia, exclusividad). No existe y no está en el informe.

### P18. **"¿No terminas siendo una entidad financiera, un seguro o una cobranza sin licencia?"**

> El fiado ya existe y no cobra interés, así que no hay usura. No hay prima ni indemnización, así que no es seguro. La plata del vendedor no pasa por mí, así que no capto dinero del público. Y el programa solo le habla a quien fía, porque un mensaje al vendedor sobre lo que debe podría leerse como cobranza. Lo que queda abierto es si una regla pagada por quien fía puede leerse como seguro. Eso va al abogado.

- **Respaldo:** Sección 2, punto "No soy entidad financiera" (R20, R21) y "Reglas y límites" (R19); Tabla 3, fila 1 (concepto legal).
- **Trampa a evitar:** decir "es 100% legal". Tengo una pregunta abierta y la nombro.

---

## Motivación y ejecución

### P19. **"Para un minorista eres un desconocido. ¿Por qué te abriría la puerta?"**

> No le pido que me crea. Llego con un vendedor que ya le compra, el primer mes es gratis y el disparador es un número del IDEAM que revisa solo. El vendedor no me entrega nada: su trato sigue con el minorista de siempre. Solo 5,6% de la gente confía mucho en desconocidos, por eso pongo la confianza en unos pocos minoristas, no en miles de vendedores. Y la paciencia que hoy es un favor se vuelve una regla.

- **Respaldo:** Sección 2, punto "Soy un desconocido" (R23); Tabla 2, fila "Semana 1".
- **Trampa a evitar:** hablar de carisma o de contactos que no están en el informe. La respuesta es el diseño, no la persona.

### P20. **"Si entras mañana al fellowship, ¿qué haces la primera semana? ¿Y qué harías distinto?"**

> Primero, el campo que me faltó. Antes de firmar con nadie, 6 vendedores y un minorista me cuentan la última vez que llovió: si le esperaron, si la mercancía se dañó, en qué se fue la plata. Después, contar: con 5 minoristas necesito 40 vendedores con fiado diario. En el mes 1, si ni 1 de 5 minoristas la acepta gratis, paro. Lo que haría distinto: hacer esas conversaciones yo mismo antes de entregar.

- **Respaldo:** Sección 4, "Cómo sé si me equivoqué"; Sección 2, "Usuario y alcance"; Anexo C, "Preguntas que faltan".
- **Trampa a evitar:** responder con visión de escala ("en dos años, cinco países"). Aquí quieren ver que sé qué pregunta mata la idea y que la hago primero.

---

## De reserva (red team)

### P23. **"¿Cómo mediste la lluvia? ¿Lo hiciste tú o un agente?"**

> Estación del IDEAM 0026055120 en Univalle, registros cada 10 minutos. Sumo la lluvia de 7:00 a 18:59 y solo cuento días con al menos 60 de 72 registros. Del 27 de septiembre de 2025 al 26 de septiembre de 2026: 26 de 294 días de venta con 5 mm o más, 3 rachas de dos días, ninguna de tres. El código lo escribí con ayuda de IA y el cálculo lo corrí yo. El umbral no está calibrado contra ventas y no medí la distancia a los carritos.

- **Respaldo:** Anexo C, "Lluvia" (R14); Anexo C, "Cómo investigué y cómo usé la IA".
- **Trampa a evitar:** decir "la medí yo" en el pitch y no poder explicar el método en 20 segundos sin notas. Ensayar esta respuesta en voz alta.

### P24. **"¿Qué vendedor te abre la puerta del minorista en la semana 1?"**

> Todavía ninguno. Es parte de la misma salida de campo: los seis vendedores de la prueba son los primeros candidatos.

- **Respaldo:** Tabla 2, fila "Semana 1"; Sección 4, "Cómo sé si me equivoqué".
- **Trampa a evitar:** insinuar un contacto que no existe.

---

## Si preguntan "¿por qué te importa este problema?"

No va con respuesta modelo, porque tiene que ser mía y verdadera. Estructura de 20 segundos:
1. Una frase con mi razón real (Cali, gente cercana que conoce casos, lo que sea cierto).
2. La frase que me enganchó del campo: "tienen que pagar un gota a gota con otro gota a gota".
3. Cierre: "Al vendedor no le falta crédito. Le falta que un día de lluvia no cuente como quedar mal."

Si menciono a la informante, decir "una informante de Cali que conoce varios casos de amigos y familiares", salvo que decida decir quién es.

---

## Datos de bolsillo (todos están en el informe)

| Dato | Dónde |
|---|---|
| 61,8% de los ambulantes que pidieron crédito fue a un gota a gota (11,3% en tiendas) | Sección 1 [R2; R3] |
| 160.724 micronegocios al gota a gota, piso oficial | Sección 1 [R1] |
| $3.436 frente a $4.000 diarios por $100.000: solo 14% menos | Sección 1, cálculo propio [R7] |
| 87,2% del crédito formal en cuota mensual | Sección 1 [R8] |
| 26 de 294 días de venta con 5 mm o más; 3 rachas de dos días, ninguna de tres | Sección 1 y Anexo C [R14] |
| Hasta $15.000 para la casa; tercios en 3 días de venta; sextos, unos $7.800, en 8 días | Sección 2 |
| $4.000 por vendedor al mes = 2,5% del margen de $161.200 | Tabla 3, fila 3 |
| Equilibrio: mes 10 con 279 (sin salario); mes 22 con 904 (con salario) | Tabla 3 |
| Riesgo de $3,4 a $6,4 millones, de ahorros | Tabla 3, fila 6 |
| Caja del minorista: unos $562.000 un día de lluvia con 12 vendedores | Sección 3 |
| Descarte 1: neto de $5.857 a menos $26.143 por usuario al año | Sección 4 |
| Descarte 2: prima de unos $16.600 por día, 43% del ingreso diario | Sección 4 |
| Muerte: 3 o más de 6 dicen que el minorista espera | Sección 4 |
