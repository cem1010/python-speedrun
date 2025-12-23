import random
makineSayisi= random.randint(1,100)

while True :
    sayi = int(input("sayi giriniz"))

    if sayi < makineSayisi:
        print("daha buyuk sayi girin")
    if sayi >makineSayisi:
        print("daha kucuk sayı girin")
    if sayi ==makineSayisi:
        print("sayı doğru")
        break
