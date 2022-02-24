#calculator 
while True:
    sayı1 = float(input("Bir sayı girinniz:"))
    işlem = input("yapacağınız işlemi giriniz:")
    sayı2  = float(input("Bir sayı giriniz:"))    
    if işlem =="+" :
        print(sayı1+sayı2)  
    elif işlem =="-":
        print(sayı1-sayı2)
    elif işlem =="*":
        print(sayı1*sayı2)
    elif işlem =="/":
        print(sayı1/sayı2)
    break
               