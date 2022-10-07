import sys # Importamos la libreria sys para poder usar el argumento de la linea de comandos

# Si el numero de argumentos es mayor o igual a 2, entonces el nombre es el
# segundo argumento, sino, el nombre es vacio.

nombre = sys.argv[1] if len(sys.argv) >= 2 else ''
print("¡Hola!", nombre) # Imprimimos el argumento de la linea de comandos

# Ejemplo de uso: python3 hola_mundo_ordenes.py "Nombre"
