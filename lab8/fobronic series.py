#PROBLEM NO 3
def fibonacciseries(a):
    l=[]
    x=0
    y=1
    for i in range (0,a):
        l.append(x)
        v=x+y
        x=y
        y=v
    return l
a=10
print(fibonacciseries(a))
        



    