
def validar_numero(numero: int) -> None:
    if numero < 0:
        raise ValueError("Error: el número no puede ser negativo")


def convertir_entero(entrada: str) -> int:
    try:
        return int(entrada)
    except ValueError:
        raise ValueError("Error: debe introducir un número entero") from None


def leer_numero(mensaje: str = "") -> int:
    entrada: str = input(mensaje)
    numero: int = convertir_entero(entrada)
    validar_numero(numero)

    return numero


def linea_piramide(n: int) -> str:
    linea: str = f"{n} => 0 "
    cont: int = 1
    total: int = 0

    while cont <= n:
        linea += f"+ {cont} "
        total += cont
        cont += 1

    if n > 0:
        linea += f"= {total}"

    return linea


def piramide_descendente(num: int) -> str:
    res: str = ""
    n: int = num

    while n >= 0:
        res += linea_piramide(n) + "\n"
        n -= 1

    return res


def main() -> None:
    try:
        numero: int = leer_numero("Introduzca un número: ")
    except ValueError as e:
        print(e)
    else:
        piramide: str = piramide_descendente(numero)
        print(f"\nSu pirámide de sumas es la siguiente:\n{piramide}", end="")


if __name__ == "__main__":
    main()
