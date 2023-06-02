class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if self.esta_vacia():
            return None
        return self.items.pop()

    def cima(self):
        if self.esta_vacia():
            return None
        return self.items[-1]

pila = Pila()
pila.apilar(1)
pila.apilar(2)
pila.apilar(3)
print("Cima de la pila:", pila.cima())
print("Desapilando elementos:")
while not pila.esta_vacia():
    print(pila.desapilar())
