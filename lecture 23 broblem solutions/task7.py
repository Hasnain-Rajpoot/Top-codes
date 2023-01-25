y=[[5,6,82,2],[2,10,45,1]]
count=0
s=0
for i in range(0,len(y)):
    for j in range(0,len(y[i])):
            count=count+ y[i][j]
            s+=1
print(s)            
print(count/s)            
