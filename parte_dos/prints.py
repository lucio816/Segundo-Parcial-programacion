def mostrar_menu_principal() -> None:
    """
    Imprime en pantalla el menu principal con las 6 opciones del programa.

    Args:
        No recibe parametros.

    Returns:
        None: solo imprime en pantalla, no devuelve ningun valor.
    """
    print("\n" + "=" * 68)
    print("   UTN FRA - SISTEMA DE EGRESADOS - TECNICATURA EN PROGRAMACIÓN")
    print("=" * 68)
    print("1. Cargar alumnos")
    print("2. Mostrar egresados por plan")
    print("3. Mostrar egresados anteriores al año 2000")
    print("4. Buscar alumno por nombre o apellido")
    print("5. Salón de la fama (promedio >= 9)")
    print("6. Salir")
    print("=" * 68)


def mostrar_submenu_carga() -> None:
    """
    Imprime en pantalla el submenu de carga de alumnos (desde archivo o manual).

    Args:
        No recibe parametros.

    Returns:
        None: solo imprime en pantalla, no devuelve ningun valor.
    """
    print("\n--- Cargar Alumnos ---")
    print("1. Cargar desde archivo (alumnos.json)")
    print("2. Carga manual")


def mostrar_mensaje(mensaje: str, tipo: str) -> None:
    """
    Imprime un mensaje en pantalla con un formato distinto segun el tipo

    Args:
        mensaje (str): el texto del mensaje que se quiere mostrar.
        tipo (str): "exito" para mensajes de exito, "error" para mensajes
                    de error

    Returns:
        None: solo imprime en pantalla, no devuelve ningun valor.
    """
    if tipo == "exito":
        print(f"\n[+] {mensaje}")
    elif tipo == "error":
        print(f"\n[!] {mensaje}")
    else:
        print(f"\n[i] {mensaje}")


def mostrar_encabezado_tabla() -> None:
    """
    Imprime el encabezado de la tabla que se usa para mostrar listas de alumnos
    (nombres de columnas y una linea separadora).

    Args:
        No recibe parametros.

    Returns:
        None: solo imprime en pantalla, no devuelve ningun valor.
    """
    print(f"\n| {'LEGAJO':<8} | {'NOMBRE':<15} | {'APELLIDO':<15} | {'EGRESO':<7} | {'PLAN':<6} | {'PROMEDIO':<8} |")
    print("-" * 76)


def mostrar_alumno(alumno: dict) -> None:
    """
    Imprime una fila de la tabla con los datos de un unico alumno.

    Args:
        alumno (dict): diccionario con los datos del alumno (legajo, nombre,
                        apellido, egreso, plan y nota_promedio).

    Returns:
        None: solo imprime en pantalla, no devuelve ningun valor.
    """
    print(f"| {alumno['legajo']:<8} | {alumno['nombre']:<15} | {alumno['apellido']:<15} | "
          f"{alumno['egreso']:<7} | {alumno['plan']:<6} | {alumno['nota_promedio']:<8.2f} |")


def mostrar_lista_alumnos(lista_alumnos: list) -> None:
    """
    Imprime en pantalla la tabla completa de alumnos 

    Args:
        lista_alumnos (list): lista de diccionarios de alumnos a mostrar.

    Returns:
        None: solo imprime en pantalla, no devuelve ningun valor.
    """
    if len(lista_alumnos) == 0:
        mostrar_mensaje("No hay alumnos para mostrar.", "error")
    else:
        mostrar_encabezado_tabla()
        for i in range(len(lista_alumnos)):
            mostrar_alumno(lista_alumnos[i])
        print("-" * 76)


def mostrar_ficha_alumno(alumno: dict) -> None:
    """
    Imprime en pantalla una ficha con todos los datos de un alumno recien
    creado, para que el usuario los revise antes de confirmar el alta.

    Args:
        alumno (dict): diccionario con los datos del alumno a mostrar.

    Returns:
        None: solo imprime en pantalla, no devuelve ningun valor.
    """
    print("\n--- Datos del nuevo alumno ---")
    print(f"Nombre:   {alumno['nombre']}")
    print(f"Apellido: {alumno['apellido']}")
    print(f"Legajo:   {alumno['legajo']}")
    print(f"Egreso:   {alumno['egreso']}")
    print(f"Plan:     {alumno['plan']}")
    print(f"Nota:     {alumno['nota_promedio']}")


def mostrar_cantidad_encontrados(cantidad: int) -> None:
    """
    Imprime en pantalla cuantos alumnos se encontraron en una busqueda.

    Args:
        cantidad (int): la cantidad de alumnos encontrados.

    Returns:
        None: solo imprime en pantalla, no devuelve ningun valor.
    """
    print(f"\n[i] Se encontraron {cantidad} alumno(s).")


def mostrar_promedio_general(promedio: float) -> None:
    """
    Imprime en pantalla el promedio general de un grupo de alumnos,
    con dos decimales.

    Args:
        promedio (float): el valor del promedio a mostrar.

    Returns:
        None: solo imprime en pantalla, no devuelve ningun valor.
    """
    print(f"\n[i] Nota promedio general de los egresados encontrados: {promedio:.2f}")