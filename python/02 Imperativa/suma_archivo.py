"""
# MODO PARA QUE TE IMPRIMA EN PANTALLA.

f = open('suma.txt', 'r') # abre el archivo en modo lectura.
a = int(f.readline().rstrip()) # lee la primera linea y la quita el salto de linea.
b = int(f.readline().rstrip()) # lee la segunda linea y la quita el salto de linea.
print('La suma de', a, 'y', b, 'es', a+b) # imprime la suma de a y b.
f.close() # cierra el archivo. Este comando es opcional. Si no se cierra solo.
"""

# MODO PARA QUE TE LO GUARDE EN UN ARCHIVO.
f = open('suma.txt', 'r+') # abre el archivo en modo lectura y escritura.
a = int(f.readline().rstrip())
b = int(f.readline().rstrip())
# Se puede utilizar el método write() para escribir en el archivo.
# Pero este método esperaría un string. Habría que convertir todo a string.
print('La suma de', a, 'y', b, 'es', a+b, file=f) # imprime la suma de a y b en el archivo.
# Lo guarda al final porque el cursor esta al final. Con el método seek() podemos mover el cursor.
f.close() # cierra el archivo. Este comando es opcional. Si no se cierra solo.
