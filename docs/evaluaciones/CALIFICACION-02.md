# Retroalimentación — Laboratorio 02: Dividir y vencer

**Estudiante:** Tomás González Zapata · **Laboratorio:** Laboratorio evaluativo 02 — Dividir y vencer
**Fecha límite:** 2026-10-21 23:59 · **Versión revisada:** commit `760f8a4`

Excelente trabajo, muy completo y ordenado.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 19 / 20 |
| Calidad de la explicación teórica | 20 / 20 |
| Corrección de la implementación | 25 / 25 |
| Calidad del análisis de las gráficas | 22 / 25 |
| Documentación y organización del informe | 10 / 10 |
| **Total** | **96 / 100** |
| **Nota (0–5)** | **4.80** |

## 1. Corrección conceptual (19 / 20)
**Lo que hizo bien:**
- Identifica que divide y vencerás empieza a ganar entre 10 y 50 registros y explica por qué al inicio pierde.
- Compara bien con el máximo de un arreglo: combinar cuesta `Θ(1)`, la recurrencia da `Θ(n)` y dividir no mejora nada.
- Recomienda divide y vencerás y declara que las cifras a 1.000.000 de registros son estimaciones, con su razonamiento.

**Lo que puede mejorar:**
- Al estimar la fuerza bruta, dos puntos de partida dan 10,6 y 6,8 horas. Convendría decir cuál usaría como referencia y por qué.

## 2. Calidad de la explicación teórica (20 / 20)
**Lo que hizo bien:**
- Explica de dónde sale cada término de `T(n) = 2T(n/2) + Θ(n)`.
- Resuelve con el método maestro y verifica la condición del caso 2.
- Justifica el `Θ(n²)` de la fuerza bruta sumando `n + (n-1) + ... + 1`.

## 3. Corrección de la implementación (25 / 25)
**Lo que hizo bien:**
- Las tres funciones dan la suma correcta en todos los casos pedidos y no modifican la lista recibida.
- `subarreglo_maximo` resuelve los tres casos sin usar la fuerza bruta.
- `pruebas.py` cubre los casos pedidos y 40 listas aleatorias.
- El código tiene type hints, docstrings y cumple PEP 8.

## 4. Calidad del análisis de las gráficas (22 / 25)
**Lo que hizo bien:**
- La gráfica tiene título, ejes rotulados, leyenda, ambas curvas y nueve tamaños; la vista logarítmica ayuda a ver los tamaños pequeños.
- Los valores de la tabla coinciden con la gráfica publicada.
- Calcula el factor al duplicar de 1000 a 2000 para ambos algoritmos (4,25 y 2,19) y lo contrasta con lo esperado.

**Lo que puede mejorar:**
- Entre 2000 y 4000 la fuerza bruta se multiplicó por cerca de 6,5, y no lo comenta. Solo menciona el 2,58 de 4000 a 8000 como ruido.
- Falta el factor de divide y vencerás en el segundo par de tamaños.

## 5. Documentación y organización del informe (10 / 10)
**Lo que hizo bien:**
- Estructura de carpetas correcta, informe en el orden pedido, gráfica visible y enlaces a cada código.
- Instrucciones de reproducción claras y cinco commits descriptivos.

## ¿El código funciona?
Sí. Las pruebas pasan, las dos soluciones coinciden con una comprobación propia en listas aleatorias y la medición genera la gráfica sin errores.

## Para el próximo laboratorio
- Analice todos los pares de tamaños consecutivos, también los que no se ven como espera, y explique las causas.
- Elija un solo punto de referencia para las estimaciones y justifique la elección.
- Mantenga la costumbre de repetir las mediciones y de verificar los resultados.
