def g(a):
    s = [a[0]]
    for x, y in zip(a[1:], a[:-1]):
        i = len(s) - 1
        if u(x) ^ u(y):
            s += [x]
        else:
            s[i] += x

    return s == a and a or g(s)

simplifiedArray = g
u = lambda n: n>1 and all([n % j for j in range(2,n//2+1)]) 

print(simplifiedArray([-3, 4, 5, 2, 0, -10]))
