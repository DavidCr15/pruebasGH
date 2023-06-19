def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n - 1):
        for j in range(0, n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr


def shellSort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i

            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp
        gap //= 2


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        smaller = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quicksort(smaller) + [pivot] + quicksort(greater)


# Obtener la lista de números del usuario
num_input = input("Ingresa una lista de números separados por espacios: ")
nums = list(map(int, num_input.split()))

# Llamar al algoritmo de Bubble Sort para ordenar la lista
sorted_nums_bubble = bubble_sort(nums[:])

# Llamar al algoritmo de ShellSort para ordenar la lista
sorted_nums_shell = nums[:]
shellSort(sorted_nums_shell)

# Llamar al algoritmo de Quicksort para ordenar la lista
sorted_nums_quick = quicksort(nums[:])

# Imprimir las listas ordenadas
print("Lista original:", nums)
print("Lista ordenada con Bubble Sort:", sorted_nums_bubble)
print("Lista ordenada con ShellSort:", sorted_nums_shell)
print("Lista ordenada con Quicksort:", sorted_nums_quick)
