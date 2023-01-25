print("M Hasnain Raza\nbseds2205")


def factorial(list):
    y = []
    u = 1
    for i in list:
        
        for j in range(1, i+1):

            u = u*j

        y.append(u)
        u = 1
    return y


list = [2, 4, 5, 6, 8, 9]


print(factorial(list))
