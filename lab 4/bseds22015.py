x = int(input("enter:"))
count = 0
for i in range(1, 10):
    for j in range(2, i):

        if i % j == 0:
            break
    else:
        count += 1
        print(i)
print("total number that are prime", count)
