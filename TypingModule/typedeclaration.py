def add_numbers(num1: int, num2: int = 10) -> int:
    return num1 + num2


print(add_numbers(3, 5))
print(add_numbers(3.4, 6.6))  # Will also work, so type declaration doesnt have effect in runtime.

a: int = 3
b: float = 3.14
c: str = 'abc'
d: bool = False
e: list = ['a', 'b', 'c']
f: tuple = (1, 2, 3)
g: dict = {'a': 1, 'b': 2}


def greet(name: str) -> str:
    base: str = 'Hello, '
    return f'{base}{name}'


print(greet('Bob'))  # Hello, Bob

num1: int = int(input("Enter first number: "))
num2: int = int(input("Enter second number: "))

print(f'Addition of {num1} and {num2} are {num1 + num2}')
print(f'Product of {num1} and {num2} are {num1 * num2}')
