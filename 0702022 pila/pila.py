class Pila:
    def __init__(self):
        self.elementos = []

    def push(self, dato):
        self.elementos.append(dato)

    def pop(self):
        if not self.esta_vacia():
            return self.elementos.pop()
        else:
            return "La pila está vacía"

    def peek(self):
        if not self.esta_vacia():
            return self.elementos[-1]
        else:
            return "La pila está vacía"

    def esta_vacia(self):
        return len(self.elementos) == 0

    def tamaño(self):
        return len(self.elementos)


if __name__ == "__main__":
    pila = Pila()
    pila.push(10)
    pila.push(20)
    pila.push(30)

    print("Elemento en la cima:", pila.peek())   # 30
    print("Tamaño de la pila:", pila.tamaño())  # 3

    print("Sacando elemento:", pila.pop())      # 30
    print("Sacando elemento:", pila.pop())      # 20

    print("¿Está vacía?", pila.esta_vacia())    # False
    print("Sacando elemento:", pila.pop())      # 10
    print("¿Está vacía?", pila.esta_vacia())    # True
