def busquedaLineal(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


lista = [2, 5, 7, 10, 12, 15, 18, 20, 25]
elemento_buscado = 12

resultado = busquedaLineal(lista, elemento_buscado)

if resultado != -1:
    print("El elemento", elemento_buscado, "se encuentra en el puesto", resultado)
else:
    print("El elemento", elemento_buscado, "no se encuentra en el puesto.")
