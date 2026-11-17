
def validar_numero(numero: int) -> None:
    """
    Comprueba que un número esté dentro del intervalo permitido.

    Args:
        numero: Número entero que se desea validar.

    Raises:
        ValueError: Si el número no está comprendido entre 0 y 20.
    """
    if numero < 0 or numero > 20:
        raise ValueError("Error: el número debe estar en el rango 0-20")


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
        raise ValueError(
            "Error: debe introducir un número entero"
        ) from None



def leer_numero(mensaje: str = "") -> int:
    """
    Solicita un número entero comprendido entre 0 y 20.

    Repite la petición mientras el usuario no introduzca
    un número que pueda convertirse a entero y que esté
    dentro del intervalo permitido.

    Args:
        mensaje: Texto que se muestra al solicitar el número.

    Returns:
        Número entero válido introducido por el usuario.
    """
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
    """
    Comprueba que una respuesta sea 'S' o 'N'.

    Args:
        respuesta: Respuesta previamente normalizada a mayúsculas
            y sin espacios iniciales ni finales.

    Raises:
        ValueError: Si la respuesta no es 'S' ni 'N'.
    """
    if respuesta not in ("S", "N"):
        raise ValueError("Error: debe responder 's' o 'n'")


def leer_respuesta(mensaje: str = "") -> bool:
    """
    Solicita una respuesta afirmativa o negativa.

    Repite la petición hasta recibir una respuesta válida,
    sin distinguir mayúsculas y minúsculas ni considerar
    los espacios iniciales y finales.

    Args:
        mensaje: Texto que se muestra al solicitar la respuesta.

    Returns:
        True si el usuario responde 'S'.
        False si el usuario responde 'N'.
    """
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
    """
    Construye una línea de la pirámide descendente.

    Los sumandos aparecen ordenados desde n hasta 0.

    Args:
        n: Número que determina el primer sumando.

    Returns:
        Cadena con la operación y su resultado.
        Para n=3: '3 => 3 + 2 + 1 + 0 = 6'.
    """
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
    """
    Construye una pirámide descendente de sumas.

    Genera las líneas desde num hasta 0, incluyendo
    un salto de línea al final de cada una.

    Args:
        num: Número inicial de la pirámide.

    Returns:
        Cadena con todas las líneas de la pirámide.
    """
    res: str = ""
    n: int = num

    while n >= 0:
        res += linea_piramide_descendente(n) + "\n"
        n -= 1

    return res


def main() -> None:
    """
    Ejecuta el programa principal.

    Solicita números enteros entre 0 y 20, mostrando
    sus pirámides descendentes de sumas.

    Permite generar nuevas pirámides hasta que el usuario
    responde negativamente.
    """
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
