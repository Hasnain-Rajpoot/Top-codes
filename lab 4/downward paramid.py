l = 4
for i in range(l):
    
    for j in range(i+1):
        print((' '), end=" ")

    for b in range(i,l):
        print("*", end=" ")
    for b in range(i,l-1):
        print("*", end=" ")
    print()
