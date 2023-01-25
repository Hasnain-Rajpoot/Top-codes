print(" NOTE\nfirst number must be less than second number")

while True:
    x = int(input("enter the first number:"))
    y = int(input("enter the second number:"))
    if x < y:
        break
sum = 0
while x <= y:
    if x % 2 != 0:
        sum = sum+x
        print(x)
        x += 1
    else:
        x += 1

print("the sum of all odd numbers is = ", sum)
