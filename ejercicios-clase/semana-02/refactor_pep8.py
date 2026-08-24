def calcular_promedio(lista: list[int]) -> float:
    """Calcula el promedio de una lista de números enteros.

    Args:
        lista: Números enteros cuyo promedio se calculará.

    Returns:
        El promedio de los números recibidos.
    """
    suma = 0
    for numero in lista:
        suma = suma + numero
    return suma / len(lista)


def main() -> None:
    """Calcula y muestra el promedio de una lista de ejemplo."""
    numeros = [1, 2, 3, 4, 5]
    print(calcular_promedio(numeros))


if __name__ == "__main__":
    main()
