import pdb  # Usage just like GDB


def Test(a, b):
    sum = 0
    pdb.set_trace()  # Debugger activates the next line
    for i in range(b):
        sum += i * a
    return sum


pdb.pm()  # Activates if program crashes
