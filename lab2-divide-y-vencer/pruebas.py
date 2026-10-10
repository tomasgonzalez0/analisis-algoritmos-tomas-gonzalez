"""Pruebas reproducibles para los algoritmos de subarreglo máximo."""

import random

from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo


def verificar_resultado(
    valores: list[float], resultado: tuple[int, int, float]
) -> None:
    """Comprueba que los índices y la suma de un resultado sean coherentes."""
    inicio, fin, suma = resultado
    assert 0 <= inicio <= fin < len(valores)
    assert abs(sum(valores[inicio:fin + 1]) - suma) < 1e-9


def comparar_algoritmos(valores: list[float], suma_esperada: float) -> None:
    """Verifica suma, coherencia y preservación de la entrada."""
    copia = valores.copy()
    resultado_fuerza = subarreglo_fuerza_bruta(valores)
    resultado_divide = subarreglo_maximo(valores, 0, len(valores) - 1)

    verificar_resultado(valores, resultado_fuerza)
    verificar_resultado(valores, resultado_divide)
    assert abs(resultado_fuerza[2] - suma_esperada) < 1e-9
    assert abs(resultado_divide[2] - suma_esperada) < 1e-9
    assert abs(resultado_fuerza[2] - resultado_divide[2]) < 1e-9
    assert valores == copia


def probar_casos_conocidos() -> None:
    """Ejecuta los casos deterministas requeridos por la guía."""
    comparar_algoritmos([-3, 5, -2, 8, -6, 3, 9, -4], 17)
    comparar_algoritmos([-7.5], -7.5)
    comparar_algoritmos([-8, -3, -5, -11], -3)
    comparar_algoritmos([1, 2, 3.5, 4], 10.5)
    comparar_algoritmos([-5, 4, -1, 3, -2], 6)
    comparar_algoritmos([2, -2, 2], 2)
    comparar_algoritmos([1.25, -0.5, 2.75, -5.0], 3.5)


def probar_listas_aleatorias() -> None:
    """Compara ambos algoritmos sobre cuarenta listas reproducibles."""
    generador = random.Random(20261003)

    for _ in range(40):
        tamano = generador.randint(1, 60)
        valores = [generador.randint(-100, 100) for _ in range(tamano)]
        copia = valores.copy()
        resultado_fuerza = subarreglo_fuerza_bruta(valores)
        resultado_divide = subarreglo_maximo(valores, 0, tamano - 1)

        verificar_resultado(valores, resultado_fuerza)
        verificar_resultado(valores, resultado_divide)
        assert resultado_fuerza[2] == resultado_divide[2]
        assert valores == copia


def main() -> None:
    """Ejecuta todas las pruebas y muestra un resumen breve."""
    probar_casos_conocidos()
    probar_listas_aleatorias()
    print("Pruebas superadas: 7 casos conocidos y 40 listas aleatorias.")


if __name__ == "__main__":
    main()
