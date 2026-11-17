NUMERO_MAXIMO: int = 20
NUMERO_MINIMO: int = 0


def validar_numero(numero: int) -> None:
    """
    Comprueba que un número esté dentro del intervalo permitido.

    Args:
        numero: Número entero que se desea validar.

    Raises:
        ValueError: Si el número no está comprendido entre NUMERO_MINIMO y NUMERO_MAXIMO.
    """
    if numero < NUMERO_MINIMO or numero > NUMERO_MAXIMO:
        raise ValueError("Error: el número debe estar en el rango " + 
                         f"{NUMERO_MINIMO}-{NUMERO_MAXIMO}")


def convertir_entero(entrada: str) -> int:
    """
    Convierte una cadena de texto en un número entero.

    Args:
        entrada: Cadena que se desea convertir.

    Returns:
        Número entero obtenido de la conversión.

    Raises:
        ValueError: Si la cadena no representa un número entero.
    """
    try:
        return int(entrada)
    except ValueError:
        raise ValueError("**Error: entrada no válida! debe ser un número entero**")


def leer_numero(mensaje: str = "") -> int:
    """
    Solicita un número entero válido dentro del intervalo de 0 a 20.

    Repite la petición hasta que el usuario introduce un número
    que supera las comprobaciones de conversión y validación.

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
        respuesta: Respuesta que se desea validar, previamente
            normalizada a mayúsculas y sin espacios exteriores.

    Raises:
        ValueError: Si la respuesta no es 'S' ni 'N'.
    """
    if respuesta not in ("S", "N"):
        raise ValueError("**Error: debe responder 's' o 'n'**")


def leer_respuesta(mensaje: str = "") -> bool:
    """
    Solicita una respuesta afirmativa o negativa.

    Ignora las diferencias entre mayúsculas y minúsculas,
    así como los espacios iniciales y finales.
    Repite la petición hasta obtener una respuesta válida.

    Args:
        mensaje: Texto que se muestra al solicitar la respuesta.

    Returns:
        True si el usuario responde 'S'.
        False si responde 'N'.
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


def borrar_consola(num_lineas: int = 50) -> None:
    """
    Simula la limpieza de la consola imprimiendo líneas vacías.

    Args:
        num_lineas: Número de líneas vacías que se imprimirán.
            Por defecto, 50.
    """
    print("\n" * num_lineas, end="")

    # Alternativa mediante un bucle:
    #
    # for _ in range(num_lineas):
    #     print()
    #
    # El guion de la actividad exige utilizar un bucle.


def linea_piramide_ascendente(n: int) -> str:
    """
    Construye una línea de la pirámide ascendente.

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

    # Alternativa utilizando join():
    #
    # sumandos = " + ".join(str(i) for i in range(n, -1, -1))
    # linea = f"{n} => {sumandos}"
    # if n > 0:
    #     linea += f" = {sum(range(n + 1))}"

    return linea


def piramide_descendente(num: int) -> str:
    """
    Construye la parte descendente de una pirámide de sumas.

    Genera las líneas desde num hasta 0, incluyendo
    un salto de línea al final de cada una.

    Args:
        num: Número inicial de la pirámide.

    Returns:
        Cadena que contiene todas las líneas descendentes.
    """
    res: str = ""
    n: int = num

    while n >= 0:
        res += linea_piramide_descendente(n) + "\n"
        n -= 1

    # Alternativa: almacenar las líneas en una lista y
    # unirlas al final mediante "\n".join(...).
    # Esto evita concatenaciones sucesivas de cadenas.

    return res


def piramide_ascendente(num: int) -> str:
    """
    Construye la parte ascendente de una pirámide de sumas.

    Genera las líneas desde 1 hasta num, evitando repetir
    la fila correspondiente al cero.

    Args:
        num: Número final de la pirámide.

    Returns:
        Cadena que contiene todas las líneas ascendentes.
        Devuelve una cadena vacía cuando num es cero.
    """
    res: str = ""
    n: int = 1

    while n <= num:
        res += linea_piramide_ascendente(n) + "\n"
        n += 1

    return res


def main() -> None:
    """
    Ejecuta el programa principal de generación de pirámides.

    Solicita números al usuario, genera las pirámides de sumas
    descendentes y ascendentes y permite repetir el proceso.

    Cuando el usuario decide finalizar, simula la limpieza
    de la consola y muestra un mensaje de despedida.
    """
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
