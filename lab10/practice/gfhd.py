x=4
p=1
for i in range(1,x+1):
    p=p*i 
print(p)    
y=500
for j in range(11):
    for k in range(2,y):
        if y%k==0:
            break
    if y%k!=0:
        print(y)
