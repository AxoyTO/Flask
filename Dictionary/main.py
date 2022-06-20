# Data Structures
# Dictionary
'''
my_dictionary = {'Key': 'Value', ('K', 'E', 'Y'): 5}
print(my_dictionary)

print(my_dictionary.keys())
print(my_dictionary.values())

dictionary1 = {x: x + 1 for x in range(10)}
print(dictionary1)

print(dictionary1.keys())
print(dictionary1.values())
'''

emptyDict = {}  # empty dictionary
intDict = {1: 'apple', 2: 'ball'}  # dictionary with integer keys
mixDict = {'name': 'John', 'age': 26}  # dictionary with mixed keys
my_dict = dict({1: 'apple', 2: 'ball'})  # using dict()
seqDict = dict([(1, 'apple'), (2, 'ball')])  # from sequence having each item as pair

print(emptyDict)
print(mixDict)
print(mixDict['name'])
print(mixDict.get('age'))

try:
    print(mixDict.get('address'))  # Output:None
    print(mixDict['address'])  # KeyError
except KeyError as k:
    print(k)

mixDict['name'] = 'Oguz'
mixDict['age'] = 23
mixDict['address'] = 'Ankara'
print(mixDict)
'''
for i in mixDict.items():
    print(i)
'''
# print(list(sorted(mixDict.keys())))

# print(len(mixDict))

squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(len(squares))
print(squares.pop(4))  # Remove item x and return it's value
print(squares)

print(squares.popitem())  # Remove last item, return (key,value)
print(squares)

squares.clear()  # Remove all items
print(squares)

del squares  # Delete the dictionary
try:
    print(squares)
except NameError as e:
    print(e)
