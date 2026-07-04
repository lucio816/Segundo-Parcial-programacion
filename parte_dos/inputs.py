from funciones import es_cadena_flotante, validar_nombre_apellido, es_cadena_numerica, validar_año_egreso, validar_plan, validar_nota_promedio


def pedir_opcion_menu(minimo: int, maximo: int) -> int:
    """
    Le pide al usuario que ingrese un numero entero dentro de un rango,
    y no lo deja seguir hasta que ingrese algo valido.

    Args:
        minimo (int): el valor mas chico permitido (incluido).
        maximo (int): el valor mas grande permitido (incluido).

    Returns:
        int: el numero entero que ingreso el usuario
    """
    opcion_valida = False
    resultado = 0

    while not opcion_valida:
        entrada = input(f"\nSeleccione una opción ({minimo}-{maximo}): ")

        if es_cadena_numerica(entrada):
            valor = int(entrada)
            if valor >= minimo and valor <= maximo:
                resultado = valor
                opcion_valida = True
            else:
                print(f"[!] ERROR: Ingrese un número entre {minimo} y {maximo}.")
        else:
            print("[!] ERROR: Entrada inválida. Ingrese un número entero.")

    return resultado


def pedir_nombre_apellido(mensaje: str) -> str:
    """
    Le pide al usuario un nombre o apellido y no lo deja seguir hasta que
    ingrese un texto valido (minimo 3 letras, sin numeros ni simbolos).

    Args:
        mensaje (str): el texto que se muestra para pedir el dato
                        (por ejemplo "Ingrese el nombre: ").

    Returns:
        str: el nombre o apellido ingresado por el usuario, ya validado.
    """
    valido = False
    resultado = ""

    while not valido:
        entrada = input(mensaje)
        if validar_nombre_apellido(entrada):
            resultado = entrada
            valido = True
        else:
            print("[!] ERROR: Debe tener al menos 3 caracteres y solo letras/espacios (sin números ni símbolos).")

    return resultado


def pedir_año_egreso() -> int:
    """
    Le pide al usuario el año de egreso hasta que
    ingrese un numero entero dentro del rango permitido 

    Args:
        No recibe parametros.

    Returns:
        int: el año de egreso ingresado por el usuario, ya validado.
    """
    valido = False
    resultado = 0

    while not valido:
        entrada = input(f"Ingrese el año de egreso ({1991}-{2026}): ")
        if es_cadena_numerica(entrada):
            valor = int(entrada)
            if validar_año_egreso(valor):
                resultado = valor
                valido = True
            else:
                print(f"[!] ERROR: El año debe estar entre {1991} y {2026}.")
        else:
            print("[!] ERROR: Ingrese un número entero válido.")

    return resultado


def pedir_plan() -> int:
    """
    Le pide al usuario el plan de estudios y no lo deja seguir hasta que
    ingrese uno de los tres planes validos.

    Args:
        No recibe parametros.

    Returns:
        int: el plan de estudios ingresado por el usuario (1991, 2003 o 2024).
    """
    valido = False
    resultado = 0

    while not valido:
        print("\nPlanes disponibles: 1991 - 2003 - 2024")
        entrada = input("Ingrese el plan de estudios: ")
        if es_cadena_numerica(entrada):
            valor = int(entrada)
            if validar_plan(valor):
                resultado = valor
                valido = True
            else:
                print("[!] ERROR: El plan debe ser 1991, 2003 o 2024.")
        else:
            print("[!] ERROR: Ingrese un número entero válido.")

    return resultado


def pedir_nota_promedio() -> float:
    """
    Le pide al usuario la nota promedio y no lo deja seguir hasta que
    ingrese un numero decimal valido dentro del rango permitido (6-10).

    Args:
        No recibe parametros.

    Returns:
        float: la nota promedio ingresada por el usuario, ya validada.
    """
    valido = False
    resultado = 0.0

    while not valido:
        entrada = input(f"Ingrese la nota promedio ({6}-{10}): ")
        if es_cadena_flotante(entrada):
            valor = float(entrada)
            if validar_nota_promedio(valor):
                resultado = valor
                valido = True
            else:
                print(f"[!] ERROR: La nota debe estar entre {6} y {10}.")
        else:
            print("[!] ERROR: Ingrese un número válido (ej: 8.5).")

    return resultado


def pedir_confirmacion(mensaje: str) -> bool:
    """
    Le pregunta algo al usuario y espera una respuesta de si o no

    Args:
        mensaje (str): la pregunta que se le quiere hacer al usuario 

    Returns:
        bool: True si el usuario respondio que si . False si respondio que no 
    """
    respuesta_valida = False
    resultado = False

    while not respuesta_valida:
        entrada = input(mensaje + " (s/n): ")
        if entrada == "s" or entrada == "S":
            resultado = True
            respuesta_valida = True
        elif entrada == "n" or entrada == "N":
            resultado = False
            respuesta_valida = True
        else:
            print("[!] ERROR: Responda con 's' para Sí o 'n' para No.")

    return resultado


def pedir_texto_busqueda(mensaje: str) -> str:
    """
    Le pide al usuario un texto para buscar (nombre o apellido)

    Args:
        mensaje (str): el texto que se muestra para pedir el dato.

    Returns:
        str: el texto de busqueda ingresado por el usuario, ya validado.
    """
    valido = False
    resultado = ""

    while not valido:
        entrada = input(mensaje)
        if validar_nombre_apellido(entrada):
            resultado = entrada
            valido = True
        else:
            print("[!] ERROR: Ingrese al menos 3 letras (sin números ni símbolos).")

    return resultado