def MatrixMultiplication(a, b):
    r = [0,1,2]
    return [[sum([a[i][k] * b[k][j] for k in r])  for j in r] for i in r]

a = [[1,2,3],
     [4,5,6],
     [7,8,1]]

b = [[1,2,3],
     [3,2,1],
     [4,5,2]]

print(MatrixMultiplication(a,b))