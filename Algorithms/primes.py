
def simplifiedArray(a, R=[2,3]):
    for i in range(max(R)+2,max(a) + 1,2):
        q = 1
        for x in filter(lambda r: r<i/2, R):
            if not(i % x):
                q = 0
                break
        if q:
            R += [i]
    print(R)
    c = [a[0]]
    s = []
    p = a[0] in R
    for x in a[1:]:
        if (x in R) == p:
            c += [x]
        else:
            s += [sum(c)]
            c = [x]
            p = not p
    s += [sum(c)]
    return a if s == a else simplifiedArray(s,R)



print( simplifiedArray([1, 2, 1009, 5, 6, 4, 2, 30000]) )
