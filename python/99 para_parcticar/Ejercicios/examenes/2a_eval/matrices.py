'''
Programar en Python un modelo orientado a objetos del problema de representar matrices
cuadradas de números y hacer operaciones entre ellas. Para ello:

    Escribir una clase Matriz cuyo constructor reciba una secuencia de números que represente
    a los diferentes elementos almacenados por filas.
    Por ejemplo, la matriz: estilo mostrar elástico paréntesis izquierdo tabla fila 2 4 9
    fila 6 5 1 fila 3 8 7 fin tabla elástico paréntesis derecho se podría representar de la
    siguiente forma: Matriz([2, 4, 9, 6, 5, 1, 3, 8, 7])
    Indicación: El número de filas y columnas que debe tener la matriz es la raíz cuadrada
    del número de elementos de la secuencia.
    Implementar un getter llamado elem(fila, col) que devuelva el número situado en la fila
    y columna especificadas, suponiendo que se empieza a contar desde cero, las filas se
    cuentan de arriba abajo y las columnas de izquierda a derecha.
    Una matriz se puede sumar con otra matriz siempre que sean del mismo tamaño (mismo número
    de filas y columnas). La suma de dos matrices A

blancoy B (con elementos aij y bij) da como resultado una nueva matriz C cuyos elementos
cij cumplen que cij=aij+bij

    . Por ejemplo: Error converting from MathML to accessible text.
    Para ello, implementar en la clase Matriz una operación suma(otra) que realice la suma
    con otra matriz y devuelva la matriz resultante (ver ejemplos en los tests). Si las dos
    matrices no tienen el mismo tamaño, debe devolver None.


Importante

Al principio de cada test, se hace:

una = Matriz([2, 4, 9, 6, 5, 1, 3, 8, 7])
otra = Matriz([1, 1, 1, 2, 2, 2, 3, 3, 3])

Por ejemplo:
Test 	Resultado
print(una.elem(1, 2))
1

print(una.suma(otra).elem(2, 1))
11

print(una.suma(Matriz([1, 2, 3, 4])))
None
'''
from math import sqrt

class Matriz:
    def __init__(self, numeros) -> None:
        self.__numeros = numeros
        self.__nfilas = sqrt(len(self.__numeros))
        self.__fila = []
        self.__matriz = []
        for i in self.__numeros:
            self.__fila.append(i)
            if len(self.__fila) == self.__nfilas:
                self.__matriz. append(self.__fila)
                self.__fila = []

    def elem(self, fil, col):
        """_summary_

        Args:
            fil (_type_): _description_
            col (_type_): _description_

        Returns:
            _type_: _description_
        """
        fila = self.__matriz[fil]
        col = fila[col]
        return col

    def tamanyo(self):
        e = []
        for f in self.__matriz:
            for elem in f:
                e.append(elem)
        t = len(e)
        return t

    def suma(self, otra):
        """_summary_

        Args:
            otra (_type_): _description_

        Returns:
            _type_: _description_
        """
        l = []
        if self.tamanyo() != otra.tamanyo():
            return None
        for e in range(int(self.__nfilas)):
            for i in range(int(self.__nfilas)):
                l.append(self.elem(e, i) + otra.elem(e, i))

        nueva = Matriz(l)
        return nueva
