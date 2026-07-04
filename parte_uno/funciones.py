
def buscar_alumnos_por_6(matriz: list, nota_limite: int) -> list:
    """
    Busca qué alumnos tienen al menos una nota menor al límite establecido.
    Reutilizable para buscar desaprobados (< 7) y aplazos (< 4).

    Recibe:
        - matriz: la lista de listas con las notas (list).
        - nota_limite: la nota que sirve de tope para filtrar (int).
    Devuelve: una lista con los índices (posiciones) de los alumnos encontrados (list).
    """
    alumnos_encontrados = []

    for i in range(len(matriz)):
        notas_alumno = matriz[i]
        tiene_nota_menor = False

        for j in range(len(notas_alumno)):
            if notas_alumno[j] < nota_limite:
                tiene_nota_menor = True

        if tiene_nota_menor:
            alumnos_encontrados.append(i)

    return alumnos_encontrados


def calcular_porcentaje(cantidad: int, total: int) -> float:
    """
    Calcula el porcentaje de una cantidad sobre el total.

    Recibe: la cantidad a evaluar (int) y el total general (int).
    Devuelve: el porcentaje calculado (float).
    """
    if total == 0:
        return 0.0

    porcentaje = (cantidad * 100) / total
    return porcentaje


def obtener_mejores_trimestres(matriz: list) -> list:
    """
    Calcula el promedio,sumando la notas de cada trimestre

    Recibe: la matriz de notas (list).
    Devuelve: una lista con los números de los trimestres ganadores (list).
    """
    suma_t1= 0
    suma_t2 = 0
    suma_t3 = 0

    for i in range(len(matriz)):
        suma_t1 += matriz[i][0]
        suma_t2 += matriz[i][1]
        suma_t3 += matriz[i][2]

    sumas_trimestres = [suma_t1, suma_t2, suma_t3]

    mayor_suma= sumas_trimestres[0]
    for i in range(len(sumas_trimestres)):
        if sumas_trimestres[i] > mayor_suma:
            mayor_suma = sumas_trimestres[i]

    trimestres_ganadores = []
    for i in range(len(sumas_trimestres)):
        if sumas_trimestres[i] == mayor_suma:
            trimestres_ganadores.append(i + 1)

    return trimestres_ganadores
