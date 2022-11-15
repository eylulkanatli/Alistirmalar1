kalan=0
x=int(input("Lütfen bir sayı giriniz: "))

for i in range(2,x):
    if x%i==0:
        kalan+=1
if kalan==0:
    print(x,"asal bir sayıdır.")
else:
    print(x,"asal bir sayı değildir.")
