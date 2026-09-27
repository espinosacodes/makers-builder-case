# Revisión final con la rúbrica (27 sep 2026)

Archivo revisado: report/docs/informe-docs.md, contra docs/02-criterios-evaluacion.md. Foco en el criterio 07 y en si la ambición se lee con evidencia o inflada.

Estado de encaje antes de cambios: estricto, página 5 al 95%; nominal, página 4 al 98%. Probé los cuatro cambios de abajo juntos en una copia: estricto 97% de la página 5, nominal 100% de la página 4, ambos PASS. El archivo original quedó restaurado sin tocar.

## Puntaje por criterio

| # | Criterio | Nota | Por qué |
|---|---|---|---|
| 01 | Efectividad | 4 | Ataca la causa (el día sin ventas rompe el fiado) con un solo mecanismo para los cuatro puntos. Queda abierta la premisa de que el minorista no espera ya. |
| 02 | Especificidad | 5 | Tabla 2 dice quién, cuándo, con qué y dónde está la plata; ahora incluye persona natural y capital propio en la semana 0. |
| 03 | Creatividad | 4 | Plazo activado por dato público dentro de un crédito que ya existe; no aparece hecho. Se parece a un seguro paramétrico, pero el descarte 2 explica la diferencia con números. |
| 04 | Diagnóstico | 4 | Tesis propia (precio 14% menor no basta; la forma del producto sí), cruzada con campo y lluvia medida. |
| 05 | Fuentes | 4 | Cuadros y páginas citados. Baja un punto por las cifras de verificación del Anexo C, que suman 272 y no 243 (cambio 3). |
| 06 | Trazabilidad | 5 | Tabla 1 lleva cada rasgo a un hallazgo y a su respaldo. |
| 07 | Juicio cuantitativo | 4 (5 con los cambios 1 y 2) | Supuestos a la vista, fuente del dinero explícita (capital propio [S]; Fondo Emprender condicional; WWB y BID Lab fuera de la caja), y dice cuándo no cierra. Dos fallas: el conservador "sin salario" usa la estructura de costos anterior, y el plan austero no dice cuándo alcanza para pagar un mínimo. |
| 08 | Descartes y autocrítica | 4 | Descartes reales con números y riesgo en tres capas con umbrales. |

Total: 34/40 (antes 33/40). Con los cambios 1 a 3, 36/40.

## Criterio 07 en detalle

Verifiqué contra models/business_model.py:

- Plan austero base: equilibrio mes 10, 279 que pagan, caja $3.386.800 (concepto gratis) o $6.386.800 (pagado). Coincide con la Tabla 3.
- Fila 2: $430.000 = 200.000 + 80.000 + 150.000; desde el mes 7, más $350.000 de contador. Coincide.
- Fila 3 y 4: 4.000 × 90% menos 800 = 2.800; 27, 108 y 416 que pagan. Coincide.
- Con salario desde el mes 1: $2.530.905, 904, mes 22, $34.523.005. Coincide.
- Falla A: "sin salario cierra en el mes 27 con $15,1 millones" sale del escenario "conservative without founder salary", que paga SAS, contador y abogado desde el mes 1 ($3,9 millones de entrada, $780.000 fijos). Con la estructura del plan austero sobre la rampa conservadora el modelo da mes 27 y $10.038.000 (concepto gratis) o $13.038.000 (pagado). El texto mezcla dos planes.
- Falla B: el modelo imprime "first month the surplus pays a full minimum wage: 22" en el plan austero base, y en el austero conservador el excedente nunca llega a un mínimo en 60 meses. El informe dice "Mi mínimo sale solo del excedente" pero no cuándo. Un jurado lo lee como costo escondido en tiempo no pagado; decirlo es justo lo que pide el criterio ("si tu modelo no cierra, dilo").

Ambición: se lee con evidencia, no inflada. Anexo D tiene condiciones de entrada, WWB no cuenta como plata, BID Lab exige 12 meses de datos y "no sumo ingresos de ahí". Dos detalles la inflan un poco: "la regla sirve en otras ciudades" afirma lo que no se ha probado, y la suma 5,7 millones es cálculo propio sin marca. El cambio 2 los corrige.

## Cambios obligatorios (máximo 4, sin agregar largo)

### 1 y 2. Párrafos bajo la Tabla 3 (líneas 74 y 76), en un solo reemplazo

Reemplazar las líneas 74 y 76 completas por:

> Con mi salario desde el mes 1: 904 vendedores, mes 22 y $34,5 millones.
>
> **¿Cierra? Sin salario, en el mes 10; con salario, en el mes 22.** Elijo lo primero: arriesgo $3,4 a $6,4 millones y no $34,5 millones que no tengo, pero me pago un mínimo completo solo desde el mes 22. En un caso conservador (la mitad del ritmo, 8 vendedores por minorista y 20% sin cobrar) no cierra con salario en 60 meses; sin salario cierra en el mes 27 con $10 a $13 millones, sin pagarme un mínimo en 60 meses. Si no cierra, será por volumen y por una tarifa que nadie ha pagado todavía, no por riesgo de crédito; por eso cobro desde el segundo mes. Escenario, no caso base: la regla podría servir en otras ciudades porque solo pide fiado y lluvia abierta: México y Ecuador publican lluvia horaria sin registro [R32; R33], en Perú 35% de los préstamos informales se paga a diario [R12, p. 15] y cinco países suman 5,7 millones de ambulantes [R34, tabla 1; cálculo propio] (Anexo D). No sumo ingresos de ahí: fuera de Colombia no he medido el fiado.

Qué arregla: el conservador queda con la misma estructura de costos del plan (falla A), aparece cuándo el negocio paga un mínimo (falla B), "sirve" pasa a "podría servir" y la suma de WIEGO queda marcada. Para que salga del largo, quité el $2.530.905 (ya está implícito en la fila 2) y la cláusula del mayorista que paga por sus minoristas, que ya está en la Tabla 2, en "Para quien paga", en "Cómo sé si me equivoqué" y en el Anexo D. Queda con 1 palabra más que el original, y el cambio 3 compensa.

Para que Anexo B ("el plan sin salario lo calculé con el mismo modelo en Python") siga siendo cierto, el script debe imprimir el austero conservador. En models/business_model.py, junto a LEAN_FREE_LEGAL y LEAN_PAID_LEGAL:

```python
def lean_conservative(legal_opinion, label):
    # Lean cost structure on the conservative ramp (half the signing pace, 80% collection)
    return Scenario(
        name=f"lean conservative, legal opinion {label}",
        fee=CONSERVATIVE.fee, collection=CONSERVATIVE.collection,
        direct_cost=CONSERVATIVE.direct_cost,
        retailers=conservative_retailers, vendors_per_retailer=conservative_vendors_per_retailer,
        include_wage=False, fixed_schedule=lean_fixed,
        one_off_by_month={LEAN_SAS_MONTH: SAS_REGISTRATION},
        initial_investment={"printed vendor cards and pilot material": PRINTED_MATERIAL,
                            "lawyer opinion on 5 questions": legal_opinion},
        salary_from_margin=True,
    )
```

y pasarlos por print_scenario en el bloque del plan austero. Resultado esperado: mes 27; caja 10.038.000 y 13.038.000; mínimo completo no alcanzado en 60 meses.

### 3. Cifras de verificación (Anexo C)

Las cuatro categorías suman 272, no 243, y 192 + 49 + 1 = 242. Un jurado que sume lo ve como descuido en la parte que habla de rigor. Hasta confirmar cómo se solapan, reemplazar:

> En la primera pasada de verificación se revisaron 243 cifras: 192 confirmadas, 49 corregidas, 30 marcadas como no verificadas y 1 eliminada por fuente inexistente.

por:

> En la primera pasada de verificación se revisaron 243 cifras; el detalle por resultado está en el repositorio.

Si se aclara el solapamiento (por ejemplo, que las 30 no verificadas son un subconjunto), se puede volver al desglose con esa aclaración, pero también hay que corregir el README del repositorio, que tiene la misma frase.

### 4. Ninguno más

No encontré otra falla que valga el espacio. Los números de la Tabla 3, la fuente del dinero y el tratamiento de WWB, Fondo Emprender y BID Lab siguen las decisiones de Santiago.

## Revisión rápida de reglas

- Sin raya ni semirraya, sin guion espaciado usado como raya.
- Sin enlaces markdown ni HTML; URL solo en Anexo A y en la línea del repositorio.
- R37 y R38 aparecen por primera vez en el Anexo D, después de R36; el orden es correcto.
- Sin nombres de personas del campo ni edad.
