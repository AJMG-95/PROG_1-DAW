def mas_repetido(lista):
    """Recibe una lista y devuelve un conjunto con los elemetos más repetidos.
    de la lista

    Args:
        lista (list): Lista que se le pasa a la función.

    Returns:
        set: conjunto que contiene los elementos más repetidos de la lista.
    """
    c = []
    s = set()
    for i in lista:
        a = lista.count(i)
        c.append(a)
    for i in lista:
        if lista.count(i) == max(c):
            s.add(i)
    return s

def mas_repetido_2(lista):
    """Recibe una lista y devuelve un conjunto con los elemetos más repetidos.
    de la lista

    Args:
        lista (list): Lista que se le pasa a la función.

    Returns:
        set: conjunto que contiene los elementos más repetidos de la lista.
    """
    maximo = max(lista.count(x) for x in lista)
    return {x for x in lista if lista.count(x) == maximo}
