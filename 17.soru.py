x=int(input("3 veya 4 basamaklı bir sayı giriniz:"))
if 99<x and x<10000:
    if x==int(str(x)[::-1]):
        print("Girdiğiniz sayı palindromik bir sayıdır.")
    else:
        print("Girdiğiniz sayı palindromik bir sayı değildir.")
else:
    print("3 veya 4 basamaklı bir sayı girmediniz lütfen tekrar deneyiniz.")
 
    
        
