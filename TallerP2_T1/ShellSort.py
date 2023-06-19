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

# Ejemplo de uso y prueba
arr1 = [4, 2, 8, 5, 1, 3, 7, 6]
arr2 = [9, 2, 1, 6, 3, 8, 5, 7, 4]
arr3 = [5, 4, 3, 2, 1]
arr4 = [1, 2, 3, 4, 5]
arr5 = []

print("Conjunto de datos original 1:", arr1)
shellSort(arr1)
print("Conjunto de datos ordenado 1:", arr1)

print("Conjunto de datos original 2:", arr2)
shellSort(arr2)
print("Conjunto de datos ordenado 2:", arr2)

print("Conjunto de datos original 3:", arr3)
shellSort(arr3)
print("Conjunto de datos ordenado 3:", arr3)

print("Conjunto de datos original 4:", arr4)
shellSort(arr4)
print("Conjunto de datos ordenado 4:", arr4)

print("Conjunto de datos original 5:", arr5)
shellSort(arr5)
print("Conjunto de datos ordenado 5:", arr5)
