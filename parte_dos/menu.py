from prints import *
from funciones import *
from inputs import *
from archivos import *


def iniciar_programa() -> None:
    """
    Muestra el menu en un bucle, controla que el usuario no pueda consultar datos antes de haber cargado alumnos
    manejo de opciones 

    Args:
        No recibe parametros.

    Returns:
        None: no devuelve nada. Termina cuando el usuario elige la opcion6 (Salir), despues de guardar los datos en "alumnos.json".
    """
    lista_alumnos = []
    datos_cargados = False
    continuar = True

    while continuar:
        mostrar_menu_principal()
        opcion = pedir_opcion_menu(1, 6)

        match opcion:
            case 1:
                mostrar_submenu_carga()
                sub_opcion = pedir_opcion_menu(1, 2)

                if sub_opcion == 1:
                    if not existe_archivo("alumnos.json"):
                        mostrar_mensaje("No se encontró el archivo alumnos.json", "error")
                    else:
                        mantener = True
                        if len(lista_alumnos) > 0:
                            mantener = pedir_confirmacion("Ya hay alumnos cargados en memoria. ¿Desea conservarlos?")

                        alumnos_archivo = leer_json("alumnos.json")

                        if not mantener:
                            lista_alumnos = []

                        cantidad_agregados = 0
                        for i in range(len(alumnos_archivo)):
                            alumno_actual = alumnos_archivo[i]
                            if not existe_legajo(lista_alumnos, alumno_actual["legajo"]):
                                lista_alumnos.append(alumno_actual)
                                cantidad_agregados += 1

                        mostrar_mensaje(f"Se cargaron {cantidad_agregados} alumno(s) desde el archivo.", "exito")
                        if len(lista_alumnos) > 0:
                            datos_cargados = True

                elif sub_opcion == 2:
                    nombre = pedir_nombre_apellido("Ingrese el nombre: ")
                    apellido = pedir_nombre_apellido("Ingrese el apellido: ")
                    egreso = pedir_año_egreso()
                    plan = pedir_plan()
                    nota_promedio = pedir_nota_promedio()

                    legajo = generar_legajo_unico(lista_alumnos)
                    nuevo_alumno = crear_diccionario_alumno(legajo, nombre, apellido, egreso, plan, nota_promedio)

                    mostrar_ficha_alumno(nuevo_alumno)
                    if pedir_confirmacion("¿Confirma que desea agregar este alumno?"):
                        lista_alumnos.append(nuevo_alumno)
                        mostrar_mensaje("Alumno agregado correctamente.", "exito")
                        datos_cargados = True
                    else:
                        mostrar_mensaje("Operación cancelada. El alumno no fue agregado.", "info")

            case 2:
                if datos_cargados:
                    plan = pedir_plan()
                    resultado = filtrar_por_plan(lista_alumnos, plan)

                    if len(resultado) == 0:
                        mostrar_mensaje(f"No hay alumnos egresados del plan {plan}.", "error")
                    else:
                        mostrar_lista_alumnos(resultado)
                else:
                    mostrar_mensaje("Primero debe cargar alumnos (Opción 1).", "error")

            case 3:
                if datos_cargados:
                    resultado = filtrar_egresados_antes_de(lista_alumnos, 2000)

                    if len(resultado) == 0:
                        mostrar_mensaje("No hay egresados anteriores al año 2000.", "error")
                    else:
                        mostrar_lista_alumnos(resultado)
                        promedio = calcular_promedio_general(resultado)
                        mostrar_promedio_general(promedio)
                else:
                    mostrar_mensaje("Primero debe cargar alumnos (Opción 1).", "error")

            case 4:
                if datos_cargados:
                    texto = pedir_texto_busqueda("Ingrese nombre o apellido a buscar (mínimo 3 letras): ")
                    resultado = buscar_por_nombre_o_apellido(lista_alumnos, texto)

                    mostrar_cantidad_encontrados(len(resultado))
                    if len(resultado) > 0:
                        mostrar_lista_alumnos(resultado)
                else:
                    mostrar_mensaje("Primero debe cargar alumnos (Opción 1).", "error")
            case 5:
                if datos_cargados:
                    resultado = filtrar_salon_de_la_fama(lista_alumnos)

                    if len(resultado) == 0:
                        mostrar_mensaje("Todavía no hay alumnos con promedio mayor o igual a 9.", "error")
                    else:
                        mostrar_lista_alumnos(resultado)
                else:
                    mostrar_mensaje("Primero debe cargar alumnos (Opción 1).", "error")

            case 6:

                guardar_json("alumnos.json", lista_alumnos)
                mostrar_mensaje("Datos guardados correctamente. ¡Hasta la próxima!", "exito")
                continuar = False