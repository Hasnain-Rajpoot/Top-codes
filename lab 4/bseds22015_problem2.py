n = int(input("enter the number"))
x = 0
y = 1
for i in range(n):
    print(x)
    c = x
    x = y
    y = c+y
