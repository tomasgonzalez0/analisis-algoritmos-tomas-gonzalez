"""Compara experimentalmente insertion sort y merge sort."""

from collections.abc import Callable
from pathlib import Path
from statistics import median
from time import perf_counter

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from algoritmos import insertion_sort, merge_sort
from datos import generar_aleatorio

TAMANOS = [100, 200, 400, 800, 1600, 3200, 6400]
REPETICIONES = 3
Algoritmo = Callable[[list[int]], tuple[list[int], int]]


def medir_algoritmo(
    algoritmo: Algoritmo, datos: list[int]
) -> tuple[float, int, list[int]]:
    """Mide un algoritmo y retorna tiempo, comparaciones y resultado.

    Args:
        algoritmo: función de ordenamiento instrumentada que se medirá.
        datos: lote que recibirá el algoritmo en cada repetición.

    Returns:
        Tiempo mediano, comparaciones y lista ordenada.
    """
    tiempos = []
    comparaciones = 0
    resultado = []

    for _ in range(REPETICIONES):
        inicio = perf_counter()
        resultado_actual, comparaciones_actuales = algoritmo(datos)
        fin = perf_counter()
        tiempos.append(fin - inicio)

        if resultado and resultado != resultado_actual:
            raise RuntimeError("El resultado cambió entre repeticiones.")
        if comparaciones and comparaciones != comparaciones_actuales:
            raise RuntimeError("Las comparaciones cambiaron entre repeticiones.")
        resultado = resultado_actual
        comparaciones = comparaciones_actuales

    return median(tiempos), comparaciones, resultado


def ejecutar_experimento() -> list[tuple[int, float, float, int, int]]:
    """Compara ambos algoritmos usando un mismo lote por tamaño.

    Returns:
        Mediciones de tiempo y comparaciones para cada tamaño.
    """
    resultados = []

    for tamano in TAMANOS:
        datos = generar_aleatorio(tamano)
        entrada_original = datos.copy()

        tiempo_insertion, comp_insertion, salida_insertion = medir_algoritmo(
            insertion_sort, datos
        )
        tiempo_merge, comp_merge, salida_merge = medir_algoritmo(
            merge_sort, datos
        )

        if datos != entrada_original:
            raise RuntimeError("Un algoritmo modificó el lote original.")
        if salida_insertion != salida_merge:
            raise RuntimeError("Los algoritmos produjeron órdenes distintos.")

        resultados.append(
            (
                tamano,
                tiempo_insertion,
                tiempo_merge,
                comp_insertion,
                comp_merge,
            )
        )

    return resultados


def graficar(resultados: list[tuple[int, float, float, int, int]]) -> None:
    """Genera la gráfica comparativa de tiempo de la Parte 4.

    Args:
        resultados: mediciones obtenidas para ambos algoritmos.
    """
    carpeta = Path(__file__).resolve().parent / "graficas"
    carpeta.mkdir(exist_ok=True)

    tamanos = [resultado[0] for resultado in resultados]
    tiempos_insertion = [resultado[1] * 1000 for resultado in resultados]
    tiempos_merge = [resultado[2] * 1000 for resultado in resultados]

    figura, eje = plt.subplots(figsize=(9, 5.5))
    eje.plot(tamanos, tiempos_insertion, marker="o", label="Insertion sort")
    eje.plot(tamanos, tiempos_merge, marker="o", label="Merge sort")
    eje.set_title("Tiempo de ordenamiento en el escenario aleatorio")
    eje.set_xlabel("Tamaño de entrada (registros)")
    eje.set_ylabel("Tiempo mediano (milisegundos)")
    eje.grid(alpha=0.3)
    eje.legend()
    figura.tight_layout()
    figura.savefig(carpeta / "parte4_tiempo.png", dpi=160)
    plt.close(figura)


def mostrar_resultados(
    resultados: list[tuple[int, float, float, int, int]],
) -> None:
    """Muestra las mediciones comparativas en la terminal.

    Args:
        resultados: mediciones obtenidas para ambos algoritmos.
    """
    print("tamaño;insertion_ms;merge_ms;comp_insertion;comp_merge")
    for resultado in resultados:
        tamano, tiempo_insertion, tiempo_merge, comp_insertion, comp_merge = (
            resultado
        )
        print(
            f"{tamano};{tiempo_insertion * 1000:.6f};"
            f"{tiempo_merge * 1000:.6f};{comp_insertion};{comp_merge}"
        )


def main() -> None:
    """Ejecuta la comparación, muestra los datos y crea la gráfica."""
    resultados = ejecutar_experimento()
    mostrar_resultados(resultados)
    graficar(resultados)


if __name__ == "__main__":
    main()
