v=[2, 4, 5, 6,5,2, 8, 9]
for i in range(len(v)):
    for k in range(i,len(v)):
        if v[i]==v[k]:
            v.pop(v[k])
print(v)            