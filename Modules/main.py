import importlib
import sys

import custommodules as cm
from custommodules import add
import math
import customprint as cp
from math import *

print(sys.path)
'''for word in sys.modules:
    print(word)'''
print(math.__name__)
print(dir(math))

print(math.cos(0))
print(pi)

print(cm.add(2, 3))
print(add(5, 6))
print(dir(cm))
importlib.reload(cp)
