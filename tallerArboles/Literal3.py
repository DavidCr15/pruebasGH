class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

def encontrar_minimo(arbol):
    while arbol.izquierdo is not None:
        arbol = arbol.izquierdo
    return arbol

def eliminar_valor(arbol, valor):
    if arbol is None:
        return None

    if valor < arbol.valor:
        arbol.izquierdo = eliminar_valor(arbol.izquierdo, valor)
    elif valor > arbol.valor:
        arbol.derecho = eliminar_valor(arbol.derecho, valor)
    else:
        if arbol.izquierdo is None:
            return arbol.derecho
        elif arbol.derecho is None:
            return arbol.izquierdo
        else:
            minimo = encontrar_minimo(arbol.derecho)
            arbol.valor = minimo.valor
            arbol.derecho = eliminar_valor(arbol.derecho, minimo.valor)
    
    return arbol

# Crear un árbol binario de ejemplo
raiz = Nodo(5)
raiz.izquierdo = Nodo(3)
raiz.derecho = Nodo(7)
raiz.izquierdo.izquierdo = Nodo(2)
raiz.izquierdo.derecho = Nodo(4)

# Eliminar un valor del árbol
valor_eliminar = 3
raiz = eliminar_valor(raiz, valor_eliminar)
