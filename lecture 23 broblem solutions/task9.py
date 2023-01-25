x=int(input("number of rows:"))
y=int(input("number of columns:"))
v=[]
u=[]
for i in range(x):
    for j in range(y):
        u.append(0)
    v.append(u)
    u=[]
    
print(v)        