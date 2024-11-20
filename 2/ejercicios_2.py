"1) Cree un programa que incorpore el modulo sys, al cual desde la terminal se le puedan pasar tres parametros. El programa debe tomar los parametros e indicar en la terminal si son multiplos de dos. Utilice la estrucutra if/else para resolver el problema"

import sys

valor_4 = int(sys.argv[1])
valor_5 = int(sys.argv[2])
valor_6 = int(sys.argv[3])

if valor_4 % 2 == 0:
    print(f"{valor_4} es multiplo de dos")
else:
    print(f"{valor_4} no es multiplo de dos")
if valor_5 % 2 == 0:
    print(f"{valor_5} es multiplo de dos")
else:
    print(f"{valor_5} no es multiplo de dos")
if valor_6 % 2 == 0:
    print(f"{valor_6} es multiplo de dos")
else:
    print(f"{valor_6} no es mulitplo de 2")


"2) Cree una lista de fruta de 2 elementos, y realice un programa que muestre una oracion conteniendo los dos elementos de la lista concatenandolos con texto para formar oracion con sentido. Presente el resultado en la terminal del editor."

fruit_list = ["manzana", "pera"]

print(f"estas son las frutas que compre " + fruit_list[0] + " y " + fruit_list[1])

"3) tome dos valore por console, y guarde en una lista"

mi_lista=[]

valor_1 = int(input("ingrese un valor:"))
valor_2 = int(input("ingreseotro valor:"))
suma_valores = valor_1 + valor_2

mi_lista.extend([valor_1, valor_2, suma_valores])

print("Esta es mi Lista: ", mi_lista)



