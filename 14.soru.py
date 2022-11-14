l=[]
for a in range(1,6):
    for b in range(1,6):
            if a*b==6 and a>b:
                c = a-b
                l.append(c)
x = min(l)
if a-b ==x:
    print(a,b)
    

           
