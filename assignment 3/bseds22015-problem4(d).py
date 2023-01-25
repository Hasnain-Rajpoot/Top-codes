print("M Hasnain Raza\nbseds2205")


def multiplyNum(a):
    sum = 0
    for i in range(len(a)):
        for j in range(len(a[i])):
            a[i][j] *= 3

    return a


a = [[5, 2, 2],
    [2, 5, 2],
    [2, 2, 5]]
p = multiplyNum(a)

for l in p:
    print(l)
