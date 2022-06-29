def fibonacci(k):
    a = 0
    b = 1
    print(a, b, end=" ")
    for i in range(10):
        c = a + b
        a = b
        b = c
        print(c, end=" ")
    print()


def bubble_sort(l):
    print(l)
    for i in range(len(l)):
        for j in range(i, len(l)):
            if(l[i] > l[j]):
                l[i], l[j] = l[j], l[i]

    print(l)


l = [4, 3, 0, 2, 9, 1, 8]


def star_pyramid(r):
    for i in range(r):
        print(' '*(r-i-1)+'*'*(2*i+1))


def is_prime(k):
    r = range(2, k//2+1)
    for i in r:
        if k % i == 0:
            print("NO")
            return
    print("YES")


def is_palindrome(s):
    if s == s[::-1]:
        print("YES")
    else:
        print("NO")


l = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
print(l)
print(list(map(int, l)))
