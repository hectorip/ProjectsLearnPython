def simplifiedArray(a):
    d = a[0]
    s = [d]
    p = u(d)
    i= 0
    for x in a[1:]:
        q = u(x)
        if q ^ p:
            s += [x]
            i +=1
            p = q
        else:
            s[i] += x
            
    return s == a and a or simplifiedArray(s)

u = lambda n: n>1 and all([(n%j) for j in range(2, int(n**0.5)+1)])

print(simplifiedArray([-3, 4, 5, 2, 0, -10]))
