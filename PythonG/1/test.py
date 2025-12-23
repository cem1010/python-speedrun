


def ana_program():
    def uzaklık():
        print("oldu")
        pass
    print("hoşgeldiniz, dönüşüm için seçim yapınız.")
    while True:
        print ("test")
        uzaklık()
        a= input("gsayı seç")
        # Kodlarını buraya al
        # ...
        # Artık uzaklık() fonksiyonu aşağıda olsa bile Python
        # ana_program'ı en sonda çalıştıracağı için hepsini tanımış olacak.
        pass



def sıcaklık(deger):
    # ... işlemler
    pass

# En sona sihirli dokunuş:
if __name__ == "__main__":
    ana_program()

