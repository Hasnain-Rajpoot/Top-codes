f=open("exam-results.txt","r")
t=[]
h=open("exa.txt","a")
d=f.read()
e=d.split("\n")
for j in range(len(e)):
    e[j].split(",")
    t.append(e[j].split("\t\t"))
t.pop(0)    
print(t)
for o in range(len(t)):
    for h in range(len(t[o])):
        a=t[o][0]
    print(a) 
p=f.readline()
h.write(p)
h.write("\n")
h.close    