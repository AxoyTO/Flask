from multipledispatch import dispatch


class Complex:
    """This class simulates complex numbers"""

    def __init__(self, real=0, imaginary=0):
        self.__real = real
        self.__imaginary = imaginary

    def GetReal(self):
        return self.__real

    def GetImaginary(self):
        return self.__imaginary

    def SetReal(self, real):
        if type(real) not in (int, float):
            raise Exception("Real must be integer or float!")
        self.__real = real

    def SetImaginary(self, imag):
        if type(imag) not in (int, float):
            raise Exception("Imaginary must be integer or float!")
        self.__imaginary = imag

    def __str__(self):
        return "{r} + {i}i".format(r=self.__real, i=self.__imaginary)

    def __add__(self, other):
        return Complex(
            self.GetReal() + other.GetReal(), self.GetImaginary() + other.GetImaginary()
        )

    def __mul__(self, other):
        if type(other) in (int, float):
            return Complex(self.GetReal() * other, self.GetImaginary() * other)
        else:
            return Complex(
                self.GetReal() * other.GetReal()
                - self.GetImaginary() * other.GetImaginary()
                + self.GetReal() * other.GetImaginary()
                + self.GetImaginary() * other.GetReal()
            )

    def __truediv__(self, other):
        if type(other) in (int, float):
            return Complex(
                self.GetReal() / float(other), self.GetImaginary() / float(other)
            )
        else:
            a, b, c, d = (
                self.GetReal(),
                self.GetImaginary(),
                other.GetReal(),
                other.GetImaginary(),
            )
            nominator = c * c + d * d
            return Complex((a * c + b * d) / nominator, (b * c - a * d) / nominator)


a = Complex(5, 0.3)
b = Complex(-3, 4)

print(a)
print(b)
print(a + b)
print(a * 2)
print(a * b)
print(a / b)
print(b / 2)


# passing 2 parameters
@dispatch(int, int)
def product(first, second):
    result = first * second
    print(result)


# passing 3 parameters
@dispatch(int, int, int)
def product(first, second, third):
    result = first * second * third
    print(result)


# can also pass data type of any value as per requirement
@dispatch(float, float, float)
def product(first, second, third):
    result = first * second * third
    print(result)


# calling product method with 3 arguments
product(2, 3, 2)  # this will give output of 12
product(2.2, 3.4, 2.3)  # this will give output of 17.985999999999997
