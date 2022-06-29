import re

'''
regex = re.compile('x([xy]+)(y)(z)')
match = regex.search('xyxxxyxxxyxyxyz')
print(match.groups())
print(match.group(0))  # -> whole text
print(match.group(1))
print(match.group(2))
print(match.group(3))
'''

'''
# ?P<> grup isimlendirme
regex = re.compile('x(?P<birinci>[xy]+)(?P<ikinci>y)(?P<third>z)')
match = regex.search('xyxxxyxxxyxyxyz')
print(match.groups())
print(match.group('birinci'))
print(match.group('ikinci'))
print(match.group('third'))

# Make a dictionary out of groups
print(match.groupdict())
'''

# x|y = [xy]
regex = re.compile('y(?P<bir>(?P<iki>x|y)+)')
match = regex.search('yxxyyxyxy')
print(match.groups())
print(match.group(0))
print(match.group('bir'))
print(match.group('iki'))
