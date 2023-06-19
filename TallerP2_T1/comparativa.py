import time

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

# Realizar múltiples ejecuciones para Bubble Sort y medir el tiempo de ejecución
num_executions = 10
execution_times_bubble = []

for _ in range(num_executions):
    start_time = time.time()
    sorted_nums_bubble = bubble_sort(nums[:])
    end_time = time.time()
    execution_times_bubble.append(end_time - start_time)

average_time_bubble = sum(execution_times_bubble) / num_executions

# Realizar múltiples ejecuciones para ShellSort y medir el tiempo de ejecución
execution_times_shell = []

for _ in range(num_executions):
    start_time = time.time()
    sorted_nums_shell = nums[:]
    shellSort(sorted_nums_shell)
    end_time = time.time()
    execution_times_shell.append(end_time - start_time)

average_time_shell = sum(execution_times_shell) / num_executions

# Realizar múltiples ejecuciones para Quicksort y medir el tiempo de ejecución
execution_times_quick = []

for _ in range(num_executions):
    start_time = time.time()
    sorted_nums_quick = quicksort(nums[:])
    end_time = time.time()
    execution_times_quick.append(end_time - start_time)

average_time_quick = sum(execution_times_quick) / num_executions

# Imprimir las listas ordenadas y los tiempos de ejecución promedio
print("Lista original:", nums)
print("Lista ordenada con Bubble Sort:", sorted_nums_bubble)
print("Tiempo promedio de ejecución Bubble Sort: %.6f segundos" % average_time_bubble)
print("Lista ordenada con ShellSort:", sorted_nums_shell)
print("Tiempo promedio de ejecución ShellSort: %.6f segundos" % average_time_shell)
print("Lista ordenada con Quicksort:", sorted_nums_quick)
print("Tiempo promedio de ejecución Quicksort: %.6f segundos" % average_time_quick)
