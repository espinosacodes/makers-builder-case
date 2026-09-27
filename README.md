# Cláusula de lluvia del fiado · Builder Case, Makers Fellowship 2026

Santiago Espinosa · Cali, Colombia · 27 de septiembre de 2026

Este repositorio contiene todo el proceso detrás de mi propuesta para el Builder Case de Makers Fellowship: la investigación, las fuentes, las verificaciones, el trabajo de campo anonimizado, los modelos de números, el prototipo y las versiones del informe.

**La pregunta del reto:** por qué el crédito informal ("gota a gota") sigue ganándole al sistema formal entre los micronegocios de América Latina, y qué se puede construir sin ser entidad financiera, para alguien con ingreso diario y sin ahorro, siendo un desconocido.

**Mi respuesta en una línea:** para el vendedor que vive del fiado diario, el gota a gota no gana por precio; gana la tarde en que un día sin ventas (la lluvia) rompe el fiado sin interés que ya tiene con su minorista. La propuesta es una regla escrita, activada por un dato público de lluvia del IDEAM, que corre en tercios el pago del fiado de ese día. No presto, no aseguro y la plata del vendedor nunca pasa por mí.

## Dónde está cada cosa

| Carpeta o archivo | Qué hay |
|---|---|
| `report/docs/informe-docs.md` | Versión final del informe (la que se pega en Google Docs), con anexos |
| `report/MAKERS_SANTIAGO_ESPINOSA_CALI.pdf` | Versión larga del informe (v2), con 10 páginas de anexos |
| `report/versions/` | Versiones anteriores (v1 y v2) |
| `report/brief-*.md` | Los tres enfoques independientes del informe y la decisión final |
| `report/review-*.md` | Revisiones adversariales con la rúbrica, de hechos y de cumplimiento, ronda por ronda |
| `report/fact-pack.md` | Las cifras que se podían usar, con fuente, y las que no |
| `report/numbers.md`, `models/` | Modelo de negocio y cálculos propios (usura con cuota diaria, lluvia en Cali, economía unitaria) |
| `report/prototipo.xlsx` | Prototipo: hoja de cálculo con fórmulas que hace el cálculo central del mecanismo |
| `docs/research/00-sintesis.md` | Síntesis de toda la investigación: cifras verificadas, tesis, puntos ciegos, mecanismos, descartes y revisión adversarial |
| `docs/research/01` a `13` | Un archivo por frente de investigación, cada uno con su tabla de verificación |
| `docs/00` a `docs/09` | El reto, la rúbrica, mi lectura del caso, guías de campo y notas de campo anonimizadas |
| `prompt.md` | El prompt que usé para investigar con otros agentes |

## Cómo se hizo

1. **Lectura del caso y de la rúbrica** (`docs/03-analisis-del-caso.md`): qué puntúa, qué respuestas son predecibles y qué hipótesis probar.
2. **Investigación en 10 frentes** (tamaño, comparación regional, mecanismo informal, evidencia académica, intentos formales, mercado, estructura legal, confianza y fiado, voz del usuario, puntos ciegos), más frentes posteriores sobre venta de cartera, reportados, el día malo y financiación. Cada cifra lleva entidad, documento, cuadro o página, URL, año y nivel de confianza.
3. **Verificación escéptica:** un agente distinto abrió cada fuente citada para confirmar valor, año y entidad. En la primera pasada se revisaron 243 cifras; el detalle por resultado está en los archivos de verificación de este repositorio.
4. **Campo:** una informante clave de Cali que conoce muchos casos (dos notas de voz) y conversaciones con vendedores de carrito en la estación Universidades del MIO, hechas por un colaborador en mi nombre el 26 de septiembre. Las notas están anonimizadas. Nadie contactó prestamistas, siguiendo la regla del reto.
5. **Cálculos propios con datos abiertos:** precio máximo legal de un préstamo con cuota diaria (usura certificada de septiembre de 2026), días de lluvia en la estación IDEAM de la Universidad del Valle, peso del crédito de proveedores en Cali (DANE, EMICRON).
6. **Diseño y descarte de mecanismos** con puntaje adversarial según la rúbrica (sección 10 de la síntesis y `docs/research/12-mecanismos-dia-malo.md`).
7. **Redacción y revisión:** tres enfoques independientes, un juez, y varias rondas de revisión (rúbrica, hechos, cumplimiento) hasta la versión final.

### Uso de IA

El reto permite usar IA y la usé a fondo: agentes de Claude (Anthropic) orquestados en flujos de trabajo para buscar, leer fuentes primarias, verificar cifras, diseñar y criticar. Las decisiones, el trabajo de campo y la elección final son míos. Cifras aproximadas del proceso al 27 de septiembre de 2026, 08:40 (hora Colombia):

| Métrica | Valor |
|---|---|
| Agentes ejecutados | unos 120 |
| Llamadas a herramientas (búsquedas, lecturas de fuentes, cálculos) | unas 4.100 |
| Tokens generados por los modelos | unos 3,4 millones |
| Tokens procesados en total (la mayoría, lectura repetida de contexto en caché) | unos 550 millones |

## Reproducir los números

```
python3 models/usury_cap.py        # precio máximo legal con cuota diaria (usura sep 2026)
python3 models/unit_economics.py   # economía del préstamo diario escalonado (mecanismo descartado)
python3 models/business_model.py   # las seis respuestas de números de la cláusula de lluvia
```

La usura cambia cada mes: los resultados dependen de la certificación de septiembre de 2026.

## Privacidad y material excluido

- No se publican audios (ni de la informante ni de terceros), ni nombres o detalles que identifiquen a nadie. Las notas de campo están anonimizadas.
- No se publica el material crudo de búsquedas de la primera corrida (texto de terceros sin verificar), ni los archivos originales del reto tal como los distribuyó la organización.
- Las fuentes citadas son públicas; los enlaces están en cada archivo de investigación y en el Anexo A del informe.
