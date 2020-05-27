def gcd(a, b):
    if a < b:
        tmp = a
        a = b
        b = tmp

    while a > b:
        while a > b:
            a = a - b
        tmp = a
        a = b
        b = tmp
    return a


def extended_gcd(a, b):
    listA = []
    listB = []
    x1 = 0
    y1 = 1
    gcd = -1
    swap  = (a > b)

    if swap:
        tmp = a
        a = b
        b = tmp

        x1 = 1
        y1 = 0

    while True:
        if b % a == 0:
            gcd = a

            while listA:
                a = listA.pop()
                b = listB.pop()

                y = x1
                x = y1 - x1 * (b / a)

                x1 = x
                y1 = y

            break
        else:
            listA.append(a)
            listB.append(b)

            b = b % a
            tmp = a
            a = b
            b = tmp

    if swap:
        return y1, x1, gcd
    return x1, y1, gcd
