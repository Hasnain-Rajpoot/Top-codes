
f = open("test4.txt",'r+')
for i in range(9):
  f.write("4 line in file \n")
f.close()
f = open("test4.txt",'r')

for i in range(30):
  d=f.read(6)
  print(d)


