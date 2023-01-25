import random
x=int(input("number of rows:"))
y=int(input("number of columns:"))
v=[]
u=[]
for i in range(x):
    for j in range(y):
        u.append(random.randrange(-10,10))
    v.append(u)
    u=[]
for k in v:
    print(k)