"""Generadores de lotes de registros para los escenarios de Tamiza."""

import random


def generar_aleatorio(n: int, semilla: int = 42) -> list[int]:
    """Genera un lote de n registros en orden aleatorio (escenario A).

    Args:
        n: cantidad de registros del lote.
        semilla: semilla del generador aleatorio, para que el
            experimento sea reproducible.

    Returns:
        Lista de n indices de riesgo enteros distintos, desordenada.
    """
    if n < 0:
        raise ValueError("El tamaño del lote no puede ser negativo.")

    valores = list(range(n))
    random.Random(semilla).shuffle(valores)
    return valores


def generar_casi_ordenado(n: int, semilla: int = 42) -> list[int]:
    """Genera un lote casi ordenado: 98% ordenado y 2% al final (escenario B).

    Args:
        n: cantidad de registros del lote.
        semilla: semilla del generador aleatorio.

    Returns:
        Lista de n indices de riesgo enteros distintos, con el primer
        98% en el orden que el algoritmo produce y el 2% restante
        desordenado al final.
    """
    if n < 0:
        raise ValueError("El tamaño del lote no puede ser negativo.")

    cantidad_ordenada = int(n * 0.98)
    limite_cola = n - cantidad_ordenada
    parte_ordenada = list(range(n - 1, limite_cola - 1, -1))
    parte_desordenada = list(range(limite_cola))
    random.Random(semilla).shuffle(parte_desordenada)
    cola_descendente = all(
        parte_desordenada[indice] > parte_desordenada[indice + 1]
        for indice in range(len(parte_desordenada) - 1)
    )
    if len(parte_desordenada) > 1 and cola_descendente:
        parte_desordenada[0], parte_desordenada[-1] = (
            parte_desordenada[-1],
            parte_desordenada[0],
        )
    return parte_ordenada + parte_desordenada


def generar_inverso(n: int) -> list[int]:
    """Genera un lote en el orden exactamente contrario (escenario C).

    Args:
        n: cantidad de registros del lote.

    Returns:
        Lista de n indices de riesgo enteros distintos, en el orden
        inverso al que el algoritmo debe producir.
    """
    if n < 0:
        raise ValueError("El tamaño del lote no puede ser negativo.")

    return list(range(n))
