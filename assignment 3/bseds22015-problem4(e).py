print("M Hasnain Raza\nbseds2205")


def sumMatrix(a, b):
    result = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]
    for i in range(len(a)):
        for j in range(len(a[i])):
            result[i][j] = a[i][j]+b[i][j]

    return result


a = [[5, 2, 2],
     [2, 5, 2],
     [2, 2, 5]]
b = [[15, 6, 6],
     [6, 15, 6],
     [6, 6, 15]]
p = sumMatrix(a, b)
for l in p:
    print(l)
