# Brief del informe, ángulo "campo primero"

Arquitecto: campo primero. Fecha: 27 sep 2026, 02:30. Base: rúbrica (docs/02), reto de la plataforma (docs/00, cuatro puntos), síntesis 00 completa (secciones 1 a 11.6; la 11.7 no existe todavía), frentes 12a y 12b, docs 06, 07 y 09, y los tres scripts de `models/`. El archivo `12-mecanismos-dia-malo.md` no existía al escribir esto; E y F se tomaron de `models/bad_day_mechanisms.py` y de 12b.

Regla de lectura para quien redacte: todo número de este brief trae su fuente y su confianza. Los marcados **[NUEVO]** los saqué en esta sesión directamente del anexo del DANE (archivo `anex-EMICRON-24Ciudades-2025.xlsx` del scratchpad, script `bycity.py`); son lectura directa de fuente primaria, pero no están todavía en la síntesis: hay que copiarlos al anexo de método con cuadro y CV antes de usarlos.

---

## 1. Tesis del informe (una frase)

**El vendedor de carrito no necesita más crédito, porque ya tiene uno diario y sin interés, el fiado de mercancía de su minorista; lo que le falta es una regla que distinga un día de lluvia de un mal pagador, y en ese hueco entra el gota a gota, que vende un día de plazo al 20% y se cobra primero porque amenaza, mientras el sistema formal le ofrece plata a meses a alguien a quien le falta un día.**

Versión corta para el título de la página 1: "Al vendedor no le falta crédito. Le falta un día de plazo cuando llueve."

Qué la sostiene y qué la refutaría (para el texto):
- Sostiene: campo (fiado diario, lluvia, gota a gota circular), Cali A.M. con más crédito de proveedores que gota a gota [NUEVO, ver sección 3], la sanción del fiado es la exclusión (Martínez Benavides 2021), 18 de 20 episodios de lluvia fuerte en 2025 duraron un solo día (12b, cálculo propio IDEAM).
- Refutaría: que en campo el minorista ya espere sin problema cuando llueve (entonces el hueco no existe), o que el gota a gota se tome sobre todo para otras cosas (hogar, otra deuda) y no para no perder el fiado.

---

## 2. Mecanismo elegido

### 2.1 Cuál

**E refinado: "La regla del día de lluvia".** Un disparador público (lluvia medida por el IDEAM en horario de venta) mueve automáticamente la fecha de pago del fiado del día dentro de la cadena que ya fía, hasta 3 días secos, sin recargo. Nadie le presta plata al vendedor, nadie le vende un seguro. Nosotros ponemos el dato, la regla escrita y el registro por WhatsApp; el plazo lo carga el minorista (fase 1) y, cuando se sume, el mayorista (fase 2, el E1 del script). Encima, después de 8 semanas cumplidas, el vendedor gana un "comodín" al mes para un día malo que no sea lluvia (enfermedad, familia).

Refinamientos frente al E original, cada uno trazado a un hallazgo:
- **El minorista respalda, no cobra.** Él decide quién entra a la regla (su recomendación es la puerta), pero la regla, no él, decide cuándo se espera. Hallazgo: "le tuvo paciencia solamente porque era amiga mía" y "yo no le digo nada, dígale usted" (informante, doc 07, hallazgos 1 y 2).
- **La deuda aplazada viaja pegada al fiado, que ya es lo primero que se paga.** No competimos por un puesto en la fila de pagos con una amenaza. Hallazgo: al que amenaza se le paga primero y al formal se lo deja caer (doc 07, hallazgo 7, hipótesis); perder el fiado es perder el trabajo de mañana (Martínez Benavides 2021: "que no vuelva por acá").
- **Cero rastro formal.** No pide RUT, factura, Nequi ni cédula en foto; no reporta a centrales; nada viaja a la DIAN. Hallazgo: los vendedores no se formalizan por miedo a impuestos (doc 09, hallazgo 5); 93,3% de los ambulantes no tiene RUT (EMICRON ambulantes 2025, Cuadros 13 y 13.1; alta).
- **Disparador externo, no la palabra del deudor; flexibilidad solo con historial.** Hallazgo: en Barranquilla y Cartagena la flexibilidad a clientes nuevos subió el impago (Brune, Giné y Karlan 2025; alta); con un dato público nadie tiene que decidir "¿de verdad no vendió?".
- **Descartado E2** (prestarle nosotros el plazo al minorista): con 1% de impago del minorista el neto por vendedor es de -$14.537 al año y nos convierte en prestamista (`bad_day_mechanisms.py`, cálculo propio).

### 2.2 Por qué este y no los otros

- **A (ventanilla del tendero)** era el mejor de la síntesis (27 de 40), pero el campo le quitó la base: el nodo diario del vendedor de carrito no es el tendero del barrio sino el minorista que le fía la mercancía (doc 09, hallazgo 1). Además presta plata a precio legal con montos de ambulante y pierde de -$26.143 a +$5.857 por usuario al año (`unit_economics.py`), y un prestamista legal sin amenaza queda de último en la fila de pagos (doc 07, hallazgo 7).
- **C (cuota diaria de la deuda mensual)**: solo 22,5% de los ambulantes que piden crédito va a una entidad regulada (EMICRON ambulantes 2025, Cuadro 18.1; alta); casi no tienen cuota mensual que convertir. Nada del campo apunta a una cuota formal como origen.
- **F (día de lluvia pagado, seguro paramétrico)**: el evento es frecuente, así que la prima es casi un gasto fijo (sección 7).
- **E** ataca el momento exacto que el campo describe (el día en que el fiado se rompe), usa una relación de crédito que ya existe y no mueve plata nuestra.

### 2.3 Puntajes 1 a 5 (mi juicio de evaluador, sin indulgencia)

| Criterio | E refinado | A | C | F |
|---|---|---|---|---|
| 01 Efectividad (causa raíz, un mecanismo) | 4 | 2 | 2 | 2 |
| 02 Especificidad | 4 | 4 | 3 | 3 |
| 03 Creatividad | 4 | 2 | 3 | 3 |
| 04 Diagnóstico | 4 | 3 | 3 | 3 |
| 05 Fuentes | 3 | 4 | 3 | 3 |
| 06 Trazabilidad | 5 | 3 | 3 | 3 |
| 07 Juicio cuantitativo | 3 | 3 | 2 | 3 |
| 08 Descartes y autocrítica | 4 | 3 | 3 | 3 |
| **Total (de 40)** | **31** | **24** | **22** | **23** |

Por qué E no saca 5 en todo: la evidencia de campo es de segunda mano y de un resumen oral (05 baja a 3); no sé el tamaño del fiado de un carrito, ni el impago de lo aplazado, ni si el minorista puede esperar (07 en 3); no cubre choques que no sean lluvia salvo con el comodín (01 en 4). A baja frente a la síntesis porque el campo movió el nodo.

### 2.4 A cuál de las 10 respuestas predecibles se parece y qué la hace distinta

Se parece a la **6 (crédito de proveedor para inventario)** y a la **9 (cuaderno de fiado digital)**. Lo distinto está en el mecanismo, no en el nombre:
1. No crea ni amplía crédito de proveedor: el fiado ya existe y ya es gratis. Lo único que cambia es **cuándo vence**, y solo en días que un tercero neutral certifica.
2. No digitaliza el cuaderno para generar historial ni para que un banco preste; el registro existe solo para llevar lo aplazado.
3. No es seguro: no hay prima ni indemnización. Mueve tiempo, no plata (Casaburi y Willis 2018, AER: aplazar el pago valió más que el pago contingente; alta).
4. Resuelve el problema que hoy obliga al minorista a elegir entre excluir y perdonar: no puede verificar si el vendedor tuvo un día malo o le está mintiendo. El dato público quita esa discusión.
Ninguna de las 10 respuestas toca el día de lluvia ni el fiado que ya funciona. No se encontró en el mercado un producto colombiano que pague o aplace por lluvia a un comerciante urbano (12b, búsqueda limitada: ausencia de evidencia, no prueba). Precedentes cercanos en otro contexto: Tienda Pago (plazo a tiendas, sin disparador), seguros paramétricos agrícolas, BRAC con cuotas aplazables.

---

## 3. El usuario exacto

**Quién.** Vendedor de carrito estacionario (se para todos los días en el mismo punto de alto flujo) que cada mañana saca fiado, sin interés, la mercancía del día a un minorista y se la paga en la tarde. Opera como persona natural, sin RUT, en efectivo. Primer lugar: la estación Universidades del MIO, en el sur de Cali, donde se hicieron las conversaciones (doc 09).

**Cuántos (con fuente).**
- Cali A.M.: **17.745 micronegocios ambulantes** ("ambulante, sitio al descubierto"), de los cuales **9.752 estacionarios** y 7.993 móviles. DANE, EMICRON 24 ciudades 2025, Cuadros D.1_24C y D.5_24C (CV 8% y 10%). **[NUEVO]**
- Nacional (24 ciudades): 286.061 ambulantes; entre los que piden crédito, 61,8% va al gota a gota y 22,5% a una entidad regulada (EMICRON ambulantes 2025, Cuadros 18, 18.1 y 24; alta).
- Por qué Cali cuenta distinto: entre los micronegocios de Cali A.M. que pidieron crédito (35.496), el crédito de proveedores es 11,6% (4.105) y el gota a gota 8,8% (3.130; CV 18%). En el total de 24 ciudades es al revés: 3,0% frente a 35,6% (Cuadro H.4_24C). El 11,6% ya está en doc 09 (cálculo propio, CV 16,6%, precisión baja); el 8,8% es **[NUEVO]**. Lectura: en Cali el fiado de proveedor pesa más que el gota a gota, así que lo que hay que proteger es el fiado.
- Cuántos tienen fiado diario: **no se sabe**. Las encuestas casi no lo ven (solo 1,8% de los ambulantes dice haber pedido crédito a un proveedor, Cuadro 18.1, probablemente porque no llaman "crédito" a la mercancía fiada; 12a). Referencia externa: 38% de los ambulantes de cinco ciudades dice que el crédito del proveedor es "muy importante" (WIEGO, Roever 2014; alta, no es Colombia). Si se usa, rotularlo como supuesto: 30 a 40% de los 9.752 estacionarios, unos 2.900 a 3.900 en Cali.
- Qué NO decir: no inventar cuántos vendedores habló el colaborador; no decir que el usuario es "el tendero de 15 años".

---

## 4. El mecanismo paso a paso

### 4.1 Tabla (va en la página 3)

| Momento | Quién | Qué hace | Con qué | Dónde está la plata |
|---|---|---|---|---|
| Semana 0 | Yo | Constituyo la SAS, monto el bot de WhatsApp, conecto la lectura del IDEAM (estación 0026055120, Universidad del Valle, y de respaldo la 0026085170, Base Aérea) y consulto al abogado si una regla de aplazamiento atada al clima, pagada por el minorista, puede leerse como seguro | SAS, bot, API de datos.gov.co | Capital propio en la cuenta de la SAS |
| Semana 1 | Yo y un minorista que fía a carritos en Universidades (llego por los vendedores) | Firmamos una regla de una página: si el IDEAM marca 5 mm o más entre 7:00 y 18:59, el fiado no pagado ese día pasa a los siguientes días secos, hasta 3, sin recargo, y al otro día hay mercancía. El umbral se calibra con los días malos que él recuerde | Hoja impresa, conversación | Nada se mueve |
| Día 0 del vendedor | Minorista | Inscribe a los vendedores que él ya conoce y a quienes les fía hace varias semanas (él decide quién entra) | Mensaje al bot: nombre o apodo, teléfono si tiene, autorización de datos (Ley 1581) | Nada se mueve. Sin RUT, sin Nequi, sin cédula en foto |
| Cada mañana | Vendedor y minorista | Igual que hoy: saca la mercancía fiada; el minorista anota en su cuaderno | Mercancía | Inventario del minorista en el carrito |
| Cada tarde, día normal | Vendedor | Igual que hoy: paga el fiado en efectivo | Efectivo | Del bolsillo del vendedor a la caja del minorista |
| 7 p. m., día de lluvia | Bot | Lee el dato; si hay disparo, avisa al minorista y a sus vendedores: "Hoy fue día de lluvia en la zona. Lo que no alcanzó a pagar hoy se reparte en los próximos 3 días secos. Mañana hay mercancía." El minorista confirma cuánto quedó pendiente de cada uno | WhatsApp, tarjeta impresa con la regla | El pendiente queda como cuenta por cobrar del minorista. Nadie desembolsa |
| Días secos siguientes | Vendedor | Paga el fiado del día más un tercio de lo aplazado; el bot le muestra el saldo | Efectivo | Del vendedor al minorista |
| Si no se pone al día en 3 días secos | Minorista | Sale de la regla hasta que pague; el minorista aplica lo que ya aplica hoy. Nosotros nunca cobramos, nunca llamamos a nadie, nunca reportamos | Nada | Riesgo del minorista, igual que hoy con el fiado de cada mañana |
| Semana 8 en adelante | Vendedor con historial limpio | Gana un comodín al mes: un día malo que no es lluvia (enfermedad, familia), con la misma regla de 3 días | WhatsApp | Igual que el día de lluvia |
| Cada mes | Minorista (fase 1) o mayorista (fase 2) | Paga una cuota por vendedor activo en la regla | Bre-B o Nequi | Del minorista o mayorista a la SAS |
| Fase 2 | Mayorista que surte al minorista | En días de disparo, corre también un día el cobro al minorista (E1): el plazo sube hacia quien tiene más capital | Regla ampliada | Cuenta por cobrar del mayorista |

Casos borde que el texto tiene que nombrar (criterio 02): hueco del dato del IDEAM (en 2025 faltó cobertura diurna completa en 58 días; se usa la estación de respaldo y, si faltan ambas, el minorista marca el día y se revisa después); lluvia en la estación y no en el punto (riesgo de base; la estación queda en el campus de Meléndez, cerca de Universidades: verificar distancia con mapa antes de afirmarlo); vendedor que cambia de minorista (el historial es con el minorista, no se transfiere); lluvia de varios días (en 2025 ningún episodio pasó de 3 días; 12b).

### 4.2 Cómo UN mecanismo resuelve los cuatro puntos

El mecanismo es uno: **un dato público que mueve la fecha de pago de un crédito que ya existe entre comerciantes que ya se conocen.**
1. **No soy entidad financiera.** No presto, no capto, no aseguro. El aplazamiento es crédito comercial entre comerciantes, sin interés (no aplica usura), y ya existe hoy. No hay prima ni pago contingente de nuestra parte. Pregunta abierta al abogado (12b, pregunta 2): que el pago del minorista por el servicio no convierta la regla en actividad aseguradora; la respuesta segura es no cobrarle nunca al vendedor.
2. **Ingreso diario sin ahorro.** La regla existe justamente para el día sin ingreso. No pide saldo previo ni cuota al vendedor, y lo aplazado se paga en pedazos del tamaño del día siguiente.
3. **Soy un desconocido de 22 años.** El vendedor nunca me entrega plata ni tiene que creerme nada: la regla vive dentro de la relación que ya tiene con su minorista. El minorista me cree porque no le pido plata ni que cambie su cuaderno, y le doy algo que hoy no tiene: una razón externa para esperar sin tener que juzgar a nadie. La recomendación que hoy compra paciencia como favor personal (doc 07) se vuelve una regla.
4. **El problema ya tiene soluciones.** Todas venden plata (bancos, microfinancieras, Nequi y DaviPlata con cuota mensual; CREO y los fondos de Cali con montos de 30 a 70 veces el gota a gota; Bogotá con préstamos de 30 días) o cubren el estado del mundo (seguros agrícolas). Bold y los adelantos sobre ventas exigen venta digital y su cobro cae justo cuando caen las ventas (StoneCo 2T26). Las distribuidoras dan plazo a tiendas, no a carritos. Ninguna mueve la fecha de un crédito gratis que ya funciona el día en que se rompe.

---

## 5. Esquema página por página (cuerpo de 2.300 a 2.700 palabras y 3 tablas; opcional una cuarta pequeña)

Formato: carta, títulos cortos, citas en línea abreviadas (ej. "DANE, EMICRON 2025, C. H.4_24C") y referencias completas en el anexo. Primera persona singular. Nada de "nosotros" salvo cuando hable de la SAS.

### Página 1. Diagnóstico: una mañana de lluvia (unas 520 palabras, sin tabla)
- **Apertura con la escena del campo** (unas 120 palabras): en la estación Universidades del MIO, el vendedor saca fiado la mercancía del día a un minorista que no le cobra interés; si llueve y no vende, no le puede pagar; ahí entra el gota a gota, y después un gota a gota paga otro (doc 09). Decir desde el principio de dónde viene: conversaciones hechas por un colaborador a mi nombre el 26 sep, en resumen oral.
- **Tamaño** (unas 150 palabras): 5.297.252 micronegocios (EMICRON 2024, I.1); 14,2% pidió crédito y de ellos 22,9% fue a un gota a gota, 160.724 negocios (H.2 y H.4): piso oficial, no techo (las encuestas dan de 0,3 a 1,4 millones de adultos y los gremios hablan de 4 a 12 millones sin método: decir el rango y no usar ninguna cifra de la lista 1.4). Ambulantes: 61,8% de los que piden crédito va al gota a gota (46,4% en 2019). Cali: 17.745 ambulantes [NUEVO]; crédito de proveedores 11,6% frente a gota a gota 8,8% entre los que pidieron [NUEVO para el 8,8%].
- **Consecuencias** (unas 120 palabras): deuda que paga deuda (informante: "para pagarle a uno, se meten en otro"; colaborador: "se vuelve algo circular"); en Perú 36% pide para pagar otras deudas (IPE 2024); rescatar la deuda no saca de la trampa, se vuelve a deber en seis semanas (Karlan, Mullainathan y Roth 2019). Amenaza como primera respuesta al atraso en los casos de Cali (informante) y 31 cobradiarios asesinados en Atlántico en 2025 (El Tiempo; media, decirlo). El caso de la vendedora de arepas: un choque cerró el negocio (informante, segunda mano).
- **Tesis** (unas 130 palabras): la frase de la sección 1, con "por qué falla el formal" (vende monto a meses: 87,2% de los créditos se pagan en cuota mensual, Encuesta de Demanda 2022, p. 58; y cada operación le cuesta $1.117.131 fijos, Asobancaria BE 1475) y "qué hace bien el informal" (aparece el mismo día, cobra en días de venta, seis días a la semana y descansa cuando el deudor no sale: informante, hallazgo 9).

### Página 2. Lo que encontré y lo que cambia (unas 560 palabras y Tabla 1)
- **Método honesto** (unas 90 palabras): (a) una informante clave en Cali que conoce varios casos de amigos y familiares, dos notas de voz del 27 sep, segunda mano, sin muestreo; (b) conversaciones con vendedores de carrito en Universidades hechas por un colaborador el 26 sep, resumen oral, número exacto de vendedores desconocido; (c) no hablé en persona con vendedores y no contacté prestamistas. Sirve para mecanismos e hipótesis, no para medir. Por eso cada hallazgo va cruzado con un dato oficial o un estudio.
- **Tabla 1. Hallazgo, qué lo respalda, qué decidí** (6 filas, compacta):
  1. Fiado diario sin interés del minorista | WIEGO 2014 ("I take stock on credit every morning then pay back in the evening"); Cali 11,6% crédito de proveedores | El nodo es el minorista, no el tendero ni una app.
  2. El día de lluvia rompe el fiado y entra el gota a gota | IDEAM: 26 de 294 días de venta con disparo en los últimos 12 meses; 18 de 20 episodios de 2025 duraron un día (cálculo propio, 12b) | Lo que falta es tiempo, no plata: aplazar hasta 3 días.
  3. Un gota a gota paga otro | Karlan, Mullainathan y Roth 2019; IPE 2024 (36%) | No prestar: un préstamo más se suma a la cadena.
  4. La recomendación compra paciencia y quien recomienda no quiere cobrar | IPE 2024 (82% llega por recomendación); informante | El minorista decide quién entra, pero nunca cobra por nosotros.
  5. Al que amenaza se le paga primero | UNODC 2025 (la amenaza es la forma principal de cobro, Costa Rica); informante (hipótesis) | Lo aplazado viaja con el fiado, que ya es lo primero que se paga.
  6. No se formalizan por miedo a impuestos | 93,3% de ambulantes sin RUT; 87,9% dice que no necesita registros (EMICRON ambulantes 2025, C. 12 a 13.1) | Nada que pida RUT, factura, Nequi ni reporte.
- **Contradicción que hay que decir, no esconder** (unas 80 palabras): la etnografía de Palmira (Palomino-Martínez 2025) muestra un prestamista que castiga negando el siguiente préstamo; en Cali lo primero que aparece es la amenaza. Lectura: la renovación premia al que paga y la amenaza castiga al que se atrasa. Un servicio legal no puede copiar el castigo, así que no debe competir en la fila de pagos.
- **Qué hace bien el informal y qué no ve el formal** (unas 120 palabras): estar el día del choque; precio en pesos por día (en cuota diaria el préstamo legal se ve apenas 12 a 15% más barato: cálculo propio, `usury_cap.py`, usura sep 2026 de 88,13% E.A.); la usura subió de 52,89% a 88,13% sin más acceso (SFC 2025). El formal no puede entrar a este tramo con préstamos: la síntesis ya lo demuestra con números (6.0).

### Página 3. La propuesta (unas 600 palabras y Tabla 2)
- Nombre y frase del mecanismo (unas 60 palabras).
- Usuario exacto y cuántos (unas 110 palabras; sección 3 de este brief).
- **Tabla 2: paso a paso** (sección 4.1, recortada a 8 filas para que quepa; los casos borde en 2 líneas debajo).
- Cómo resuelve los cuatro puntos (unas 230 palabras; sección 4.2). Cerrar con la frase: "El mismo dato que le quita la licencia al problema le quita la desconfianza: nadie tiene que creerle a nadie que llovió."
- A cuál respuesta predecible se parece y qué la hace distinta (unas 90 palabras; sección 2.4, puntos 1, 3 y 4).
- Qué aprendí de lo que ya existe (unas 110 palabras): Casaburi y Willis (el que compra o vende la mercancía es el canal y el tiempo pesa más que el estado); Brune, Giné y Karlan (flexibilidad solo con historial); Bogotá con Monet (lo corto y repetible se usa, pero el embudo digital pierde a 71% de los inscritos); Tandas para el Bienestar y BanEcuador (sin relación continua no hay repago).

### Página 4. Los números (unas 450 palabras y Tabla 3)
- Tabla 3 con las seis respuestas, cada una con su supuesto (sección 6).
- Un párrafo sobre lo que gana el vendedor: cubrir un día de lluvia con un gota a gota de $100.000 al 20% cuesta $20.000, más de media jornada de ingreso mixto (unos $38.000 por día de venta; cálculo propio sobre DANE, síntesis 10.3 #19). Con la regla, $0.
- Un párrafo sobre el riesgo que carga el minorista (lo aplazado y su impago; sección 6).
- **Decir sin rodeos que el modelo no cierra en 12 meses** con cuota pagada por el minorista, y qué lo haría cerrar.

### Página 5. Descartes, riesgo y qué voy a probar (unas 500 palabras; tabla opcional de puntajes, 4 columnas)
- Descarte 1, A (unas 150 palabras) y descarte 2, F (unas 150 palabras): sección 7.
- Riesgo real principal y riesgos secundarios (unas 130 palabras): sección 7.
- Prueba de 4 semanas y qué la refutaría (unas 70 palabras): 1 minorista, sus carritos, una temporada de lluvias (octubre y noviembre son los meses con más disparos: 12b). Métricas: porcentaje de lo aplazado pagado en 3 días secos (umbral propio: 95%); cuántos vendedores dicen haber tomado un gota a gota en el periodo frente al mes anterior; si el minorista sigue en la semana 8; si él o su mayorista pagarían. Refuta: que el minorista no pueda esperar, o que lo aplazado no se pague.

---

## 6. Plan de números

### 6.1 Lo que el modelo tiene que calcular (las seis respuestas)

Todo es cálculo propio con supuestos a la vista. Conviene un script nuevo en `models/` (código y comentarios en inglés) que junte esto con `bad_day_mechanisms.py`. Proyección indicativa que hice en esta sesión (scratchpad `field_first_projection.py`):

| # | Pregunta | Valor indicativo | Supuesto y fuente |
|---|---|---|---|
| 1 | Inversión inicial | unos $4,5 millones | Estimación propia sin cotización: constitución SAS y registro $0,6 M; dos consultas de abogado $1,5 M; WhatsApp Business y servidor por 3 meses $0,3 M; tarjetas y hojas de la regla $0,3 M; transporte y tiempo de piloto 3 meses $1,8 M. El bot y la lectura del IDEAM los construyo yo (costo en efectivo cero; decirlo) |
| 2 | Costo mensual | $1,2 M (meses 1 a 6, yo sin salario) y $6 M (mes 7 en adelante, con una persona de campo de medio tiempo) | Estimación propia. Sensibilidad con los $10 M de la convención de la síntesis 6.0 |
| 3 | Cuánto deja cada usuario | $2.700 al mes por vendedor activo: cuota de $3.000 que paga el minorista menos unos $300 de mensajes | Supuesto sin precedente (igual que el precio del acreedor en C). Nosotros no tenemos pérdida por impago porque no movemos plata; el impago de lo aplazado lo carga el minorista y va en la fila siguiente |
| 3b | Impago (lo pide el caso si se mueve plata) | Lo aplazado por vendedor al año: $390.000 a $1.612.000; impago de 2 a 10%: $7.800 a $161.200 al año para el minorista; costo del plazo: $487 a $2.014 al año | `bad_day_mechanisms.py`: 26 días de disparo al año (IDEAM, cálculo propio); fiado diario de $30.000 (supuesto) a $62.000 (cota: ventas diarias menos ingreso mixto de un ambulante, DANE vía frentes 01 y 08; media); 50 a 100% del fiado queda sin pagar el día de lluvia (supuesto). Referencias de impago: microcrédito 6,9% (SFC jul 2026), Aflore 5,7% (fuente interesada) |
| 4 | Usuarios e ingresos | Mes 3: 30 vendedores (1 minorista), neto -$1,12 M; mes 6: 150 (unos 5 minoristas), neto -$0,80 M; mes 12: 600 (unos 20 minoristas en estaciones del MIO y universidades), neto -$4,38 M al mes | Rampa supuesta: unos 30 carritos por minorista (supuesto; preguntar en campo) |
| 5 | Break-even | 2.222 vendedores activos con $3.000 al mes y costo fijo de $6 M (cerca del mes 27 con la rampa); 1.053 si el que paga es el mayorista a $6.000 | 2.222 es 23% de los 9.752 estacionarios de Cali [NUEVO]; o sea, con cuota del minorista hay que salir de Cali o subir el pagador |
| 6 | Cuánto para sobrevivir | unos $10,7 M hasta el mes 6 (piloto con capital propio); unos $70 M hasta el break-even del escenario del minorista; bastante menos en el escenario del mayorista | Suma de inversión y pérdidas. De dónde: ahorro propio para el piloto; después capital semilla o un mayorista socio que pague por vendedor activo |

**Lo que hay que decir textual en la página 4:** "Con la cuota pagada por el minorista el modelo no cierra en 12 meses. Cierra si quien paga es el que más gana con que el vendedor no se caiga (el mayorista o la marca que vende en ese carrito) o si el costo fijo se queda en el nivel del piloto. Esa es la hipótesis de negocio que el piloto tiene que probar antes de gastar más."

### 6.2 Supuestos clave y sus fuentes (para la tabla y el anexo)

| Supuesto | Valor | Fuente | Confianza |
|---|---|---|---|
| Días de venta con disparo (5 mm o más entre 7:00 y 18:59, lunes a sábado) | 26 de 294 días con dato (27 sep 2025 a 26 sep 2026), unos 2 al mes, concentrados en marzo a mayo y octubre a noviembre | Cálculo propio sobre IDEAM, estación 0026055120, datos.gov.co (12b; `bad_day_mechanisms.py`) | alta en el método, media en el dato (huecos) |
| Duración de los episodios | 18 de 20 de un día, 1 de dos, 1 de tres (2025) | Idem | media |
| Ingreso mixto de un ambulante | unos $1.003.293 al mes; unos $38.000 por día de venta (26 días) | Cálculo propio sobre EMICRON ambulantes 2025, Cuadro 24; convención de la síntesis 10.3 #19 | media |
| Fiado diario de un carrito | $30.000 a $62.000 | 62.000 es cota (ventas menos ingreso); 30.000 es supuesto puro | baja: pregunta de campo |
| Precio del gota a gota | 20% por ciclo; Cali 2016: 20,4% mensual en promedio | Enunciado del caso; Martínez y Rivera-Acevedo 2019, Data in Brief (alta, dato viejo) | alta |
| Costo del plazo para quien lo carga | 12% E.A. | Convención de los scripts | supuesto |
| Cuota por vendedor activo | $3.000 (minorista) o $6.000 (mayorista) | Supuesto sin precedente | baja: es lo que el piloto mide |
| Usura (solo para el descarte A y F) | 88,13% E.A. popular productivo; 29,24% consumo | SFC, Resolución 1260 de 2026 | alta (cambia el 30 sep) |

No usar: ninguna cifra de la tabla 1.4 de la síntesis; "3 a 4 veces lo que sacan" de la informante; el 21,6% de microdatos; el 20,91% de Fenalco como hecho; el precio de 5 a 6 centavos por peso de la cartera.

---

## 7. Descartes y riesgo

### 7.1 Descarte 1: la ventanilla del tendero (A), prestar a diario con el tendero como punto de pago
- **Por qué parecía buena.** Era el mecanismo mejor puntuado de mi investigación (27 de 40). Copiaba lo que el informal hace bien: cuota diaria que el deudor inicia, montos que suben con cada ciclo cumplido, renovación como premio (Palomino-Martínez 2025: más de 150 clientes y solo 3 o 4 se fueron sin pagar). Y apuntaba al usuario correcto: 61,8% de los ambulantes que piden crédito va al gota a gota.
- **Qué la mató.** Tres cosas, dos del campo. (1) El nodo diario del vendedor de carrito no es el tendero sino el minorista que le fía (doc 09). (2) Al que amenaza se le paga primero; un prestamista legal que no puede amenazar queda de último en la fila (doc 07, hipótesis). (3) Los números: con montos de ambulante y precio legal, el neto va de -$26.143 a +$5.857 por usuario al año, y con 1% de pérdida harían falta unos 20.500 usuarios activos para cubrir $10 M al mes (`unit_economics.py`). Además, un préstamo más se suma a la cadena de deuda que paga deuda.

### 7.2 Descarte 2: el día de lluvia pagado (F), un seguro paramétrico vendido con el fiado
- **Por qué parecía buena.** El choque es externo y medible con un dato público, existe un precedente para trabajadoras informales urbanas (SEWA, India, 2024; decir "existe un precedente" sin cifras, fuente baja), y la startup solo sería canal de una aseguradora vigilada, sin licencia propia.
- **Qué la mató.** La frecuencia. Un seguro sirve para lo raro y caro; en Cali el día malo por lluvia es frecuente y corto. Pagar el fiado entero cada día de disparo cuesta $5.373 de prima pura por día de venta y $16.636 con la siniestralidad de los microseguros colombianos (32,3%, RIF 2025, p. 172; alta): 44% del ingreso mixto diario (cálculo propio, `bad_day_mechanisms.py`). Aplazar el mismo día cuesta decenas de pesos. La demanda de seguros de lluvia es baja aun a buen precio (Cole et al. 2013; alta). Lección que me llevé: el vendedor necesita tiempo, no una indemnización (Casaburi y Willis 2018).
- (Si hace falta una línea más: refinanciar o comprar la deuda del gota a gota también se descartó, por Karlan, Mullainathan y Roth 2019. Solo mencionarla; la rúbrica pide dos.)

### 7.3 Riesgo real principal de mi propuesta
**La regla le pasa el día malo al minorista. Si él también vive al día y le paga de contado a su mayorista, solo muevo el hueco un eslabón arriba, y el gota a gota entra por él.** WIEGO (2014) encontró que no todos los proveedores fían "porque también pueden haber tomado préstamos" (Accra), y en Colombia 39,55% de los tenderos reporta proveedores más duros (Fenalco 2026; media). No sé si el minorista de Universidades puede esperar de 1 a 3 días. Si no puede, la regla necesita al mayorista (fase 2) desde el principio, y eso es una venta más difícil. Qué haría: probarlo en la primera conversación con el minorista ("¿a quién le paga usted y cuándo? la última vez que llovió, ¿qué hizo?"), y si no puede esperar, ir al mayorista antes de inscribir a un solo vendedor.

Riesgos secundarios (una línea cada uno): lo aplazado no se paga y el minorista abandona la regla; riesgo de base y huecos del dato del IDEAM; que la lluvia no sea el choque principal de un carrito universitario (vacaciones, paros; hipótesis sin dato de 12a); que el abogado lea la regla como seguro; que mi evidencia de campo sea de segunda mano y de un resumen oral sin número de vendedores (lo digo en la página 2 y lo corrijo con la prueba).

---

## 8. Anexos (empiezan en página nueva con el título "ANEXOS")

1. **Prototipo.** Lo mínimo que se puede construir hoy: un script (Python, código en inglés) que lee la API del IDEAM para la estación de la Universidad del Valle, decide si hubo disparo, arma el mensaje de WhatsApp para el minorista y los vendedores y reparte lo aplazado en los siguientes días secos; más la tarjeta impresa de la regla. Decir qué hace, qué no hace (no envía WhatsApp real, no tiene registro de vendedores), cuánto tomó, con qué se hizo y que **no se le ha mostrado a ningún vendedor ni minorista**. Base existente: `scratchpad/rain_cali.py`. Incluir la tabla mensual de disparos de 12b.
2. **Método de campo y notas.** Informante clave: dos notas de voz del 27 sep, transcritas en local con Whisper, anonimizadas, sin nombres ni barrios; tabla de hallazgos con citas anonimizadas (docs 06 y 07). Conversaciones del colaborador: fecha, lugar, resumen oral transcrito, número de vendedores desconocido, sin citas textuales directas de los vendedores. Reglas cumplidas: no contacté prestamistas ni cobradores, no grabé ni fotografié a nadie. Preguntas de campo pendientes (doc 09, preguntas 1 a 5, y síntesis 11.6, preguntas 15 y 16).
3. **Uso de IA, dicho con honestidad.** Usé Claude (Claude Code) para investigación de escritorio en 12 frentes en paralelo, cada uno con su tabla de verificación; un agente como evaluador adversarial que puntuó mis mecanismos y marcó 19 afirmaciones sin respaldo; Whisper local para transcribir. Lo que hice yo: elegir el campo, las preguntas, el colaborador, descartar A pese a ser el mejor puntuado, y revisar cada cifra del cuerpo contra la fuente primaria. Lista de cifras que circulan y no usé (síntesis 1.4) como prueba de rigor.
4. **Cálculos propios.** `usury_cap.py` (precio máximo legal con cuota diaria), `unit_economics.py` (A), `bad_day_mechanisms.py` (E y F), conteo de lluvia del IDEAM, lectura de EMICRON 24 ciudades para Cali (Cuadros D.1_24C, D.5_24C y H.4_24C con CV), y la proyección de 24 a 36 meses. Supuestos en una tabla.
5. **Tabla completa hallazgo a decisión** (versión larga de la Tabla 1, con los refinamientos de la sección 2.1).
6. **Mapa de soluciones existentes** compacto (síntesis 4, recortado a 8 filas: microfinancieras, CREO, Nequi y DaviPlata, Bold, Bogotá con Monet, distribuidoras y Tienda Pago, seguros paramétricos agrícolas, apps no vigiladas).
7. **Preguntas para el abogado**: regla de aplazamiento atada al clima y pagada por el minorista frente a actividad aseguradora (Decreto 1692 de 2020 no leído); tratamiento de datos mínimo (Ley 1581); si un recordatorio del saldo aplazado cuenta como contacto de cobranza (Ley 2300).
8. **Referencias completas** con URL: DANE EMICRON (2024, 24 ciudades 2025, ambulantes 2025), Encuesta de Demanda 2022, RIF 2025, SFC Res. 1260 de 2026 y "Realidades de las microfinanzas" 2025, Asobancaria BE 1475, IDEAM datos.gov.co, Palomino-Martínez 2025, Martínez Benavides 2021, Martínez y Rivera-Acevedo 2019, WIEGO 2014, IPE 2024, UNODC 2025, Karlan, Mullainathan y Roth 2019, Brune, Giné y Karlan 2025, Casaburi y Willis 2018, Cole et al. 2013, El Tiempo 20 nov 2025, Leyes 2300 de 2023, 2157 de 2021, 1581 de 2012, Código de Comercio y Código Penal arts. 305 y 316.

---

## Notas para el redactor

- Sin guiones largos ni medianos en ningún lado; rangos con "a". Sin tríadas retóricas ni frases de relleno.
- La informante se cita siempre así: "una informante de Cali que conoce varios casos de amigos y familiares (nota de voz, 27 sep 2026)". Nunca como dato.
- El colaborador: "conversaciones con vendedores de carrito en la estación Universidades del MIO (Cali), hechas por un colaborador a mi nombre el 26 sep 2026; resumen oral". Sin número de vendedores.
- El caso del cobrador que era policía no entra al cuerpo; si entra al anexo, solo como explicación de por qué el deudor no acude a la policía, sin detalles.
- Las cifras [NUEVO] (17.745, 9.752, 7.993, 3.130 y 8,8%) hay que copiarlas al anexo de cálculos con el cuadro y el CV antes de dejarlas en el cuerpo.
