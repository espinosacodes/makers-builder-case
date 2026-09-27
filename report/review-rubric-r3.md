# Revisión con la rúbrica, ronda 3

Revisado: `report/MAKERS_SANTIAGO_ESPINOSA_CALI.pdf` (15 páginas; cuerpo en las páginas 1 a 5; "ANEXOS" abre la página 6), contra `report/versions/v1_MAKERS_SANTIAGO_ESPINOSA_CALI.pdf` (la versión que puntuó 32 en la ronda 2). Punto de vista: evaluador del Makers Fellowship que ya leyó más de cien propuestas de este caso. Texto extraído con pypdf y páginas 2 a 5 revisadas como imagen.

## Chequeo de entrega (descalifica si falla)

| Regla | Estado |
|---|---|
| Nombre exacto `MAKERS_SANTIAGO_ESPINOSA_CALI.pdf` | Cumple |
| Cuerpo de 5 páginas o menos; anexos después | Cumple (`check.py`: RESULT: ALL PASS; 5.137 palabras en el cuerpo). La página 5 llega hasta el pie: cualquier agregado sin recorte equivalente empuja el cuerpo a una sexta página |
| Fuentes verificables | Cumple: 39 referencias con URL, cuadro o página |
| Raya y semirraya | 0 en el PDF; no hay guion con espacios |
| Nombres, edad, campo inventado | No aparecen; el colaborador sigue sin número de vendedores y nadie dice haber entrevistado en persona |
| Fuente de la plata | Neutral ("capital de la SAS", "capital semilla que hoy no tengo"); no se inventó fuente |

Nada descalifica. Los seis pendientes de la sección 6 de `ENTREGA.md` entraron y se leen bien: la caja del minorista ($562.000 con 12 vendedores), el punto débil de las rachas con la prueba en sextos, cómo se alimenta el registro, el techo por cobertura de estaciones, la tarifa anclada en 2,5% del margen y el Cuadro 21.1 completo. Revisé las cuentas nuevas y cuadran: 12 × $46.820 = $561.840; 12 × $93.640 = $1.123.680; $62.000 × 26 × 10% = $161.200 y $4.000 / $161.200 = 2,5%; $15.607 + $20.809 = $36.416 y $38.600 menos eso = $2.184; $46.820 / 6 = $7.803, 20,2% de $38.600.

## Puntaje (1 a 5)

| # | Criterio | v1 (r2) | Ahora | Justificación en una línea |
|---|---|---|---|---|
| 01 | Efectividad | 3 | 4 | Ahora nombra los dos agujeros que yo habría encontrado (la caja del minorista cuando llueve para todos y los $2.184 tras una racha) y dice qué hace con cada uno; sigue siendo un solo disparador de unos 2 días al mes sobre una premisa de segunda mano. |
| 02 | Especificidad | 4 | 4 | El registro ya tiene entrada ("¿vendedor 3 pagó su tercio?"); queda un choque interno: la prueba en sextos no cabe en la ventana de cierre de 5 días que usan la Tabla 2 y los umbrales de la página 5. |
| 03 | Creatividad | 4 | 4 | Plazo de cero días que solo abre un dato público, pagado por quien fía y sin financiador; el precedente de las cláusulas de huracán está dicho. Sin prueba con IA no llega a 5. |
| 04 | Diagnóstico | 4 | 4 | Tesis propia y refutable intacta; el recorte del dato de cuentas (96,5%) quita un golpe contra la respuesta "bancarizar", pero el argumento de la forma del producto lo sostiene. |
| 05 | Fuentes | 4 | 4 | Igual que antes: casi todo primario con cuadro o página; restan R39 (nota de bufete) y que el hallazgo central sea un resumen oral. |
| 06 | Trazabilidad | 4 | 4 | La tarifa ya tiene ancla y el piso de $15.000 se traza al 28,9% (Anexo J); la ventana de 3 días sigue sin hallazgo propio. |
| 07 | Juicio cuantitativo | 4 | 4 | Caja simultánea, techo por estaciones y tarifa anclada: es de lo más honesto que he leído. No sube a 5 porque "¿de dónde saldría?" sigue sin respuesta para los $26 millones. |
| 08 | Descartes y autocrítica | 5 | 5 | A y F muertos con números propios, tres capas de riesgo con umbrales fijados antes de oír respuestas y ahora el punto débil de la propia regla en el cuerpo. |
| | **Total** | **32** | **33 de 40** | |

**¿Mejor que v1?** Sí. Gana un punto en 01 y se refuerzan 02, 06 y 07 sin perder nada que pese: los recortes (35,6% de 24 ciudades, 36% de Perú, 96,5% de cuentas, beneficiarios de CREO) eran contexto, y todos siguen citados o en anexos. Con los arreglos 1 y 2 de abajo, 02 queda firme y cerca de 5.

## Lo que hay que arreglar (ninguno bloquea; de más a menos importante)

Regla para todos: el cuerpo está lleno hasta el pie de la página 5. Cada agregado va con su recorte (arreglo 3) y después se corre `render.sh` y `check.py` hasta ver RESULT: ALL PASS y ANEXOS arriba de la página 6.

### 1. Los sextos no caben en la ventana de cierre de 5 días
- **Dónde.** Página 3, "Lo que no cubre", última frase: "Lo primero que pruebo con el minorista es pagar en sextos, unos $7.800 diarios por cada día de lluvia (20% del ingreso de un día; cálculo propio)." Choca con la Tabla 2, fila "Puente sin cerrar" ("a los 5 días de venta (3 de tercios y 2 de margen)") y con la página 5, "Cómo sé si me equivoqué": "al menos 90% de los puentes se cierra en 5 días de venta".
- **Por qué cuesta.** Pagando en sextos, un puente dura 6 días de venta como mínimo: con la regla escrita, todo puente de la prueba saldría "sin cerrar" y el vendedor quedaría no elegible. Es el tipo de incoherencia que un evaluador que leyó con cuidado la Tabla 2 detecta de inmediato, y pega en 02.
- **Reescritura (página 3, reemplaza las dos últimas frases de "Lo que no cubre"; incluye el arreglo 2).** "Su punto débil son dos días de lluvia seguidos: los tercios se suman y en los dos días de venta siguientes le quedan $2.184 para la casa (Anexo A). Lo primero que pruebo con el minorista es pagar en sextos, unos $7.800 diarios por cada día de lluvia (20% del ingreso de un día; cálculo propio); con sextos, el puente se cierra en 8 días de venta y no en 5."
- **Y en la página 5**, cambiar "al menos 90% de los puentes se cierra en 5 días de venta" por "al menos 90% de los puentes se cierra a tiempo (5 días de venta, u 8 con sextos)".

### 2. "Dos días seguidos le quedan $2.184" se lee como si fueran los días de lluvia
- **Dónde.** Página 3, "Lo que no cubre": "los tercios se suman y dos días seguidos le quedan $2.184 para la casa (Anexo A)."
- **Por qué cuesta.** Tal como está, parece que los $2.184 son lo que le queda los días de lluvia, cuando esos días guarda $15.000. Son los dos días de venta que siguen a la racha (días 15 y 16 del Anexo A). Ya va resuelto en la reescritura del arreglo 1.

### 3. Recorte para que los arreglos 1 y 2 no rompan las 5 páginas
- **Dónde.** Página 3, "Reglas", última frase: "El programa solo habla con el minorista (y con el mayorista si entra): 48,4% de los ambulantes usa celular en el negocio [R4, C. 14.1] y un mensaje al vendedor sobre lo que debe podría leerse como cobranza [R13]."
- **Por qué.** El 48,4% ya está en la Tabla 1 (fila "No se formalizan") y la Tabla 2 ya dice que al vendedor no se le pide celular. Es redundancia pura y libera unas 15 palabras, que es lo que agregan los arreglos 1 y 2.
- **Reescritura.** "El programa solo habla con el minorista (y con el mayorista si entra): un mensaje al vendedor sobre lo que debe podría leerse como cobranza [R13]."
- Si aun así se pasa, segundo recorte: en la página 5, "Para el vendedor", quitar la última frase ("En un mes de ejemplo del prototipo (Anexo A, lluvia inventada), tres días de lluvia terminan en 3 préstamos encadenados y $29.231 de interés."), que está completa en el Anexo A.

### 4. "¿De dónde saldría?" sigue sin fuente (solo lo puede cerrar Santiago)
- **Dónde.** Página 4, Tabla 3, fila 6: "Los $8,5 millones del arranque sin salario los pondría como capital de la SAS, nunca como préstamos del público [R15]; la diferencia hasta $34,5 millones sería capital semilla que hoy no tengo". Mismo texto en el Anexo E.2.
- **Por qué cuesta.** La pregunta 6 del caso pide la fuente, y es lo único que separa 07 de un 5. No se inventa nada: si Santiago no confirma, se deja como está.
- **Reescritura (solo con la fuente que Santiago confirme).** "Los $8,5 millones del arranque sin salario salen de [fuente que confirme Santiago], como capital de la SAS, nunca como préstamos del público [R15]; los $26 millones restantes solo los busco como capital semilla si el piloto pasa los umbrales del mes 3." Mismas palabras en el Anexo E.2. La segunda mitad también es una decisión de Santiago; si no la comparte, se deja la frase actual.

### 5. La página 5 es un muro: marcar las tres capas del riesgo sin gastar espacio
- **Dónde.** Página 5, párrafo "El riesgo real tiene tres capas." (unas 280 palabras seguidas; la página tiene 1.218).
- **Por qué cuesta.** Es la sección que más puntos da en 08 y un evaluador con cien PDF lee en diagonal: hoy "La segunda" y "La tercera" se pierden a mitad de línea.
- **Arreglo (cero palabras nuevas).** En `informe.html`, línea 197, envolver en negrita "La primera", "La segunda" y "La tercera" (por ejemplo `<strong>La segunda</strong> es que nadie quiera cargar...`). No cambia el largo.

### 6. El Anexo C no cuenta la última revisión
- **Dónde.** Página 9, Anexo C, "Revisión adversarial": termina en "Una tercera, sobre este documento, me hizo agregar el piso para la casa, la tarde en que el aviso todavía no llega y el riesgo de que la regla se copie."
- **Por qué cuesta.** El jurado pregunta cómo llegaste; los cambios de esta ronda (caja del minorista, punto débil de las rachas, registro, techo por estaciones) son buenos ejemplos de autocrítica y hoy no aparecen como tales. Está en anexos, así que no toca el límite de páginas.
- **Reescritura (agregar al final del párrafo).** "Una cuarta me hizo medir la caja del minorista en un día de lluvia, poner en el cuerpo el punto débil de las rachas de dos días y decir cómo se alimenta el registro."

## Lo que ya está bien y no hay que tocar

- "El costo no es lo difícil; la caja sí." y el cálculo de los $562.000: responde la primera pregunta dura antes de que la hagan.
- "El techo real no son esos 17.745, sino los que trabajan cerca de una de las 3 estaciones": junto con "en Cali serían unos 50 ... y este negocio no existiría", es honestidad que casi nadie tiene.
- La tarifa anclada en 2,5% del margen, marcada como cálculo propio con sus [S].
- El Cuadro 21.1 completo con la advertencia de que no separa pagarle al que fía de comprar mercancía.
- La tesis, "Dos cosas no cuadran", "Por qué la lluvia", los dos descartes y "Cómo sé si me equivoqué".

## Opcional, solo si sobra tiempo antes de las 12:00

- **Prueba de originalidad con IA (unos 15 minutos).** Pegar el enunciado y la cita del colaborador en tres modelos y dejar en el Anexo C, en una línea, si alguno propuso un aplazamiento del fiado pagado por quien fía y activado por un dato público. Es lo único que sube 03 a 5. Si no se hace, no mencionarla.
