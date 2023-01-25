x=input("Enter the six numbers:\n")
for j in x:
    s=int(j)
    v=0
    for h in range(6):
        v+=s
        print(v,end=" ")
    print("\n")