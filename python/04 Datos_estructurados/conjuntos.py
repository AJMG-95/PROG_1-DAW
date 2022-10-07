'''
Escribir una funcion que devuelva True si todos los elementos de una lista
son subconjunto del conjunto x
'''

def validate_subset(subsets, my_set):
    for sub in subsets:
        if not set(sub) <= set(my_set):
            return False
    return True

def valida_subconjunto(subsets, my_set):
    return all(set(sub) <= my_set for sub in subsets)
