def MatrixMultiplication(a,b):
    r = [0,1,2]
    z = []
    for i in r:
        t = [0] * 3
        for j in r:
            for k in r:
                t[j] += a[i][k] * b[k][j]
        z += [t]
    return z

