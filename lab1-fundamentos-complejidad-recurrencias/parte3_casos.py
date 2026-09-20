"""Mide insertion sort sobre los tres escenarios de entrada de Tamiza."""

from collections.abc import Callable
from pathlib import Path
from statistics import median
from time import perf_counter

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from algoritmos import insertion_sort
from datos import generar_aleatorio, generar_casi_ordenado, generar_inverso

TAMANOS = [100, 200, 400, 800, 1600, 3200, 6400]
REPETICIONES = 3
GENERADORES: tuple[tuple[str, Callable[[int], list[int]]], ...] = (
    ("A - Aleatorio", generar_aleatorio),
    ("B - Casi ordenado", generar_casi_ordenado),
    ("C - Orden inverso", generar_inverso),
)


def medir_escenario(datos: list[int]) -> tuple[float, int]:
    """Mide insertion sort y retorna la mediana en segundos y comparaciones."""
    tiempos = []
    comparaciones = 0

    for _ in range(REPETICIONES):
        inicio = perf_counter()
        _, comparaciones_actuales = insertion_sort(datos)
        fin = perf_counter()
        tiempos.append(fin - inicio)

        if comparaciones and comparaciones != comparaciones_actuales:
            raise RuntimeError("El conteo de comparaciones cambió entre pruebas.")
        comparaciones = comparaciones_actuales

    return median(tiempos), comparaciones


def ejecutar_experimento() -> dict[str, list[tuple[int, float, int]]]:
    """Ejecuta las mediciones de todos los tamaños y escenarios."""
    resultados = {nombre: [] for nombre, _ in GENERADORES}

    for tamano in TAMANOS:
        for nombre, generador in GENERADORES:
            datos = generador(tamano)
            tiempo, comparaciones = medir_escenario(datos)
            resultados[nombre].append((tamano, tiempo, comparaciones))

    return resultados


def graficar(resultados: dict[str, list[tuple[int, float, int]]]) -> None:
    """Genera las gráficas de comparaciones y tiempo de la Parte 3."""
    carpeta = Path(__file__).resolve().parent / "graficas"
    carpeta.mkdir(exist_ok=True)

    figura, eje = plt.subplots(figsize=(9, 5.5))
    for escenario, mediciones in resultados.items():
        tamanos = [medicion[0] for medicion in mediciones]
        comparaciones = [medicion[2] for medicion in mediciones]
        eje.plot(tamanos, comparaciones, marker="o", label=escenario)
    eje.set_title("Comparaciones de insertion sort por escenario")
    eje.set_xlabel("Tamaño de entrada (registros)")
    eje.set_ylabel("Comparaciones entre elementos")
    eje.grid(alpha=0.3)
    eje.legend()
    figura.tight_layout()
    figura.savefig(carpeta / "parte3_comparaciones.png", dpi=160)
    plt.close(figura)

    figura, eje = plt.subplots(figsize=(9, 5.5))
    for escenario, mediciones in resultados.items():
        tamanos = [medicion[0] for medicion in mediciones]
        tiempos_ms = [medicion[1] * 1000 for medicion in mediciones]
        eje.plot(tamanos, tiempos_ms, marker="o", label=escenario)
    eje.set_title("Tiempo de insertion sort por escenario")
    eje.set_xlabel("Tamaño de entrada (registros)")
    eje.set_ylabel("Tiempo mediano (milisegundos)")
    eje.grid(alpha=0.3)
    eje.legend()
    figura.tight_layout()
    figura.savefig(carpeta / "parte3_tiempo.png", dpi=160)
    plt.close(figura)


def mostrar_resultados(
    resultados: dict[str, list[tuple[int, float, int]]],
) -> None:
    """Muestra una tabla de mediciones en la terminal."""
    print("escenario;tamaño;tiempo_ms;comparaciones")
    for escenario, mediciones in resultados.items():
        for tamano, tiempo, comparaciones in mediciones:
            print(
                f"{escenario};{tamano};{tiempo * 1000:.6f};"
                f"{comparaciones}"
            )


def main() -> None:
    """Ejecuta el experimento, muestra sus datos y crea las gráficas."""
    resultados = ejecutar_experimento()
    mostrar_resultados(resultados)
    graficar(resultados)


if __name__ == "__main__":
    main()
