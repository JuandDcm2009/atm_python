productos = ["cuaderno", "colores", "maleta", "cartuchera"]
carrito = []

menu = f"""
+----------------------+
   Utiles Escolares
+----------------------+

    1. Agregar utiles
    2. Listar utiles
    3. Actualizar Item
    4. Eliminar Item

+----------------------+
"""

def imprimirTitulo(title):

    print("\n\n+----------------------+")
    print(f"      {title}")
    print("+----------------------+\n")

def imprimirLista(lista):
    for i in range(len(lista)):
         print(f"       {i + 1}. {lista[i]}")
    print("")
    print("+----------------------+\n")

    
def agregarUtiles():
    imprimirTitulo("Añadir Utiles")
    imprimirLista(productos)
    _input = str(input("Ingrese el nombre del producto: "))
    for i in range(len(productos)):
        if productos[i] == _input:
            carrito.append(_input)
            input("Continuar...")
            break

def listarUtiles():
    imprimirTitulo("Lista de Utiles")
    imprimirLista(carrito)
    input("Continuar...")

def actualizarItem():
    imprimirTitulo("Actualizar Item")
    imprimirLista(carrito)
    print("Ingrese el codigo del Item: ")
    _input = int(input()) - 1
    if _input >= 0 and _input <= len(carrito):
        imprimirLista(productos)
        idd = _input
            
        _input = str(input("Ingrese el nombre del producto: "))
    for i in range(len(productos)):
        if productos[i] == _input:
            carrito.pop(idd)
            carrito.insert(idd, _input)
            input("Continuar...")
            break

def eliminarItem():
    imprimirTitulo("Eliminar Item")
    imprimirLista(carrito)
    _input = int(input("Ingrese el codigo del producto: ")) - 1
    if _input >= 0 and _input <= len(carrito):
        carrito.pop(_input)
        print("Producto eliminado..")
    else: 
        print("Ese producto no existe.")
    input("Continuar...")

while True:
    
    
    print(menu)
    opcion = input("Ingrese una opcion: ")

    if opcion == "1":
        agregarUtiles()

    elif opcion == "2":
        listarUtiles()

    elif opcion == "3":
        actualizarItem()

    elif opcion == "4":
        eliminarItem()

    