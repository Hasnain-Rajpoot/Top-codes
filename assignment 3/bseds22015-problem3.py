print("M Hasnain Raza\nbseds2205")


def subtraction(a, b):
    result = [[0, 0],
            [0, 0]]
    for i in range(len(a)):
        for j in range(len(a[i])):
            result[i][j] = a[i][j]-b[i][j]

    return result


a = [[1, 2],
    [3, 4]]
b = [[5, 6],
    [0, 7]]
p = subtraction(a, b)
for l in p:
    print(l)
