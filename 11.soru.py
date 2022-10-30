a=[]
for x in range(1,350):
    if 125%x==200%x==350%x:
        a.append(x)
buyuk=max(a)
print(buyuk)
