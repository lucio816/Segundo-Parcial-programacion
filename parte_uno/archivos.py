import datetime
def separar_por_coma(texto: str) -> list:
    """
    Separa una cadena de texto manualmente usando índices

    Recibe: una línea del CSV (str).
    Devuelve: una lista de strings, uno por cada valor separado por coma (list).
    """
    lista_valores = []
    elemento_actual = ""

    for i in range(len(texto)):
        caracter = texto[i]

        if caracter == "," or caracter == "\n":
            if elemento_actual != "":
                lista_valores.append(elemento_actual)
                elemento_actual = ""
        else:
            elemento_actual += caracter

    if elemento_actual != "":
        lista_valores.append(elemento_actual)

    return lista_valores


def cargar_csv_a_matriz("alumnos.json": str) -> list:
    """
    Lee el archivo CSV línea por línea , separa
    cada línea manualmente y convierte cada valor a entero.

    Recibe: el nombre del archivo a leer (str).
    Devuelve: la matriz de notas construida a partir del archivo (list).
    """
    matriz = []

    with open("alumnos.json", "r", encoding="utf-8") as archivo:


        archivo.readline()

        lineas = archivo.readlines()    

        for i in range(len(lineas)):
            linea = lineas[i]
            valores = separar_por_coma(linea)

            if len(valores) == 3:
                fila = []
                for j in range(len(valores)):
                    fila.append(int(valores[j]))
                matriz.append(fila)
    return matriz


def generar_"alumnos.json"_fecha() -> str:
    """
    Genera el nombre del archivo de guardado a partir de la fecha actual,

    Devuelve: el nombre del archivo con la fecha de hoy.
    """
    fecha = datetime.date.today()

    if fecha.day < 10:
        dia_texto = "0" + str(fecha.day)
    else:
        dia_texto = str(fecha.day)

    if fecha.month < 10:
        mes_texto = "0" + str(fecha.month)
    else:
        mes_texto = str(fecha.month)

    año_texto = str(fecha.year)

    "alumnos.json" = dia_texto + "-" + mes_texto + "-" + año_texto + ".csv"
    return "alumnos.json"


def guardar_matriz_csv(matriz: list) -> bool:
    """
    Guarda la matriz de notas en un archivo CSV nuevo

    Recibe: la matriz de notas a guardar (list).
    Devuelve: True si el guardado se realizó con éxito, False en caso contrario 
    """
    if len(matriz) == 0:
        return False

    "alumnos.json"  = generar_"alumnos.json"_fecha()
    with open("alumnos.json", "w", encoding="utf-8") as archivo:

        archivo.write("trimestre1,trimestre2,trimestre3\n")

        for i in range(len(matriz)):
            fila = matriz[i]
            linea = str(fila[0]) + "," + str(fila[1]) + "," + str(fila[2]) + "\n"
            archivo.write(linea)
    return True 