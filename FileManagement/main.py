# File Management

# open(filename, access, buffering)
'''
file = open("C:\\Users\\toaxo\\Desktop\\MyCPP\\TryCPR\\dataFromGC.txt", "r")
print(file.read(90))  # Reading 90 bytes(chars)! 1char=1byte
print(file.tell())  # Like tellp and tellg, tells where the cursor is in the file.
file.seek(5)  # Sets the cursor
print(file.tell())
file.close()
'''

'''
print()
file = open("C:\\Users\\toaxo\\Desktop\\MyCPP\\TryCPR\\dataFromGC.txt", "r")
for line in file:
    print(line)

file.close()
'''
print()
path = "C:\\Users\\toaxo\\Desktop\\MyCPP\\TryCPR\\dataFromGC.txt"
# Getting the length of string path
pathLength = len(path)
# Reversing the file path to find the last occuring \
reversePath = path[pathLength::-1]
k = 0
for i in reversePath:
    k += 1
    if i == '\\':
        tmp = i
        break
# Detected where the last \ occurs in the file path.
# print(k)
'''
file = open(path, "r")
print("File Name: {}".format(file.name[-k + 1:]))
print("File Path: {}".format(file.name))
print("File Mode: {}".format(file.mode))
print("is closed? {}".format(str(file.closed)))
if str(file.closed) == "False":
    print("The file is open")
file.close()
if str(file.closed) == "False":
    ...
else:
    print("The file is now closed.")
'''
print(path)
'''
file = open(path, "w")
if str(file.closed) == "True":
    print("File can not be opened")
else:
    try:
        print(file.read())
    except Exception as e:
        print("The file is {}. Opening the file in reading mode.".format(e))

file.seek(0)
file.write("Hello client!\n")
file.close()
'''

'''
try:
    file = open(path, "a+")
    #print(file.tell())
    file.seek(0)
    print(file.read())
    print("The file {} consists of {} chars.".format(file.name[-k + 1:], file.tell()))
    file.seek(0)
    file.writelines("Hello Client!")
    file.seek(0)
    print(file.read())
    #newStr = "Hello client."
    #str = file.read()[:len(newStr)]
    #print(str)
    #file.seek(0)
    #file.write(newStr)
    #file.seek(len(newStr))
    #print(file.read())
    print()
    print("File is closed? {}".format(str(file.closed)))
finally:
    file.close()

print("After finally: File is closed? {}".format(str(file.closed)))
'''

with open(path, 'r', encoding='utf-8') as original:
    print("Filename: {}".format(original.name[-k + 1:]))
    text = original.read()
    print(original.read())

'''
with open(path, 'r+', encoding='utf-8') as modified:
    str = "Hello client!"
    modified.write(str + " Welcome to the TryCPR.cpp file text!\n" + text)
    modified.seek(0)
    print(modified.read())
'''

print("is it closed? {}".format(str(original.closed)))
print()
with open(path, 'r', encoding = 'utf-8') as modified:
    for line in modified:
        print(line)