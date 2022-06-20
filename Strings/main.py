# Strings

str1 = "Hello"
str2 = "world"
print(str1 + " " + str2[:3] + str2[-1] + "!")
str3 = "Earl"
str4 = "4th"
str3 = str3[:3] + str4[-2:] + "!"
print("Oops.. I meant " + str1 + " " + str3)

print("{0} {1}".format("Hello", "reader!"))
print("On {Day} {Subject} will {Verb} {Object}.".format(Day='monday',
                                                        Subject='she',
                                                        Object='me',
                                                        Verb='meet'))

print('{:<50}'.format("left aligned"))  # 50 chars left aligned
print('{:>50}'.format("right aligned"))  # 50 chars right aligned
print('BINARY OF 21 IS {:b}'.format(21))  # BINARY
print('HEX OF 21 IS {:x}'.format(21))  # HEX
print('OCTAL OF 21 IS {:o}'.format(21))  # OCTAL

print('I am a string in "Python"')
print('I\'m a string in "Python"')  # escape character
print(r'c:\number\nan')  # r escape
print("""\
        Hello:
                User defined look
                Python output.
                    It's cool. Isn't it?""")