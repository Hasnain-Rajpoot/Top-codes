l = 5
for i in range(l):
    for j in range(l+1):
        print((' '), end=" ")

    for b in range(i, l):
        print("*", end=" ")
    print()
