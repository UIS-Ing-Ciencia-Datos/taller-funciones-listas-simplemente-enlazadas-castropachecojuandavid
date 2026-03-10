# ===========================================
# By: Nury Farelo - Estructuras Datos
# Name: Lista Simplemente Enlazada 
# ===========================================

# Clase Nodo
class Nodo:
    def __init__(self, data):
        self.data = data
        self.siguiente = None

# Clase Lista enlazada simple
class ListaSE:
    def __init__(self):
        self.cabeza = None

    # Lista Vacia
    def vacio(self):
        if self.cabeza == None:
            print("Está vacia")
        else:
            print("Lista no vacia")

    # Mostrar lista
    def mostrar(self):
        if self.cabeza is None:
            print("Lista vacía")
            return
        actual = self.cabeza
        elementos = []
        while actual is not None:
            elementos.append(str(actual.data))
            actual = actual.siguiente
        print(" -> ".join(elementos))

    # Agregar al inicio
    def agregarInicio(self, data):
        nuevo_nodo = Nodo(data)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo

    # ✅ Insertar al final
    def agregarFinal(self, data):
        nuevo_nodo = Nodo(data)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return
        actual = self.cabeza
        while actual.siguiente is not None:
            actual = actual.siguiente
        actual.siguiente = nuevo_nodo

    # ✅ Insertar antes de un elemento X
    def insertarAntes(self, x, data):
        if self.cabeza is None:
            print("Lista vacía")
            return
        # Si el elemento X es la cabeza
        if self.cabeza.data == x:
            nuevo_nodo = Nodo(data)
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
            return
        # Recorrer hasta encontrar el nodo anterior a X
        actual = self.cabeza
        while actual.siguiente is not None:
            if actual.siguiente.data == x:
                nuevo_nodo = Nodo(data)
                nuevo_nodo.siguiente = actual.siguiente
                actual.siguiente = nuevo_nodo
                return
            actual = actual.siguiente
        print(f"El elemento {x} no fue encontrado")

    # ✅ Insertar después de un elemento X
    def insertarDespues(self, x, data):
        if self.cabeza is None:
            print("Lista vacía")
            return
        actual = self.cabeza
        while actual is not None:
            if actual.data == x:
                nuevo_nodo = Nodo(data)
                nuevo_nodo.siguiente = actual.siguiente
                actual.siguiente = nuevo_nodo
                return
            actual = actual.siguiente
        print(f"El elemento {x} no fue encontrado")

    # ✅ Eliminar el primero
    def eliminarPrimero(self):
        if self.cabeza is None:
            print("Lista vacía")
            return
        eliminado = self.cabeza.data
        self.cabeza = self.cabeza.siguiente
        print(f"Elemento {eliminado} eliminado")

    # ✅ Eliminar el último
    def eliminarUltimo(self):
        if self.cabeza is None:
            print("Lista vacía")
            return
        # Si solo hay un elemento
        if self.cabeza.siguiente is None:
            eliminado = self.cabeza.data
            self.cabeza = None
            print(f"Elemento {eliminado} eliminado")
            return
        # Recorrer hasta el penúltimo nodo
        actual = self.cabeza
        while actual.siguiente.siguiente is not None:
            actual = actual.siguiente
        eliminado = actual.siguiente.data
        actual.siguiente = None
        print(f"Elemento {eliminado} eliminado")

    # ✅ Buscar elemento por su valor (devuelve True o False)
    def buscarElemento(self, valor):
        if self.cabeza is None:
            print("Lista vacía")
            return False
        actual = self.cabeza
        while actual is not None:
            if actual.data == valor:
                print(f"Elemento {valor} encontrado: Verdadero")
                return True
            actual = actual.siguiente
        print(f"Elemento {valor} encontrado: Falso")
        return False

    # ✅ Contar cuántos elementos tiene la lista
    def contarElementos(self):
        contador = 0
        actual = self.cabeza
        while actual is not None:
            contador += 1
            actual = actual.siguiente
        print(f"La lista tiene {contador} elemento(s)")
        return contador


# ===========================================
# PRUEBAS
# ===========================================
lista = ListaSE()

print("=== Agregar elementos ===")
lista.agregarFinal(10)
lista.agregarFinal(20)
lista.agregarFinal(30)
lista.mostrar()                          # 10 -> 20 -> 30

print("\n=== Insertar al final ===")
lista.agregarFinal(40)
lista.mostrar()                          # 10 -> 20 -> 30 -> 40

print("\n=== Insertar antes de 20 ===")
lista.insertarAntes(20, 15)
lista.mostrar()                          # 10 -> 15 -> 20 -> 30 -> 40

print("\n=== Insertar después de 20 ===")
lista.insertarDespues(20, 25)
lista.mostrar()                          # 10 -> 15 -> 20 -> 25 -> 30 -> 40

print("\n=== Eliminar el primero ===")
lista.eliminarPrimero()
lista.mostrar()                          # 15 -> 20 -> 25 -> 30 -> 40

print("\n=== Eliminar el último ===")
lista.eliminarUltimo()
lista.mostrar()                          # 15 -> 20 -> 25 -> 30

print("\n=== Buscar elementos ===")
lista.buscarElemento(25)                 # Verdadero
lista.buscarElemento(99)                 # Falso

print("\n=== Contar elementos ===")
lista.contarElementos()                  # 4
