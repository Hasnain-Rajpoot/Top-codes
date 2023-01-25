
print("M Hasnain Raza\nbseds2205")


def duplicate_remove(a):
    y = []
    for i in a:
        if i not in y:
            y.append(i)

    return y


a = [6, 7, -2, 11, 7, -2]
print(duplicate_remove(a))
