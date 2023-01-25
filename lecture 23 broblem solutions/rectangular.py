
n=3
v=[]
u=[]
for i in range(6):
    for j in range(n):
        u.append(0)
    v.append(u)
    u=[]

    n+=2
print(v)        