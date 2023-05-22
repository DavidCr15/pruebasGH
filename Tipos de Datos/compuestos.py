lista =[]

print(type(lista))

lista= ["Ecuador", "Peru", "Mexico"]
print(lista)

lista=["Juan", 45, 6.5, True,["Ecuador", "Peru", "Mexico"]]
print(lista)

lista= ["Ecuador", "Peru", "Mexico"]
lista.append ("Brasil")
print(lista)

lista2 = lista.copy()
print(lista2)


lista2.clear()
print(lista2)


lista2 = lista.copy()
print(lista2.count("Peru"))
lista2.append("Bolivia")
lista2.append("Peru")
print(lista2.append("Colombia"))
print(lista2)

print(len(lista2))

print(lista2[4])

lista2[5]="Peru"
print(lista2)

#eliminar elementos de una lista

lista2.pop()
print(lista2)

lista2.remove("Brasil")
print(lista2)

lista2.reverse()
print(lista2)

lista2.sort()
print(lista2)

lista3 = [4, 5, "B","b","c"]
lista3.sort
print(lista3)

#tupla
tupla =()
print(type(tupla))

#tupla.append("Kevin")
#print(tupla)


tupla2 = ["Juan", "Pedro", "Maria", "Juan"]
print(tupla2.count("Juan"))
print(tupla2.index("Maria"))
#print(tupla.index())

#print(tupla[2])
#print(tupla[3])

lista=list(tupla2)
print(type(lista))


lista.append("Mario")
print(lista)

tupla2 =tuple(lista)
print(tupla2)

#range
rango=range(6)
print(set)

#set
set={2,3,4,5,6,6}
print(set)
print(type(set))

#diccionarios
cliente001 = {
    "Nombre" : "David",
    "Cedula" : 1724988140,
    "Celular" : "0964058605",
    "Correo": "cdpincha1@espe.edu.ec"
}

print(cliente001)
print(type(cliente001))

print(cliente001["Correo"])
print(cliente001.get("Celular"))

cliente001["Nombre"]= "Cristian"
print(cliente001.get("Nombre"))