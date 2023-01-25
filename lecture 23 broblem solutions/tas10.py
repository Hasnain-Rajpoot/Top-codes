
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
k=[]        
p=[4,5,6,4,"ads",]
for j in range (len(p)-1,0,-1):
    k.append(p[j])
print(k)    