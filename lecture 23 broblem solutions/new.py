a=[]
b=[]
row=2
column=2
x=3
for i in range(row):
    for k in range (column):
        a.append(x)
        x+=1
    b.append(a)
    a=[]
for k in b:
    print(k)   
for l in range (0,len(b)): 
        for j in range (0,len(b[l])):
            if [l]==[j]:
                b[l][j]+=5
            if b[l][j]>7:
                b[l][j]+=5

print(b)                    
