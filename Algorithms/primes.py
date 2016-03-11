def simplifiedArray(a):
    s = [a[0]]
    for x, y in zip(a[1:], a[:-1]):
        i = len(s) - 1
        if u(x) ^ u(y):
            s += [x]
        else:
            s[i] += x

    return s == a and a or simplifiedArray(s)

u = lambda n: n>1 and all([(n%j) for j in range(2, int(n**0.5)+1)]) 

print(simplifiedArray([-3, 4, 5, 2, 0, -10]))
