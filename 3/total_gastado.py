"""Ejercicio 5
Suponga que tiene una verdulería y carga la cantidad y el precio de lo comprado por un cliente. Realice un programa que tome de a uno la cantidad y el precio comprado por el cliente y al finalizar la compra retorne el monto total gastado. 
"""

is_loading = True
my_products = {}

while is_loading:
    cantidad = int(input("ingrese el producto: "))
    precio = float(input("ingrese el precio del producto: "))
    my_products[cantidad] = precio
    print(my_products)
    opcion = input("desea cargar mas productos? marque S o N para salir")
    if opcion == "N":
        is_loading = False
        total = sum(my_products.values())
        print(f"El total es {total}")

