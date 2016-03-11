
def simplifiedArray(a, R=[2,3]):
    c = [a[0]]
    s = []
    p = prime(a[0])
    for x in a[1:]:
        if prime(x) == p:
            c += [x]
        else:
            s += [sum(c)]
            c = [x]
            p = not p
    s += [sum(c)]
    print(s)
    return a if s == a else simplifiedArray(s,R)

def prime(n):
    q = 1
    if n < 2:
        return 0
    if n == 2:
        return 1
    if not(n % 2):
        return 0
    for x in range(3, (n//2)+ 2,2):
        if not(n % x):
            q = 0
            break

    return q



print( simplifiedArray([1, 2, 3, 5, 6, 4, 2, 3]) )
