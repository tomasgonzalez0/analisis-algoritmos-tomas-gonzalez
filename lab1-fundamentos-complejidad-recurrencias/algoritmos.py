"""Algoritmos de ordenamiento instrumentados para el Laboratorio 1."""


def insertion_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de indices de riesgo con el metodo de insercion.

    No modifica la lista recibida: trabaja sobre una copia.

    Args:
        datos: lista de indices de riesgo a ordenar.

    Returns:
        Una tupla con la lista ordenada y el numero total de
        comparaciones entre elementos realizadas durante el proceso.
    """
    ordenados = datos.copy()
    comparaciones = 0

    for indice in range(1, len(ordenados)):
        clave = ordenados[indice]
        posicion = indice - 1

        while posicion >= 0:
            comparaciones += 1
            if ordenados[posicion] >= clave:
                break
            ordenados[posicion + 1] = ordenados[posicion]
            posicion -= 1

        ordenados[posicion + 1] = clave

    return ordenados, comparaciones
