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


def merge_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de indices de riesgo con el metodo de mezcla.

    No modifica la lista recibida: trabaja sobre una copia.

    Args:
        datos: lista de indices de riesgo a ordenar.

    Returns:
        Una tupla con la lista ordenada y el numero total de
        comparaciones entre elementos realizadas durante el proceso.
    """
    return _ordenar_por_mezcla(datos.copy())


def _ordenar_por_mezcla(datos: list[int]) -> tuple[list[int], int]:
    """Divide una lista, ordena sus mitades y contabiliza comparaciones.

    Args:
        datos: lista que se dividirá y ordenará de forma recursiva.

    Returns:
        Lista descendente y total de comparaciones entre sus elementos.
    """
    if len(datos) <= 1:
        return datos.copy(), 0

    mitad = len(datos) // 2
    izquierda, comparaciones_izquierda = _ordenar_por_mezcla(datos[:mitad])
    derecha, comparaciones_derecha = _ordenar_por_mezcla(datos[mitad:])
    mezcla, comparaciones_mezcla = _mezclar(izquierda, derecha)

    comparaciones = (
        comparaciones_izquierda
        + comparaciones_derecha
        + comparaciones_mezcla
    )
    return mezcla, comparaciones


def _mezclar(
    izquierda: list[int], derecha: list[int]
) -> tuple[list[int], int]:
    """Combina dos listas descendentes y cuenta comparaciones de elementos.

    Args:
        izquierda: primera mitad ordenada de forma descendente.
        derecha: segunda mitad ordenada de forma descendente.

    Returns:
        Lista combinada y comparaciones hechas durante la mezcla.
    """
    resultado = []
    indice_izquierdo = 0
    indice_derecho = 0
    comparaciones = 0

    while (
        indice_izquierdo < len(izquierda)
        and indice_derecho < len(derecha)
    ):
        comparaciones += 1
        if izquierda[indice_izquierdo] >= derecha[indice_derecho]:
            resultado.append(izquierda[indice_izquierdo])
            indice_izquierdo += 1
        else:
            resultado.append(derecha[indice_derecho])
            indice_derecho += 1

    resultado.extend(izquierda[indice_izquierdo:])
    resultado.extend(derecha[indice_derecho:])
    return resultado, comparaciones
