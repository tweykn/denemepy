def toplama(a, b):
    return a + b

def cikarma(a, b):
    return a - b

def carpma(a, b):
    return a * b

def bolme(a, b):
    if b != 0:
        return a / b
    else:
        return "Hata: Bir sayı sıfıra bölünemez!"

def hesap_makinesi():
    print("Hesap Makinesi")
    print("1. Toplama")
    print("2. Çıkarma")
    print("3. Çarpma")
    print("4. Bölme")

    secim = input("Seçiminizi yapın (1/2/3/4): ")

    if secim in ['1', '2', '3', '4']:
        try:
            sayi1 = float(input("Birinci sayıyı girin: "))
            sayi2 = float(input("İkinci sayıyı girin: "))

            if secim == '1':
                print(f"Sonuç: {toplama(sayi1, sayi2)}")
            elif secim == '2':
                print(f"Sonuç: {cikarma(sayi1, sayi2)}")
            elif secim == '3':
                print(f"Sonuç: {carpma(sayi1, sayi2)}")
            elif secim == '4':
                print(f"Sonuç: {bolme(sayi1, sayi2)}")
        except ValueError:
            print("Hata: Lütfen geçerli bir sayı girin!")
    else:
        print("Hata: Geçersiz seçim!")

if __name__ == "__main__":
    hesap_makinesi()    