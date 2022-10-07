"""
Adivinar un número
"""
import random

numero_a_adivinar = random.randint(1, 100)

while True:
    try:
        numero = int(input('Introduzca un numero: '))
        if numero == numero_a_adivinar:
            print('!Acertaste¡')
            break
        if numero < numero_a_adivinar:
            print('Es demasido pequeño')
        else:
            print('Es demasiado grande')
    except ValueError:
        print('Debe introducir un número valido')
