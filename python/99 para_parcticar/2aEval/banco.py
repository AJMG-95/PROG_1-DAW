''' Banco.
  Diseñar y codificar un modelo orientado a objetos de un banco donde hay
  cuentas corrientes que tienen un titular y unos movimientos.

  Los titulares son clientes del banco.
  Los clientes del banco pueden ser titulares de varias cuentas al mismo tiempo.

  Los movimientos pertenecen a una sola cuenta. Para ello:
    a) Crear la clase Cliente con los atributos __dni, __nombre y __apellidos.

    b) Crear la clase Movimiento con los atributos __concepto y __cantidad.
       Los movimientos son inmutables.

    c) Crear la clase Cuenta con los atributos __numero, __titular,
       __movimientos y __saldo.

  i. No se puede cambiar el número de una cuenta.

  ii. Se puede añadir un movimiento a una cuenta, pero no cambiar ni eliminar
    movimientos.

  iii. Tampoco se puede modificar directamente el saldo, sino que se debe
    actualizar directamente a partir de los movimientos que se realicen en
    la cuenta.

  d) Crear un módulo principal.py que use las clases anteriores para
     representar un modelo dinámico de objetos donde el cliente
     Antonio Martínez tiene dos cuentas corrientes, cada una de ellas con tres
     movimientos. Imprimir por pantalla el saldo actual de cada cuenta.

  e) ¿Cómo se podría implementar la generación automática e incremental
     del número de cuenta cuando se crea una cuenta nueva? Codificarlo.
     (Indicación: Usar atributos estáticos.)

  f) ¿Cómo se podría implementar la colección de cuentas del banco de forma
     que se pueda acceder de forma eficiente a una cuenta concreta a partir
     de su número?
     Codificarlo.
'''


class Movimiento:
    def __init__(self, concepto, cantidad) -> None:
        self.__concepto = concepto
        self.__cantidad = float(cantidad)

    def get_concepto(self) -> str:
        return self.__concepto

    def get_cantidad(self) -> float:
        return self.__cantidad


class Cliente:
    def __init__(self, dni, nombre, apellidos) -> None:
        self.__cliente = {"dni": dni, "nombre": nombre, "apellidos": apellidos}

    def get_info(self, info) -> str:
        if info in self.__cliente:
            return self.__cliente[info]

    def __repr__(self) -> str:
        dni = self.__cliente["dni"]
        nombre = self.__cliente["nombre"]
        apellidos = self.__cliente["apellidos"]
        cliente = f"DNI: {dni}, Nombre: {nombre}, Apellidos: , {apellidos}"
        return cliente


class Banco:
    def __init__(self) -> None:
        self.__clientes = {}

    def set_clienCuenta(self, cliente, numcuenta:str) -> None:
        if cliente in self.__clientes:
            self.__clientes[cliente].append(numcuenta)
        else:
            self.__clientes[cliente] = [numcuenta]

    def get_clienCuenta(self, cliente) -> tuple:
        dni = cliente.get_info("dni")
        nombre = cliente.get_info("nombre")
        apellidos = cliente.get_info("apellidos")
        print("Nombre: ", nombre, " Apellidos: ", apellidos,
              " DNI: ", dni, "\nCuentas: ", self.__clientes[cliente])

    def get_cuentaClient(self, numcuenta) -> str:
        for cliente in self.__clientes:
            for cuentas in self.__clientes[cliente]:
                if numcuenta in cuentas:
                    return cliente


class Cuenta:
    def __init__(self, num, cliente) -> None:
        self.__titular = cliente
        self.__num = num
        self.__mov = []
        self.__saldo = 0.0

    def get_numCuenta(self):
        return self.__num

    def get_titular(self):
        return self.__titular

    def get_movimientos(self):
        return self.__mov

    def get_saldo(self):
        return self.__saldo

    def realizarMovimiento(self, mov, cantidad):
        if mov == "Retirar":
            if self.__saldo - cantidad >= 0:
                self.__saldo -= cantidad
                self.__mov.append((mov, cantidad))
            else:
                raise ValueError("Saldo Insuficiente.")
        elif mov == "Ingresar":
            self.__saldo += cantidad
            self.__mov.append((mov, cantidad))
        else:
            raise ValueError("Movimiento Incorrecto (Retirar | Ingresar).")

    def __repr__(self) -> str:
        cuenta = f"Número: {self.__num}, Saldo: {self.__saldo}, Movimientos: , {self.__mov}"
        return cuenta
