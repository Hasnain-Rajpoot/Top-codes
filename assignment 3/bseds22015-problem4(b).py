print("M Hasnain Raza\nbseds2205")


def diagonalSum(a):
    sum = 0
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i] == a[j]:
                sum = sum+a[i][j]
    return sum


a = [[5, 2, 2],
    [2, 5, 2],
    [2, 2, 5]]
print(diagonalSum(a))
