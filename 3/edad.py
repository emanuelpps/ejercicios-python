"""Ejercicio 4
Escriba un programa que solicite la edad de la persona e imprima todos los años que la persona ha cumplido. 
"""

import datetime


edad = int(input("ingrese su edad: "))
anio_actual = int(datetime.datetime.now().strftime("%Y"))
anio = anio_actual - edad

while anio < anio_actual:
    anio += 1
    print(anio)
