
print("hoşgeldiniz, dönüşüm için seçim yapınız.")
def uzaklık(deger):
    secim=input("hangisinden hangisine dönüşüm? (1.km->mil 2.mil->km)")
    if(secim=="1"):
        sonuc=0.62*deger
        return str(deger)+"kilometre = "+str(sonuc)+" mil dir."
    elif(secim=="2"):
        sonuc = 1.60 * deger
        return  str(deger)+"mil = "+str(sonuc)+" km dir."
def sıcaklık(deger):
    secim = input("hangisinden hangisine dönüşüm? (1.C->fahrenight 2.fahrenight->C)")
    if (secim == "1"):
        sonuc= (deger*1.8)+32
        return str(deger)+" derece,"+str(sonuc)+" fahrenight dir."
    elif (secim=="2"):
        sonuc = (deger -32) /1.8
        return str(deger) + " fahrenight," + str(sonuc) + " derece dir."
while True:
    print("1. Sıcaklık,2.Uzaklık")
    girilen=input()
    deger = int(input("değer giriniz"))
    if(girilen=="1"):
        a=sıcaklık(deger)
        print(a)
    elif(girilen=="2"):
        a=uzaklık(deger)
        print(a)


