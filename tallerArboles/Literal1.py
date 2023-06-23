class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

def contar_nodos(arbol):
    if arbol is None:
        return 0
    else:
        return 1 + contar_nodos(arbol.izquierdo) + contar_nodos(arbol.derecho)

# Crear un árbol binario de ejemplo
raiz = Nodo(1)
raiz.izquierdo = Nodo(2)
raiz.derecho = Nodo(3)
raiz.izquierdo.izquierdo = Nodo(4)
raiz.izquierdo.derecho = Nodo(5)

# Calcular la cantidad de nodos
cantidad_nodos = contar_nodos(raiz)
print("Cantidad de nodos:", cantidad_nodos)
