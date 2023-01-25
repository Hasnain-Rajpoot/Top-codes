#bseds22015
#m hasnain raza







def sumnum(num):


  sum =0
  while (num>0):
      sum =sum+num%10
      num=num//10
  return sum


num=int(input("enter a number:"))
print (sumnum (num))
