class Cola:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def encolar(self, item):
        self.items.append(item)

    def desencolar(self):
        if self.esta_vacia():
            return None
        return self.items.pop(0)

    def frente(self):
        if self.esta_vacia():
            return None
        return self.items[0]

cola = Cola()
cola.encolar(1)
cola.encolar(2)
cola.encolar(3)
print("Frente de la cola:", cola.frente())
print("Desencolando elementos:")
while not cola.esta_vacia():
    print(cola.desencolar())
