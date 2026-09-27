# Revisión con la rúbrica, ronda 1

Revisado: `report/MAKERS_SANTIAGO_ESPINOSA_CALI.pdf` (15 páginas: cuerpo de 5, "ANEXOS" abre la página 6), `report/informe.html` y `report/brief-final.md`. Punto de vista: evaluador del Makers Fellowship que ya leyó más de cien propuestas de este caso.

## Chequeo de entrega (descalifica si falla)

| Regla | Estado |
|---|---|
| Nombre exacto `MAKERS_SANTIAGO_ESPINOSA_CALI.pdf` | Cumple |
| Cuerpo de 5 páginas o menos; anexos después | Cumple (páginas 1 a 5; "ANEXOS" en la página 6) |
| Fuentes verificables | Cumple: 37 referencias con URL y cuadro o página |
| Raya y semirraya | 0 en el PDF y 0 en el HTML; no hay guion con espacios |
| Nombres, parentesco, tercera ronda, contacto con prestamistas | No aparecen |

Nada descalifica. El cuerpo tiene unas 4.500 palabras en 5 páginas: se lee, pero es denso. Cada recorte ayuda.

## Puntaje (1 a 5)

| # | Criterio | Puntaje | Justificación en una línea |
|---|---|---|---|
| 01 | Efectividad | 3 | Una sola pieza toca los cuatro puntos con elegancia, pero la premisa (el minorista exige el mismo día) no está confirmada, el día de lluvia el vendedor igual se va a la casa con $0 y el mecanismo cubre unos 26 días al año mientras los choques grandes (enfermedad, familia, vacaciones) quedan fuera. |
| 02 | Especificidad | 4 | La Tabla 2 dice quién, qué, cuándo, con qué y dónde está la plata; faltan la tarde de la lluvia tardía (el aviso llega a las 8:30 p. m. y el vendedor paga antes), el tope de 3 frente a 2 y cómo llego al primer minorista. |
| 03 | Creatividad | 4 | Contra la pila de apps de préstamo, tenderos-agente y cuadernos digitales, un aplazamiento del fiado disparado por un dato público y pagado por el acreedor es distinto; no llega a 5 porque no nombra los precedentes de cláusulas atadas a un índice y no hizo la prueba de las IA. |
| 04 | Diagnóstico | 4 | Tesis propia y refutable ("vende plata a meses a alguien a quien le faltan uno o dos días"), con cálculo propio contra el precio; pero la frase de tesis generaliza a todo el gota a gota desde un resumen oral sobre carritos de una estación. |
| 05 | Fuentes | 4 | Casi todo con cuadro o página y primario; restan la lectura floja de Casaburi y Willis, AB InBev como prueba para carritos y que el hallazgo central sea de segunda mano. |
| 06 | Trazabilidad | 4 | La Tabla 1 y el Anexo J son lo mejor del documento; quedan sin hallazgo el minorista como pagador, la tarifa de $4.000 y que la lluvia (y no otro choque) sea el disparador correcto. |
| 07 | Juicio cuantitativo | 4 | Supuestos a la vista, caso conservador que no cierra y dicho; pero el cuerpo esquiva que el propio DANE sugiere unos 50 ambulantes con crédito de proveedor en Cali, frente a los 904 del equilibrio. |
| 08 | Descartes y autocrítica | 4 | A y F son opciones reales descartadas con números propios y el riesgo va en dos capas; falta el riesgo de negocio más obvio (la regla se copia gratis) y sobra citar mis propios puntajes de IA como razón. |
| | **Total** | **31 de 40** | |

Con los arreglos 1 a 5, 01 puede subir a 4 y el total quedar en 32 a 33. Ninguno pide nuevo trabajo de campo.

## Lo que hay que arreglar (de más a menos grave)

### 1. El DANE dice que el universo puede ser diminuto y el cuerpo lo esquiva
- **Dónde.** Página 3: "El DANE casi no lo ve: solo 1,8% de los ambulantes que pidieron crédito se lo pidió a un proveedor [R4, C. 18.1], probablemente porque nadie llama 'crédito' a la mercancía del día. El equilibrio pide 904 vendedores, 5,1% de los ambulantes de Cali A.M. si todos sacaran fiado."
- **Por qué cuesta.** Un evaluador hace la cuenta en 10 segundos: 17.745 × 15,4% × 1,8% ≈ 50 ambulantes en Cali con crédito de proveedor. Contra 904 del equilibrio, parece que el mercado no existe. "Probablemente" explica el dato sin ponerlo a prueba y lo lee a favor. Pega en 07 (números que tengan sentido para este contexto) y en 08.
- **Reescritura.** "El DANE casi no lo ve: solo 1,8% de los ambulantes que pidieron crédito se lo pidió a un proveedor [R4, C. 18.1]. Tomado literal, en Cali serían unos 50 ambulantes (17.745 × 15,4% × 1,8%, cálculo propio) y este negocio no existiría. Hay otra lectura: nadie llama 'crédito' a la mercancía del día, y el fiado de mañana a tarde sí aparece en WIEGO [R23]. No sé cuál es la correcta. Por eso lo primero que hago es contar, con los minoristas de la estación Universidades, cuántos carritos sacan fiado diario; si en los 5 primeros minoristas no llego a 40 vendedores, el modelo no cierra y lo digo." Llevar ese umbral también a "Cómo sé si me equivoqué".

### 2. El día de lluvia el vendedor se va a la casa con $0
- **Dónde.** Anexo A, fila del día 5 (y 13, 14): "Cláusula: paga al que fía $30.180 ... queda para la casa $0". Supuesto "Parte de lo vendido el día de lluvia que abona a su deuda 100%". En el cuerpo: "lo que el vendedor no alcanzó a pagar de su fiado ese día se paga en tercios".
- **Por qué cuesta.** El punto 2 del caso es "ingreso diario, sin ahorro". Con la regla tal como está, el día sin ventas el vendedor le entrega todo al minorista y no lleva nada para comer, que es exactamente cuando se pide (el propio PDF cita que 28,9% del crédito del ambulante va a gasto personal [R4, C. 21.1]). El brief decía "la cláusula deja lo poco que se vendió para la casa"; el prototipo hace lo contrario. Un evaluador que lea la tabla del anexo lo ve y concluye que el gota a gota sigue entrando esa misma tarde, ahora por la comida. Pega en 01 y 07.
- **Reescritura (regla, página 3 y Tabla 2).** "El día de lluvia, el vendedor se queda con lo que vendió hasta $15.000 [S] para la casa; lo que pase de ahí abona al fiado, y el resto se paga en tercios en los 3 días de venta siguientes." Rehacer el Anexo A con ese piso (en el ejemplo de $62.000, el aplazado sube de $31.820 a unos $46.800 y cada tercio a unos $15.600, 40% del ingreso de un día; decirlo) y actualizar E.3, que ya supone todo el fiado aplazado, así que el costo para quien fía casi no cambia. Si no hay tiempo para rehacer el prototipo, al menos decirlo en "Lo que no cubre": "Ese día el vendedor no lleva nada a la casa: si la plata del gota a gota era para comer, la cláusula no la reemplaza."

### 3. Falta el riesgo de negocio más obvio: la regla se copia gratis y la lluvia la ve cualquiera
- **Dónde.** Página 4, punto 3: "les doy una razón externa para esperar sin tener que juzgar si el vendedor miente". Página 5, "El riesgo real tiene dos capas".
- **Por qué cuesta.** El minorista está en la misma calle y ve que llovió. Después del mes gratis ya conoce la regla y puede aplicarla sin pagar $4.000 por vendedor. La segunda capa de riesgo habla de quién carga el plazo, no de por qué alguien me pagaría a mí. Un evaluador de viabilidad pregunta eso primero. Además, la lluvia no le dice al minorista si el vendedor miente sobre cuánto vendió, así que el argumento de "razón externa" se cae si no se reformula. Pega en 07 y 08.
- **Reescritura (agregar como tercera capa, 3 líneas).** "La tercera es que la regla se copia. La lluvia la ve cualquiera, y después del mes gratis el minorista puede aplicarla sin mí. Lo que cobro no es el dato: es la regla fijada antes del día, que evita negociar caso por caso y que el vendedor 'quede mal', el registro de quién tiene un puente abierto y quién dejó de ser elegible, y el acuerdo con el mayorista que corre el pago del minorista. Si en el mes 3 un minorista sigue usando la regla y deja de pagar, eso me dice que el producto es la regla y no el servicio, y el modelo de tarifa no cierra." En el punto 3 de la página 4, cambiar "sin tener que juzgar si el vendedor miente" por "sin tener que decidir caso por caso si le cree".

### 4. La tesis generaliza a todo el gota a gota desde un resumen oral sobre carritos
- **Dónde.** Primera frase del PDF: "Mi tesis: el gota a gota no le gana al sistema formal por precio, y los requisitos explican solo una parte. Le gana la tarde en que un día sin ventas rompe el crédito que el vendedor ya tiene".
- **Por qué cuesta.** La evidencia de esa tarde es un resumen oral de un colaborador sobre vendedores de una estación, sin conteo. Los casos de la informante empiezan por "la necesidad o porque van a poner un negocio" y por choques familiares, y el PDF mismo deja fuera a la vendedora de arepas. Una tesis universal apoyada en un caso de segunda mano es lo que el evaluador marca como sobreventa. Pega en 04 y 01.
- **Reescritura.** "Mi tesis: para el vendedor que vive del fiado diario, el gota a gota no le gana al formal por precio, y los requisitos explican solo una parte. Le gana la tarde en que un día sin ventas rompe el crédito que ya tiene, el fiado sin interés de su minorista. El formal no compite ahí porque vende plata a meses a alguien a quien le faltan uno o dos días. No es la única puerta al gota a gota (la necesidad del hogar y los choques familiares también lo son), pero es la que un tercero puede cerrar sin prestar."

### 5. No explica por qué la lluvia y no el choque más grande de esos carritos
- **Dónde.** Página 3, "Lo que no cubre. Enfermedad, choques familiares, vacaciones universitarias o paros".
- **Por qué cuesta.** Los carritos están en una estación que se llama Universidades: su caída de ventas más grande probablemente es el calendario académico, no 26 días de lluvia. Y el propio R27 que el PDF cita dice que 44% de los que usaron el pase en Barranquilla y Cartagena lo usaron por calamidad personal o familiar. Sin una razón, el disparador parece elegido porque hay datos, no porque sea el choque que importa. Pega en 01 y 06.
- **Reescritura (2 líneas antes de "Lo que no cubre").** "Por qué la lluvia. Las vacaciones y los paros se ven venir: ese día el vendedor no saca fiado o saca menos. La lluvia llega después de que ya sacó la mercancía, y deja una deuda de hoy que no puede pagar hoy. Ese es el momento que describió el colaborador. Enfermedad y choques familiares también llegan así, pero no tienen un dato público que nadie pueda discutir, y en Colombia la flexibilidad pedida por el deudor subió el impago [R27]; por eso quedan fuera."

### 6. La tarde de la lluvia tardía y dos reglas que no cuadran
- **Dónde.** Tabla 2, "Si llueve tarde, el aviso sale hacia las 8:30 p. m. con el día completo" y "Si no cierra en 5 días de venta". Reglas: "Tope de 3 días de disparo seguidos y de 2 fiados aplazados por vendedor [S]".
- **Por qué cuesta.** La tesis dice que el gota a gota llega "esa misma tarde". Si llueve a las 4 p. m., el dato se publica hacia las 5:30 y el vendedor paga antes: esa tarde no sabe si está cubierto y el gota a gota sigue siendo la salida segura. Y "3 días seguidos" con "2 fiados aplazados" se contradicen: en el tercer día de lluvia seguida, ¿rige o no? Pega en 02.
- **Reescritura (Tabla 2, fila "Día de lluvia", y Reglas).** Agregar fila: "Tarde de un día con lluvia, antes del aviso | Vendedor y minorista | Si el vendedor no alcanza, el minorista anota el saldo y nadie decide esa tarde. Si el aviso de las 8:30 p. m. confirma 5 mm, el saldo va en tercios; si no, se paga completo al otro día, como hoy | Cuaderno del minorista | La deuda sigue con él". Reglas: "Un vendedor puede tener como máximo 2 días aplazados abiertos a la vez [S]; un tercer día de lluvia seguido se paga como hoy. En 12 meses no hubo rachas de tres [R12]." Y alinear "5 días de venta" con los tercios: "si a los 5 días de venta (3 de tercios más 2 de margen) no se cerró".

### 7. El punto 3 (desconocido de 22 años) no dice cómo llego al primer minorista
- **Dónde.** Tabla 2, semana 1: "Le propongo la cláusula a un minorista que fía a carritos cerca de la estación Universidades". Página 4, punto 3.
- **Por qué cuesta.** El caso pregunta "¿por qué confiaría en ti?". El PDF responde bien del lado del vendedor, pero con el minorista solo ofrece "el primer mes es gratis". No dice quién me presenta. Pega en 01 y 02.
- **Reescritura (Tabla 2, semana 1).** "Llego por los vendedores con los que conversó el colaborador: les pregunto a quién le sacan fiado y voy con uno de ellos. Le propongo la cláusula al minorista con la tabla de lluvia del último año de su calle (Anexo F) y el primer mes gratis." Punto 3, una frase: "No llego en frío: llego con un vendedor que ya le compra."

### 8. Citar mis propios puntajes de IA como argumento
- **Dónde.** Página 5, Descarte 1: "Parecía buena porque fue mi mejor opción antes del campo (27 de 40 en mi revisión adversarial con la rúbrica)". Anexo C: "Puntuó A 27, C 23, B 21 y D 15"; "puntuó la primera versión de la cláusula (27 de 40)". Anexo H, columna "Puntaje".
- **Por qué cuesta.** Que un agente de IA me haya puntuado con la rúbrica del jurado no es una razón por la que A parecía buena, y en el cuerpo se lee como jugar con la rúbrica. Es la frase del documento que más suena a proceso de IA. Pega en 08.
- **Reescritura.** Descarte 1: "Parecía buena porque iba al usuario con más gota a gota, copiaba lo que el informal hace bien (cuota diaria, renovación como premio, recomendación) y no necesitaba visitas de cobro." Quitar el número. En el Anexo C dejar la revisión adversarial como método, sin puntajes, o con una línea: "la usé para encontrar huecos, no como nota". Quitar la columna "Puntaje" del Anexo H o renombrarla "orden en mi revisión".

### 9. Dos fuentes que no dicen lo que el texto les hace decir
- **Dónde.** Página 4: "mover el pago en el tiempo pesa más que indemnizar (72% frente a 5% de adopción [R28])" y Anexo J, "El problema del seguro es el momento del pago [R28] | Mover el pago en el tiempo en vez de indemnizar". Página 4: "el crédito atado a mercancía que rota se paga (AB InBev tiene 93,6% de sus cuentas por cobrar al día [R35])".
- **Por qué cuesta.** En Casaburi y Willis los dos brazos son seguro: lo que cambia es cuándo se paga la prima (descontada de la cosecha o por adelantado), no aplazar frente a indemnizar. Quien conozca el paper lo marca. AB InBev cobra a distribuidores y bares, no a carritos, así que 93,6% no dice nada de este usuario. Pega en 05.
- **Reescritura.** "cuando la prima se descuenta de la cosecha en vez de pagarse por adelantado, la adopción pasa de 5% a 72% [R28]: para el que no tiene ahorro pesa más cuándo paga que qué le cubren; por eso la devolución va en los días de venta." AB InBev: quitarlo del cuerpo y del Anexo J, o bajarlo a "en la cadena formal de bebidas el crédito comercial se paga (93,6% al día [R35]), aunque son distribuidores, no carritos". Si se quita, la fila del Anexo J pasa a "Impago bajo: supuesto que mide el piloto [S]".

### 10. Originalidad: nombrar el precedente más cercano y, si hay tiempo, hacer la prueba de las IA
- **Dónde.** Página 4: "No encontré a nadie que corra la fecha de un crédito que ya existe con un dato público (búsqueda limitada)" y "A qué se parece".
- **Por qué cuesta.** Existen cláusulas que suspenden pagos de deuda cuando un índice o un desastre medido pasa un umbral (deuda soberana con cláusula de huracán, algunos créditos agrícolas). Un evaluador que las conozca lee "no encontré a nadie" como que no se buscó, y la rúbrica pregunta por la primera respuesta de una IA. Nombrarlo antes que el evaluador convierte un riesgo en un punto a favor. Pega en 03.
- **Reescritura (una línea al final de "A qué se parece").** "La idea de suspender un pago cuando un índice público pasa un umbral existe en deuda de países y en crédito agrícola; no la encontré en el crédito de mercancía de un día entre comerciantes informales, sin financiador y pagada por quien fía." Solo si se hace antes de entregar: pegar el enunciado del caso más el hallazgo del colaborador en tres modelos, guardar la respuesta tal cual en el Anexo C y decir en una línea si alguno propuso el aplazamiento pagado por el acreedor. Si no se hace, no mencionarlo.

## Lo que ya está bien y no hay que tocar

- La Tabla 1 (hallazgo, respaldo, decisión) y el Anexo J: es la mejor trazabilidad que he visto en este caso.
- "Dos cosas no cuadran" y los umbrales fijados antes de oír las respuestas: autocrítica real.
- El cálculo propio de lluvia del IDEAM con huecos y rezago declarados.
- La honestidad sobre el campo (colaborador, informante, sin conteo, nadie contactó prestamistas).
- "¿Cierra?" dicho de frente, con el caso conservador que no cierra en 60 meses.
- El descarte F con primas propias y la frase "las pérdidas pequeñas y frecuentes se suavizan con plazo; se aseguran las raras".
