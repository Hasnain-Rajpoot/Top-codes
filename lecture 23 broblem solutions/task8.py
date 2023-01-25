y=[[5,6,82,2],[2,10,45,1]]
print(y)
for i in range(0,len(y)):
    for j in range(0,len(y[i])):
        if y[i][j]>5:
            y[i][j]= y[i][j]-7
        else:
            y[i][j]= y[i][j]+7
print(y)            
