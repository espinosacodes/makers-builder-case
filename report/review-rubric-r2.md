# Revisión con la rúbrica, ronda 2

Revisado: `report/MAKERS_SANTIAGO_ESPINOSA_CALI.pdf` (15 páginas; cuerpo en las páginas 1 a 5; "ANEXOS" abre la página 6), `report/informe.html` y `report/brief-final.md`. Punto de vista: evaluador del Makers Fellowship que ya leyó más de cien propuestas de este caso. Comparado contra `review-rubric-r1.md` y `review-log.md`.

## Chequeo de entrega (descalifica si falla)

| Regla | Estado |
|---|---|
| Nombre exacto `MAKERS_SANTIAGO_ESPINOSA_CALI.pdf` | Cumple |
| Cuerpo de 5 páginas o menos; anexos después | Cumple (`check.py`: ALL PASS; 5.045 palabras en el cuerpo) |
| Fuentes verificables | Cumple: 39 referencias con URL, cuadro o página |
| Raya y semirraya | 0 en el PDF y 0 en el HTML; no hay guion con espacios |
| Nombres, parentesco, tercera ronda, contacto con prestamistas | No aparecen |
| Cifras de la lista "no usar" (síntesis 1.3 y 1.4) | Solo aparecen en la tabla "Cifras que circulan y no usé" del Anexo C, que es su uso correcto |

Nada descalifica. Los diez arreglos de la ronda 1 entraron y se notan: la tesis está acotada, el piso de $15.000, la lectura literal del DANE (unos 50) con umbral de muerte, "Por qué la lluvia", la tercera capa de riesgo y el precedente de las cláusulas de huracán.

## Puntaje (1 a 5)

| # | Criterio | Puntaje | Justificación en una línea |
|---|---|---|---|
| 01 | Efectividad | 3 | Una sola pieza resuelve los cuatro puntos de verdad, pero cubre un solo disparador (unos 2 días al mes) en un segmento de tamaño desconocido, la premisa no está confirmada en primera persona y los tercios le quitan 40% del ingreso al hogar justo después del día malo. |
| 02 | Especificidad | 4 | La Tabla 2 es de lo mejor que he leído en este caso; falta cómo se entera el programa de que el puente se cerró (el registro, que es lo que cobro, no tiene entrada) y qué pasa cuando llueve para los 12 vendedores del minorista a la vez. |
| 03 | Creatividad | 4 | Un plazo de cero días que solo se abre con un dato público, pagado por el acreedor y sin financiador no está en el mercado ni en la respuesta típica (seguro paramétrico, que aquí es el descarte 2); no llega a 5 porque el alivio de pagos atado al clima es una familia conocida y no hay prueba con IA. |
| 04 | Diagnóstico | 4 | Tesis propia, acotada y refutable, con cálculo propio contra el precio y las dos contradicciones dichas de frente; sigue apoyada en un resumen oral de segunda mano. |
| 05 | Fuentes | 4 | Casi todo primario con cuadro o página; restan el salario mínimo tomado de una nota de bufete (R39), el 10% de Corabastos de un working paper y que el hallazgo central sea de segunda mano. |
| 06 | Trazabilidad | 4 | Tabla 1 y Anexo J trazan casi todo; quedan sin hallazgo la tarifa de $4.000, la ventana de 3 días (las rachas justifican el tope de 2 abiertos, no los tercios) y el piso de $15.000. |
| 07 | Juicio cuantitativo | 4 | Supuestos a la vista, "no cierra con salario" dicho y el caso de 50 vendedores enfrentado; falta la exposición simultánea de quien fía, el techo real por cobertura de estaciones y de dónde sale la plata. |
| 08 | Descartes y autocrítica | 5 | A y F son opciones reales muertas con números propios y una lección que pasa a la cláusula; el riesgo va en tres capas con umbrales fijados antes de oír respuestas. |
| | **Total** | **32 de 40** | |

Con los arreglos 1 a 4, 01 puede pasar a 4 y 07 queda firme en 4: total de 33. Ninguno pide campo nuevo.

## Lo que hay que arreglar (de más a menos grave)

### 1. La lluvia le cae a todos los vendedores del minorista el mismo día, y el documento lo mide por vendedor
- **Dónde.** Página 5, "Para quien paga": "Por vendedor al año, le cuesta la tarifa ($48.000), unos $2.000 de costo del dinero y el impago de lo aplazado." Anexo E.3 y Anexo A ("Mayor saldo aplazado que cargó quien fía $93.640").
- **Por qué cuesta.** Es el primer cálculo que hace un evaluador que haya pensado en crédito: el choque es covariado. Con 10 a 13 vendedores por minorista (Tabla 3), un día de lluvia le deja al minorista de $468.200 a $608.660 sin cobrar esa tarde, y una racha de dos días de $936.400 a $1.217.320 (cálculo propio: vendedores × $46.820 o × $93.640). "$2.000 de costo del dinero" hace ver el plazo como gratis cuando el límite no es el costo sino la caja para surtirse a la mañana siguiente. Si el evaluador lo descubre solo, lee la segunda capa de riesgo como vaga. Pega en 07 y 01.
- **Reescritura (agregar al final de "Para quien paga", unas 50 palabras).** "El costo no es el problema; la caja sí. La lluvia le cae a todos sus vendedores a la vez: con 12, un día de lluvia le deja unos $562.000 sin cobrar esa tarde y una racha de dos días, $1,12 millones (cálculo propio). Si no los tiene para surtirse mañana, la cláusula sube al mayorista desde el primer día, y eso es lo que pregunto antes de inscribir a nadie." En la segunda capa del riesgo, cambiar "Y si el minorista vive al día, solo muevo el hueco un eslabón arriba" por "Y si el minorista no tiene esos $562.000 de caja un día de lluvia, solo muevo el hueco un eslabón arriba."

### 2. Los tercios le quitan al hogar el 40% del ingreso justo después del día malo, y lo peor está solo en el anexo
- **Dónde.** Tabla 2, "Días de venta 1 a 3": "un tercio de lo aplazado (con fiado de $62.000, unos $15.600, 40% de lo que gana en un día)". Anexo A: "los días 15 y 16 el vendedor paga $36.416 de lo aplazado y le quedan $2.184 para la casa".
- **Por qué cuesta.** El punto 2 del caso es "ingreso diario, sin ahorro". Tras una racha de dos días (hubo 3 en 12 meses), el vendedor se lleva $2.184 a la casa dos días seguidos: ese es exactamente el día en que se pide un gota a gota para comer, y el cuerpo no lo dice. Además la ventana de 3 días no tiene hallazgo que la justifique: las rachas cortas justifican el tope de 2 días abiertos, no los tercios. El propio documento muestra que alargar el plazo casi no le cuesta a quien fía: con 2,5 días el costo del dinero es $2.014 al año por vendedor; con 4,5 días serían unos $3.628 (cálculo propio, misma tasa de 20% E.A.). Pega en 01 y 06.
- **Reescritura mínima (sin rehacer el prototipo; en "Lo que no cubre", una frase).** "El punto débil son las rachas de dos días: los tercios se suman y dos días seguidos le quedan unos $2.200 para la casa (Anexo A). Lo primero que pruebo con el minorista es pagar en sextos, unos $7.800 diarios (20% del ingreso), que a él le cuesta unos $1.600 más al año por vendedor en costo del dinero; entre dos días de lluvia pasan en promedio 11 días de venta, así que cabe (cálculo propio)." Si hay tiempo para rehacer `build_prototype.py`, mejor cambiar la regla a sextos y actualizar la Tabla 2, la Figura 1, el Anexo A y el plazo promedio del Anexo E.1.

### 3. El registro es lo que cobro, pero la Tabla 2 no dice cómo se alimenta
- **Dónde.** Tabla 2, "Días de venta 1 a 3": "Al final, el programa le confirma al minorista 'puente cerrado'". Página 5, tercera capa: "Lo que cobro no es el dato: es la regla fijada antes del día [...]; el registro de quién tiene un puente abierto y quién dejó de ser elegible".
- **Por qué cuesta.** El programa no ve pagos: nada en la tabla le dice que el vendedor 3 pagó su tercio. Si el registro depende de que el minorista reporte, el evaluador pregunta qué pasa cuando no reporta, y la defensa contra la copia (el registro) queda sin mecanismo. Es el único hueco del paso a paso. Pega en 02 y 08.
- **Reescritura (en la celda "Qué hace" de "Días de venta 1 a 3").** "El vendedor saca fiado como siempre y paga lo del día más un tercio de lo aplazado (con fiado de $62.000, unos $15.600, 40% de lo que gana en un día). Cada noche el programa le pregunta al minorista '¿vendedor 3 pagó su parte? sí/no'. Con el tercer 'sí' marca 'puente cerrado'; si no responde, el puente sigue abierto y el vendedor no puede abrir otro." Con eso el tope de 2 días abiertos y la regla de "no elegible" pasan a tener dato.

### 4. El techo real no son 17.745 ambulantes sino los que están cerca de una estación con dato
- **Dónde.** Página 3, "Usuario, cliente y alcance": "el techo en Cali A.M. son esos 17.745 ambulantes". Página 5: "Riesgos menores: que llueva en Meléndez y no en el carrito (no medí la distancia)". Anexo F: solo 3 estaciones en Cali con datos al día.
- **Por qué cuesta.** El equilibrio pide 904 vendedores, unos 75 minoristas. Eso no cabe alrededor de una sola estación. Con 3 estaciones para toda Cali, la diferencia entre la lluvia de la estación y la del carrito deja de ser un riesgo menor en cuanto el piloto sale de Meléndez: en un día en que llueve en el carrito y no en la estación, la cláusula no rige y el vendedor vuelve al gota a gota. Pega en 07.
- **Reescritura (una frase después de "el techo en Cali A.M. son esos 17.745 ambulantes").** "En la práctica el techo es menor: solo cuentan los que trabajan cerca de una de las 3 estaciones del IDEAM con dato al día en Cali (Anexo F), y no he medido a qué distancia la lluvia de la estación deja de ser la del carrito. Lo mido en el piloto contra los días que el minorista recuerda como malos." Y en la página 5 cambiar "Riesgos menores: que llueva en Meléndez y no en el carrito (no medí la distancia)" por "Riesgo menor en el piloto, mayor al crecer: que llueva en el carrito y no en la estación."

### 5. "¿De dónde saldría?" tiene una respuesta vacía
- **Dónde.** Tabla 3, fila 6: "la diferencia hasta $34,5 millones sería capital semilla que hoy no tengo". Anexo E.2, mismo texto.
- **Por qué cuesta.** La pregunta 6 del caso pide la fuente. "Capital que hoy no tengo" no es una fuente, y el evaluador lo lee como pregunta sin responder. El `review-log.md` ya lo dejó pendiente de confirmación de Santiago. Pega en 07.
- **Reescritura (Santiago debe poner la fuente real; no inventar).** "Arranco sin salario: los $8,5 millones salen de [fuente real: ahorro propio, socios de la familia como accionistas u otra], como capital de la SAS, nunca como préstamos del público [R15]. Los $26 millones restantes solo los busco si el piloto pasa los umbrales del mes 3, con [convocatoria o inversionista concreto]; si no los consigo, sigo sin salario y el equilibrio llega en el mes 10." Si no hay una fuente que nombrar, al menos la primera frase con la fuente de los $8,5 millones.

### 6. La tarifa de $4.000 no tiene ancla, y el ancla está en el propio documento
- **Dónde.** Tabla 3, fila 3: "Tarifa de $4.000 [S, sin precedente de precio]". Anexo E.1, fila "Tarifa".
- **Por qué cuesta.** Es el número que decide si el modelo cierra (con $2.000 no cierra en 36 meses) y es el único rasgo central sin hallazgo ni razón. El documento ya tiene el dato para anclarlo: el margen que le deja un vendedor a quien fía es $1.934.400 al año (Anexo A, hoja 2), unos $161.200 al mes, y $4.000 son 2,5% de eso (cálculo propio). Además, la razón de pago ("si le evita perder 1 de cada 20 vendedores") descansa en que los minoristas pierden vendedores por deudas, que ningún hallazgo muestra todavía. Pega en 06 y 07.
- **Reescritura (Tabla 3, fila 3, columna de supuesto).** "Tarifa de $4.000 [S]: 2,5% de los unos $161.200 de margen que le deja un vendedor al mes a quien fía (margen de 10% [S], Anexo E.3); sin precedente de precio". En "Para quien paga", agregar al final: "No sé todavía si los minoristas pierden vendedores por deudas; es la segunda pregunta que les hago (Anexo D)."

### 7. La primera capa de riesgo cita un solo pedazo del Cuadro 21.1
- **Dónde.** Página 5: "o si la plata del gota a gota del día malo se va sobre todo al hogar (entre los ambulantes, 28,9% del crédito va a gasto personal [R4, C. 21.1])".
- **Por qué cuesta.** El mismo cuadro dice 50,7% al negocio, 28,9% a gasto personal y 20,5% a ambos (dato de confianza alta en la síntesis). Citar solo el 28,9% se lee como elegir el número; dar los tres es más honesto y además acota cuánto del problema puede tocar la cláusula. Pega en 04 y 05.
- **Reescritura.** "(entre los ambulantes, 50,7% del crédito va al negocio, 28,9% a gasto personal y 20,5% a los dos [R4, C. 21.1]; el DANE no separa pagarle al que fía de comprar mercancía)".

### 8. Hacer espacio: los arreglos suman unas 250 palabras y el cuerpo ya está en 5.045
- **Dónde.** Página 1, "Consecuencias" y "Por qué falla el formal"; página 4, punto 4.
- **Por qué cuesta.** El cuerpo ya bajó a 9,5 pt. No hay que bajar más la letra: un jurado con cien PDF lee en diagonal y la página 1 tiene más de veinte cifras antes de llegar al campo. Recortar datos de contexto protege el mecanismo.
- **Cortes propuestos (unas 120 a 150 palabras).** (a) Página 1: quitar "En las 24 ciudades principales la proporción sube a 35,6% [R3, C. H.4_24C]." (b) Página 1: quitar "La deuda paga deuda: en Perú, 36% de quienes piden al informal lo hacen para pagar otras deudas [R21], y" y dejar solo la cita de Cali. (c) Página 1: quitar "Tampoco es falta de cuentas: 96,5% de los adultos tiene un producto de depósito y solo 8,0% pidió prestado a un banco en el último año [R7; R9]." (d) Página 4, punto 4: quitar "y el programa CREO, que tenía 15.779 beneficiarios en enero de 2024 [R31]" (la lista ya se entiende con tres). Si el arreglo 2 se hace completo (sextos), el Anexo A ya lo explica y en el cuerpo basta la frase.

### 9. Una fila de la Tabla 1 le atribuye a la fuente una lectura propia
- **Dónde.** Tabla 1, fila 4: "El que fía no sabe si fue un mal día o un mal pagador; su sanción es la exclusión [R30]".
- **Por qué cuesta.** R30 respalda la exclusión como sanción; que "no sabe si fue un mal día o un mal pagador" es inferencia tuya. En la tabla que más puntos da en 06, mezclar hallazgo y lectura propia es lo que un evaluador cuidadoso marca.
- **Reescritura.** "Su sanción es la exclusión [R30]; leo que no puede distinguir un mal día de un mal pagador (lectura mía)".

## Lo que ya está bien y no hay que tocar

- La tesis acotada ("para el vendedor que vive del fiado diario... pero es la que un tercero puede cerrar sin prestar").
- "Dos cosas no cuadran" y "Tomado literal, en Cali serían unos 50... y este negocio no existiría": honestidad que casi nadie tiene en este caso.
- "Por qué la lluvia": convierte un disparador que parecía elegido por conveniencia en una decisión con razón y con R27.
- Los dos descartes con cifras propias y la frase "las pérdidas pequeñas y frecuentes se suavizan con plazo; se aseguran las raras".
- "Cómo sé si me equivoqué" con umbrales fijados antes de oír las respuestas, incluida la señal de que el producto es la regla y no el servicio.
- El Anexo F (lluvia con huecos, rezago y estaciones de respaldo) y el Anexo A con el punto débil de las rachas dicho.

## Opcional, solo si sobra tiempo antes de las 12:00

- **Prueba de originalidad con IA (unos 15 minutos).** Pegar el enunciado del caso más la cita del colaborador en tres modelos y guardar las respuestas tal cual en el Anexo C, con una línea: si alguno propuso un aplazamiento del fiado pagado por quien fía y activado por un dato público. Es la única forma de subir 03 a 5. Si no se hace, no mencionarla.
- **Campo en primera persona.** La galería Santa Elena abre el domingo en la mañana. Dos o tres preguntas del Anexo D a vendedores o a un minorista subirían 01 y 04 más que cualquier arreglo de texto. Solo si se reporta tal cual (cuántas personas, qué dijeron, sin nombres) y sin contactar a nadie que preste; si no se hace, no cambia nada.
