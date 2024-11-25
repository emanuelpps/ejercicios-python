"""Ejercicio 3
Escriba un programa que consulte al usuario por una oración y comente al usuario cuantas veces aparecen todas las vocales considerando minúsculas, mayúsculas y acentos.  
"""

vocales = ["a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú"]

oracion = str(input("ingrese una oracion: "))

for char in oracion:
    if char in vocales:
        print(f"La vocal {char} aparece {oracion.count(char)} veces en la oración")
