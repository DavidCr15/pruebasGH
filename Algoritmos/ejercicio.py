            if algoritmo == "burbuja":
                peliculas.sort(key=lambda pelicula: pelicula.anio)
            elif algoritmo == "shell":
                # Implementar el algoritmo de ordenamiento ShellSort por año
                def shell_sort_anio(peliculas):
                    n = len(peliculas)
                    gap = n // 2

                    while gap > 0:
                        for i in range(gap, n):
                            temp = peliculas[i]
                            j = i

                            while j >= gap and peliculas[j - gap].anio > temp.anio:
                                peliculas[j] = peliculas[j - gap]
                                j -= gap

                            peliculas[j] = temp

                        gap //= 2

                shell_sort_anio(peliculas)
            elif algoritmo == "quick":
                # Implementar el algoritmo de ordenamiento Quicksort por año
                def partition_anio(peliculas, low, high):
                    pivot = peliculas[high].anio
                    i = low - 1

                    for j in range(low, high):
                        if peliculas[j].anio < pivot:
                            i += 1
                            peliculas[i], peliculas[j] = peliculas[j], peliculas[i]

                    peliculas[i + 1], peliculas[high] = peliculas[high], peliculas[i + 1]
                    return i + 1

                def quick_sort_anio(peliculas, low, high):
                    if low < high:
                        pivot_index = partition_anio(peliculas, low, high)
                        quick_sort_anio(peliculas, low, pivot_index - 1)
                        quick_sort_anio(peliculas, pivot_index + 1, high)

                quick_sort_anio(peliculas, 0, len(peliculas) - 1)
            else:
                print("Algoritmo de ordenamiento inválido.")
        else:
            print("Criterio de ordenamiento inválido.")
    else:
        print("No se han ingresado películas.")


def menu():
    peliculas = []

    while True:
        print("------ MENÚ ------")
        print("1. Ingresar película")
        print("2. Mostrar películas")
        print("3. Eliminar película")
        print("4. Modificar película")
        print("5. Ordenar películas por nombre")
        print("6. Ordenar películas por año")
        print("0. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre de la película: ")
            anio = int(input("Ingrese el año de la película: "))
            pelicula = Pelicula(nombre, anio)
            peliculas.append(pelicula)
            print("Película ingresada exitosamente.")
        elif opcion == "2":
            mostrar_peliculas(peliculas)
        elif opcion == "3":
            eliminar_pelicula(peliculas)
        elif opcion == "4":
            modificar_pelicula(peliculas)
        elif opcion == "5":
            ordenar_peliculas(peliculas, "nombre")
        elif opcion == "6":
            ordenar_peliculas(peliculas, "anio")
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")


menu()