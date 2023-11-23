from nodo import Nodo

class Arbol: 
    #Funciones privadas
    def __init__(self, dato):
        self.raiz = Nodo(dato)
        
    #Metodo de insercion
    def __recursive_insert(self, nodo, dato):
        if dato < nodo.dato:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(dato)
            else:
                self.__recursive_insert(nodo.izquierda, dato)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(dato)
            else:
                self.__recursive_insert(nodo.derecha, dato)
                
    #Recorrido inorden, preorden y postorden
    def __inorden(self, nodo):
        if nodo is not None:
            self.__inorden(nodo.izquierda)
            print(nodo.dato, end=", ")
            self.__inorden(nodo.derecha)
            
    def __preorden(self, nodo):
        if nodo is not None:
            print(nodo.dato, end=", ")
            self.__preorden(nodo.izquierda)
            self.__preorden(nodo.derecha)
            
    def __postorder(self, nodo):
        if nodo is not None:
            self.__postorder(nodo.izquierda)
            self.__postorder(nodo.derecha)
            print(nodo.dato, end=", ")
    
    #Metodo de busqueda
    def __busqueda(self, nodo, busqueda):
        if nodo is None:
            return None
        if nodo.dato == busqueda:
            return nodo
        if busqueda < nodo.dato:
            return self.__busqueda(nodo.izquierda, busqueda)
        else:
            return self.__busqueda(nodo.derecha, busqueda)

    #Metodo de eliminar
    def eliminar(self, dato):
        self.raiz = self.__recursive_delete(self.raiz, dato)

    def __recursive_delete(self, nodo, dato):
        if nodo is None:
            return nodo

        # Buscar el nodo a eliminar
        if dato < nodo.dato:
            nodo.izquierda = self.__recursive_delete(nodo.izquierda, dato)
        elif dato > nodo.dato:
            nodo.derecha = self.__recursive_delete(nodo.derecha, dato)
        else:
            # Caso 1: Nodo con un hijo o sin hijos
            if nodo.izquierda is None:
                return nodo.derecha
            elif nodo.derecha is None:
                return nodo.izquierda

            # Caso 3: Nodo con dos hijos
            nodo.dato = self.__get_min_value(nodo.derecha)
            nodo.derecha = self.__recursive_delete(nodo.derecha, nodo.dato)

        return nodo

    def __get_min_value(self, nodo):
        current = nodo
        while current.izquierda is not None:
            current = current.izquierda
        return current.dato
        
    #Funciones publicas
    def agregar(self, dato):
        self.__recursive_insert(self.raiz, dato)
        
    def inorden(self):
        print("Inorden: ")
        self.__inorden(self.raiz)
        print("")
        
    def preorden(self):
        print("Preorden: ")
        self.__preorden(self.raiz)
        print("")
        
    def postorden(self):
        print("Postorden:")
        self.__postorder(self.raiz)
        print("")
        
    def buscar(self, busqueda):
        return self.__busqueda(self.raiz, busqueda)