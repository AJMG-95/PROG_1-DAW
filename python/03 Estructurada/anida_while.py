M = [
    [2, 5, 9]
    [4, 2, 1]
    [8, 7, 6]
    [2, 9, 4]
]

# Recorre la lista por fila:
i = 0
while i < len(M):
    # Recorre la fila actual por columnas:
    j = 0
    while j < len(M[i]):
        print(M[i][j], end='')
        j += 1
    print()
    i += 1
