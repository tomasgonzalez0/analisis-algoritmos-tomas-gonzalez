# Retroalimentación — Laboratorio 01: Fundamentos, complejidad y recurrencias

**Estudiante:** Tomás González Zapata · **Laboratorio:** Laboratorio evaluativo 01 — Fundamentos, complejidad y recurrencias
**Fecha límite:** 2026-10-06 23:59 · **Versión revisada:** commit `5ab837b`

Excelente trabajo: un informe completo, con datos propios y conclusiones bien apoyadas en ellos.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 23 / 25 |
| Calidad de la explicación teórica | 23 / 25 |
| Corrección de la implementación | 18 / 20 |
| Calidad del análisis de las gráficas | 18 / 20 |
| Documentación y organización del informe | 10 / 10 |
| **Total** | **92 / 100** |
| **Nota (0–5)** | **4.60** |

## 1. Corrección conceptual (23 / 25)
**Lo que hizo bien:**
- Distingue bien entre corrección y eficiencia y nombra la restricción incumplida: la ventana de cuatro horas.
- Explica que un servidor el doble de rápido no cambia el crecimiento cuadrático del algoritmo.
- Da un segundo ejemplo propio (búsqueda entre 500.000 productos con respuesta en menos de 300 ms), con datos y restricción.
- Identifica dos perjuicios concretos (el paciente y el operador del centro de contacto) y dice quién asume cada costo.
- Discute con claridad que el orden de la lista decide a quién se llama primero.

**Lo que puede mejorar:**
- La parte ambiental dice que más tiempo de CPU es más energía, pero se queda sin un orden de magnitud. Un cálculo aproximado con sus propios tiempos (horas por noche por años) la haría más convincente.

## 2. Calidad de la explicación teórica (23 / 25)
**Lo que hizo bien:**
- Define peor, mejor y promedio indicando sobre qué conjunto de entradas se toma cada uno, y justifica que usaría el peor caso.
- La predicción quedó escrita antes del experimento y es coherente con el orden de mayor a menor.
- La recurrencia de merge sort está explicada término a término y resuelta con el método maestro, verificando la condición del caso 2.
- El análisis línea a línea de insertion sort es detallado y la tabla de complejidades es correcta.

**Lo que puede mejorar:**
- El caso promedio de insertion sort se afirma con una frase ("una fracción lineal del prefijo"). Se agradecería mostrar el cálculo del promedio, aunque sea simple.

## 3. Corrección de la implementación (18 / 20)
**Lo que hizo bien:**
- `insertion_sort` y `merge_sort` ordenan bien en todos los escenarios, no alteran la lista recibida y cuentan solo comparaciones entre elementos.
- No usa `sorted()` ni `list.sort()`; la mezcla de merge sort es propia y recursiva.
- Los generadores dan listas de valores distintos, con semilla reproducible, y el lote casi ordenado tiene el 2 % al final.
- Tiene *type hints* y *docstrings* en todas las funciones.

**Lo que puede mejorar:**
- En `parte3_casos.py` y `parte4_complejidad.py` varias importaciones quedan después de otras instrucciones, lo que incumple PEP 8.

## 4. Calidad del análisis de las gráficas (18 / 20)
**Lo que hizo bien:**
- Las tres gráficas existen, con título, ejes rotulados con unidades y leyenda, y las curvas comparten ejes.
- Identifica con datos el peor caso (C), el mejor (B) y el cercano al promedio (A), y lo contrasta con su predicción.
- Compara merge sort e insertion sort en la gráfica, la relaciona con las complejidades calculadas y explica el comportamiento para tamaños pequeños.
- El concepto técnico recomienda merge sort, responde a la compra del servidor con datos medidos, extrapola a 1.200.000 registros declarándolo como estimación y discute memoria y estabilidad.

**Lo que puede mejorar:**
- En las gráficas de escala lineal la curva del escenario B queda pegada al eje. Una escala logarítmica o un recuadro ampliado ayudaría a verla.
- La extrapolación se apoya en un solo tamaño (6400); contrastarla con otro tamaño daría más confianza.

## 5. Documentación y organización del informe (10 / 10)
**Lo que hizo bien:**
- Carpeta y archivos con los nombres pedidos, gráficas incrustadas con ruta relativa que funciona y enlaces al código en cada parte práctica.
- Instrucciones de reproducción incluidas y seis commits descriptivos del laboratorio.

## ¿El código funciona?
Sí. Los scripts corren sin errores, los algoritmos ordenan bien y el conteo de comparaciones coincide con lo esperado (por ejemplo, 99 en una lista ya ordenada de 100). Se generan las tres gráficas.

## Para el próximo laboratorio
- Cuantificar con un cálculo aproximado los argumentos sobre consumo de recursos.
- Mostrar el desarrollo completo del caso promedio cuando lo afirme.
- Respetar el orden de las importaciones y revisar el código con la herramienta de estilo antes de entregar.
- Elegir escalas de gráfica que permitan ver todas las curvas, incluso las que crecen poco.
