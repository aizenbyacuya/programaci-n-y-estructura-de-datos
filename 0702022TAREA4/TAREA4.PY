class NodoCarpeta:
    def __init__(self, nombre):
        self.nombre = nombre
        self.subcarpetas = {}
        self.padre = None

    def agregar_carpeta(self, nombre):
        if nombre in self.subcarpetas:
            print(f"⚠️ La carpeta '{nombre}' ya existe.")
        else:
            nueva = NodoCarpeta(nombre)
            nueva.padre = self
            self.subcarpetas[nombre] = nueva
            print(f"📁 Carpeta '{nombre}' creada exitosamente.")

    def mostrar_contenido(self):
        if not self.subcarpetas:
            print("📂 Esta carpeta está vacía.")
        else:
            print("📂 Subcarpetas:")
            for nombre in self.subcarpetas:
                print(f" - {nombre}")

    def eliminar_carpeta(self, nombre):
        if nombre in self.subcarpetas:
            del self.subcarpetas[nombre]
            print(f"🗑️ Carpeta '{nombre}' eliminada.")
        else:
            print(f"⚠️ No existe la carpeta '{nombre}'.")

    def obtener_carpeta(self, nombre):
        return self.subcarpetas.get(nombre, None)


def ruta_actual(carpeta):
    ruta = []
    actual = carpeta
    while actual:
        ruta.append(actual.nombre)
        actual = actual.padre
    return "/".join(reversed(ruta))


def simulador():
    raiz = NodoCarpeta("root")
    actual = raiz

    while True:
        print("\n==============================")
        print(f"📍 Carpeta actual: /{ruta_actual(actual)}")
        print("==============================")
        print("[1] Crear carpeta")
        print("[2] Ver subcarpetas")
        print("[3] Eliminar carpeta")
        print("[4] Entrar a una carpeta")
        print("[5] Subir (volver atrás)")
        print("[6] Salir")
        print("==============================")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Nombre de la nueva carpeta: ")
            actual.agregar_carpeta(nombre)

        elif opcion == "2":
            actual.mostrar_contenido()

        elif opcion == "3":
            nombre = input("Nombre de la carpeta a eliminar: ")
            actual.eliminar_carpeta(nombre)

        elif opcion == "4":
            nombre = input("Nombre de la carpeta a abrir: ")
            siguiente = actual.obtener_carpeta(nombre)
            if siguiente:
                actual = siguiente
            else:
                print("⚠️ Carpeta no encontrada.")

        elif opcion == "5":
            if actual.padre:
                actual = actual.padre
            else:
                print("📍 Ya estás en la raíz.")

        elif opcion == "6":
            print("👋 Programa finalizado.")
            break

        else:
            print("❌ Opción inválida, intenta de nuevo.")


if __name__ == "__main__":
    simulador()
