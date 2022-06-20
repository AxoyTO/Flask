# Data Structures
# Lists

import functools as f

from functools import reduce

list1 = [1, 'abc', (2, 3)]
print(list1)
print(list1 * 2)
print(list1[1] * 2)
print(2 in list1)
print(list1 == [1, 'abc', (2, 3)])
print(list1[0:2])
list1.append(6)  # Append(Add) to the end of the list
print(list1)
list1[len(list1):] = ['Seven']  # Another way to add to the end of the list
list1.extend([8, 'nine', 'ten'])  # Adding several items to the end of the list
print(list1)
print(list1 + ['AddTwoLists'])
list1.insert(1, 'two')
print(list1)
del list1[2]  # Delete list element
print(list1)
del list1  # Delete entire list

newList = ['O', 'G', 'U', 'Z', 'H', 'A', 'N', 'A', 'K', 'S', 'O', 'Y']
print(newList)
newList.remove('A')  # Removes the first occuring of x
newList.pop(4)  # Removes and returns the item at index x
newList.pop()  # Removes and returns the last element
print(newList)
newList.clear()
print(newList)

listy = [0, 1, 2, 3, 4, 5, 'Six', 'Seven']
listy.reverse()  # Reverses the list
print(listy)

listy[0:2] = []
listy.sort()  # Gives error if list elements are of different types, sorting in the ascending order
print(listy)

print(list(map(lambda x: x ** 2 + 3 * x + 1, [1, 2, 3, 4])))
print(list(filter(lambda x: x < 4, [1, 2, 3, 4, 5, 4, 3, 2, 1])))
print(f.reduce(lambda x, y: x * y, [1, 2, 3, 4]))

'''
def sum(a, b):
    print(f"a={a} , b={b}, {a} + {b} = {a + b}")
    return a + b
'''

scores = [1, 2, 3, 4, 5]
# total = reduce(sum, scores)
total = reduce(lambda a, b: a + b, scores)
print(total)
