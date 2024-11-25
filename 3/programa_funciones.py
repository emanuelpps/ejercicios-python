mi_compra = {}


def opcion():
    selection = str(input("Ingrese la opcion que desea \n 1 - Dar de alta una compra  \n 2 - Dar de baja una compra  \n 3 - Consultar todas las compras realizadas  \n 4 - Modificar compra realizada \n"))
    if selection == "1":
        alta()
    if selection == "2":
        baja()
    if selection == "3":
        consulta()
    if selection == "4":
        modificar()


def alta():
    producto = str(input("ingrese el producto: "))
    precio = float(input("ingrese el precio del producto: "))
    mi_compra[producto] = precio
    print("Producto dado de alta")
    opcion()


def baja():
    producto_bajar = str(
        input("escribe el nombre del prodcuto a dar de baja: "))
    del mi_compra[producto_bajar]
    opcion()


def consulta():
    print(mi_compra)
    opcion()


def modificar():
    nuevo_producto = str(input("ingrese el nuevo producto: "))
    producto_reemplazar = str(
        input("Ingrese el producto por que que lo quiere reemplazar"))
    mi_compra[nuevo_producto] = mi_compra.pop(producto_reemplazar)
    mi_compra[nuevo_producto] = str(input("ingrese su valor"))
    opcion()


opcion()
