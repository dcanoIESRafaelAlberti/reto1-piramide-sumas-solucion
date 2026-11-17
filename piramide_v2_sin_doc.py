NUMERO_MAXIMO: int = 20
NUMERO_MINIMO: int = 0


def validar_numero(numero: int) -> None:
    if numero < NUMERO_MINIMO or numero > NUMERO_MAXIMO:
        raise ValueError("Error: el número debe estar en el rango 0-20")


def convertir_entero(entrada: str) -> int:
    try:
        return int(entrada)
    except ValueError:
        raise ValueError(
            "Error: debe introducir un número entero"
        ) from None



def leer_numero(mensaje: str = "") -> int:
    numero: int | None = None

    while numero is None:
        entrada: str = input(mensaje)

        try:
            valor: int = convertir_entero(entrada)
            validar_numero(valor)
        except ValueError as e:
            print(e)
        else:
            numero = valor

    return numero


def validar_respuesta(respuesta: str) -> None:
    if respuesta not in ("S", "N"):
        raise ValueError("Error: debe responder 's' o 'n'")


def leer_respuesta(mensaje: str = "") -> bool:
    respuesta: str | None = None

    while respuesta is None:
        entrada: str = input(mensaje).strip().upper()

        try:
            validar_respuesta(entrada)
        except ValueError as e:
            print(e)
        else:
            respuesta = entrada

    return respuesta == "S"


def linea_piramide_descendente(n: int) -> str:
    linea: str = f"{n} => "
    cont: int = n
    total: int = 0

    while cont > 0:
        linea += f"{cont} + "
        total += cont
        cont -= 1

    linea += "0"

    if n > 0:
        linea += f" = {total}"

    return linea


def piramide_descendente(num: int) -> str:
    res: str = ""
    n: int = num

    while n >= 0:
        res += linea_piramide_descendente(n) + "\n"
        n -= 1

    return res


def main() -> None:
    continuar: bool = True

    while continuar:
        numero: int = leer_numero("Introduzca un número: ")
        piramide: str = piramide_descendente(numero)

        print(
            f"\nSu pirámide de sumas es la siguiente:\n{piramide}",
            end=""
        )

        continuar = leer_respuesta(
            "¿Quiere hacer otra pirámide? (s/n) "
        )


if __name__ == "__main__":
    main()
