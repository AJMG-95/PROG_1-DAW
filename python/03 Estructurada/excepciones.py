# Factorial de un numero:
def fact(n): return 1 if n == 0 else n * fact(n - 1)


try:
    num = input('Introduce un numero: ')
    res = fact(int(num))
    print('El factorial de ', num, 'es', res)
except ValueError:
    print('El valor inrtroducido no es un numero entero')
else:
    print('Todo ha salido bien')

'''
# Hace el inverso de un nuemero
try:
    num = input('Intoduce un numero: ')
    res = 1 / (int(num))
    print('El innverso de', num, 'es', res)
except ValueError:
    print('Número ncorrecto introducido.')
except ZeroDivisionError:
    print('No se puede dividir entre cero')
else:
    print('Todo ha salido bien')
finally:
    print('El prpgrama ha finalizado')
'''

# Hace el inverso de un numero, esta version es más interactiva con el usuario y por ello es
# mejor/preferible

while True:
    try:
        num = int(input('Intoduce un numero: '))
        res = 1 / num
    except ValueError:
        print('Valor introducido incorrecto.')
    except ZeroDivisionError:
        print('No se puede dividir entre 0.')
    else:
        break  # Sale del bucle cuando los datos de entrada y los resultados obtenidos son correctos
        # Se ejecuta cuando no se lanza ninguna excepción
print(f'El inverso de {num} es {res}')
