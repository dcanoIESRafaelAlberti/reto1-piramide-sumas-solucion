
def validar_numero(numero: int) -> None:
    """
    Comprueba que un número entero no sea negativo.

    Args:
        numero: Número entero que se desea validar.

    Raises:
        ValueError: Si el número es negativo.
    """
    if numero < 0:
        raise ValueError("Error: el número no puede ser negativo")


def convertir_entero(entrada: str) -> int:
    """
    Convierte una cadena de texto en un número entero.

    Args:
        entrada: Cadena de texto que se desea convertir.

    Returns:
        Número entero obtenido de la conversión.

    Raises:
        ValueError: Si la entrada no representa un número entero.
    """
    try:
        return int(entrada)
    except ValueError:
        raise ValueError("Error: debe introducir un número entero") from None


def leer_numero(mensaje: str = "") -> int:
    """
    Solicita un número entero no negativo.

    Args:
        mensaje: Texto que se muestra al solicitar el número.

    Returns:
        Número entero válido introducido por el usuario.

    Raises:
        ValueError: Si la entrada no es un entero no negativo.
    """
    entrada: str = input(mensaje)
    numero: int = convertir_entero(entrada)
    validar_numero(numero)

    return numero


def linea_piramide(n: int) -> str:
    """
    Construye una línea de la pirámide de sumas.

    Los sumandos aparecen ordenados desde 0 hasta n.

    Args:
        n: Número que determina el último sumando.

    Returns:
        Cadena con la operación y su resultado.
        Para n=3: '3 => 0 + 1 + 2 + 3 = 6'.
    """
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
    """
    Construye una pirámide descendente de sumas.

    Genera las líneas desde num hasta 0.

    Args:
        num: Número inicial de la pirámide.

    Returns:
        Cadena con todas las líneas de la pirámide.
    """
    res: str = ""
    n: int = num

    while n >= 0:
        res += linea_piramide(n) + "\n"
        n -= 1

    return res


def main() -> None:
    """
    Ejecuta el programa principal.

    Solicita un número entero no negativo y muestra
    su pirámide descendente de sumas.

    Si la entrada no es válida, muestra un mensaje
    de error y finaliza el programa.
    """
    try:
        numero: int = leer_numero("Introduzca un número: ")
    except ValueError as e:
        print(e)
    else:
        piramide: str = piramide_descendente(numero)
        print(f"\nSu pirámide de sumas es la siguiente:\n{piramide}", end="")


if __name__ == "__main__":
    main()
