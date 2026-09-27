# Análisis del caso: qué nos están pidiendo de verdad

Lectura propia del reto (`01-builder-case.md`) cruzada con la rúbrica (`02-criterios-evaluacion.md`).
Todo lo marcado como **hipótesis** está por verificar con fuentes o con entrevistas. Nada de este archivo es todavía un hallazgo.

## 1. Lo no negociable (descalifica si falla)

- [ ] Archivo: `MAKERS_SANTIAGO_ESPINOSA_CALI.pdf`.
- [ ] Máximo **5 páginas** sin contar anexos. Prototipo, tablas largas, guía de entrevistas y bibliografía extendida van a anexos.
- [ ] Fuentes verificables, con link. Preferir primarias (DANE, Banca de las Oportunidades, SFC, Banco de la República, Banco Mundial, papers con metodología).
- [ ] Fecha: trabajar contra **domingo 27 sep 2026, 12:00 PM hora Colombia** (el contador de la plataforma dice 29/09 15:26, pero el documento oficial dice 27; usar la más estricta).
- [ ] Reglas de campo: **no contactar prestamistas informales**; no grabar ni fotografiar sin permiso explícito.
- [ ] Una vez enviado no se puede modificar.

## 2. Cómo se reparte el puntaje (y dónde conviene invertir tiempo)

El Bloque 1 dice explícitamente "lo que más importa". Traducido a decisiones:

| Criterio | Lo que implica en la práctica |
|----------|-------------------------------|
| 01 Efectividad | Un solo mecanismo que resuelva a la vez: operar sin licencia, flujo de caja diario sin ahorro, y confianza hacia un desconocido de 22 años. Si hay tres "features" para tres problemas, pierde puntos. Además debe atacar la causa raíz, no el síntoma "tasa alta". |
| 02 Especificidad | Paso a paso: **quién hace qué, cuándo y con qué**. Día 1, día 2, día 30. Qué hace el usuario, qué hace el aliado, qué hacemos nosotros, dónde está la plata en cada momento. |
| 03 Creatividad | El mecanismo no puede existir ya en el mercado ni ser la primera respuesta de una IA. **Cambiarle el nombre no cuenta.** |
| 04 Diagnóstico | Tesis propia de por qué falla el formal y qué hace bien el informal. No un resumen de reportes. |
| 05 Fuentes | Pocas y primarias. Cinco rastreables valen más que quince blogs. |
| 06 Trazabilidad | Cada rasgo de la propuesta amarrado a un hallazgo concreto (dato o entrevista). Conviene una tabla "hallazgo → decisión de diseño". |
| 07 Juicio cuantitativo | Números con supuesto a la vista. Si el modelo no cierra, decirlo y explicar por qué. Incluir tasa de no pago si se mueve dinero. |
| 08 Descartes y autocrítica | Dos alternativas reales con razones específicas, y nombrar el riesgo real de la propia propuesta. |

## 3. La advertencia más importante del documento

> "Vamos a recibir más de cien propuestas... sabemos, con bastante precisión, cómo serán muchas de ellas... Con los mismos insumos, es fácil terminar en las mismas conclusiones."

Esto es una lista implícita de lo que **no** va a puntuar en creatividad. Respuestas predecibles (lo que sale en la primera respuesta de cualquier IA):

1. App de **scoring alternativo** con datos de ventas, celular o redes para que un banco preste.
2. **Marketplace** que conecta micronegocios con bancos o fintechs.
3. App o bot de **microcréditos por WhatsApp** en alianza con una entidad vigilada ("gota a gota digital y barato").
4. Digitalizar **natilleras, cadenas o tandas** (ROSCAs) con una app.
5. **Educación financiera** gamificada.
6. **Crédito de proveedor / BNPL para inventario** vía plataformas B2B.
7. **Préstamos grupales** tipo Grameen con garantía solidaria.
8. **Ahorro programado** diario antes de dar crédito ("primero ahorra, después te presto").
9. **Cuaderno de fiado digital** para generar historial.
10. Adelanto sobre ventas con datáfono o QR (merchant cash advance).

Ninguna es mala por sí sola, pero casi todas ya existen (Tul, Chiper, Treinta, Aflore, Nequi, Addi, Mercado Pago, Tala, Kueski, Yape, microfinancieras, programas del gobierno). Si terminamos en una de ellas, el diferencial tiene que venir de **un hallazgo que los demás no tienen**, y ese hallazgo tiene que cambiar el mecanismo, no solo el nombre.

## 4. Reformular el problema (hipótesis a probar)

El enunciado empuja a pensar "el problema es la tasa". Hipótesis de trabajo para no caer ahí:

**H1. El gota a gota no vende crédito; vende otras cosas que el banco no vende.** Candidatos:
- Velocidad (plata el mismo día, sin papeles).
- **Cobro diario en persona**: cuota pequeña que calza con ingreso diario y funciona como dispositivo de compromiso (alguien viene, no hay que acordarse ni ir a ningún lado).
- Precio expresado en pesos por día ("mil pesos diarios"), no en tasa. La tasa no es la variable con la que decide.
- Renovación fácil: línea de liquidez recurrente, no un crédito puntual.
- No reporta a centrales de riesgo ni exige historial.
- Relación personal y flexibilidad (a veces).
- Enforcement por miedo y violencia: el lado oscuro, y la razón por la que el formal no lo puede copiar.

**H2. El formal no falla por falta de interés sino por economía unitaria.** Originar, verificar y cobrar un crédito de montos muy pequeños cuesta casi lo mismo que uno grande, y con tope de usura el margen no alcanza. Además el calendario mensual no calza con ingresos diarios. Verificar: costo de originación de microfinancieras, tasa de usura vigente para microcrédito y consumo de bajo monto.

**H3. "Bancarizar" no es el cuello de botella.** Colombia tiene indicadores altos de tenencia de productos financieros (verificar cifra de Banca de las Oportunidades), pero bajo uso de crédito formal por micronegocios. Si la gente ya tiene Nequi o Daviplata y aun así usa gota a gota, el problema no es la cuenta.

**H4. Parte del uso no es para el negocio.** Emergencias del hogar, pagar otra deuda, temporadas (enero, temporada escolar, diciembre). Si la necesidad es liquidez de emergencia y no capital de trabajo, la solución cambia.

**H5. El micronegocio también es prestamista.** El tendero fía a sus clientes (cuaderno de fiado). Parte de su hueco de caja puede venir de la plata que tiene prestada a vecinos. Verificar cuánto pesa el fiado en las ventas.

**H6. La confianza no se construye, se toma prestada.** Un joven de 22 años no gana la confianza de un tendero de 15 años con una app. Pero el tendero ya confía en alguien que lo visita con frecuencia (preventista de Bavaria/Postobón/Nutresa, distribuidor, corresponsal bancario, junta de acción comunal, cooperativa, parroquia). Además hay una desconfianza específica hacia apps de préstamo por las apps extorsivas ("montadeudas" en México, casos en Colombia). Verificar.

**H7. Hay segmentos que el formal no puede atender por documentación**, por ejemplo migrantes venezolanos con o sin PPT. Podrían ser el segmento más expuesto al gota a gota. Verificar tamaño y uso.

## 5. Las cuatro restricciones como un solo mecanismo

La rúbrica pide que un mismo mecanismo resuelva las restricciones. Preguntas guía para evaluar cualquier idea candidata:

1. **Licencia:** ¿quién pone la plata y quién asume el riesgo? Si no somos entidad vigilada: ¿originamos para una vigilada, operamos como corresponsal, usamos crowdfunding regulado, sandbox de la SFC, cooperativa, o el modelo no mueve crédito (ahorro, inventario, cuentas por cobrar)? ¿Qué pasa el día 1, sin ninguna licencia?
2. **Flujo diario:** ¿la cuota o el aporte se mueve al ritmo de las ventas del día? ¿Qué pasa en un día malo? ¿Funciona sin ahorro previo?
3. **Confianza:** ¿a través de quién llega el producto? ¿Por qué el usuario le cree a ese canal, y por qué ese canal nos cree a nosotros?
4. **Ya existen soluciones:** ¿qué parte del problema dejan sin resolver las existentes y por qué?

Si una idea necesita tres piezas distintas para responder las tres primeras, es señal de que el mecanismo no es el correcto.

## 6. Preguntas que la investigación tiene que responder

Tamaño y consecuencias:
- ¿Cuántos micronegocios hay en Colombia (y LatAm)? ¿Cuántos piden crédito, a quién, por cuánto, para qué? (DANE EMICRON, módulo de financiamiento).
- ¿Cuántas personas usan gota a gota? ¿Monto típico, plazo, tasa efectiva, frecuencia de renovación?
- Consecuencias: sobreendeudamiento, violencia, extorsión, economía criminal, efecto en crecimiento del negocio, salud mental.

Formal:
- ¿Qué intentos formales hubo (Banca de las Oportunidades, CREO / Crédito Popular, Banco de los Pobres en Medellín, microfinancieras, Nequi, Daviplata, Tandas para el Bienestar en México, Mibanco y Yape en Perú)? ¿Qué resultados tuvieron, con cifras?
- ¿Cuánto cuesta originar y cobrar un microcrédito? ¿Cuál es la tasa de usura vigente por modalidad?

Informal:
- ¿Cómo funciona operativamente el gota a gota (montos, plazos, cobro, renovación, garantías sociales, violencia)? Solo con fuentes secundarias: prensa investigativa, estudios académicos, Policía, Fiscalía.
- Evidencia académica sobre frecuencia de pago, trampas de deuda, sesgo al presente, ahorro de compromiso, ROSCAs, recolectores diarios de ahorro (susu en Ghana).

Mercado y regulación:
- ¿Qué fintechs y empresas atacaron este segmento, qué funcionó, qué murió y por qué?
- ¿Qué estructuras legales permiten operar en Colombia sin ser entidad vigilada?

## 7. Trabajo de campo (lo pide el diagnóstico)

Hablar con personas que viven el problema. Reglas: no contactar prestamistas; consentimiento explícito; no grabar sin permiso; no pedir datos personales innecesarios.

A quién (en este orden de prioridad):
1. Tenderos de barrio (la persona "de 15 años detrás de un mostrador").
2. Vendedores ambulantes y de plaza de mercado (ingreso más diario y volátil).
3. Peluquerías, talleres, misceláneas.
4. Personas alrededor del ecosistema: preventista o repartidor de una distribuidora, corresponsal bancario, asesor de una microfinanciera, líder de junta de acción comunal.

Principios (estilo "The Mom Test"): preguntar por el pasado concreto, no por intenciones futuras. Nunca "¿usaría usted esta app?".

Preguntas base:
- Cuénteme de la última vez que necesitó plata para el negocio o para la casa. ¿Qué pasó? ¿Cuánto? ¿Para qué? ¿Cuánto tardó en conseguirla?
- ¿Cómo maneja la plata de un día normal? ¿Separa la del negocio y la de la casa? ¿Dónde la guarda?
- ¿Qué pasa en un día malo de ventas?
- ¿Cómo le paga a sus proveedores? ¿Le dan plazo? ¿Quién lo visita y cada cuánto?
- ¿Usted fía? ¿Cuánto tiene fiado hoy, más o menos? ¿Le pagan?
- ¿Ha intentado sacar un crédito en un banco, cooperativa o app? ¿Qué pasó?
- ¿Conoce a alguien que haya usado "préstamos diarios"? ¿Por qué cree que la gente los usa? (Preguntar en tercera persona reduce la vergüenza y el riesgo.)
- ¿En quién confía para temas de plata? ¿Por qué?
- ¿Tiene Nequi, Daviplata u otra cuenta? ¿Para qué la usa? ¿Le pagan por QR?

Registrar en una tabla: fecha, tipo de negocio, barrio o zona (sin datos personales), citas textuales, hallazgo, qué hipótesis confirma o refuta.

## 8. Estructura sugerida del PDF (5 páginas)

| Página | Contenido |
|--------|-----------|
| 1 | Diagnóstico: tamaño, consecuencias, tesis propia de por qué falla el formal y qué hace bien el informal. |
| 2 | Hallazgos de campo y el punto ciego que encontramos; tabla hallazgo → decisión de diseño. |
| 3 | La propuesta: usuario exacto, mecanismo paso a paso (quién, qué, cuándo, con qué), cómo resuelve las 4 restricciones con un mismo mecanismo, estructura legal, soluciones similares y qué aprendimos de ellas. |
| 4 | Números: inversión inicial, costos mensuales, margen por usuario (con no pago), usuarios mes 3/6/12, break-even, necesidad total de caja y de dónde sale. Cada número con su supuesto. |
| 5 | Dos alternativas descartadas con criterio, riesgo principal de la propuesta y cómo lo mitigamos. Fuentes principales. |
| Anexos | Prototipo (qué hace, qué no, tiempo, herramientas, feedback), guía y tabla de entrevistas, modelo financiero, bibliografía completa. |

## 9. Siguientes pasos

1. Correr la investigación con `../prompt.md` en varios agentes (y el workflow que deja resultados en `research/`).
2. Salir a hacer entrevistas en paralelo; son la fuente del hallazgo diferencial.
3. Consolidar hallazgos en `research/00-sintesis.md` y elegir la tesis.
4. Definir mecanismo, números y descartes.
5. Prototipo mínimo (bot de WhatsApp u hoja de cálculo del mecanismo central) y mostrárselo a al menos un entrevistado.
6. Maquetar el PDF, revisar el checklist de la sección 1, entregar.
