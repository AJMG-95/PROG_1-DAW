class Tablero:
    MAX_FILAS = 6
    MAX_COLUMNAS = 7

    def __init__(self) -> None:
        self.__tablero = []
        for _ in range(Tablero.MAX_COLUMNAS):
            self.__tablero.append([])

    @staticmethod
    def __fila_valida(fila):
        if fila not in range(Tablero.MAX_FILAS):
            raise ValueError('Fila icnorrecta')

    @staticmethod
    def __columna_valida(col):
        if col not in range(Tablero.MAX_COLUMNAS):
            raise ValueError("Columna incorrecta")

    def meter(self, ficha, col):
        # Compribar si la columna es valida y no esta llena
        Tablero.__columna_valida(col)
        columna = self.__tablero[col]
        if len(columna) > Tablero.MAX_FILAS:
            raise ValueError('Columna llena')
        columna.append(ficha)
        return self

    def ficha(self, fila, col):
        Tablero.__fila_valida(fila)
        Tablero.__columna_valida(col)
        columna = self.__tablero[col]
        if fila + 1 <= len(columna):
            return columna[fila]
# Para acceder a una fila almenos tiene que haber n elementos + 1,
#   siendo n el numero de la fila al que se quiere acceder.
        return None


class Ficha:
    def __init__(self, color) -> None:
        if color not in ('B', 'N'):
            raise ValueError('El color no es correcto')
        self.__color = color

    def color(self):
        return self.__color
