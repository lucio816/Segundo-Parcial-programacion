import random


def es_caracter_valido_nombre(caracter: str) -> bool:
    """
    Se fija si un solo caracter es una letra valida para un nombre o un espacio.

    Args:
        caracter (str): un unico caracter a evaluar.

    Returns:
        bool: True si es letra (mayuscula, minuscula, con tilde o n) o espacio.
              False si es un numero, simbolo o cualquier otro caracter.
    """
    valido = False
    codigo = ord(caracter)

    es_mayuscula = codigo >= 65 and codigo <= 90
    es_minuscula = codigo >= 97 and codigo <= 122
    es_espacio = codigo == 32

    if es_mayuscula or es_minuscula or es_espacio :
        valido = True
    return valido


def validar_nombre_apellido(cadena: str) -> bool:
    """
    Valida que un nombre o apellido cumpla con las reglas del enunciado:
    al menos 3 caracteres y que todos sean letras o espacios.

    Args:
        cadena (str): el texto ingresado por el usuario (nombre o apellido).

    Returns:
        bool: True si la cadena es valida. False si tiene menos de 3
              caracteres o contiene numeros/simbolos.
    """
    if len(cadena) < 3:
        return False

    es_valido = True
    for i in range(len(cadena)):
        if not es_caracter_valido_nombre(cadena[i]):
            es_valido = False

    return es_valido


def convertir_minuscula(cadena: str) -> str:
    """
    Pasa una cadena a minusculas letra por letra, sumando 32 al codigo ASCII
    de cada letra mayuscula (reemplaza al metodo .lower(), que no se puede usar).

    Args:
        cadena (str): el texto original, puede tener mayusculas o minusculas.

    Returns:
        str: una nueva cadena igual a la original pero toda en minusculas.
    """
    resultado = ""

    for i in range(len(cadena)):
        caracter = cadena[i]
        codigo = ord(caracter)

        debe_convertir = (
            (codigo >= 65 and codigo <= 90) or
            codigo == 193 or codigo == 201 or codigo == 205 or
            codigo == 211 or codigo == 218 or codigo == 209
        )

        if debe_convertir:
            caracter = chr(codigo + 32)

        resultado += caracter

    return resultado


def contiene_subcadena(cadena_completa: str, subcadena: str) -> bool:
    """
    busca si hay uns¿a subcadena dentro de un texto

    Args:
        cadena_completa (str): el texto donde se busca (por ejemplo, un apellido).
        subcadena (str): el texto que se quiere encontrar (lo que escribio el usuario).

    Returns:
        bool: True si 'subcadena' aparece en algun lugar de 'cadena_completa'.
              False si no aparece, o si alguna de las dos esta vacia/es mas larga.
    """
    largo_completa = len(cadena_completa)
    largo_sub = len(subcadena)

    if largo_sub == 0 or largo_sub > largo_completa:
        return False

    encontrado = False
    cantidad_posiciones = largo_completa - largo_sub + 1

    for i in range(cantidad_posiciones):
        coincide = True
        for j in range(largo_sub):
            if cadena_completa[i + j] != subcadena[j]:
                coincide = False
        if coincide:
            encontrado = True

    return encontrado


def es_cadena_numerica(cadena: str) -> bool:
    """
    Verifica que un texto este formado solo por digitos (0-9)

    Args:
        cadena (str): el texto ingresado por el usuario.

    Returns:
        bool: True si todos los caracteres son digitos y la cadena no esta vacia.
            False en caso contrario.
    """
    if len(cadena) == 0:
        return False

    es_valido = True
    for i in range(len(cadena)):
        codigo = ord(cadena[i])
        if codigo < 48 or codigo > 57:
            es_valido = False

    return es_valido


def es_cadena_flotante(cadena: str) -> bool:
    """
    Verifica que un texto tenga la forma de un numero decimal valido
    Args:
        cadena (str): el texto ingresado por el usuario 
    Returns:
        bool: True si la cadena se puede convertir a float de forma valida.
              False si tiene letras, mas de un punto, o no tiene ningun digito.
    """
    if len(cadena) == 0:
        return False

    cantidad_puntos = 0
    es_valido = True
    tiene_digito = False

    for i in range(len(cadena)):
        caracter = cadena[i]
        if caracter == ".":
            cantidad_puntos += 1
        elif ord(caracter) >= 48 and ord(caracter) <= 57:
            tiene_digito = True
        else:
            es_valido = False

    if cantidad_puntos > 1:
        es_valido = False

    return es_valido and tiene_digito


def validar_año_egreso(año: int) -> bool:
    """
    Chequea que el año de egreso este dentro del rango permitido por la consigna.

    Args:
        año (int): el año de egreso ingresado por el usuario.

    Returns:
        bool: True si el año esta entre 1991 y 2026. False si no.
    """
    
    if año >= 1991 and año <= 2026:
        vale = True
    else:
        vale = False
    return vale


def validar_plan(plan: int) -> bool:
    """
    Chequea que el plan de estudios sea uno de los tres permitidos.

    Args:
        plan (int): el numero de plan ingresado por el usuario.

    Returns:
        bool: True si el plan es 1991, 2003 o 2024. False en cualquier otro caso.
    """
    plan_valido=[1991, 2003, 2024]
    es_valido = False
    for i in range(len((plan_valido))):
        if (plan_valido)[i] == plan:
            es_valido = True
    return es_valido


def validar_nota_promedio(nota: float) -> bool:
    """
    Chequea que la nota promedio este dentro del rango permitido por la consigna.

    Args:
        nota (float): la nota promedio ingresada por el usuario.

    Returns:
        bool: True si la nota esta entre 6 y 10  False si no.
    """
    if  nota >= 6 and nota <= 10 :
        vale = True
    else:
        vale = False
    return vale


def existe_legajo(lista_alumnos: list, legajo: int) -> bool:
    """
    Recorre la lista de alumnos para saber si un numero de legajo ya esta en uso.

    Args:
        lista_alumnos (list): lista de diccionarios, cada uno representa un alumno.
        legajo (int): el numero de legajo que se quiere comprobar.

    Returns:
        bool: True si algun alumno de la lista ya tiene ese legajo. False si esta libre.
    """
    existe = False
    for i in range(len(lista_alumnos)):
        if lista_alumnos[i]["legajo"] == legajo:
            existe = True
    return existe


def generar_legajo_unico(lista_alumnos: list) -> int:
    """
    Genera un numero de legajo aleatorio de 6 cifras que no este repetido
    en la lista de alumnos.

    Args:
        lista_alumnos (list): lista de diccionarios de alumnos ya cargados.

    Returns:
        int: un numero de 6 cifras (entre 100000 y 999999) que todavia
            no le pertenece a ningun alumno de la lista.
    """
    legajo_generado = random.randint(100000, 999999)
    while existe_legajo(lista_alumnos, legajo_generado):
        legajo_generado = random.randint(100000, 999999)
    return legajo_generado


def crear_diccionario_alumno(legajo: int, nombre: str, apellido: str,egreso: int, plan: int, nota_promedio: float) -> dict:
    """
    Arma el diccionario de un alumno a partir de sus datos sueltos

    Args:
        legajo (int): numero de legajo del alumno.
        nombre (str): nombre del alumno.
        apellido (str): apellido del alumno.
        egreso (int): año en el que egreso.
        plan (int): plan de estudios (1991, 2003 o 2024).
        nota_promedio (float): nota promedio del alumno.

    Returns:
        dict: un diccionario con las claves "legajo", "nombre", "apellido",
              "egreso", "plan" y "nota_promedio" cargadas con esos valores.
    """
    alumno = {
        "legajo": legajo,
        "nombre": nombre,
        "apellido": apellido,
        "egreso": egreso,
        "plan": plan,
        "nota_promedio": nota_promedio
    }
    return alumno


def ordenar_por_promedio_descendente(lista_alumnos: list) -> None:
    """
    Ordena la lista de alumnos de mayor a menor nota promedio, usando el
    algoritmo de la burbuja
    Args:
        lista_alumnos (list): lista de diccionarios de alumnos. 
    Returns:
        None: no devuelve nada 
    """
    
    largo = len(lista_alumnos)
    for i in range(largo - 1):
        for j in range(largo - 1 - i):
            if lista_alumnos[j]["nota_promedio"] < lista_alumnos[j + 1]["nota_promedio"]:
                auxiliar = lista_alumnos[j]
                lista_alumnos[j] = lista_alumnos[j + 1]
                lista_alumnos[j + 1] = auxiliar


def filtrar_por_plan(lista_alumnos: list, plan: int) -> list:
    """
    Arma una lista nueva solo con los alumnos que pertenecen a un plan
    de estudios determinado.

    Args:
        lista_alumnos (list): lista de diccionarios de alumnos.
        plan (int): el plan por el que se quiere filtrar (1991, 2003 o 2024).

    Returns:
        list: lista de diccionarios con los alumnos de ese plan. Puede
              devolver una lista vacia si ninguno pertenece a ese plan.
    """
    resultado = []
    for i in range(len(lista_alumnos)):
        if lista_alumnos[i]["plan"] == plan:
            resultado.append(lista_alumnos[i])
    return resultado


def filtrar_egresados_antes_de(lista_alumnos: list, año_limite: int) -> list:
    """
    Arma una lista nueva solo con los alumnos que egresaron antes de un
    año determinado.

    Args:
        lista_alumnos (list): lista de diccionarios de alumnos.
        año_limite (int): el año de corte (los alumnos egresados antes de ese año)

    Returns:
        list: lista de diccionarios con los alumnos que egresaron antes de ño_limite
    """
    resultado = []
    for i in range(len(lista_alumnos)):
        if lista_alumnos[i]["egreso"] < año_limite:
            resultado.append(lista_alumnos[i])
    return resultado


def buscar_por_nombre_o_apellido(lista_alumnos: list, texto_buscado: str) -> list:
    """
    Busca alumnos cuyo nombre o apellido contenga el texto buscado, sin
    importar mayusculas/minusculas y  coincidencias parciales

    Args:
        lista_alumnos (list): lista de diccionarios de alumnos.
        texto_buscado (str): el texto por usuario

    Returns:
        list: lista de diccionarios con todos los alumnos cuyo nombre o
            apellido contiene el texto buscado. Puede devolver una lista vacia.
    """
    resultado = []
    texto_min = convertir_minuscula(texto_buscado)

    for i in range(len(lista_alumnos)):
        alumno_actual = lista_alumnos[i]
        nombre_min = convertir_minuscula(alumno_actual["nombre"])
        apellido_min = convertir_minuscula(alumno_actual["apellido"])

        coincide_nombre = contiene_subcadena(nombre_min, texto_min)
        coincide_apellido = contiene_subcadena(apellido_min, texto_min)

        if coincide_nombre or coincide_apellido:
            resultado.append(alumno_actual)

    return resultado


def filtrar_salon_de_la_fama(lista_alumnos: list) -> list:
    """
    Arma la lista de alumnos con nota promedio mayor o igual a 9
    Args:
        lista_alumnos (list): lista de diccionarios de alumnos.

    Returns:
        list: lista de diccionarios con los alumnos destacados (promedio >= 9)
    """
    resultado = []
    for i in range(len(lista_alumnos)):
        if lista_alumnos[i]["nota_promedio"] >= 9:
            resultado.append(lista_alumnos[i])

    ordenar_por_promedio_descendente(resultado)
    return resultado


def calcular_promedio_general(lista_alumnos: list) -> float:
    """
    Calcula el promedio de las notas de un grupo de alumnos, sumando a mano
    y dividiendo por la cantidad.

    Args:
        lista_alumnos (list): lista de diccionarios de alumnos 
    Returns:
        float: el promedio de "nota_promedio" de todos los alumnos de la lista
    """
    if len(lista_alumnos) == 0:
        return 0.0

    acumulador = 0.0
    for i in range(len(lista_alumnos)):
        acumulador += lista_alumnos[i]["nota_promedio"]
        prom = acumulador / len(lista_alumnos)
    return prom