from enum import Enum

class CMP(Enum):
    LT = 1
    EQ = 2
    GT = 3

def cmp_lists(a, b):
    minlen = min(len(a), len(b))
    for i in range(minlen):
        cmpval = cmp(a[i], b[i])
        if cmpval == CMP.LT:
            return CMP.LT
        elif cmpval == CMP.GT:
            return CMP.GT
    
    if len(a) == len(b):
        return CMP.EQ
    elif len(a) < len(b):
        return CMP.LT
    return CMP.GT

def cmp_ints(a, b):
    if (a < b):
        return CMP.LT
    elif (a == b):
        return CMP.EQ
    return CMP.GT

def cmp(a, b):
    if isinstance(a, int):
        if isinstance(b, int):
            return cmp_ints(a, b)
        else:
            return cmp_lists([a], b)
    else:
        if isinstance(b, int):
            return cmp_lists(a, [b])
        else:
            return cmp_lists(a, b)

def bubblesort(arr):
    offset = 1
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(arr) - offset):
            if cmp(arr[i], arr[i+1]) == CMP.GT:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
        offset += 1
    return arr

with open("13.in") as f:
    part1 = 0

    i = 1
    white = "\n"
    while len(white) == 1:
        a = eval(f.readline())
        b = eval(f.readline())
        white = f.readline()

        if cmp(a, b) == CMP.LT:
            part1 += i

        i += 1
    print("Part 1:", part1)

with open("13.in") as f:
    white = "\n"
    packets = [[[2]], [[6]]]
    while len(white) == 1:
        packets.append(eval(f.readline()))
        packets.append(eval(f.readline()))
        white = f.readline()

    bubblesort(packets)
    part2 = 1
    for i in range(len(packets)):
        if packets[i] == [[2]] or packets[i] == [[6]]:
            part2 *= (i+1)
    print("Part 2: ", part2)
