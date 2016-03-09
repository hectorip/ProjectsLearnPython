def lightBulbs(lights, n):
    for i in range(n):
        j = -1
        l = lights[:]
        for bulb in l:
            if l[j]:
                lights[j+1] = int(not bulb)
            j += 1
        print(lights)
    return lights

def rlightBulbs(l, n):
    print(n)
    r = l[:]
    for j in range(len(l)):
        if l[j-1]:
            r[j] = int(not l[j])

    print(r)
    return r if n == 1 else rlightBulbs(r, n-1)

print(rlightBulbs([0, 1, 1, 0, 1], 2))
