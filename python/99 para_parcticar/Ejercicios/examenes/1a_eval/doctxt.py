def completar():
    """Busca los * en las lineas de un archivo .txt cuyas lineas
    son cadenas con los caracteres  numericos y si hay un * lo cambia por
    el número o números que faltan de menor a mayor
    """
    # Leer el contenido del archivo
    with open('datos.txt', 'r') as f:
        lineas = [list(c.rstrip()) for c in f.readlines()]
    # Procesar los datos
    for linea in lineas:
        # Encontrar el primer numero que no está
        for i in range(1, 10):
            if str(i) not in linea:
                linea[linea.index('*')] = str(i)
    # Volcar el resultado en el archivo
    with open('datos.txt', 'w') as f:
        f.writelines([''.join(linea) + '\n' for linea in lineas])

def completar2(): #El resultado es por si da errores de permiso
    """Busca los * en las lineas de un archivo .txt cuyas lineas
    son cadenas con los caracteres  numericos y si hay un * lo cambia por
    el número o números que faltan de menor a mayor
    """
    # Leer el contenido del archivo
    with open('datos.txt', 'r') as f:
        lineas = [list(c.rstrip()) for c in f.readlines()]
    # Procesar los datos
    for linea in lineas:
        # Encontrar el primer numero que no está
        for i in range(1, 10):
            if str(i) not in linea:
                linea[linea.index('*')] = str(i)
    # Volcar el resultado en el archivo
    with open('resultado.txt', 'w') as f:
        f.writelines([''.join(linea) + '\n' for linea in lineas])
