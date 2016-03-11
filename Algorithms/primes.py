def simplifiedArray(a):
    r = o()
    c = [a[0]]
    s = []
    p = f(a[0])
    for x in a[1:]:
        if f(x) == p:
            c += [x]
        else:
            s += [sum(c)]
            c = [x]
            p = not p
    s += [sum(c)]
    return a if s == a else simplifiedArray(s)


def o():
    p = [2,3,5,7,9]
    for i in range(11,999,2):
        q = 1
        for x in p:
            if not(i % x):
                q = 0
                break
        if q:
            p += [i]
    return p
def f(n, p):
    if n in p:
        return True, p
    else:
        return False, p

print( simplifiedArray([1, 2, 3, 5, 6, 4, 2, 3]) )
