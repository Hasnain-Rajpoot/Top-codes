a="how are you"
b="how are  you"
for i in range(len(a)):
    if a[i]!=b[i]:
            print(False)
            break
else:
    print(True)
p=[3,3,4,5,6,7,5]
# for k in p:
#     for l in range(0,len(p)):
#         if p[k]==p[l]:
#             p.pop(k)
#             p[l]=p[k]
# print(p)            