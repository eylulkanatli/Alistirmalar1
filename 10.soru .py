c=[]
for i in range(10000,100000):
    if int(str(i)[0])==int(str(i)[3]) and int(str(i)[1])==int(str(i)[4]):
        c.append(i)
print(len(c))
