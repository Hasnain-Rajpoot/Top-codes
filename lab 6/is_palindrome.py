#TASK3

def ispalindrome(string):
    new_str = ""
    for i in string:
        new_str = i + new_str

    if string==new_str:
        return True
    else:
        return False

n="jadaj"
print(ispalindrome(n))        



n="jadaj"
p=""
for i in range(len(n)-1,-1,-1):
    p=p+n[i]   
if p==n:
    print(True)
else:
        print(False)        
