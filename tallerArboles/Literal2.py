class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

def buscar_valor(arbol, valor):
    if arbol is None:
        return False
    elif arbol.valor == valor:
        return True
    elif valor < arbol.valor:
        return buscar_valor(arbol.izquierdo, valor)
    else:
        return buscar_valor(arbol.derecho, valor)

# Crear un árbol binario de ejemplo
raiz = Nodo(5)
raiz.izquierdo = Nodo(3)
raiz.derecho = Nodo(7)
raiz.izquierdo.izquierdo = Nodo(2)
raiz.izquierdo.derecho = Nodo(4)

# Buscar un valor en el árbol
valor_buscar = 4
encontrado = buscar_valor(raiz, valor_buscar)
print("Valor", valor_buscar, "encontrado:", encontrado)
