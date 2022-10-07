class Racional:
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def __eq__(self, otro):
        if type(self) != type(otro):
            return NotImplemented
        return self.numer() * otro.denom() == self.denom() * otro.numer()

    def numer(self):
        return self.num

    def denom(self):
        return self.den
