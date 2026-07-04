import os
import json


def existe_archivo(nombre_archivo: str) -> bool:
    """
    Se fija si un archivo existe en el disco.

    Args:
        nombre_archivo (str): la ruta o nombre del archivo a comprobar

    Returns:
        bool: True si el archivo existe. False si no existe.
    """
    return os.path.exists(nombre_archivo)


def leer_json(nombre_archivo: str) -> list:
    """
    Lee un archivo JSON y devuelve su contenido como lista de diccionarios.

    Args:
        nombre_archivo (str): la ruta o nombre del archivo JSON a leer
                               (por ejemplo "alumnos.json").

    Returns:
        list: la lista de diccionarios de alumnos leida del archivo, o una
              lista vacia si
    """
    lista_alumnos = []

    if existe_archivo(nombre_archivo):
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            contenido = json.load(archivo)
            if type(contenido) == list:
                lista_alumnos = contenido

    return lista_alumnos


def guardar_json(nombre_archivo: str, lista_alumnos: list) -> bool:
    """
    Guarda la lista de alumnos en un archivo JSON, sobrescribiendo el
    contenido anterior si el archivo ya existia.

    Args:
        nombre_archivo (str): la ruta o nombre del archivo donde se va a
        lista_alumnos (list): la lista de diccionarios de alumnos a guardar.

    Returns:
        bool: True una vez que el archivo se guardo correctamente.
    """
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        json.dump(lista_alumnos, archivo, indent=4, ensure_ascii=False)
    return True