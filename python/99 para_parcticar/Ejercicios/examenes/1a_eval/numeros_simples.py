def numeros_simples(inicio, fin):
    def es_simple(numero):
        digitos = [int(x) for x in str(numero)]
        return sum(d ** i for i, d in enumerate(digitos, 1)) == numero
    return [x for x in range(inicio, fin + 1) if es_simple(x)]
