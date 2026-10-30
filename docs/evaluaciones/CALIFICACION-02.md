# Retroalimentación — Laboratorio 02: Dividir y vencer

**Estudiante:** Tomás González Zapata · **Laboratorio:** Laboratorio evaluativo 02 — Dividir y vencer
**Fecha límite:** 2026-10-30 23:59 · **Versión revisada:** commit `7c440fc`

Muy buen trabajo: el laboratorio está completo, ordenado y bien sustentado con sus propias mediciones.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 18 / 20 |
| Calidad de la explicación teórica | 20 / 20 |
| Corrección de la implementación | 25 / 25 |
| Calidad del análisis de las gráficas | 23 / 25 |
| Documentación y organización del informe | 10 / 10 |
| **Total** | **96 / 100** |
| **Nota (0–5)** | **4.80** |

## 1. Corrección conceptual (18 / 20)
**Lo que hizo bien:**
- Identificó con sus datos el tamaño donde divide y vencerás empieza a ganar (entre 10 y 50 registros) y explicó por qué pierde en tamaños muy pequeños.
- Comparó correctamente con hallar el máximo de un arreglo: combinar cuesta poco, pero igual hay que mirar todos los elementos, así que dividir no mejora el orden.
- Recomendó un algoritmo y declaró que las cifras para 1.000.000 de registros son estimaciones, con el razonamiento detrás.

**Lo que puede mejorar (y cómo corregirlo):**
- La estimación de fuerza bruta cambia mucho según el tamaño base (más de 10 horas contra menos de 7), y no explica bien a qué se debe esa diferencia.
  → *Cómo corregirlo:* revise qué pasó con el tiempo medido en los tamaños que usó como base y diga cuál de las dos bases le parece más confiable y por qué.

## 2. Calidad de la explicación teórica (20 / 20)
**Lo que hizo bien:**
- Planteó la recurrencia explicando cada término (dos mitades y un caso cruzado lineal) y la resolvió con el método maestro verificando la condición del caso 2.
- Justificó el `Θ(n²)` de la fuerza bruta con la suma de los ciclos.

## 3. Corrección de la implementación (25 / 25)
**Lo que hizo bien:**
- Las tres funciones resuelven bien todos los casos pedidos (serie de ocho días, un elemento, todos negativos, todos positivos y un caso cruzado) y coinciden en 40 listas aleatorias.
- `subarreglo_maximo` resuelve los tres casos sin usar la fuerza bruta y ninguna función modifica la lista recibida.
- Tiene *type hints*, *docstrings* con `Args` y `Returns` y el formato de líneas en blanco pedido.

## 4. Calidad del análisis de las gráficas (23 / 25)
**Lo que hizo bien:**
- La gráfica tiene ambas curvas en los mismos ejes, título, ejes rotulados y leyenda, con nueve tamaños, y los valores del informe coinciden con lo que se ve (por ejemplo, fuerza bruta cerca de 1600 ms y divide y vencerás cerca de 9 ms en n = 8000).
- Calculó el factor al duplicar de 1000 a 2000 para ambos algoritmos y lo contrastó con lo esperado.

**Lo que puede mejorar (y cómo corregirlo):**
- Algunos saltos de la curva de fuerza bruta no se parecen a un factor de 4 (por ejemplo, entre 4000 y 8000 y entre 500 y 1000), y lo atribuye al ruido sin mirar otros pares de tamaños.
  → *Cómo corregirlo:* calcule el factor en otro par consecutivo que se duplique y diga si el patrón general sí se mantiene.

## 5. Documentación y organización del informe (10 / 10)
**Lo que hizo bien:**
- El laboratorio está en una ubicación válida (`laboratorios/lab2-divide-y-vencer/`) con todos los archivos del entregable.
- El informe sigue el orden pedido, incrusta la gráfica con ruta que funciona, enlaza el código de cada parte e incluye instrucciones para reproducir.
- Hay varios commits con mensajes descriptivos.

## ¿El código funciona?
Sí. Las pruebas pasan sin errores y la medición corre completa, imprime los tiempos y genera la gráfica.
