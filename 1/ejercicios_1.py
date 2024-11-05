""" Cree un programa que tome tres valores por consola multiplique el primero por el segundo, y le sume el tercero. Presente el resultado en la terminal del editor """

valor_1 = int(input("cargue un valor"))
valor_2 = int(input("cargue un valor"))
valor_3 = int(input("cargue un valor"))

print(valor_1 * valor_2 + valor_3)

""""""

"""Cree un programa que incorpore el modulo sys, al cual desde la terminal se le puedan pasar tres parametros. El programa debe tomar los parametros e indicar en la terminal si son multiplos de dos"""

import sys

valor_4 = int(sys.argv[1])
valor_5 = int(sys.argv[2])
valor_6 = int(sys.argv[3])
print(f"valor_4 es múltiplo de 2: {valor_4 % 2 == 0}")
print(f"valor_5 es múltiplo de 2: {valor_5 % 2 == 0}")
print(f"valor_6 es múltiplo de 2: {valor_6 % 2 == 0}")

""""""