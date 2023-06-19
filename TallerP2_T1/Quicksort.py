def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        smaller = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quicksort(smaller) + [pivot] + quicksort(greater)

# Ejemplo de uso
arr1 = [4, 2, 8, 5, 1, 3, 7, 6]
arr2 = [9, 2, 1, 6, 3, 8, 5, 7, 4]
arr3 = [5, 4, 3, 2, 1]
arr4 = [1, 2, 3, 4, 5]
arr5 = []

sorted_arr1 = quicksort(arr1)
print("Arreglo ordenado 1:", sorted_arr1)

sorted_arr2 = quicksort(arr2)
print("Arreglo ordenado 2:", sorted_arr2)

sorted_arr3 = quicksort(arr3)
print("Arreglo ordenado 3:", sorted_arr3)

sorted_arr4 = quicksort(arr4)
print("Arreglo ordenado 4:", sorted_arr4)

sorted_arr5 = quicksort(arr5)
print("Arreglo ordenado 5:", sorted_arr5)
