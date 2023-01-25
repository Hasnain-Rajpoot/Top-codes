x = int(input("enter:"))
y = int(input("enter:"))
count = 0
for i in range(x, y+1):
    for j in range(2, i):

        if i % j == 0:
            break
    else:
        count += 1
print(count)
