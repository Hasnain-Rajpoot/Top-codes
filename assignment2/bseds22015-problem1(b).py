#bseds22015
#m hasnain raza





def is_prime(x):

 n  = 0
 for y in range (2,x):
     if (x%y==0):   
        return (False)
        n = 1
        break
 if n != 1:
     return (True)
    
x=int(input("enter a number:"))
print (is_prime(x))
