class Barco:
    def __init__(self, tamanyo) -> None:
        self.__tamanyo = tamanyo
        self.__golpes = 0

    def tamanyo(self):
        return self.__tamanyo

    def golpes(self):
        return self.__golpes

    def tocado(self):
        return self.golpes() > 0

    def hundido(self):
        return self.golpes() == self.tamanyo()


class Tablero:
    N_FILAS = 10
    N_COL = 10

    def __init__(self, n_filas=N_FILAS, n_col=N_COL) -> None:
        self.__n_filas = n_filas
        self.__n_col = n_col
        self.__tablero = {}

    def num_filas(self):
        return self.__n_filas

    def num_col(self):
        return self.__n_col

    def colocar_barco(self, barco, posicion, direccion):
        ...

j1 = Tablero()
j2 = Tablero()
