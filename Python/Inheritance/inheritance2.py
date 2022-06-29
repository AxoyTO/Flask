import math
from typing import Set


class Complex(object):
    "this class simulates complex numbers"

    def __init__(self, real, imaginary):
        if (type(real) not in (int, float)) or type(imaginary) not in (int, float):
            raise Exception("Args are not int or float!")
        self.SetReal(real)
        self.SetImaginary(imaginary)

    def GetReal(self):
        return self.__real

    def GetImaginary(self):
        return self.__imaginary

    def Modulus(self):
        return math.sqrt(self.GetReal() ** 2 + self.GetImaginary() ** 2)

    def Phi(self):
        return math.atan2(self.GetImaginary(), self.GetReal())

    def SetReal(self, val):
        if type(val) not in (int, float):
            raise Exception("Val has to be int or float!")
        self.__real = val

    def SetImaginary(self, val):
        if type(val) not in (int, float):
            raise Exception("Val has to be int or float!")
        self.__imaginary = val

    real = property(GetReal, SetReal)
    imaginary = property(GetImaginary, SetImaginary)


try:
    c = Complex(2, 1.4)
    c.SetReal(-3)
    c.SetImaginary(4)
    print(c.GetReal(), c.GetImaginary())
    print("Modulus = ", c.Modulus(), "\nPhi = ", c.Phi())
except Exception as e:
    print(e)
