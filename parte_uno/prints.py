

def mostrar_menu() -> None:
    """
    Imprime en pantalla las opciones del menú principal.
    """
    print("\n" + "=" * 40)
    print(" SISTEMA DE NOTAS")
    print("=" * 40)
    print("1. Cargar notas (Manual o CSV)")
    print("2. Mostrar alumnos desaprobados (Nota < 7)")
    print("3. Mostrar alumnos con aplazos (Nota < 4)")
    print("4. Mostrar porcentaje de aprobados y desaprobados")
    print("5. Mostrar trimestre con mejor promedio")
    print("6. Salir y Guardar")
    print("=" * 40)

def mostrar_matriz_notas(matriz: list) -> None:
    """
    Recorre e imprime la matriz de notas dándole formato de tabla.

    Recibe: la matriz de los almunos
    """
    print("\n--- LISTADO DE NOTAS ---")

    for i in range(len(matriz)):
        notas_alumno = matriz[i]
        print(f"Alumno {i + 1}: Trimestre 1: {notas_alumno[0]} | " f"Trimestre 2: {notas_alumno[1]} | Trimestre 3: {notas_alumno[2]}")

    print("-" * 24)

def mostrar_lista_alumnos(indices: list, matriz: list, titulo: str, mensaje_vacio: str) -> None:
    """
    Muestra los alumnos cuyos índices fueron encontrados por una búsqueda, Si no hay ninguno, informa
    al usuario con el mensaje correspondiente.

    Recibe:
        - indices: lista de posiciones de alumnos a mostrar (list).
        - matriz: la matriz completa de notas (list).
        - titulo: encabezado a mostrar (str).
        - mensaje_vacio: mensaje si no hay alumnos que cumplan la condición (str).
    """
    print(f"\n--- {titulo} ---")

    if len(indices) == 0:
        print(mensaje_vacio)
    else:
        for i in range(len(indices)):
            posicion = indices[i]
            notas_alumno = matriz[posicion]
            print(f"Alumno {posicion + 1}: Trimestre 1: {notas_alumno[0]} | "f"Trimestre 2: {notas_alumno[1]} | Trimestre 3: {notas_alumno[2]}")

    print("-" * 24)


def mostrar_porcentajes(porcentaje_aprobados: float, porcentaje_desaprobados: float) -> None:
    """
    Muestra el porcentaje de alumnos aprobados y desaprobados.

    Recibe: el porcentaje de aprobados y de desaprobados.
    """
    print("\n--- PORCENTAJE DE APROBACIÓN ---")
    print(f"Aprobados:    {porcentaje_aprobados:.2f} %")
    print(f"Desaprobados: {porcentaje_desaprobados:.2f} %")
    print("-" * 32)


def mostrar_mejor_trimestre(trimestres_ganadores: list) -> None:
    """
    Muestra cuál o cuáles trimestres tuvieron el mejor promedio,
    contemplando la posibilidad de empate.

    Recibe: la lista de trimestres ganadores (list).
    """
    print("\n--- TRIMESTRE CON MEJOR PROMEDIO ---")

    if len(trimestres_ganadores) == 1:
        print(f"El trimestre con mejor promedio fue el Trimestre {trimestres_ganadores[0]}.")
    else:
        texto = "Hay un empate entre los Trimestres: "
        for i in range(len(trimestres_ganadores)):
            texto = texto + str(trimestres_ganadores[i])
            if i < len(trimestres_ganadores) - 1:
                texto = texto + ", "
        print(texto)

    print("-" * 36)

def mostrar_error(mensaje: str) -> None:
    """
    Imprime un mensaje de error con un formato llamativo.

    Recibe: el mensaje de error a mostrar
    """
    print(f"\n[!] ERROR: {mensaje}")


def mostrar_exito(mensaje: str) -> None:
    """
    Imprime un mensaje de exito con un formato claro.

    Recibe: el mensaje de exito a mostrar (str).
    """
    print(f"\n[+] ÉXITO: {mensaje}")






