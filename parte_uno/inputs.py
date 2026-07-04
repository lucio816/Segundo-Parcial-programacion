
from prints import mostrar_error

def validar_entero(cadena: str) -> bool:
    """
    Verifica si una cadena de texto contiene únicamente caracteres
    numéricos (dígitos del 0 al 9)

    Recibe: la cadena a evaluar (str).
    Devuelve: True si es un número válido, False si contiene letras o símbolos (bool).
    """
    if len(cadena) == 0:
        return False

    es_valido = True

    for i in range(len(cadena)):
        caracter = cadena[i]
        if caracter < '0' or caracter > '9':
            es_valido = False

    return es_valido


def pedir_nota(mensaje: str, mensaje_error: str) -> int:
    """
    Solicita al usuario una nota por consola, validando que sea un número
    entero y que esté en el rango de 1 a 10

    Recibe:
        - mensaje: el texto para pedir el dato (str).
        - mensaje_error: el texto para mostrar si el usuario se equivoca (str).
    Devuelve: la nota validada (int).
    """
    nota_valida = False
    nota = 0

    while nota_valida == False:
        entrada = input(mensaje)

        if validar_entero(entrada):
            nota = int(entrada)

            if nota >= 1 and nota <= 10:
                nota_valida = True
            else:
                mostrar_error(mensaje_error)
        else:
            mostrar_error(mensaje_error)

    return nota


def pedir_opcion_menu() -> int:
    """
    Solicita al usuario que ingrese una opción del menú principal (1 a 6)
    y valida que sea un número entero dentro de ese rango.

    Devuelve: la opción elegida.
    """
    opcion_valida = False
    opcion = 0

    while opcion_valida == False:
        entrada = input("\nSeleccione una opción: ")

        if validar_entero(entrada):
            opcion = int(entrada)

            if opcion >= 1 and opcion <= 6:
                opcion_valida = True
            else:
                mostrar_error("La opción debe estar entre 1 y 6.")
        else:
            mostrar_error("Debe ingresar un número entero.")

    return opcion


def pedir_tipo_de_carga() -> str:
    """
    el submenu de la opcion de cargar notas
    Devuelve: "a" si eligió carga manual, "b" si eligió carga por CSV (str).
    """
    opcion_valida = False
    respuesta = ""

    while opcion_valida == False:
        entrada  = input("\n¿Cómo desea cargar las notas?\n"
                              "  a. Carga secuencial (manual)\n"
                              "  b. Carga desde archivo CSV\n"
                              "Opción: ")

        if len(entrada) == 1 and (entrada == "a" or entrada == "A"):
            respuesta = "a"
            opcion_valida = True
        elif len(entrada) == 1 and (entrada == "b" or entrada == "B"):
            respuesta = "b"
            opcion_valida = True
        else:
            mostrar_error("Debe ingresar 'a' o 'b'.")

    return respuesta


def cargar_notas_manual(cantidad_alumnos: int) -> list:
    """
    Realiza la carga secuencial de notas por consola para una cantidad
    fija de alumnos, pidiendo las notas de los 3 trimestres a cada uno
    y validando que estén en el rango 1 a 10.

    Recibe: la cantidad de alumnos a cargar (int).
    Devuelve: la matriz de notas cargada manualmente (list).
    """
    matriz = []

    for i in range(cantidad_alumnos):
        print(f"\n--- Cargando notas del Alumno {i + 1} ---")
        fila = []

        for j in range(3):
            mensaje_pedido = f"Ingrese la nota del Trimestre {j + 1}: "
            mensaje_error = "Nota inválida. Debe ser un número entero entre 1 y 10."
            nota = pedir_nota(mensaje_pedido, mensaje_error)
            fila.append(nota)

        matriz.append(fila)

    return matriz