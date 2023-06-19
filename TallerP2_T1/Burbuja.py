def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n - 1):
        for j in range(0, n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr


# Obtener la lista de números del usuario
num_input = input("Ingresa una lista de números separados por espacios: ")
nums = list(map(int, num_input.split()))

# Llamar al algoritmo de Burbuja para ordenar la lista
sorted_nums = bubble_sort(nums)

# Imprimir la lista ordenada
print("Lista ordenada:", sorted_nums)