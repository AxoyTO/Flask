import re

# FLAGS
# print(re.findall('x*y', 'XXXYYYXXXY'), re.IGNORECASE)
# print(re.findall('(^xy{2}) | (yx{2}$)', 'xyxyxxxyxx\nxyyxxxxx'), re.MULTILINE)
# print(re.findall('z.x', 'xyyyyz\nxyyxx'), re.DOTALL)

regex = re.compile('''
                            #This is comment
       \w+              #alphanumeric
    @                 #at
    \w+               #alphanumeric
    .                 #dot
    (com|net|org)     #com or org or net
    ''', re.VERBOSE)

print(regex.search('this1@email12.com').start())
re.compile('pattern', re.IGNORECASE | re.VERBOSE | re.DOTALL)
print(re.findall('(?i)x*y', 'XXXYYYXXXy'))
