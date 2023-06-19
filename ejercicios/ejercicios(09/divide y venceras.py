def distribution_sort(arr):
    min_val = min(arr)
    max_val = max(arr)
    range_val = max_val - min_val + 1

    count = [0]*range_val

    for num in arr:
        count[num-min_val]+=1

    output = []

    for i in range (range_val):
        output.extend([i+min_val]*count[i])

    return output
 #solicitar al usuario una lista de números 
numbers = input("Ingresa una lista de números separados por espacios: ").split()
numbers = [int(num) for num in numbers]

#ordenar la lista de números utilizando el algoritmo de ordenación por distribución
sorted_numbers = distribution_sort(numbers)
#imprimir la lista ordenada
print("Lista ordenada: ")
print(sorted_numbers)