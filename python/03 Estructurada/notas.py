'''
Escribir un programa que calcule la note media de la asignatura
'''

NOTAS = [('Manuel', 7.5),
      ('Ester', 8.0),
      ('Ezequiel', 6),
      ('Antonio', 6.5),
      ('Marco', 9.3),
      ('Paco', 3.1),
      ('Richard', 0)
]

#suma = 0
#i = 0
#while i < len(NOTAS):
#    suma += NOTAS[i][1]
#    i += 1
#media = suma / len(NOTAS)
#print('La media es: ', media)

'''
Escribir un programa que imprima los nombres de los alumn@s suspensos
'''

i = 0
while i < len(NOTAS):
    if NOTAS[i][1] < 4.5:
        print(NOTAS[i][0], ' Suspeso')
    i += 1

# Es posible guardar NOTAS[i] en una variable 'elemento' antes del if de forma que:
# elemento = NOTAS[i]
# Y en el codigo donde pone NOTAS[i] escribo elemento

'''
Escribir un prigrama que imprima cuantos alumnos han aprobados y cuantos han suspendido
'''
i = 0
aprob = 0
susp = 0
while i < len(NOTAS):
    if NOTAS[i][1] >= 4.5:
        aprob += 1
    else:
        susp += 1
    i += 1
print('Hay', aprob, 'aprobados y', susp, 'suspensos.')
print(f"Hay {aprob} aprobados y {susp} suspensos.")
