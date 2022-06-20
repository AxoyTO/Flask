# Lambda Function
f = lambda x, y, z=0: x + y
print(f(2, 3))

# Nested lambda functions
k = lambda a: lambda b: lambda c: a * b * c
print(k(5)(4)(3))

m = lambda c: lambda a, b: lambda d: (c * (a + b)) % d
print(m(2)(4, 3)(11))
