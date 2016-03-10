def MatrixMultiplication(a, b):
    r = [0,1,2]
    z = []
    for i in r:
        t = [0] * 3
        for j in r:
            for k in r:
                t[j] += a[i][k] * b[k][j]
        z += [t]
    return z

a = [[1,2,3],
           [4,5,6],
           [7,8,1]]
b = [[1,2,3],
           [3,2,1],
           [4,5,2]]

print(MatrixMultiplication(a,b))