class Trabajador:
    def __init__(self, nombre, salario):
        self.set_nombre(nombre)
        self.set_salario(salario)

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre

    def set_salario(self, salario):
        self.__salario = salario

    def get_salario(self):
        return self.__salario

    def descripcion(self):
        return f"Soy {self.get_nombre()}"


class Docente(Trabajador):
    def get_nrp(self):
        return self.__nrp

    def set_nrp(self, nrp):
        self.__nrp = nrp

    def descripcion(self):
        return super().descripcion() + f" y mi especialidad es {self.get_nrp()}"
