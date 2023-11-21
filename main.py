from arbol import Arbol

arbol = Arbol("Ricardo")
arbol.agregar("Jack")
arbol.agregar("Lion")
arbol.agregar("Adia")
arbol.agregar("JassR")
arbol.agregar("Ero")
nombre = input("Ingresa un nombre: ")
arbol.agregar(nombre)
arbol.preorden()
arbol.inorden()
arbol.postorden()

#Busqueda
busqueda = input("Buscar en el arbol: ")
nodo = arbol.buscar(busqueda)
if nodo is None:
    print(f"{busqueda} no existe")
else: 
    print(f"{busqueda} si existe")