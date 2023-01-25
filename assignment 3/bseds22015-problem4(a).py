print("M Hasnain Raza\nbseds2205")


def matrix(rows, columns):
    y = []
    l = []
    for i in range(rows):
        for j in range(columns):
            y.append(0)
        l.append(y)
        y = []
    return l


rows = 3
columns = 3
p = matrix(rows, columns)
for k in p:
    print(k)
