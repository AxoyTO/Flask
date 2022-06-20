# Data Structures
# Sets

my_set = set(['one', 'two', 'three', 'one'])
my_set1 = set(['two', 'three', 'four'])

print(my_set | my_set1)  # Union
print(my_set ^ my_set1)  # Intersection
print(my_set & my_set1)  # AND
print(my_set - my_set1)
a = my_set1 - my_set
print(a)
my_set.add('five')  # Add element to set
print(my_set)
my_set.update(['six', 'seven', 'eight'])  # Add multiple elements to set
print(my_set)
my_set.update([4, 5], {1, 2, 3})
print(my_set)
my_set.discard(4)  # Discard removes an element, doesn't return error if no element already
my_set.remove(3)  # Remove removes an element, raise error if no such element
print(my_set.pop())  # Takes no arguments! Pops a random element
print(my_set)

print(1 in my_set)  # True if there is 1, else False

for i in my_set:
    print(i)

for i in set("Oguz"):
    print(i)

A = frozenset([1, 2, 3, 4])  # Frozenset is an immutable set.
# Tuples are immutable lists
