l = 7
for i in range(l):
    for j in range(i,l):
        print(' ', end=" ")
    c=1
    for b in range(i+1):
        print(c, end=" ")
        c+=1
    print()
