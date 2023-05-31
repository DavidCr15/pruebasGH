class Cola:
    def __init__(self):
        # La cola vacía se representa por una lista vacía
        self.items = []

    def encolar(self, x):
        self.items.append(x)

    def desencolar(self):
        if self.es_vacia():
            raise ValueError("La cola está vacía")
        return self.items.pop(0)

    def es_vacia(self):
        return len(self.items) == 0

