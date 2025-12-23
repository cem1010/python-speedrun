

kilo,boy=input("kilo_boy giriniz").split("_")
kilo=float(kilo)
boy=float(boy)/100
vki=kilo/(boy**2)

print(str(vki))
if(vki<=18.5):
    print("zayıf")
elif(18.5<vki<=24.9):
    print("Normal (İdeal)")
elif(25.0<vki<=29.9):
    print("Fazla Kilolu")
elif(30.0<vki<= 34.9):
    print("Obez 1")




