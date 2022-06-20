# Exception Handling

'''
try:
    n = int(input("Enter an integer: "))
except ValueError:
    print("That is not an integer!")
'''

'''
try:
    sum = 0
    file = open('numbers.txt', 'r')
    for number in file:
        sum = sum + 1.0 / int(number)
    print(sum)
except ZeroDivisionError:
    print("Number in file equal to zero!")
except IOError:
    print("File doesn't exist!")
finally:
    print(sum)
    file.close()
'''

'''
a = 1
def RaiseException(a):
    if type(a) != type('a'):
        raise ValueError("This is not a string")

try:
    RaiseException(a)
except ValueError as e:
    print(e)
'''


def TestCase(a, b):
    assert a < b, "a is greater than b"
try:
    TestCase(2,1)
except AssertionError as e:
    print(e)
