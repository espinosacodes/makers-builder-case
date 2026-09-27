# Prototipo: hoja de cálculo de la Cláusula de lluvia del fiado

Archivo: `report/prototipo.xlsx`. Captura para el anexo: `report/prototipo-snapshot.html`. Lo construí el 27 sep 2026.

## Qué hace hoy

Hace el cálculo central del mecanismo con fórmulas vivas. Los supuestos están en celdas amarillas y los resultados se recalculan al cambiarlos.

- **Hoja 1, libro del vendedor.** Sigue a un vendedor de carrito durante 30 días de venta, con la lluvia de cada día como dato de entrada. Si la lluvia pasa el umbral (5 mm entre 7 a. m. y 7 p. m.), rige la cláusula. Lleva dos caminos a la vez. El día de lluvia, en los dos, el vendedor guarda hasta $15.000 [S] para la casa y abona el resto a lo que debe. Con la cláusula, lo que no alcanzó a pagar de su fiado se paga en tercios en los 3 días de venta siguientes, sin recargo. Sin ella, ese hueco se cubre con un gota a gota al 20% en 30 cuotas diarias, y si vuelve a llover mientras paga, el préstamo nuevo cubre también la cuota del anterior. Muestra día por día lo que paga, lo que queda aplazado con quien fía, lo que le debe al prestamista y lo que queda para la casa.
- **Resultado del ejemplo** (fiado de $62.000, 3 días de lluvia en 30): con gota a gota, 3 préstamos, 2 de ellos para pagar también cuotas del anterior, $29.231 de interés (76% del ingreso de un día) y $63.043 pendientes al día 30. Con la cláusula no hay recargo y al día 30 no queda nada pendiente. Cada día de lluvia se aplazan $46.820 (tercios de unos $15.600, 40% del ingreso de un día). Tras los dos días seguidos de lluvia, quien fía llega a cargar $93.640 y los tercios se suman: los días 15 y 16 el vendedor paga $36.416 de lo aplazado y le quedan $2.184 para la casa.
- **Hoja 2, números de la SAS.** Inversión, costo fijo, contribución por vendedor, tabla de 36 meses, mes del equilibrio, caja necesaria y la vista de quien paga la tarifa ("se paga sola si le evita perder 5,1% de sus vendedores al año"). Da los mismos valores que `models/business_model.py`.

## Qué no hace todavía

- No lee la lluvia real. La del ejemplo es inventada para mostrar el cálculo. El dato real (26 de 294 días de venta, IDEAM 0026055120) está calculado aparte, no conectado a la hoja.
- No manda avisos por WhatsApp y no lleva el registro de un minorista real.
- No modela la mercancía que se daña, el tope de 2 días aplazados abiertos por vendedor ni la regla de "no elegible" si un puente no cierra en 5 días.
- La hoja 2 tiene solo el caso base; el conservador está en el script.

## Cuánto tomó y con qué

Cerca de 1 hora, el 27 sep 2026. Lo hice en Python con openpyxl, que escribe la hoja con sus fórmulas, y usé IA (Claude Code) para escribir y revisar el código. Evalué las fórmulas con la librería `formulas` y las comparé con un cálculo independiente en Python: 14 de 14 resultados iguales. Script: `models/build_prototype.py`.

## A quién se lo mostré

Todavía no se lo mostré a los vendedores con los que conversó el colaborador ni a ningún minorista. Lo primero que quiero ver con ellos son los supuestos amarillos que no tienen dato: cuánto sacan fiado, cuánto venden un día de lluvia y si lo que no vendieron se daña.
