NUMERO_MAXIMO: int = 20
NUMERO_MINIMO: int = 0


def validar_numero(numero: int) -> None:
    if numero < NUMERO_MINIMO or numero > NUMERO_MAXIMO:
        raise ValueError("Error: el número debe estar en el rango " + 
                         f"{NUMERO_MINIMO}-{NUMERO_MAXIMO}")


def convertir_entero(entrada: str) -> int:
    try:
        return int(entrada)
    except ValueError:
        raise ValueError("**Error: entrada no válida! debe ser un número entero**")


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
        raise ValueError("**Error: debe responder 's' o 'n'**")


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


def borrar_consola(num_lineas: int = 50) -> None:
    print("\n" * num_lineas, end="")

    # Alternativa mediante un bucle:
    #
    # for _ in range(num_lineas):
    #     print()
    #
    # El guion de la actividad exige utilizar un bucle.


def linea_piramide_ascendente(n: int) -> str:
    linea: str = f"{n} => 0 "
    cont: int = 1
    total: int = 0

    while cont <= n:
        linea += f"+ {cont} "
        total += cont
        cont += 1

    if n > 0:
        linea += f"= {total}"

    # Alternativa utilizando join():
    #
    # sumandos = " + ".join(str(i) for i in range(n + 1))
    # linea = f"{n} => {sumandos}"
    # if n > 0:
    #     linea += f" = {sum(range(n + 1))}"
    #
    # join() evita concatenaciones sucesivas de cadenas.

    return linea


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

    # Alternativa utilizando join():
    #
    # sumandos = " + ".join(str(i) for i in range(n, -1, -1))
    # linea = f"{n} => {sumandos}"
    # if n > 0:
    #     linea += f" = {sum(range(n + 1))}"

    return linea


def piramide_descendente(num: int) -> str:
    res: str = ""
    n: int = num

    while n >= 0:
        res += linea_piramide_descendente(n) + "\n"
        n -= 1

    return res

    # Alternativa: almacenar las líneas en una lista y
    # unirlas al final mediante "\n".join(...).
    # Esto evita concatenaciones sucesivas de cadenas.
    # lineas: list[str] = []

    # for n in range(num, -1, -1):
    #     lineas.append(linea_piramide_descendente(n))

    # return "\n".join(lineas) + "\n"    

    # Otra alternativa más compacta y elegante...
    # con una "expresión generadora" dentro de join().
    # En lugar de construir una lista con todas las líneas, 
    # va produciendo cada cadena conforme join() la solicita.

    # return "\n".join(
    #     linea_piramide_descendente(n)
    #     for n in range(num, -1, -1)
    # ) + "\n"


def piramide_ascendente(num: int) -> str:
    res: str = ""
    n: int = 1

    while n <= num:
        res += linea_piramide_ascendente(n) + "\n"
        n += 1

    return res


def main() -> None:
    continuar: bool = True

    while continuar:
        numero: int = leer_numero("Introduzca un número: ")

        piramide_completa: str = (
            piramide_descendente(numero) + piramide_ascendente(numero)
        )

        print(
            f"\nSu pirámide de sumas es la siguiente:\n{piramide_completa}",
            end=""
        )

        continuar = leer_respuesta("¿Quiere hacer otra pirámide? (s/n) ")

    borrar_consola()
    print("¡¡¡PROGRAMA FINALIZADO!!!")


if __name__ == "__main__":
    main()
