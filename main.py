from arbol import Arbol

arbol = Arbol("Ricardo") #Nodo raiz
arbol.agregar("Jack") #Agregar datos
arbol.agregar("Lion")
arbol.agregar("Adia")
arbol.agregar("JassR")
arbol.agregar("Ero")
nombre = input("Ingresa un nombre: ") #Para agregar
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

    # Eliminar
nodo_eliminar = "Ricardo"
arbol.eliminar(nodo_eliminar)

# Muestra los recorridos después de la eliminación
print("<-------------------------->")
print("  Preorden después de eliminar:")
arbol.preorden()

print("Inorden después de eliminar:")
arbol.inorden()


print("Postorden después de eliminar:")
arbol.postorden()

