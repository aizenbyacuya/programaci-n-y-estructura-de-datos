
class Nodo:
    """
    Clase unificada para representar Género, Artista o Canción.
    Género/Artista: usa 'tipo', 'nombre', 'hijos'.
    Canción: usa 'nombre', 'letra'.
    """
    def __init__(self, nombre, tipo=None, letra=""):
        self.nombre = nombre
        self.tipo = tipo  # 'genero', 'artista', o None para Canción
        self.letra = letra # Se usa solo si es Canción
        self.hijos = []   # Contendrá Nodos Musicales (Artistas/Canciones)

coleccion_musical = {} 

# --- FUNCIONES DE CREACIÓN Y BÚSQUEDA ---

def _buscar_artista(nombre_artista):
    """Función auxiliar para encontrar un Artista en toda la colección."""
    for genero_nodo in coleccion_musical.values():
        for artista_nodo in genero_nodo.hijos:
            if artista_nodo.nombre.lower() == nombre_artista.lower():
                return artista_nodo
    return None

def _buscar_cancion(nombre_cancion):
    """Función auxiliar para encontrar una Canción en toda la colección, devuelve (cancion, artista)."""
    for genero_nodo in coleccion_musical.values():
        for artista_nodo in genero_nodo.hijos:
            for cancion_nodo in artista_nodo.hijos:
                if cancion_nodo.nombre.lower() == nombre_cancion.lower():
                    return cancion_nodo, artista_nodo.nombre
    return None, None

def crear_nodo_modificado():
    """Permite la creación de nodos tipo género, artista o canción."""
    print("\n--- CREAR NUEVO ELEMENTO MODIFICADO ---")
    
    tipo_nodo = input("¿Qué tipo de elemento quieres crear? (genero/artista/cancion): ").lower()
    nombre = input(f"Introduce el nombre del/la {tipo_nodo.upper()}: ")
    
    if tipo_nodo == 'genero':
        if nombre in coleccion_musical:
            print(f"⚠️ El Género '{nombre}' ya existe.")
            return
        coleccion_musical[nombre] = Nodo(nombre, tipo='genero')
        print(f"✅ Género '{nombre}' creado con éxito.")
        
    elif tipo_nodo == 'artista':
        nombre_genero = input("Introduce el GÉNERO al que pertenece este artista: ")
        
        if nombre_genero not in coleccion_musical:
            print(f"❌ Error: El Género '{nombre_genero}' no existe. Créalo primero.")
            return

        genero = coleccion_musical[nombre_genero]
        if _buscar_artista(nombre):
             print(f"⚠️ El Artista '{nombre}' ya existe en algún género.")
             return
            
        nuevo_artista = Nodo(nombre, tipo='artista')
        genero.hijos.append(nuevo_artista)
        print(f"✅ Artista '{nombre}' añadido al Género '{nombre_genero}'.")
        
    elif tipo_nodo == 'cancion':
        nombre_artista = input("Introduce el nombre del ARTISTA al que pertenece: ")
        
        artista_encontrado = _buscar_artista(nombre_artista)
        
        if not artista_encontrado:
            print(f"❌ Error: El Artista '{nombre_artista}' no existe. Créalo primero.")
            return

        if _buscar_cancion(nombre)[0] is not None:
             print(f"⚠️ La Canción '{nombre}' ya existe.")
             return
            
        letra = input("Introduce la letra de la canción: \n")
        nueva_cancion = Nodo(nombre, tipo=None, letra=letra) # tipo=None es el marcador de Canción
        artista_encontrado.hijos.append(nueva_cancion)
        print(f"✅ Canción '{nombre}' añadida a '{nombre_artista}'.")
        
    else:
        print("❌ Tipo de elemento no reconocido.")


def recorrer_estructura_unificada():
    """Recorre y muestra la jerarquía completa: Género > Artista > Canción."""
    print("\n--- COLECCIÓN MUSICAL COMPLETA ---")
    if not coleccion_musical:
        print("La colección musical está vacía.")
        return

    for nombre_genero, genero in coleccion_musical.items():
        print(f"▶️ GÉNERO: {genero.nombre} [{len(genero.hijos)} Artista(s)]")
        
        if not genero.hijos: continue
            
        for artista in genero.hijos:
            print(f"  ├── ARTISTA: {artista.nombre} [{len(artista.hijos)} Canción(es)]")
            
            if not artista.hijos: continue
                
            for cancion in artista.hijos:
                print(f"  │     └── CANCIÓN: {cancion.nombre}")
    print("-" * 30)


def buscar_canciones_por_genero_modificado():
    """Busca y muestra las canciones de un género específico."""
    print("\n--- BUSCAR CANCIONES POR GÉNERO ---")
    nombre_genero = input("Introduce el nombre del GÉNERO: ")
    
    if nombre_genero not in coleccion_musical:
        print(f"❌ Error: El Género '{nombre_genero}' no existe.")
        return

    genero = coleccion_musical[nombre_genero]
    conteo_canciones = 0
    
    print(f"\n🎧 Canciones encontradas en el Género **{genero.nombre}**:")
    
    for artista in genero.hijos:
        if artista.hijos:
            print(f"  **Artista:** {artista.nombre}")
            for cancion in artista.hijos:
                print(f"    - {cancion.nombre}")
                conteo_canciones += 1
                
    if conteo_canciones == 0:
        print(f"  (No se encontraron canciones para el género '{nombre_genero}')")


def buscar_canciones_por_artista_modificado():
    """Busca y muestra las canciones de un artista específico."""
    print("\n--- BUSCAR CANCIONES POR ARTISTA ---")
    nombre_artista = input("Introduce el nombre del ARTISTA: ")
    
    artista_encontrado = _buscar_artista(nombre_artista)
            
    if not artista_encontrado:
        print(f"❌ Error: El Artista '{nombre_artista}' no existe.")
        return
        
    print(f"\n🎧 Canciones encontradas del Artista **{artista_encontrado.nombre}**:")
    
    if not artista_encontrado.hijos:
        print(f"  (El artista '{nombre_artista}' no tiene canciones registradas.)")
        return
        
    for cancion in artista_encontrado.hijos:
        print(f"  - {cancion.nombre}")


def buscar_y_mostrar_letra_modificado():
    """Busca y muestra la letra de una canción específica."""
    print("\n--- BUSCAR LETRA DE CANCIÓN ---")
    nombre_cancion = input("Introduce el nombre exacto de la CANCIÓN: ")
    
    cancion_encontrada, artista_nombre = _buscar_cancion(nombre_cancion)

    if not cancion_encontrada:
        print(f"❌ Error: La Canción '{nombre_cancion}' no fue encontrada.")
        return
        
    print("-" * 30)
    print(f"📖 LETRA de **{cancion_encontrada.nombre}** de **{artista_nombre}**:")
    print(cancion_encontrada.letra)
    print("-" * 30)


def editar_letra_cancion_modificado():
    """Edita la letra de una canción existente."""
    print("\n--- EDITAR LETRA DE CANCIÓN ---")
    nombre_cancion = input("Introduce el nombre exacto de la CANCIÓN cuya letra deseas editar: ")

    cancion_a_editar, artista_nombre = _buscar_cancion(nombre_cancion)

    if not cancion_a_editar:
        print(f"❌ Error: La Canción '{nombre_cancion}' no fue encontrada.")
        return
        
    print(f"\n**Canción seleccionada:** '{cancion_a_editar.nombre}' de '{artista_nombre}'.")
    print("--- Letra Actual ---")
    print(cancion_a_editar.letra)
    print("--------------------")
    
    nueva_letra = input("Introduce la NUEVA letra: \n")
    cancion_a_editar.letra = nueva_letra
    print(f"✅ Letra de '{cancion_a_editar.nombre}' actualizada con éxito.")


# --- FUNCIÓN PRINCIPAL DEL MENÚ (CLI) ---

def mostrar_menu_modificado():
    """Muestra las opciones del menú."""
    print("\n" + "="*40)
    print("      🎸 COLECCIÓN MUSICAL🎤")
    print("="*40)
    print("1. Recorrer la colección completa (Mostrar todo)")
    print("2. Crear nuevo elemento (Género, Artista o Canción)")
    print("3. Buscar canciones por GÉNERO")
    print("4. Buscar canciones por ARTISTA")
    print("5. Buscar y mostrar la LETRA")
    print("6. Editar la LETRA de una canción")
    print("0. Salir del sistema")
    print("="*40)

def main_modificado():
    """Función principal que ejecuta el menú interactivo."""
    while True:
        mostrar_menu_modificado()
        opcion = input("Selecciona una opción (0-6): ")
        
        if opcion == '1':
            recorrer_estructura_unificada()
        elif opcion == '2':
            crear_nodo_modificado()
        elif opcion == '3':
            buscar_canciones_por_genero_modificado()
        elif opcion == '4':
            buscar_canciones_por_artista_modificado()
        elif opcion == '5':
            buscar_y_mostrar_letra_modificado()
        elif opcion == '6':
            editar_letra_cancion_modificado()
        elif opcion == '0':
            print("👋 ¡Gracias por usar la Colección Musical! ¡Adiós!")
            break
        else:
            print("❌ Opción no válida. Por favor, selecciona un número del 0 al 6.")

if __name__ == "__main__":
    # Inicialización para demostrar la funcionalidad rápidamente
    print("--- Inicializando con datos de ejemplo (Diseño Unificado) ---")
    
    # Géneros
    coleccion_musical['Clásica'] = Nodo('Clásica', tipo='genero')
    coleccion_musical['Electrónica'] = Nodo('Electrónica', tipo='genero')

    # Artistas
    beethoven = Nodo('Beethoven', tipo='artista')
    daft_punk = Nodo('Daft Punk', tipo='artista')
    
    coleccion_musical['Clásica'].hijos.append(beethoven)
    coleccion_musical['Electrónica'].hijos.append(daft_punk)
    
    # Canciones
    beethoven.hijos.append(Nodo('Sinfonía No. 5', letra="Ta-ta-ta-TAAA!\n(Letra de ejemplo de Beethoven)"))
    daft_punk.hijos.append(Nodo('One More Time', letra="One more time, we're gonna celebrate...\n(Letra de ejemplo de Daft Punk)"))
    
    main_modificado()