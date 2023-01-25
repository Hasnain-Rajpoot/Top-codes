y=input("enter the number")
f = open("salaries.csv", 'r')
data = f.read()
m = []
table = []
sum = 0
a = data.split("\n")
a.pop()


for i in range(0, len(a)):
    table.append(a[i].split(","))
print(table)    

# for l in range(1, len(table)):
#     for j in range(1, len(table[l])):