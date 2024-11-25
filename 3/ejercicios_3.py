""" Ejercicio 1
Tome el ejercicio de cálculo de números pares e impares de la unidad 2 y agréguele un bucle al código de forma de simplificarlo."""

valor = 0

while valor < 10:
    if valor % 2 == 0:
        print("es par")
        valor += 1
    else:
        print("es impar")
        valor += 1


"""Ejercicio 2
Escriba un programa que consulte al usuario por una oración y comente al usuario cuantas veces aparece la letra “a”. 
"""

oracion = str(input("ingrese una oracion: "))


def letra_a_repetida(sentence):
    count = 0
    for char in sentence:
        if char == 'a':
            count += 1
    print(count)


letra_a_repetida(oracion)