def first_nth_primeNum(k):
        for h in range(2,k):
            if i%h==0:
                break
        else:
            return i        
k=100
print(first_nth_primeNum(k))