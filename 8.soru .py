b=[]
for i in range(100,1000):
    if i%2==0:
        if int(str(i)[0])==int(str(i)[1]) or int(str(i)[0])==int(str(i)[2]) or int(str(i)[1])==int(str(i)[2]):
            b.append(i)
print(len(b))
