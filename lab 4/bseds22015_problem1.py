x = int(input("enter:"))
y = int(input("enter:"))
for i in range(x, y+1):
    for j in range(2, i):

        if i % j == 0:
            break
    else:
        print(i, end=" ")

