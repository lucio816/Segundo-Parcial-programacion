
from inputs import pedir_opcion_menu, pedir_tipo_de_carga, cargar_notas_manual
from archivos import cargar_csv_a_matriz, guardar_matriz_csv, generar_"alumnos.json"_fecha
from funciones import buscar_alumnos_por_6, calcular_porcentaje, obtener_mejores_trimestres
from prints import (
    mostrar_menu,
    mostrar_exito,
    mostrar_error,
    mostrar_matriz_notas,
    mostrar_lista_alumnos,
    mostrar_porcentajes,
    mostrar_mejor_trimestre,
)


def ejecutar_menu() -> None:
    """
    Función principal del programa: muestra el menú en un bucle
    """


    matriz = []
    matriz_cargada = False
    carga_manual = False

    programa_activo = True

    while programa_activo:
        mostrar_menu()
        opcion = pedir_opcion_menu()

        match opcion:
            case 1:
                tipo_carga = pedir_tipo_de_carga()

                if tipo_carga == "a":
                    matriz = cargar_notas_manual(7)
                    matriz_cargada = True
                    carga_manual = True
                    mostrar_exito("Notas cargadas manualmente con éxito.")
                else:
                    matriz = cargar_csv_a_matriz("notas.csv")
                    if len(matriz) == 0:
                        mostrar_error("No se pudieron cargar datos desde notas.csv.")
                    else:
                        matriz_cargada = True
                        carga_manual = False
                        mostrar_exito("Notas cargadas desde notas.csv con éxito.")
                
                if matriz_cargada:
                    mostrar_matriz_notas(matriz)

            case 2:
                if matriz_cargada:
                    indices = buscar_alumnos_por_6(matriz,7)
                    mostrar_lista_alumnos(
                        indices,
                        matriz,
                        "ALUMNOS DESAPROBADOS",
                        "No hay alumnos desaprobados. ¡Todos tienen notas mayores o iguales a 7!"
                    )
                else:
                    mostrar_error("Primero debe cargar las notas (Opción 1).")

            case 3:
                if matriz_cargada:
                    indices = buscar_alumnos_por_6(matriz, 4)
                    mostrar_lista_alumnos(
                        indices,
                        matriz,
                        "ALUMNOS CON APLAZOS",
                        "No hay alumnos con aplazos. ¡Nadie tiene notas menores a 4!"
                    )
                else:
                    mostrar_error("Primero debe cargar las notas (Opción 1).")

            case 4:
                if matriz_cargada:
                    indices_desaprobados = buscar_alumnos_por_6(matriz, 7)
                    cantidad_desaprobados = len(indices_desaprobados)
                    cantidad_total = len(matriz)
                    cantidad_aprobados = cantidad_total - cantidad_desaprobados

                    porcentaje_aprobados = calcular_porcentaje(cantidad_aprobados, cantidad_total)
                    porcentaje_desaprobados = calcular_porcentaje(cantidad_desaprobados, cantidad_total)

                    mostrar_porcentajes(porcentaje_aprobados, porcentaje_desaprobados)
                else:
                    mostrar_error("Primero debe cargar las notas (Opción 1).")

            case 5:
                if matriz_cargada:
                    trimestres_ganadores = obtener_mejores_trimestres(matriz)
                    mostrar_mejor_trimestre(trimestres_ganadores)
                else:
                    mostrar_error("Primero debe cargar las notas (Opción 1).")

            case 6:
                if matriz_cargada and carga_manual:
                    guardado_exitoso = guardar_matriz_csv(matriz)
                    if guardado_exitoso:
                        "alumnos.json" = generar_"alumnos.json"_fecha()
                        mostrar_exito(f"Datos guardados correctamente en '{"alumnos.json"}'.")
                    else:
                        mostrar_error("No se pudo guardar el archivo.")

                programa_activo = False