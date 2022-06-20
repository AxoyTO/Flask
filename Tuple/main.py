# Data Structures
# Tuple
tup = (1, 'abc', 2, 'cde')
tup1 = 3, 'efg', True

tup2 = 'A'  # tup2 = ('A', )
print(tup)
print(tup[1])
print(tup[0:2])

try:
    tup[3] = 5  # Tuples are immutable, tuple objects are not assignable
except Exception as e:
    print(e)

tup = tup[0:4] + (5,)  # Adding an element to the tuple
print(tup)

tup = tup[1:2] + (6,)  # Modifying tuple
print(tup)

print(tup2 * 5)  # Printing tuple n times

print(5 in tup)  # Returns true if x is in tuple

for x in ('a', 'b', 'c'):  # Printing
    print(x)


def multiple_result():
    return 1, 2, 'a'


print(multiple_result())
print((1, 2, 3) == (1, 2))  # Comparing tuples
print((1, 2, 3) == (1, 2, 3))

tup = ("d", 'b', 'c', 'a', 'd')
print(min(tup))
print(max(tup))

print(len(tup))
print(tup.count('d'))  # Amount of x in tuple
print(tup.index("d"))  # Index of first occurring of x in tuple
