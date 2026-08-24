def es_bisiesto(anio: int) -> bool:
    """Determina si un año es bisiesto según las reglas del calendario."""
    if anio % 400 == 0:
        return True
    elif anio % 100 == 0:
        return False
    elif anio % 4 == 0:
        return True
    else:
        return False


def leer_anios() -> list[int]:
    """Solicita años separados por comas hasta recibir valores enteros."""
    while True:
        entrada = input("Ingrese años separados por comas: ")
        try:
            return [int(elemento.strip()) for elemento in entrada.split(",")]
        except ValueError:
            print("Entrada inválida. Ingrese únicamente años enteros.")


def main() -> None:
    """Lee, clasifica y muestra una lista de años."""
    anios = leer_anios()
    anios_bisiestos = [anio for anio in anios if es_bisiesto(anio)]

    print(f"Años ingresados: {anios}")
    print(f"Años bisiestos: {anios_bisiestos}")
    print(
        f"Cantidad de años bisiestos: {len(anios_bisiestos)} "
        f"de {len(anios)}"
    )


if __name__ == "__main__":
    main()
