# Retroalimentación — Laboratorio 03: Estructuras de datos

**Estudiante:** Tomás González Zapata · **Laboratorio:** Laboratorio evaluativo 03 — Estructuras de datos
**Fecha límite:** 2026-11-01 23:59 · **Versión revisada:** commit `ef7cac4`

Muy buen trabajo, completo y bien sustentado con sus propias mediciones.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 19 / 20 |
| Calidad de la explicación teórica | 19 / 20 |
| Corrección de la implementación | 25 / 25 |
| Calidad del análisis de las gráficas | 24 / 25 |
| Documentación y organización del informe | 10 / 10 |
| **Total** | **97 / 100** |
| **Nota (0–5)** | **4.85** |

## 1. Corrección conceptual (19 / 20)
**Lo que hizo bien:**
- Explica bien la colisión usando el ejemplo de 10, 24 y 17 con m = 7, y compara encadenamiento con direccionamiento abierto (ventajas y costos de cada uno).
- Justifica que la tabla no sirve para rangos y estima la altura del árbol degenerado (cerca de 400.000) frente a unos 19 niveles del equilibrado.
- Recomienda tabla hash más árbol equilibrado y declara que la cifra a 5.000.000 es una estimación.

**Lo que puede mejorar (y cómo corregirlo):**
- La estimación para la tabla a 5.000.000 simplemente repite el valor medido con 50.000 guías, sin explicar qué podría cambiar con tanta memoria.
  → *Cómo corregirlo:* Piense qué ocurre con el acceso a memoria cuando la tabla es mucho más grande y diga si eso movería su estimación hacia arriba o hacia abajo.
- Para el árbol degenerado dé también el número total aproximado de comparaciones al insertar todas las guías, no solo el de una búsqueda.
  → *Cómo corregirlo:* Sume las comparaciones que cuesta cada inserción sucesiva y compare ese total con el del árbol equilibrado.

## 2. Calidad de la explicación teórica (19 / 20)
**Lo que hizo bien:**
- Justifica `Θ(n)` para la lista y `Θ(1 + α)` para la tabla, nombra el supuesto de distribución uniforme y explica que con todas las guías en una casilla la tabla vuelve a costar `Θ(n)`.

**Lo que puede mejorar (y cómo corregirlo):**
- Falta precisar que el `Θ(n)` de la lista aplica a la guía inexistente porque obliga a ver todos los nodos, mientras que la existente, en promedio, ve la mitad.
  → *Cómo corregirlo:* Agregue una frase que contraste ambos casos.

## 3. Corrección de la implementación (25 / 25)
**Lo que hizo bien:**
- Las dos estructuras buscan bien (existentes e inexistentes), la colisión con m = 7 funciona, `factor_carga` da 3/7 y la tabla reutiliza la lista sin `dict`, `set` ni `hash()`.
- Las pruebas cubren 30 colecciones aleatorias; todo pasa. Hay docstrings con `Args` y `Returns`, type hints y dos líneas en blanco entre funciones.

## 4. Calidad del análisis de las gráficas (24 / 25)
**Lo que hizo bien:**
- Ambas gráficas tienen título, ejes rotulados y leyenda; la primera cubre seis valores de n con las dos curvas en los mismos ejes y la segunda seis valores de α.
- Calcula los factores de crecimiento de todos los intervalos y los contrasta con `Θ(n)`, `Θ(1)` y `Θ(1 + α)`; las cifras coinciden con lo que muestran las gráficas.

**Lo que puede mejorar (y cómo corregirlo):**
- En el último intervalo de la lista (3,51 frente a 2,5 esperado) y en la tabla se explica la diferencia solo con "ruido" en general.
  → *Cómo corregirlo:* Indique qué haría para comprobarlo (por ejemplo, repetir esa medición) y cuál sería el resultado esperado si fuera ruido.
- Para la tabla, los factores de crecimiento cerca de 1 se comparan con `Θ(1)` pero no con el pequeño aumento que predice `Θ(1 + α)` cuando α es fija.
  → *Cómo corregirlo:* Comente que con α constante la predicción es un tiempo casi igual y que esa es la lectura de sus datos.

## 5. Documentación y organización del informe (10 / 10)
**Lo que hizo bien:**
- El laboratorio está en `laboratorios/lab3-estructuras-datos/` (ubicación válida), con todos los archivos pedidos, orden correcto del informe, gráficas visibles con ruta relativa, enlaces al código en cada parte, instrucciones de reproducción y varios commits descriptivos.

## ¿El código funciona?
Sí. Las pruebas pasan sin errores y las estructuras responden igual que lo esperado. El código de medición está completo y genera las dos gráficas.
