v=[2, 4, 5, 6,5,2, 8, 9]
o=[]
for i in range(len(v)):
    if v[i]  not in o:
        o.append(v[i])
print(o)


a = [ [ 1, 2 ] , 
    [ 3, 4] ]
b = [ [ 5, 6 ] , 
    [ 0, 7] ]
c = [ [ 0, 0 ] , 
    [ 0, 0] ]    


for i in range(len(a)):
    for k in range(len(a[i])):
        c[i][k]=a[i][k]+b[i][k]
print(c)

p=[]
l=[]
import random
for i in range(3):
    for j in range(3):
        p.append(random.randrange(-10,10))
    l.append(p)
    p=[]    
print(l)



a = [ [ 1, 2 ] , 
    [ 3, 4] ]
p=0    
for i in range(len(a)):
    for k in range(len(a[i])):
        if a[i]==a[k]:
            p+=a[i][k]
print(p)

m=5
p=1
for i in range(1,m+1):
    p*=i
print(p) 
l=5
for i in range(5,-1,-1):
    print(" "*(i))
for i in range(5):
    print("*"*(i))


