def factura():
    with open('factura.txt') as f:
        lineas = [x.rstrip() for x in f.readlines()] #lee cada linea y el rstrip() quita los saltos de linea

    # Crea el encabezado
    resultado = []
    resultado.append(lineas[0] + '  Importe\n')
    resultado.append(lineas[1] + '  -------\n')

    # Rellena la linea con los distintos campos de cada linea
    # lineas[0] es el encabezado y lineas[1] las rallitas por eso se empieza en lineas[2]
    total = 0
    for linea in lineas[2:]:
        linea = linea.split()
        uds = int(linea[0])
        desc = linea[1]
        pun = float(linea[2])
        imp = uds * pun
        total += imp
        resultado.append(f'{uds:2f} {desc:15} {pun:6.2f} {imp:7.2f}\n')

    resultado.append('---------------------------------------\n')
    resultado.append(f'TOTAL:       {total:14.2f}')

    with open('resultado.txt', 'w') as f:
        f.writelines(resultado)
