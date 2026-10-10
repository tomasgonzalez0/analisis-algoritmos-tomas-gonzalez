"""Mide los algoritmos de subarreglo máximo y genera su gráfica."""

import random
from collections.abc import Callable
from pathlib import Path
from statistics import median
from time import perf_counter

import matplotlib.pyplot as plt

from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo

TAMANOS = [10, 50, 100, 250, 500, 1000, 2000, 4000, 8000]
REPETICIONES = 3
SEMILLA = 20261003
Algoritmo = Callable[[list[float]], tuple[int, int, float]]
Medicion = tuple[int, float, float, float]


def generar_valores(tamano: int) -> list[float]:
    """Genera una serie reproducible de variaciones diarias.

    Args:
        tamano: cantidad de valores que tendrá la serie.

    Returns:
        Lista de enteros entre -100 y 100, expresada como lista de float.
    """
    generador = random.Random(SEMILLA + tamano)
    return [generador.randint(-100, 100) for _ in range(tamano)]


def medir_algoritmo(
    algoritmo: Algoritmo, valores: list[float]
) -> tuple[float, float]:
    """Mide un algoritmo sin incluir la generación de los datos.

    Args:
        algoritmo: función de subarreglo máximo que se medirá.
        valores: serie que recibirá el algoritmo en cada repetición.

    Returns:
        Tiempo mediano en segundos y mejor suma encontrada.
    """
    tiempos = []
    suma_referencia = None

    for _ in range(REPETICIONES):
        inicio = perf_counter()
        resultado = algoritmo(valores)
        fin = perf_counter()
        tiempos.append(fin - inicio)

        if suma_referencia is not None and resultado[2] != suma_referencia:
            raise RuntimeError("El resultado cambió entre repeticiones.")
        suma_referencia = resultado[2]

    if suma_referencia is None:
        raise RuntimeError("No se ejecutó ninguna repetición.")
    return median(tiempos), suma_referencia


def ejecutar_divide(valores: list[float]) -> tuple[int, int, float]:
    """Ejecuta divide y vencerás sobre una serie completa.

    Args:
        valores: serie completa que se analizará.

    Returns:
        Mejor subarreglo encontrado en toda la serie.
    """
    return subarreglo_maximo(valores, 0, len(valores) - 1)


def ejecutar_experimento() -> list[Medicion]:
    """Mide ambos algoritmos con una misma serie para cada tamaño.

    Returns:
        Mediciones con tamaño, tiempos medianos y suma máxima.
    """
    resultados = []

    for tamano in TAMANOS:
        valores = generar_valores(tamano)
        copia = valores.copy()
        tiempo_fuerza, suma_fuerza = medir_algoritmo(
            subarreglo_fuerza_bruta, valores
        )
        tiempo_divide, suma_divide = medir_algoritmo(ejecutar_divide, valores)

        if suma_fuerza != suma_divide:
            raise RuntimeError(f"Las sumas no coinciden para n={tamano}.")
        if valores != copia:
            raise RuntimeError(f"La entrada fue modificada para n={tamano}.")

        resultados.append((tamano, tiempo_fuerza, tiempo_divide, suma_fuerza))

    return resultados


def graficar(resultados: list[Medicion]) -> None:
    """Genera una comparación en escalas lineal y logarítmica.

    Args:
        resultados: mediciones obtenidas para ambos algoritmos.
    """
    tamanos = [resultado[0] for resultado in resultados]
    fuerza_ms = [resultado[1] * 1000 for resultado in resultados]
    divide_ms = [resultado[2] * 1000 for resultado in resultados]

    figura, ejes = plt.subplots(1, 2, figsize=(14, 5.5))
    configuraciones = (
        (ejes[0], "Escala lineal", False),
        (ejes[1], "Escala logarítmica", True),
    )

    for eje, titulo, usar_logaritmos in configuraciones:
        eje.plot(tamanos, fuerza_ms, marker="o", label="Fuerza bruta")
        eje.plot(tamanos, divide_ms, marker="o", label="Divide y vencerás")
        if usar_logaritmos:
            eje.set_xscale("log")
            eje.set_yscale("log")
        eje.set_title(titulo)
        eje.set_xlabel("Tamaño de entrada (registros)")
        eje.set_ylabel("Tiempo mediano (milisegundos)")
        eje.grid(alpha=0.3, which="both")
        eje.legend()

    figura.suptitle("Tiempo para encontrar el subarreglo máximo")
    figura.tight_layout()
    carpeta = Path(__file__).resolve().parent / "graficas"
    carpeta.mkdir(exist_ok=True)
    figura.savefig(carpeta / "tiempo_vs_n.png", dpi=160)
    plt.close(figura)


def mostrar_resultados(resultados: list[Medicion]) -> None:
    """Muestra las mediciones en un formato fácil de reproducir.

    Args:
        resultados: mediciones obtenidas para ambos algoritmos.
    """
    print("tamaño;fuerza_bruta_ms;divide_y_venceras_ms;suma_maxima")
    for tamano, tiempo_fuerza, tiempo_divide, suma in resultados:
        print(
            f"{tamano};{tiempo_fuerza * 1000:.6f};"
            f"{tiempo_divide * 1000:.6f};{suma:.2f}"
        )


def main() -> None:
    """Ejecuta la medición, muestra los datos y genera la gráfica."""
    resultados = ejecutar_experimento()
    mostrar_resultados(resultados)
    graficar(resultados)


if __name__ == "__main__":
    main()
