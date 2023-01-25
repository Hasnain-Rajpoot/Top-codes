f = open("pre_salaries.csv", 'r')
p = open("salaries.csv", "w")
data = f.read()
m = []
table = []
sum = 0
a = data.split("\n")
a.pop()
for i in range(0, len(a)):
    table.append(a[i].split(","))
print(table)
for l in range(1, len(table)):
    for j in range(1, len(table[0])):
        sum = sum+int(table[l][j])
    m.append(sum)
    table[l].append(sum)
    tax=(sum/100)*10
    table[l].append(tax)
    take=sum-tax
    table[l].append(take)
    sum = 0
table[0].append("total")
table[0].append("tax10%")
table[0].append("Take_Home")
for b in range(0, len(table)):
    for h in range(0,len(table[b])):
        p.write(str(table[b][h]))
        p.write(",")
    p.write("\n")

p.close()

