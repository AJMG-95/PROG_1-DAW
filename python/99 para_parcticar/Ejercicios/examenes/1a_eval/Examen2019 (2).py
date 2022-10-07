def list2dict(lista):
    res = {}
    for clave, valor in enumerate(lista):
        res[clave] = valor
        res[clave - len(lista)] = valor
    return res


def dict2list(dic):
    res = []
    for valor in range(min(dic), max(dic) + 1):
        res.append(dic.get(valor))
    return res


def sobre(m, n):
    if m == 0 and n > 0:
        return 0
    elif m >= 0 and n == 0:
        return 1
    return sobre(m - 1, n - 1) + sobre(m - 1, n)


def lista_sobre_A(ultima_fila):
    res = [[1]]
    if ultima_fila == 0:
        return res
    for _ in range(ultima_fila):
        f1 = [0] + res[-1]
        f2 = res[-1] + [0]
        fila = []
        for i, f in enumerate(f1):
            fila.append(f2[i] + f)
        res.append(fila)
    return res


def lista_sobre_B(numero_filas):
    res = [[1]]
    if numero_filas == 0:
        return res
    for _ in range(numero_filas - 1):
        f1 = [0] + res[-1]
        f2 = res[-1] + [0]
        fila = []
        for i, f in enumerate(f1):
            fila.append(f2[i] + f)
        res.append(fila)
    return res


def triangulo_A(numeros_filas):
    for fila in lista_sobre_A(numeros_filas - 1):
        for i, f in enumerate(fila):
            fila[i] = f' {f:5}'
        print(''.join(fila).center(60))


def triangulo_B(ultima_fila):
    for fila in lista_sobre_B(ultima_fila + 1):
        for i, f in enumerate(fila):
            fila[i] = f' {f:5}'
        print(''.join(fila).center(60))
