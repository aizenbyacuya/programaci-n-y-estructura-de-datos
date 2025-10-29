class NodoBST:
    def __init__(self, dato):
        self.dato = dato
        self.izq = None
        self.der = None

class BST:
    def __init__(self):
        self.raiz = None

    def agregar(self, dato):
        nuevo = NodoBST(dato)
        if self.raiz is None:
            self.raiz = nuevo
        else:
            self._agregar_nodo(self.raiz, nuevo)

    def _agregar_nodo(self, actual, nuevo):
        if nuevo.dato < actual.dato:
            if actual.izq is None:
                actual.izq = nuevo
            else:
                self._agregar_nodo(actual.izq, nuevo)
        elif nuevo.dato > actual.dato:
            if actual.der is None:
                actual.der = nuevo
            else:
                self._agregar_nodo(actual.der, nuevo)

    def contiene(self, dato):
        return self._buscar(self.raiz, dato)

    def _buscar(self, actual, dato):
        if actual is None:
            return False
        if dato == actual.dato:
            return True
        elif dato < actual.dato:
            return self._buscar(actual.izq, dato)
        else:
            return self._buscar(actual.der, dato)

    def eliminar(self, dato):
        self.raiz = self._eliminar_nodo(self.raiz, dato)

    def _eliminar_nodo(self, nodo, dato):
        if nodo is None:
            return None
        if dato < nodo.dato:
            nodo.izq = self._eliminar_nodo(nodo.izq, dato)
        elif dato > nodo.dato:
            nodo.der = self._eliminar_nodo(nodo.der, dato)
        else:
            if nodo.izq is None and nodo.der is None:
                return None
            elif nodo.izq is None:
                return nodo.der
            elif nodo.der is None:
                return nodo.izq
            min_val = self._minimo(nodo.der)
            nodo.dato = min_val
            nodo.der = self._eliminar_nodo(nodo.der, min_val)
        return nodo

    def _minimo(self, nodo):
        while nodo.izq:
            nodo = nodo.izq
        return nodo.dato

    def recorrido_inorden(self):
        return self._inorden(self.raiz, [])

    def _inorden(self, nodo, lista):
        if nodo:
            self._inorden(nodo.izq, lista)
            lista.append(nodo.dato)
            self._inorden(nodo.der, lista)
        return lista

    def recorrido_preorden(self):
        return self._preorden(self.raiz, [])

    def _preorden(self, nodo, lista):
        if nodo:
            lista.append(nodo.dato)
            self._preorden(nodo.izq, lista)
            self._preorden(nodo.der, lista)
        return lista

    def recorrido_postorden(self):
        return self._postorden(self.raiz, [])

    def _postorden(self, nodo, lista):
        if nodo:
            self._postorden(nodo.izq, lista)
            self._postorden(nodo.der, lista)
            lista.append(nodo.dato)
        return lista

if __name__ == "__main__":
    arbol = BST()
    for num in [8, 3, 10, 1, 6, 14, 4, 7, 13]:
        arbol.agregar(num)

    print("Recorrido Inorden:", arbol.recorrido_inorden())
    print("Recorrido Preorden:", arbol.recorrido_preorden())
    print("Recorrido Postorden:", arbol.recorrido_postorden())

    print("¿Contiene el número 6?:", arbol.contiene(6))
    print("¿Contiene el número 15?:", arbol.contiene(15))

    arbol.eliminar(10)
    print("Inorden tras eliminar 10:", arbol.recorrido_inorden())
