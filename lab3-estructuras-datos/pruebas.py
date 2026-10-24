"""Pruebas de la lista enlazada y la tabla hash."""

from estructuras import ListaEnlazada


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


def main() -> None:
    """Ejecuta todas las pruebas disponibles."""
    probar_lista_enlazada()
    print("Pruebas de la lista enlazada superadas.")


if __name__ == "__main__":
    main()
