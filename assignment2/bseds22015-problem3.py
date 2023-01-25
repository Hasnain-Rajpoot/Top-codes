#bseds22015
#m hasnain raza



def primePosition(n):
    maxPrime = 1000000
    location = [0]*(maxPrime + 1)

    location[0] = -1
    location[1] = -1

    pos = 0
    for i in range(2, maxPrime + 1):
          if (location[i] == 0):
                pos += 1
                location[i] = pos
                for j in range( i * 2, maxPrime + 1 ,i):
                      location[j] = -1

    print(location[n])


n = int(input("Enter a number: "))
primePosition(n)
