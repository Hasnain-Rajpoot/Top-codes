n=[4,5,7,54,3]
u=[]
for i in n:
    i**=2
    u.append(i)
    i=0
print(u)  




my=[4,5,7,54,3]
u=[]
for i in  range(len(my) -1):
    u.append(my[i])
print(u)    


my=["ali","tali","bali","cali"]
for i in  range(len(my)):
    for j in range(i,len(my)):
        if my[i]>=my[j]:
            my[i],my[j]=my[j],my[i]
print(my)