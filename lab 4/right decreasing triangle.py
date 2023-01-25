l = 5
for i in range(l):
    for j in range(i, l):
        print((' '), end=" ")

    for b in range(i+1):
        print("*", end=" ")
    for b in range(i):
        print("*", end=" ")
    print()
