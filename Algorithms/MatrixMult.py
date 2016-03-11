def MatrixMultiplication(a, b):
    return [[sum([m[i] * x[i] for x in b]) for i in [0,1,2]] for m in a]

a = [[1,2,3],
     [4,5,6],
     [7,8,1]]

b = [[1,2,3],
     [3,2,1],
     [4,5,2]]

print(MatrixMultiplication(a,b))