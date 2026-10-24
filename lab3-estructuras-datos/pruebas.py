"""Pruebas de la lista enlazada y la tabla hash."""

import random

from estructuras import ListaEnlazada, TablaHash


def probar_lista_enlazada() -> None:
    """Verifica insercion, busqueda y tamano de la lista."""
    lista = ListaEnlazada()
    assert lista.tamano == 0
    assert lista.buscar(1000000010) is None

    lista.insertar(1000000010, "en bodega")
    lista.insertar(1000000024, "en reparto")
    lista.insertar(1000000005, "entregado")

    assert lista.tamano == 3
    assert lista.cabeza is not None
    assert lista.cabeza.guia == 1000000005
    assert lista.buscar(1000000010) == "en bodega"
    assert lista.buscar(1000000024) == "en reparto"
    assert lista.buscar(1000000005) == "entregado"
    assert lista.buscar(9999999999) is None


def probar_tabla_hash() -> None:
    """Verifica busquedas, colisiones y factor de carga de la tabla."""
    tabla = TablaHash(7)
    datos = (
        (10, "en bodega"),
        (24, "en reparto"),
        (17, "entregado"),
    )
    for guia, estado in datos:
        assert tabla.hash(guia) == 3
        tabla.insertar(guia, estado)

    assert tabla.tamano == 3
    assert tabla.casillas[3].tamano == 3
    assert tabla.buscar(10) == "en bodega"
    assert tabla.buscar(24) == "en reparto"
    assert tabla.buscar(17) == "entregado"
    assert tabla.buscar(99) is None
    assert tabla.factor_carga() == 3 / 7


def probar_colecciones_aleatorias() -> None:
    """Compara ambas estructuras en treinta colecciones reproducibles."""
    azar = random.Random(20261024)
    estados = ("en bodega", "en reparto", "entregado", "devuelto")

    for numero_coleccion in range(30):
        cantidad = azar.randint(10, 150)
        guias = azar.sample(range(10**9, 10**10), cantidad)
        lista = ListaEnlazada()
        tabla = TablaHash(53 + numero_coleccion)

        for posicion, guia in enumerate(guias):
            estado = estados[posicion % len(estados)]
            lista.insertar(guia, estado)
            tabla.insertar(guia, estado)

        for guia in guias:
            assert lista.buscar(guia) == tabla.buscar(guia)

        existentes = set(guias)
        inexistentes: list[int] = []
        while len(inexistentes) < 10:
            guia = azar.randint(10**9, 10**10 - 1)
            if guia not in existentes:
                inexistentes.append(guia)

        for guia in inexistentes:
            assert lista.buscar(guia) is None
            assert lista.buscar(guia) == tabla.buscar(guia)


def main() -> None:
    """Ejecuta todas las pruebas disponibles."""
    probar_lista_enlazada()
    probar_tabla_hash()
    probar_colecciones_aleatorias()
    print("Todas las pruebas fueron superadas.")


if __name__ == "__main__":
    main()
