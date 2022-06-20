# Modules and Packages
# ___init__
import importlib

from sub2.addmodule import sum
import sub2.addmodule as sub2

from sub1.prime import IsPrime
from sub1.prime import PrimesTo
import sub1.prime as sub1

'''
print(sub2.sum(4, 5))
print(sum(5, 10))

PrimesTo(100)
print(IsPrime(17))
'''

import copy

my_dictionary = {'Key': 'Values', ('K', 'E', 'Y'): 5}
my_dictionary1 = copy.deepcopy(my_dictionary)

print(my_dictionary.keys())
print(my_dictionary.values())

my_dictionary[1] = 1
print(my_dictionary)
print(my_dictionary1)

import math
import cmath

print(math.cos(math.pi))
print(math.exp(1))
print(math.ceil(1.1))
print(math.floor(4.7))

x = 5 + 4j
print(type(x))

print(math.sqrt(25))

import random as rand

print(dir(rand))
print(rand.sample([1, 2, 3, 4, 5], 2))
print(rand.randint(0, 1000))

import sys

print(sys.getrecursionlimit())
print(sys.path)

my_dictionary2 = my_dictionary
print(my_dictionary)
print(my_dictionary2)

my_dictionary2['NewKey'] = 'NewValue'
print(my_dictionary)
print(my_dictionary2)

# print(dir(math))
