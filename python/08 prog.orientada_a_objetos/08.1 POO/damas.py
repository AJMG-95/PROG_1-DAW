class Ficha:
    def __init__(self, color) -> None:
        if color not in ('B', 'N'):
            raise ValueError('El color no es correcto')
        self.__color = color

    def color(self):
        return self.__color


class Jugador:
    def __init__(self, nombre) -> None:
        self.__nombre = nombre
        self.__fichas = []

    def nombre(self):
        return self.__nombre

    def fichas(self):
        return self.__fichas

    def quitar_ficha(self, ficha):
        for pos, f in enumerate(self.fichas()):
            if f == ficha:
                del self.__fichas[pos]
                return


class Tablero:
    def __init__(self, j1, j2) -> None:
        self.__contenido = {}
        self.__j_blancas = j1
        self.__j_negras = j2
        self.__rellenar(j1, 'B', 1, 1)
        self.__rellenar(j2, 'N', 6, 2)

    def __quitar_ficha(self, ficha):
        jugador = self.__j_blancas if ficha.color() == 'B' else \
            self.__j_negras
        jugador.quitar_quitar(ficha)

    def __rellenar(self, jugador, color, fila, col):
        while len(jugador.fichas()) < 12:
            f = Ficha(color)
            jugador.fichas().append(f)
            self.__contenido[(fila, col)] = f

            if col + 2 <= 8:
                col += 2
            else:
                fila += 1
                col = 1 if fila % 2 != 0 else 2

    def ficha(self, fila, col):
        return self.__contenido.get((fila, col))

    @staticmethod
    def __nueva_posicion(fila, col, color, direccion):
        if (color, direccion) == ('B', 'IQZ'):
            if fila != 8 or col != 1:
                fila += 1
                col -= 1

        elif (color, direccion) == ('B', 'DER'):
            if fila != 8 or col != 1:
                fila += 1
                col += 1

        elif (color, direccion) == ('N', 'IQZ'):
            if fila != 8 or col != 8:
                fila -= 1
                col += 1

        elif (color, direccion) == ('N', 'DER'):
            if fila != 1 or col != 1:
                fila -= 1
                col -= 1

        return (fila, col)

    def mover(self, ficha, direccion):
        if direccion not in ('IZQ', 'DER'):
            raise ValueError('Movimiento no valido')
        if ficha is None:
            raise ValueError('No hay ficha para mover')
        encontrado = False
        for k, v in self.__contenido.items():
            if v == ficha:
                encontrado = True
                fila, col = k
                break

        if not encontrado:
            raise ValueError('La ficha no está en el tablero')
        nueva_fila, nueva_col = Tablero.__nueva_posicion(
            fila, col, ficha.color(), direccion)
        if (nueva_fila, nueva_col) == (fila, col):
            return (fila, col)

        otra_ficha = self.ficha(nueva_fila, nueva_col)

        # Comer ficha
        if otra_ficha is not None:
            if otra_ficha.color() == ficha.color():
                return (fila, col)  # La ficha no se mueve
            else:
                # Mover ficha
                self.__contenido[(nueva_fila, nueva_col)] = ficha
                del self.__contenido[(fila, col)]

                return(nueva_fila, nueva_col)
