# Review log (copia de Docs)

## 27 sep 2026, 09:00 aprox. Plan austero, ambición y repositorio

Modelo (`models/business_model.py`): nuevo escenario LEAN (`LEAN_FREE_LEGAL`, `LEAN_PAID_LEGAL`) con constantes nombradas. Sin salario hasta cubrir costos y después solo del excedente; persona natural los meses 1 a 6 (sin SAS ni contador); SAS de $600.000 en el mes 7; material $300.000; concepto legal gratis [S, no verificado] o $3.000.000. Resultado: caja $3.386.800 (gratis) o $6.386.800 (pagado), punto más bajo en el mes 9, equilibrio en el mes 10 con 279 vendedores (pagan 312); el mínimo completo sale del excedente desde el mes 22. Coincide con las cifras del chat. Con salario solo desde el mes 7, el script da $18,9 a $21,9 millones (el chat decía unos $24 millones); anotado en `report/numbers.md`, no está en el cuerpo.

`report/numbers.md`: nueva sección 1b (plan austero) y sección 6 resuelta (capital propio [S]).

`informe-docs.md`:
- Tabla 2, semana 0: arranco como persona natural; la SAS va en el mes 7. Fin de mes: "Mi única entrada".
- Tabla 3 pasa a ser el plan austero: filas 1, 2, 5 y 6 nuevas (inversión $0,3 o $3,3 millones; costo $430.000 meses 1 a 6 y $780.000 desde el 7; 279 vendedores, mes 10; caja $3,4 a $6,4 millones, capital propio [S], Fondo Emprender como ventaja condicionada). Filas 3 y 4 sin cambio. Debajo, una línea de comparación con salario ($2.530.905, 904 vendedores, mes 22, $34,5 millones).
- "¿Cierra?": sin salario cierra en el mes 10, con salario en el 22, y por qué elijo lo primero; se mantiene el conservador; frase "Escenario, no caso base" (mayorista, México y Ecuador con lluvia horaria abierta, 35% de pago diario en Perú, 5,7 millones de ambulantes en 5 países).
- "Usuario y alcance": el contraste con el DANE ahora es contra los 279 del equilibrio.
- Recortes para compensar: R1 a R5 de `13-cambios-ambicion.md`, más la sensibilidad de tarifa en "¿Cierra?" (sigue en numbers.md), "negativo desde 1,5%" en el Descarte 1, la cola de la tercera capa de riesgo y detalles de la Tabla 2.
- Anexo A: 6 referencias nuevas y renumeración por orden de aparición (R31 Fondo Emprender, R32 SMN, R33 INAMHI, R34 WIEGO 2024, R35 y R36 son las antiguas R31 y R32, R37 Fundación WWB, R38 BID Lab).
- Anexo B: la hoja 2 del prototipo reproduce el caso con salario; el plan austero sale del modelo en Python.
- Anexo C: línea del repositorio público y cifras de la primera verificación (243 revisadas: 192, 49, 30 y 1, tal como las da el README).
- Anexo D nuevo: Ruta de escala (WWB como aliada, no plata; BID Lab solo con 12 meses de datos, no como ingreso).

Pruebas: fit estricto, el cuerpo termina en la página 5 al 95% (antes 94%); nominal, página 4 al 98%. Sin rayas ni guiones espaciados, sin enlaces markdown ni HTML. `.docx` y `.txt` reconstruidos.

Pendiente: el conservador "sin salario" ($15,1 millones, mes 27) usa la estructura de costos anterior (SAS, contador y abogado desde el mes 1), no la austera. Las cifras de verificación del README suman 272, no 243 (las categorías se solapan o una cifra está mal); revisar antes de enviar.
