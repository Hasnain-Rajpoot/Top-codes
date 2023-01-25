def numdigits(n):
    y = []
    x = n
    while x > 0:

        y.insert(0, x % 10)
        x = x//10
    return y


n = 30256786544567654
print(numdigits(n))
