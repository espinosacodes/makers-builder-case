# Revisión con la rúbrica: versión condensada para Google Docs

Revisado: `report/docs/informe-docs.md` (cuerpo de 2.774 palabras con tablas) contra el cuerpo de v2 (`report/informe.html`, unas 5.000 palabras, 33 de 40 en la ronda 3). Punto de vista: evaluador del Makers que ya leyó más de cien propuestas de este caso.

## Chequeo de entrega

| Regla | Estado |
|---|---|
| Cuerpo en 5 páginas (Arial 11, 1,15, carta, márgenes de 1 pulgada) | Cumple, pero sin aire: `fit.py --strict` termina en la página 5 al 99% |
| Raya, semirraya, guion con espacios | 0 |
| Enlaces o HTML | 0 enlaces markdown, 0 etiquetas; las URL solo en el Anexo A |
| Referencias | R1 a R32, todas citadas y en orden de primera aparición |
| Nombres, edad, fuente de la plata | No aparecen nombres ni edad; la fuente de la plata sigue neutral |

## Puntaje (1 a 5)

| # | Criterio | v2 | Condensada | Qué cambió |
|---|---|---|---|---|
| 01 | Efectividad | 4 | 4 | La frase "una sola pieza" y los cuatro puntos siguen completos. Se perdió cuánto le cuesta al vendedor un día de lluvia sin la cláusula, que es lo que muestra que el mecanismo le sirve a él. |
| 02 | Especificidad | 4 | 4 (frágil) | La Tabla 2 pasó de 11 filas a 5 y sigue diciendo quién, qué, cuándo y con qué. Pero la fila "Días de venta 1 a 5" mezcla los tercios con el margen y volvió el choque con los sextos: pagar en sextos no cabe en 5 días. También se perdieron la regla del aviso que llega tarde y la de la estación sin dato. |
| 03 | Creatividad | 4 | 4 | El mecanismo es el mismo, pero se cayó la frase que lo separa del crédito de proveedor ("el plazo sigue en cero días y solo lo abre un dato público, no una solicitud"). Sin ella, el lector apurado lo confunde con un simple crédito de proveedor. |
| 04 | Diagnóstico | 4 | 4 | La tesis está intacta. Se perdió "Dos cosas no cuadran"; la mitad (el fiado de Aguablanca) sobrevive en la primera capa del riesgo. |
| 05 | Fuentes | 4 | 4 | Igual: fuentes primarias con cuadro o página, y lista limpia. |
| 06 | Trazabilidad | 4 | 4 | La Tabla 1 bajó de 7 filas a 4 y el Anexo J no está. Lo central sigue trazado. "Al vendedor no se le pide RUT" quedó sin su dato (93,3% sin RUT). |
| 07 | Juicio cuantitativo | 4 | 3 | Dos pérdidas. (1) Ya no aparece en el cuerpo el ingreso diario del vendedor ($38.600) ni cuánto le cuesta el gota a gota ese día, así que el "43% del ingreso diario" y los "$2.184 para la casa" quedan sin ancla. (2) El 1,8% del DANE ahora se descarta con un "quizá" y desapareció la lectura literal (unos 50 en Cali frente a 904), que era de lo más honesto del informe. |
| 08 | Descartes y autocrítica | 5 | 5 | Los dos descartes siguen muertos con números propios; las tres capas y los umbrales siguen. La tercera capa quedó defensiva: ya no admite que el minorista puede usar la regla gratis. |
| | **Total** | **33** | **32 de 40** | Con los arreglos de abajo vuelve a 33, y 02 y 03 quedan más firmes. |

## Lo que hay que arreglar (6, de más a menos importante)

Todo va pareado con los recortes del final. Probé el paquete completo en una copia (arreglos 1 a 6 y recortes A a G): `fit.py --strict` da PASS, el cuerpo termina en la página 5 y sobran entre 5 y 11 palabras. Si se deja fuera un arreglo, también se puede dejar fuera un recorte.

### 1. Devolver al cuerpo lo que el día de lluvia le cuesta al vendedor (07, 01)
- **Dónde.** Sección 2, viñeta "Ingreso diario sin ahorro", antes de "Devuelve en tercios".
- **Texto nuevo (se agrega).** "Ese día, cubrir el fiado con un gota a gota a 20% le costaría de 16% a 32% de lo que gana (unos $38.600 diarios [R2, C. 24]; cálculo propio)."
- **Por qué.** Sale de v2 ("Para el vendedor"): $6.000 a $12.400 sobre $38.600. Sin esto, el cuerpo no dice cuánto gana el usuario.

### 2. Devolver la lectura literal del 1,8% (07, 08)
- **Dónde.** Sección 2, "Usuario y alcance".
- **Reemplaza.** `[R2, C. 18.1], quizá porque nadie llama "crédito" a la mercancía del día. Por eso lo primero es contar:`
- **Por.** `[R2, C. 18.1]. Leído literal, en Cali serían unos 50 (17.745 × 15,4% que pide crédito [R2, C. 16.1] × 1,8%; cálculo propio), frente a los 904 del equilibrio. La otra lectura es que nadie llama "crédito" a la mercancía del día. Por eso lo primero es contar:`
- **Por qué.** Un evaluador duro va directo a ese 1,8%. En v2 el dato en contra quedaba a la vista; hoy parece que se lo explica para no enfrentarlo.

### 3. Que la ventana de cierre sea coherente con los sextos (02)
- **Tabla 2, primera celda de la fila.** Cambiar "Días de venta 1 a 5." por "Días de venta 1 a 3, más 2 de margen."
- **Reglas y límites.** Cambiar "Lo primero que pruebo es pagar en sextos, unos $7.800 diarios (cálculo propio)." por "Lo primero que pruebo es pagar en sextos, unos $7.800 diarios, y el puente cierra en 8 días de venta, no en 5 (cálculo propio)."
- **Cómo sé si me equivoqué.** Cambiar "90% de los puentes cierra a tiempo y" por "90% de los puentes cierra a tiempo (5 días de venta, u 8 con sextos) y".
- **Por qué.** Es el mismo choque que se arregló en v2. Hoy, con sextos, todos los puentes de la prueba saldrían "sin cerrar".

### 4. Devolver la frase que hace original el mecanismo (03)
- **Dónde.** Sección 2, viñeta "El problema ya tiene soluciones", después de "no encontré esa lógica en el fiado (búsqueda limitada)."
- **Texto nuevo (se agrega).** "Aquí el plazo normal sigue en cero días y solo lo abre un dato público, no una solicitud del deudor."

### 5. Trazar "sin RUT" a su dato (06)
- **Dónde.** Tabla 2, fila "Semana 1".
- **Reemplaza.** "Al vendedor no se le pide cédula, RUT ni celular"
- **Por.** "Al vendedor no se le pide cédula, RUT ni celular (93,3% no tiene RUT [R2, C. 13])"

### 6. Nombrar sin rodeos el riesgo de la copia (08)
- **Dónde.** Sección 4, "El riesgo real tiene tres capas".
- **Reemplaza.** "Tercera, que la regla se copie: no cobro el dato, sino la regla fijada de antemano, el registro y el acuerdo con el mayorista."
- **Por.** "Tercera, que la regla se copie: tras el mes gratis, el minorista puede usarla sin pagarme. Cobro la regla fijada de antemano, el registro y el acuerdo con el mayorista; si la siguen usando sin pagar, la tarifa no cierra."

## Recortes que pagan los arreglos

Ninguno quita una cita única ni cambia la numeración de las referencias.

- **A.** Reglas y límites: quitar "Nunca hay recargo para el vendedor, porque se parecería a un seguro sin licencia." Ya lo dice la viñeta "No soy entidad financiera" (no hay prima, así que no es seguro).
- **B.** Por qué falla el formal: quitar "La informante sí nombra los requisitos [Inf], así que las dos cosas se mezclan." El 14,6% por requisitos se queda, y la cita está en el Anexo C.
- **C.** Qué hace bien el informal: cambiar `su sanción es la exclusión: "que no vuelva por acá" [R10]` por `su sanción es la exclusión [R10]`.
- **D.** Tabla 2, fila "Día de lluvia": cambiar `WhatsApp al minorista: "Hoy es día de lluvia (Univalle, 6 mm a las 2:30 p. m.). Rige la cláusula."` por `WhatsApp al minorista ("Rige la cláusula", Anexo B).` El texto completo está en las maquetas del Anexo B.
- **E.** Título de la Tabla 3: cambiar "(cálculo propio; la hoja del Anexo B las reproduce)" por "(cálculo propio, Anexo B)".
- **F.** Lo que encontré en campo: quitar "Nadie contactó prestamistas." Está en el Anexo C.
- **G.** Consecuencias: cambiar `una vendedora de comida no pudo pagar tras un choque económico y familiar y "ni volvió a sacar el negocio"` por `una vendedora de comida "ni volvió a sacar el negocio"`.

## Pérdidas que acepto (no valen el espacio)

- El aviso que llega tarde (1,5 horas de rezago de la API) y la regla de la estación sin dato. Son buenas respuestas para la entrevista, pero no hay espacio.
- "Dos cosas no cuadran" completo, "Por qué la lluvia" (vacaciones y paros) y el techo por estaciones del IDEAM.
- En el Descarte 2: cubrir solo $15.000 cuesta $4.000 diarios (10%) y la póliza pide cédula.
- La Figura 1 y "Otras siete opciones" (Anexo H). La Tabla 2 cubre la figura.

Después de aplicar los cambios: correr `uv run --with pypdf python report/docs/fit.py --strict`, confirmar PASS y pegar en Docs. En Docs, revisar que la sección 4 termine en la página 5 antes de "ANEXOS".
