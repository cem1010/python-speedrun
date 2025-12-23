kelime=input("metin giriniz")
ayrıkKelimelerDizisi=kelime.split()
print(str(len(ayrıkKelimelerDizisi))+" kadar kelime")

frekans ={}

for şimdikiKelime in ayrıkKelimelerDizisi:
    for harf in şimdikiKelime:
        harf=harf.lower()
        if harf in frekans:
            frekans[harf]+=1
        else :
            frekans[harf]=1
print(frekans)