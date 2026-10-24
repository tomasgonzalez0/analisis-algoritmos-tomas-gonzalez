"""Experimentos de busqueda con una lista enlazada y una tabla hash."""

import math
import random
import statistics
import time
from collections.abc import Callable
from pathlib import Path

import matplotlib.pyplot as plt

from estructuras import ListaEnlazada, TablaHash

TAMANOS = (100, 500, 1000, 5000, 20000, 50000)
ALFAS_OBJETIVO = (0.25, 0.5, 1.0, 2.0, 4.0, 10.0)
CANTIDAD_CONSULTAS = 200
REPETICIONES = 5
ESTADOS = ("en bodega", "en reparto", "entregado", "devuelto")


def generar_guias_inexistentes(
    existentes: set[int], cantidad: int, semilla: int = 7
) -> list[int]:
    """Genera guias de diez digitos que no estan en la coleccion.

    Args:
        existentes: guias almacenadas en las estructuras.
        cantidad: cuantas guias inexistentes generar.
        semilla: semilla del generador, para reproducir la medicion.

    Returns:
        Una lista con `cantidad` guias que no pertenecen a `existentes`.
    """
    azar = random.Random(semilla)
    inexistentes: list[int] = []
    while len(inexistentes) < cantidad:
        guia = azar.randint(10**9, 10**10 - 1)
        if guia not in existentes:
            inexistentes.append(guia)
    return inexistentes


def generar_guias(cantidad: int, semilla: int) -> list[int]:
    """Genera guias distintas de diez digitos.

    Args:
        cantidad: numero de guias requeridas.
        semilla: semilla usada para obtener el mismo conjunto.

    Returns:
        Una lista reproducible de guias diferentes.
    """
    azar = random.Random(semilla)
    return azar.sample(range(10**9, 10**10), cantidad)


def es_primo(numero: int) -> bool:
    """Determina si un entero es primo.

    Args:
        numero: entero que se quiere evaluar.

    Returns:
        True si el numero es primo; de lo contrario, False.
    """
    if numero < 2:
        return False
    if numero == 2:
        return True
    if numero % 2 == 0:
        return False
    limite = math.isqrt(numero)
    divisor = 3
    while divisor <= limite:
        if numero % divisor == 0:
            return False
        divisor += 2
    return True


def primo_desde(numero: int) -> int:
    """Encuentra el primer primo mayor o igual que un numero.

    Args:
        numero: punto inicial de la busqueda.

    Returns:
        El primer numero primo desde el valor indicado.
    """
    candidato = max(2, numero)
    while not es_primo(candidato):
        candidato += 1
    return candidato


def insertar_datos(
    guias: list[int], lista: ListaEnlazada, tabla: TablaHash
) -> None:
    """Inserta los mismos envios en las dos estructuras.

    Args:
        guias: numeros de guia que se van a almacenar.
        lista: lista enlazada que recibira los datos.
        tabla: tabla hash que recibira los datos.
    """
    for posicion, guia in enumerate(guias):
        estado = ESTADOS[posicion % len(ESTADOS)]
        lista.insertar(guia, estado)
        tabla.insertar(guia, estado)


def verificar_muestra(
    guias: list[int], lista: ListaEnlazada, tabla: TablaHash
) -> None:
    """Comprueba una muestra de guias existentes en ambas estructuras.

    Args:
        guias: numeros almacenados en las estructuras.
        lista: lista enlazada que se quiere verificar.
        tabla: tabla hash que se quiere verificar.

    Raises:
        AssertionError: si alguna estructura devuelve un estado incorrecto.
    """
    cantidad = min(10, len(guias))
    posiciones = random.Random(31).sample(range(len(guias)), cantidad)
    for posicion in posiciones:
        guia = guias[posicion]
        esperado = ESTADOS[posicion % len(ESTADOS)]
        assert lista.buscar(guia) == esperado
        assert tabla.buscar(guia) == esperado


def medir_busquedas(
    buscar: Callable[[int], str | None], consultas: list[int]
) -> float:
    """Mide lotes de busquedas y obtiene la mediana de sus promedios.

    Args:
        buscar: metodo de busqueda de la estructura evaluada.
        consultas: guias que se consultaran en cada repeticion.

    Returns:
        Mediana del tiempo medio por busqueda, en microsegundos.
    """
    assert all(buscar(guia) is None for guia in consultas)
    promedios: list[float] = []
    for _ in range(REPETICIONES):
        inicio = time.perf_counter()
        for guia in consultas:
            buscar(guia)
        duracion = time.perf_counter() - inicio
        promedios.append(duracion / len(consultas) * 1_000_000)
    return statistics.median(promedios)


def ejecutar_experimento_a() -> list[tuple[int, int, float, float, float]]:
    """Compara busquedas fallidas en lista y tabla para varios tamanos.

    Returns:
        Filas con n, m, alfa y los tiempos de lista y tabla.
    """
    resultados: list[tuple[int, int, float, float, float]] = []
    for cantidad in TAMANOS:
        guias = generar_guias(cantidad, 1000 + cantidad)
        m = primo_desde(round(cantidad / 2))
        lista = ListaEnlazada()
        tabla = TablaHash(m)
        insertar_datos(guias, lista, tabla)
        verificar_muestra(guias, lista, tabla)
        consultas = generar_guias_inexistentes(
            set(guias), CANTIDAD_CONSULTAS, 700 + cantidad
        )
        tiempo_lista = medir_busquedas(lista.buscar, consultas)
        tiempo_tabla = medir_busquedas(tabla.buscar, consultas)
        resultados.append(
            (
                cantidad,
                m,
                tabla.factor_carga(),
                tiempo_lista,
                tiempo_tabla,
            )
        )
    return resultados


def ejecutar_experimento_b() -> list[tuple[int, float, float]]:
    """Mide el efecto del factor de carga sobre la tabla hash.

    Returns:
        Filas con m, factor de carga real y tiempo por busqueda.
    """
    cantidad = 20000
    guias = generar_guias(cantidad, 30000)
    existentes = set(guias)
    consultas = generar_guias_inexistentes(
        existentes, CANTIDAD_CONSULTAS, 2700
    )
    resultados: list[tuple[int, float, float]] = []

    for alfa_objetivo in ALFAS_OBJETIVO:
        m = primo_desde(round(cantidad / alfa_objetivo))
        tabla = TablaHash(m)
        lista_referencia = ListaEnlazada()
        insertar_datos(guias, lista_referencia, tabla)
        verificar_muestra(guias, lista_referencia, tabla)
        tiempo_tabla = medir_busquedas(tabla.buscar, consultas)
        resultados.append((m, tabla.factor_carga(), tiempo_tabla))
    return resultados


def graficar_experimento_a(
    resultados: list[tuple[int, int, float, float, float]], ruta: Path
) -> None:
    """Genera las vistas lineal y logaritmica del primer experimento.

    Args:
        resultados: mediciones obtenidas para ambas estructuras.
        ruta: archivo PNG donde se guardara la figura.
    """
    tamanos = [fila[0] for fila in resultados]
    tiempos_lista = [fila[3] for fila in resultados]
    tiempos_tabla = [fila[4] for fila in resultados]
    figura, ejes = plt.subplots(1, 2, figsize=(12, 5))

    for eje in ejes:
        eje.plot(tamanos, tiempos_lista, "o-", label="Lista enlazada")
        eje.plot(tamanos, tiempos_tabla, "s-", label="Tabla hash")
        eje.set_xlabel("Número de guías, n")
        eje.set_ylabel("Tiempo medio por búsqueda (µs)")
        eje.grid(True, alpha=0.3)
        eje.legend()

    ejes[0].set_title("Escala lineal")
    ejes[1].set_title("Escala logarítmica")
    ejes[1].set_xscale("log")
    ejes[1].set_yscale("log")
    figura.suptitle("Búsquedas fallidas: lista enlazada frente a tabla hash")
    figura.tight_layout()
    figura.savefig(ruta, dpi=180, bbox_inches="tight")
    plt.close(figura)


def graficar_experimento_b(
    resultados: list[tuple[int, float, float]], ruta: Path
) -> None:
    """Genera la grafica del tiempo frente al factor de carga.

    Args:
        resultados: mediciones para los diferentes factores de carga.
        ruta: archivo PNG donde se guardara la figura.
    """
    factores = [fila[1] for fila in resultados]
    tiempos = [fila[2] for fila in resultados]
    figura, eje = plt.subplots(figsize=(7, 5))
    eje.plot(factores, tiempos, "o-", label="Tabla hash")
    eje.set_title("Búsquedas fallidas según el factor de carga")
    eje.set_xlabel("Factor de carga, α = n / m")
    eje.set_ylabel("Tiempo medio por búsqueda (µs)")
    eje.grid(True, alpha=0.3)
    eje.legend()
    figura.tight_layout()
    figura.savefig(ruta, dpi=180, bbox_inches="tight")
    plt.close(figura)


def mostrar_resultados_a(
    resultados: list[tuple[int, int, float, float, float]],
) -> None:
    """Imprime la tabla del primer experimento.

    Args:
        resultados: mediciones de lista y tabla hash.
    """
    print("Experimento A")
    print("n | m | alfa | lista_us | tabla_us")
    for n, m, alfa, tiempo_lista, tiempo_tabla in resultados:
        print(
            f"{n} | {m} | {alfa:.4f} | "
            f"{tiempo_lista:.4f} | {tiempo_tabla:.4f}"
        )


def mostrar_resultados_b(
    resultados: list[tuple[int, float, float]],
) -> None:
    """Imprime la tabla del segundo experimento.

    Args:
        resultados: mediciones para varios factores de carga.
    """
    print("\nExperimento B: n = 20000")
    print("m | alfa | tabla_us")
    for m, alfa, tiempo_tabla in resultados:
        print(f"{m} | {alfa:.4f} | {tiempo_tabla:.4f}")


def main() -> None:
    """Ejecuta los experimentos, imprime resultados y crea las graficas."""
    carpeta_graficas = Path(__file__).parent / "graficas"
    carpeta_graficas.mkdir(exist_ok=True)
    resultados_a = ejecutar_experimento_a()
    resultados_b = ejecutar_experimento_b()
    graficar_experimento_a(
        resultados_a, carpeta_graficas / "lista_vs_tabla.png"
    )
    graficar_experimento_b(
        resultados_b, carpeta_graficas / "tiempo_vs_alfa.png"
    )
    mostrar_resultados_a(resultados_a)
    mostrar_resultados_b(resultados_b)


if __name__ == "__main__":
    main()
