# ===========================================
# By: Nury Farelo - Estructuras Datos
# Name: Lista Simplemente Enlazada
# Operaciones implementadas individualmente
# ===========================================

# Clase Nodo
class Nodo:
    def __init__(self, data):
        self.data = data
        self.siguiente = None

# Clase Lista Enlazada Simple
class ListaSE:
    def __init__(self):
        self.cabeza = None

    # -----------------------------------------------
    # Lista Vacía
    # -----------------------------------------------
    def vacio(self):
        if self.cabeza is None:
            print("Está vacía")
        else:
            print("Lista no vacía")

    # -----------------------------------------------
    # Agregar al inicio
    # -----------------------------------------------
    def agregarInicio(self, data):
        nuevo_nodo = Nodo(data)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo

    # -----------------------------------------------
    # 1. Insertar al final
    # -----------------------------------------------
    def insertarFinal(self, data):
        nuevo_nodo = Nodo(data)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return
        actual = self.cabeza
        while actual.siguiente is not None:
            actual = actual.siguiente
        actual.siguiente = nuevo_nodo

    # -----------------------------------------------
    # 2. Insertar antes de un elemento X
    # -----------------------------------------------
    def insertarAntes(self, x, data):
        if self.cabeza is None:
            print("La lista está vacía.")
            return
        # Caso especial: el elemento X es la cabeza
        if self.cabeza.data == x:
            nuevo_nodo = Nodo(data)
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
            return
        actual = self.cabeza
        while actual.siguiente is not None:
            if actual.siguiente.data == x:
                nuevo_nodo = Nodo(data)
                nuevo_nodo.siguiente = actual.siguiente
                actual.siguiente = nuevo_nodo
                return
            actual = actual.siguiente
        print(f"Elemento {x} no encontrado en la lista.")

    # -----------------------------------------------
    # 3. Insertar después de un elemento X
    # -----------------------------------------------
    def insertarDespues(self, x, data):
        if self.cabeza is None:
            print("La lista está vacía.")
            return
        actual = self.cabeza
        while actual is not None:
            if actual.data == x:
                nuevo_nodo = Nodo(data)
                nuevo_nodo.siguiente = actual.siguiente
                actual.siguiente = nuevo_nodo
                return
            actual = actual.siguiente
        print(f"Elemento {x} no encontrado en la lista.")

    # -----------------------------------------------
    # 4. Eliminar el primero
    # -----------------------------------------------
    def eliminarPrimero(self):
        if self.cabeza is None:
            print("La lista está vacía, no hay nada que eliminar.")
            return
        eliminado = self.cabeza.data
        self.cabeza = self.cabeza.siguiente
        print(f"Elemento eliminado: {eliminado}")

    # -----------------------------------------------
    # 5. Eliminar el último
    # -----------------------------------------------
    def eliminarUltimo(self):
        if self.cabeza is None:
            print("La lista está vacía, no hay nada que eliminar.")
            return
        # Caso especial: solo hay un nodo
        if self.cabeza.siguiente is None:
            eliminado = self.cabeza.data
            self.cabeza = None
            print(f"Elemento eliminado: {eliminado}")
            return
        actual = self.cabeza
        while actual.siguiente.siguiente is not None:
            actual = actual.siguiente
        eliminado = actual.siguiente.data
        actual.siguiente = None
        print(f"Elemento eliminado: {eliminado}")

    # -----------------------------------------------
    # 6. Buscar un elemento por su valor (True/False)
    # -----------------------------------------------
    def buscar(self, valor):
        actual = self.cabeza
        while actual is not None:
            if actual.data == valor:
                print(f"Buscar '{valor}': Verdadero")
                return True
            actual = actual.siguiente
        print(f"Buscar '{valor}': Falso")
        return False

    # -----------------------------------------------
    # 7. Contar cuántos elementos tiene la lista
    # -----------------------------------------------
    def contar(self):
        contador = 0
        actual = self.cabeza
        while actual is not None:
            contador += 1
            actual = actual.siguiente
        print(f"La lista tiene {contador} elemento(s).")
        return contador

    # -----------------------------------------------
    # Mostrar la lista
    # -----------------------------------------------
    def mostrar(self):
        if self.cabeza is None:
            print("Lista: []")
            return
        elementos = []
        actual = self.cabeza
        while actual is not None:
            elementos.append(str(actual.data))
            actual = actual.siguiente
        print("Lista: " + " -> ".join(elementos))


# ===========================================
# PRUEBAS
# ===========================================
if __name__ == "__main__":
    lista = ListaSE()

    print("=" * 45)
    print("PRUEBA: Insertar al inicio")
    lista.agregarInicio(30)
    lista.agregarInicio(20)
    lista.agregarInicio(10)
    lista.mostrar()  # 10 -> 20 -> 30

    print("\n" + "=" * 45)
    print("PRUEBA: Insertar al final")
    lista.insertarFinal(40)
    lista.insertarFinal(50)
    lista.mostrar()  # 10 -> 20 -> 30 -> 40 -> 50

    print("\n" + "=" * 45)
    print("PRUEBA: Insertar antes del elemento 30")
    lista.insertarAntes(30, 25)
    lista.mostrar()  # 10 -> 20 -> 25 -> 30 -> 40 -> 50

    print("\n" + "=" * 45)
    print("PRUEBA: Insertar después del elemento 30")
    lista.insertarDespues(30, 35)
    lista.mostrar()  # 10 -> 20 -> 25 -> 30 -> 35 -> 40 -> 50

    print("\n" + "=" * 45)
    print("PRUEBA: Eliminar el primero")
    lista.eliminarPrimero()
    lista.mostrar()  # 20 -> 25 -> 30 -> 35 -> 40 -> 50

    print("\n" + "=" * 45)
    print("PRUEBA: Eliminar el último")
    lista.eliminarUltimo()
    lista.mostrar()  # 20 -> 25 -> 30 -> 35 -> 40

    print("\n" + "=" * 45)
    print("PRUEBA: Buscar elementos")
    lista.buscar(30)   # Verdadero
    lista.buscar(99)   # Falso

    print("\n" + "=" * 45)
    print("PRUEBA: Contar elementos")
    lista.contar()     # 5 elementos

    print("\n" + "=" * 45)
    print("Estado final de la lista:")
    lista.mostrar()
