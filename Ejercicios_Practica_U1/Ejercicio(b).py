#Ejercicio B

# Crear una pila vacía
pila = []

# Apilar elementos
pila.append(1)
pila.append(2)
pila.append(3)

# Desapilar elementos
elemento = pila.pop()
print(elemento)  # Output: 3

elemento = pila.pop()
print(elemento)  # Output: 2

elemento = pila.pop()
print(elemento)  # Output: 1

# Verificar si la pila está vacía
if len(pila) == 0:
    print("La pila está vacía")
else:
    print("La pila no está vacía")
