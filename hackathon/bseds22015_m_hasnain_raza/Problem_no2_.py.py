
y=input("enter the name:  ")
f = open("salaries.csv", "r")
data = f.read()
m = []
table = []
sum = 0
a = data.split("\n")
a.pop()

for i in range(0, len(a)):
    table.append(a[i].split(","))
found=False    
for l in range(0, len(table)):
            if (y).upper() ==table[l][0].upper():
                table[l].pop()
                print(table[l])
                found=True
if found==False:
    print("invalid name")