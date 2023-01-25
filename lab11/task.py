f = open("students.csv", 'r')
data = f.read()
m = []
table = []
sum = 0
a = data.split("\n")
a.pop()
for i in range(0, len(a)):
    table.append(a[i].split(","))

for l in range(1, len(table)):
    for j in range(1, len(table[0])):
        sum = sum+int(table[l][j])
    m.append(sum)
    sum = 0

print(m)
