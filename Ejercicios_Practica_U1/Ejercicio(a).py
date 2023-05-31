#Ejercicio A

def ordenar_nombres():
    # Crear una lista vacía
    nombres = []

    # Obtener la cantidad de nombres que se ingresarán
    n = int(input("Ingrese la cantidad de nombres: "))

    # Pedir al usuario que ingrese los nombres y agregarlos a la lista
    for i in range(n):
        nombre = input(f"Ingrese el nombre {i + 1}: ")
        nombres.append(nombre)

    # Ordenar la lista de nombres en orden alfabético
    nombres.sort()

    # Mostrar los nombres ordenados
    print("Nombres en orden alfabético:")
    for nombre in nombres:
        print(nombre)

# Llamar a la función para probarla
ordenar_nombres()
