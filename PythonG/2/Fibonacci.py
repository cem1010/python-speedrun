

sayi=int(input("hangi sayıya kadar fibonacci yazdırmak istersin?"))
dizi ={}
a=0
b=1
toplam=0



def fibonacciOlustur(sayi,dizi):
    AnlıkSayi=0
    while AnlıkSayi<= sayi:
        if (AnlıkSayi==0):
            dizi[0]=0
        elif (AnlıkSayi==1):
            dizi[1] = 1
        elif (AnlıkSayi<=sayi):
            dizi[AnlıkSayi]=dizi[AnlıkSayi-1]+dizi[AnlıkSayi-2]
        AnlıkSayi = AnlıkSayi + 1
    return dizi

print (str(fibonacciOlustur(sayi,dizi)))