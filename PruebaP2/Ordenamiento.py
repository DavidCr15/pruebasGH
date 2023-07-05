def ordenamiento_seleccion(lista):
    n = len(lista)
    for i in range(n):
        indice_minimo = i
        for j in range(i+1, n):
            if lista[j] < lista[indice_minimo]:
                indice_minimo = j
        lista[i], lista[indice_minimo] = lista[indice_minimo], lista[i]
    return lista

# Ejemplo de uso
numeros = [9, 2, 5, 1, 7]
numeros_ordenados = ordenamiento_seleccion(numeros)
print(numeros_ordenados)
