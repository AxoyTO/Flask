def find_min(l):
    min = l[0][1]
    for i in l:
        if i[1] < min:
            min = i[1]
    return min


def find_val_count(l, val):
    count = 0
    for i in l:
        for j in i:
            if j == val:
                count += 1
    return count


def find_names(l, val):
    k = []
    for i in l:
        if i[1] == val:
            k.append(i[0])
    return k


if __name__ == '__main__':
    l = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        l.append([name, score])

    minim = find_min(l)
    min_count = find_val_count(l, minim)

    k = l.copy()
    for i in range(min_count):
        for j in range(len(l)):
            if l[j][1] == minim:
                print(j)
                k.pop(j)

    new_min = find_min(k)
    names = find_names(k, new_min)
    names.sort()
    for i in names: print(i)