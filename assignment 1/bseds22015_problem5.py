y=int(input("Enter the first number:"))
x=int(input("Enter the second number:"))
if y > x:
    greater=y
else:
    greater=x
    LCM=greater
while True:
    if (greater % x==0) and (greater % y ==0):
        break
    
    greater+=1
    LCM=greater
    
print(LCM)    