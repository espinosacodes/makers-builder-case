# Entrega final: Builder Case, Makers Fellowship

Revisión final del 27 sep 2026, hacia las 3:25 a. m.; versión 2 cerrada a las 3:36 a. m. Plazo: hoy a las 12:00 m., hora de Colombia.

Archivo que se entrega: `/Users/santiagoespinosa/Documents/makersBuilderCase/report/MAKERS_SANTIAGO_ESPINOSA_CALI.pdf`
Fuente: `/Users/santiagoespinosa/Documents/makersBuilderCase/report/informe.html` (se renderiza con `render.sh`).
Copias: `versions/v1_*` (versión 1) y `versions/v2_*` (versión 2, la que se entrega).

## 1. Estado del PDF (versión 2, la final)

| Punto | Estado |
|---|---|
| Versión final | v2 (copias en `versions/v2_informe.html` y `versions/v2_MAKERS_SANTIAGO_ESPINOSA_CALI.pdf`; la v1 sigue intacta en `versions/`) |
| Páginas totales | 15 (US Letter) |
| Cuerpo | Páginas 1 a 5 (5.125 palabras) |
| ANEXOS | Arriba de la página 6, en página nueva |
| Espacio libre en la página 5 | Menos de 1 línea. Cualquier frase nueva en el cuerpo exige cortar otra igual |
| Nombre del archivo | Exacto |
| Rayas y semirrayas | 0 en el PDF y 0 en el HTML |
| Nombres de personas | 0 |

Salida de `check.py` (última corrida, 27 sep 2026, 3:36 a. m.):

```
[PASS] file name: found ['MAKERS_SANTIAGO_ESPINOSA_CALI.pdf']
Total pages: 15
ANEXOS first appears on page: 6
[PASS] main body <= 5 pages: body = 5 pages; ANEXOS at top of page 6: True
[PASS] no dashes in PDF text: none found
[PASS] no dashes in informe.html (visible text): none found
[PASS] no dash chars anywhere in informe.html source: none found
[PASS] no denylisted names in informe.html: none found
[PASS] no denylisted names in PDF text: none found

Words per page:
  p 1 [body ]  1079 words
  p 2 [body ]   929 words
  p 3 [body ]   956 words
  p 4 [body ]   965 words
  p 5 [body ]  1196 words
  p 6 [annex]   893 words  <- ANEXOS
  p 7 [annex]   753 words
  p 8 [annex]   785 words
  p 9 [annex]   922 words
  p10 [annex]   800 words
  p11 [annex]   701 words
  p12 [annex]   622 words
  p13 [annex]   862 words
  p14 [annex]   704 words
  p15 [annex]   404 words
  main body total: 5125 words

RESULT: ALL PASS
```

Nota: en una corrida intermedia `check.py` marcó "Carla" en el PDF. Era la palabra "apli-carla" partida al final de una línea; ahora dice "usarla".

## 2. Lo que cambié en esta revisión final

Solo arreglos pequeños de exactitud y redacción, todos verificados contra las fuentes (`docs/07`, `docs/09`, `research/03`, `research/12b`). Salían de las revisiones de hechos y de cumplimiento de la ronda 2, que se escribieron después del último render y no se habían aplicado.

1. Página 1: el colaborador nunca dijo "cada mañana". Ahora dice "los vendedores de carrito llegan y...". En la Tabla 1 y en el Anexo J, "cada día".
2. Página 1: "es lo primero que confirmo en campo" pasó a "voy a confirmar", porque todavía no se confirmó nada.
3. Página 1: "El gota a gota llega esa misma tarde, sin papeles" no tenía fuente. Ahora dice "llega rápido" y cita el 55% de Perú que lo prefiere por la rapidez del trámite [R21].
4. Tabla 1: la lectura "no distingue un mal día de un mal pagador" quedó marcada como mía, separada de lo que dice R30. El título de la tabla remite al Anexo J.
5. Página 3: "una deuda de $31.000 a $62.000" pasó a "la mitad o todo un fiado de $62.000" (igual en el Anexo E.4).
6. Página 4: se quitó el doble "desde" ("Desde el día 1 vendo un servicio de información a través de una SAS") y "Lo que aprendí y usé" va en negrita, porque responde una pregunta del caso.
7. Tabla 3, fila 3: "$2.800 por vendedor que paga, al mes", para que cuadre con las filas 4 y 5.
8. Página 5: "Otras siete opciones descartadas" (el Anexo H tiene siete, no seis) y "que llueva en la estación y no en el carrito" (Meléndez solo se explicaba en el Anexo F).
9. Anexo A: la tarjeta dice "en sus 3 días de venta siguientes".
10. Anexo D: la cita de la informante quedó literal ("más tranquilo que un gota a gota") y "Si usted no paga, uno le cobra como sea" se atribuye a ella, no a "la comunidad".
11. Anexo E.2: "Inversión más pérdidas acumuladas" en vez de "Pérdida acumulada".
12. Anexo F: los 12.577 duplicados son de la descarga completa (sep 2024 a sep 2026), no de 2025.
13. Anexo H: la fila del QR ya tiene su referencia [R4, C. 14.1].
14. Anexo J: "Captar dinero del público en forma masiva y habitual sin autorización es delito" en lugar de la versión simplificada de "más de 20 personas".
15. Anexo C: "cambiar de A (Anexo H)".

## 3. Último puntaje con la rúbrica

**33 de 40** (ronda 3, `review-rubric-r3.md`, sobre la v2 antes de los arreglos finales; la v1 tuvo 32 en la ronda 2). El revisor de rúbrica y el de hechos (`review-facts-r3.md`) dijeron que la v2 es mejor que la v1 y que nada bloquea.

| # | Criterio | Puntaje |
|---|---|---|
| 01 | Efectividad | 4 (antes 3) |
| 02 | Especificidad | 4 |
| 03 | Creatividad | 4 |
| 04 | Diagnóstico | 4 |
| 05 | Fuentes | 4 |
| 06 | Trazabilidad | 4 |
| 07 | Juicio cuantitativo | 4 |
| 08 | Descartes y autocrítica | 5 |

Arreglos aplicados después de la ronda 3 (todos dentro de las 5 páginas):
1. Página 3, "Lo que no cubre": "hasta $15.000"; el punto débil son dos días de lluvia seguidos y los $2.184 caen en los dos días de venta siguientes (no en los de lluvia); con sextos el puente se cierra en 8 días de venta y no en 5.
2. Página 5, umbrales del piloto: "al menos 90% de los puentes se cierra a tiempo (5 días de venta, u 8 con sextos)".
3. Anexo A: con sextos, la ventana para cerrar el puente pasa de 5 a 8 días de venta.
4. Página 5, riesgos menores: se quitó "que es poco en el piloto" (la distancia no está medida) y ahora dice "(no medí la distancia)".
5. Tabla 3, fila 3: "26 días de venta al mes", para no confundirlo con los 26 días de lluvia al año.
6. Página 4, Descarte 1: "el campo mostró" pasó a "según el resumen del colaborador".
7. Página 5: "La primera", "La segunda" y "La tercera" del riesgo van en negrita.
8. Anexo C: una cuarta revisión adversarial (la caja del minorista, las rachas de dos días en el cuerpo, cómo se alimenta el registro).
9. Para hacer espacio: se quitó el 48,4% repetido en "Reglas" (sigue en la Tabla 1) y la última frase de "Para el vendedor" (el mes de ejemplo está completo en el Anexo A).

Según el revisor, lo único que sube 07 a 5 es la fuente de la plata, y lo único que sube 03 a 5 es la prueba de originalidad opcional.

## 4. Los 5 puntos más fuertes

1. **Tesis propia, acotada y refutable.** El gota a gota no gana por precio: el préstamo diario legal más caro posible cobra $3.436 por cada $100.000, frente a $4.000 (cálculo propio con la usura de septiembre de 2026). Gana en la tarde en que un día sin ventas rompe el fiado diario sin interés. El informe dice de frente lo que no cuadra (el fiado de Aguablanca que espera, la lectura literal del DANE que da unos 50 vendedores).
2. **Un solo mecanismo para los cuatro puntos de la plataforma.** Un dato público de lluvia corre la fecha de pago de un crédito que ya existe. No presto, no aseguro, la plata del vendedor nunca pasa por la SAS y la confianza se queda con el minorista de siempre. El disparador es un número del IDEAM que cualquiera revisa.
3. **Paso a paso muy concreto.** La Tabla 2 y la Figura 1 dicen quién hace qué, cuándo, con qué y dónde está la plata en cada momento: el aviso por WhatsApp, el rezago de 1,5 horas, la tarde en que el aviso no ha llegado, el tope de 2 días abiertos, el cierre en 5 días de venta y el día declarado con tope mensual.
4. **Trabajo propio con datos.** La serie de lluvia del IDEAM (26 de 294 días de venta, rachas de 1 o 2 días, huecos dichos), el prototipo en Excel con fórmulas vivas (14 de 14 comprobaciones) y un modelo de negocio con supuestos a la vista que dice "no cierra con salario en 12 meses".
5. **Descartes reales y riesgo con umbrales.** A y F murieron con números propios (neto de hasta -$26.143 por usuario al año; prima de 43% del ingreso diario) y dejan una lección que pasa a la cláusula. El riesgo va en tres capas, con umbrales de muerte fijados antes de oír respuestas, y la trazabilidad está en la Tabla 1 y el Anexo J.

## 5. Los 3 puntos más débiles y qué hacer antes de las 12:00

### Débil 1. El hallazgo central es de segunda mano
Que la lluvia rompe el fiado y empuja al gota a gota viene del resumen oral de un colaborador, sin número de vendedores ni citas de cada uno. No hay ninguna conversación en primera persona, y la única etnografía del fiado en Cali describe un fiado que espera.

### Débil 2. El lado de quien fía no está probado
La lluvia le cae a todos los vendedores del minorista el mismo día. Con 10 a 13 vendedores, un día de lluvia le deja de $468.200 a $608.660 sin cobrar esa tarde, y una racha de dos días, de $936.400 a $1.217.320 (cálculo propio con los $46.820 y $93.640 del Anexo A). El informe lo mide por vendedor y habla del costo del dinero ($2.000 al año), no de la caja para surtirse al otro día. La razón para pagar ("si le evita perder 1 de cada 20 vendedores") supone que los minoristas pierden vendedores por deudas, y ningún hallazgo lo muestra. La tarifa de $4.000 no tiene ancla.

### Débil 3. El negocio cierra despacio y falta la fuente de la plata
Con salario, el equilibrio llega en el mes 22 con 904 vendedores que pagan, y el caso conservador no cierra en 60 meses. Para los $8,5 millones del arranque y los $34,5 millones con salario, el informe dice "capital semilla que hoy no tengo". Además, en una racha de dos días los tercios le dejan al vendedor $2.184 para la casa dos días seguidos (ahora lo dice la página 3, con la prueba de pagar en sextos).

### Campo antes del mediodía (lo único que sube el puntaje de verdad)

Hoy es domingo. Los carritos de la estación Universidades pueden tener poca actividad con la universidad cerrada, así que conviene verificarlo antes de ir. Una alternativa es un sitio con vendedores y surtidores abiertos el domingo en la mañana (por ejemplo, la galería Santa Elena, donde se hizo la encuesta de 2016 [R22]). Hay que confirmar que esté abierta antes de salir.

Reglas: no contactar ni buscar prestamistas, no pedir datos de prestamistas, no grabar ni fotografiar a nadie sin permiso, no anotar nombres. Hablar en pasado concreto, no en hipotético.

**A 3 a 6 vendedores de carrito o ambulantes que saquen mercancía fiada** (preguntas del Anexo D):
1. "La última vez que llovió y no vendió, ¿qué le dijo el que le fía esa tarde? ¿Le esperó o le exigió? ¿Al otro día le fió?"
2. "Lo que no vendió ese día, ¿se le dañó o lo vendió al otro día?"
3. "¿Cuánto saca fiado en un día normal? ¿Se lo dan al mismo precio que de contado?"
4. "Si alguna vez le tocó pedir plata ese día, ¿en qué se fue esa plata: en pagarle al que le fía, en la casa o en otra cosa?"

**A 1 minorista o surtidor que fíe a vendedores:**
5. "¿Le paga a su proveedor de contado o a plazo? ¿A cuántos días?"
6. "¿Cuántos vendedores perdió este año por deudas?"
7. "La última vez que llovió duro, ¿cuántos de sus vendedores no le pagaron esa tarde? ¿Con qué plata se surtió al otro día?"
8. "¿Hoy paga algún servicio mensual para el negocio? ¿Cuánto?" (ancla de precio para la tarifa, sin preguntar en hipotético).

**Al colaborador, por teléfono (5 minutos):**
9. "¿Con cuántos vendedores hablaste? ¿Alguno te dijo cuánto saca fiado al día o si el minorista le espera cuando llueve?" Solo si da un número, se puede escribir como su recuerdo; si no, se deja "no sé cuántos".

Cómo reportarlo si se hace: cuántas personas, dónde, a qué hora y qué dijeron, en primera persona y sin nombres. Cambiar en la página 1 y en el Anexo D la frase "Yo no entrevisté vendedores en persona". Comparar contra los umbrales del Anexo D sin moverlos (si 3 o más de 6 dicen que el minorista espera, decirlo). En el cuerpo no queda espacio libre en la página 5: lo que se agregue exige cortar lo mismo, y lo demás va al Anexo D. Terminar el campo hacia las 10:30 para tener tiempo de editar, correr `render.sh` y `check.py`, y enviar antes de las 11:30. Si no se hace campo, no se cambia nada: el informe ya es honesto sobre su evidencia.

## 6. Pendientes

**Hechos en la v2** (los seis cambios de contenido de la ronda 2): la caja del minorista en un día de lluvia, las rachas de dos días y los sextos, cómo se alimenta el registro, el techo de las 3 estaciones, la tarifa anclada en el margen de quien fía y el Cuadro 21.1 completo.

**Solo los puede resolver Santiago:**
- La fuente real de los $8,5 millones (Tabla 3, fila 6, y nota del Anexo E.2). Hoy la frase es neutra y no se inventa nada. Si Santiago la confirma, la frase queda así: "Los $8,5 millones del arranque sin salario salen de [fuente], como capital de la SAS, nunca como préstamos del público [R15]; los $26 millones restantes solo los busco como capital semilla si el piloto pasa los umbrales del mes 3." No hay espacio libre en la página 5, pero esa fila está en la página 4; hay que volver a correr `render.sh` y `check.py`.
- R39: el salario mínimo de 2026 viene de una nota de Holland & Knight. Si tiene el decreto oficial, se reemplaza.
- El campo de la sección 5, si alcanza el tiempo. Sin campo no se cambia nada.

**Menores que no toqué:**
- La estación de respaldo Farallones (Anexo F) puede no quedar cerca de ningún vendedor; no verifiqué su ubicación.
- Hay dos 5,1% distintos a una página de distancia (Tabla 3: la tarifa frente al margen con fiado de $30.000; "Para quien paga": los vendedores que tendría que dejar de perder). Las dos cuentas están bien.
- El argumento del Anexo A (11 días de venta en promedio entre lluvias) no considera que la lluvia se agrupa: octubre tuvo 7 días y hubo 3 rachas de dos días.
- La prueba de originalidad con IA (opcional, criterio 03).

## 7. Pitch de 3 minutos para la entrevista

**0:00 a 0:20. La tarde de lluvia.** "Un colaborador conversó por mí con vendedores de carrito en la estación Universidades del MIO. Me trajo esto: 'Hay días en que, no sé, llovió, entonces nadie va. No le puedo pagar. Y ahí es cuando entran con un gota a gota'." (No decir que Santiago entrevistó en persona, salvo que lo haga esta mañana.)

**0:20 a 0:50. El diagnóstico.** El gota a gota no gana por precio: el préstamo diario legal más caro posible es solo 14% más barato por día. Tampoco es falta de cuentas. El formal vende plata a meses (87,2% del crédito se paga en cuota mensual) a alguien a quien le faltan uno o dos días. Entre los ambulantes que piden crédito, 61,8% va a un gota a gota (DANE). Y el vendedor ya tiene crédito diario sin interés: el fiado de su minorista. Lo que le falta es que ese fiado aguante un día malo.

**0:50 a 1:40. El mecanismo.** La cláusula de lluvia del fiado. Recorrer un día: la estación del IDEAM en Univalle pasa de 5 mm entre 7 a. m. y 7 p. m.; el programa le escribe al minorista "rige la cláusula"; el vendedor se queda con hasta $15.000 para la casa, abona el resto y paga lo que falta en tercios en sus 3 días de venta siguientes, sin recargo; al otro día recibe fiado como siempre. Quien fía paga $4.000 al mes por vendedor. Los cuatro puntos en una frase cada uno: no presto ni aseguro y la plata nunca pasa por mí; actúa solo el día sin ingreso; la confianza se queda con el minorista y el disparador es un número público; las soluciones que existen venden plata a 30 días.

**1:40 a 2:10. Los números, sin maquillaje.** Inversión de $3,9 millones, costo fijo de $2,53 millones al mes, $2.800 de contribución por vendedor. Con mi salario, equilibrio en el mes 22 con 904 vendedores; sin salario, en el mes 10 con 279. El caso conservador con salario no cierra. Si no cierra, será por volumen y por una tarifa que nadie ha pagado todavía, no por riesgo de crédito, porque no tengo cartera. Lo que lo haría cerrar es vender por mayorista.

**2:10 a 2:40. Lo que descarté y el riesgo real.** Empecé con un préstamo diario legal cobrado en la tienda: no cierra a precio legal con montos de ambulante y quedaría de último en la fila de pago. Probé asegurar el día de lluvia: con 26 días al año la prima es 43% del ingreso diario. Lección: las pérdidas pequeñas y frecuentes se suavizan con plazo; se aseguran las raras. Riesgo real: que el minorista ya espere, que nadie quiera cargar el día de lluvia (tener lista la cuenta de la caja: unos $562.000 con 12 vendedores) o que copien la regla.

**2:40 a 3:00. Cómo sé si me equivoqué.** Antes de firmar con nadie, 6 vendedores y un minorista responden sobre la última vez que llovió; si 3 o más de 6 dicen que el minorista espera, la cláusula no sirve y lo digo. Cierre: "Al vendedor no le falta crédito. Le falta que un día de lluvia no cuente como quedar mal."

**Preguntas duras que conviene tener listas:** ¿con qué caja espera el minorista si llueve para todos? ¿Por qué pagaría el minorista si hoy no le duele? ¿Qué pasa si llueve en el carrito y no en la estación? ¿Por qué Cali y no el Caribe, donde está 80,1% del gota a gota de las 24 ciudades? ¿La regla se puede leer como seguro? ¿De dónde sale la plata para arrancar?
