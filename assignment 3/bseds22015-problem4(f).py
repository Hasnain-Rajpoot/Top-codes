print("M Hasnain Raza\nbseds2205")


def subtraction(a, b):
    
    result = [[0, 0,0],
            [0, 0,0]]
    for i in range(len(a)):
        for h in range(len(a[i])):
            result[i][h]=a[i][h]+b[i][h]


    return(result)
a = [[1, 2,7],
    [3, 4,4]]
b = [[5, 6,5],
    [0, 7,2]]
p = subtraction(a, b)
for l in p:
    print(l)
X = [[12,7],
    [4 ,5],
    [3 ,8]]

result = [[0,0,0],
        [0,0,0]]
for i in range(len(X)):
    for j in range(len(X[0])):
        result[j][i] = X[i][j]

print(result)
k=5
for i in range(k):
    print(" "*(k-i),"$"*(2*i+1))
for i in range(k-2,-1,-1):
    print(" "*(k-i),"$"*(2*i+1))
