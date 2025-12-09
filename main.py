import random

print("Sayı tutturmaca oyununa hoş geldin,")
print("şimdi senden hangi 2 sayının arasında bir sayıyı tutmak istediğini öğreneceğim,")
print("daha sonra kaç hak istediğini yazabilirsin!")
min_sayı = int(input("1. sayıyı seç:"))
max_sayı = int(input("2. sayıyı seç:"))

if min_sayı >= max_sayı:
    print("1. sayı 2. sayıdan küçük olmalı.")
    exit()

harf_kullanma = 0
max_hak = int(input("Kaç canın olmasını isterdin?"))
kalan_hak = max_hak
print("Sayı tutturmaca oyunu, bakalım kaç denemede doğru sayıyı bulabileceksin!")

bilgisayar_sayı = random.randint(min_sayı, max_sayı)

while True:
    if max_hak > (max_sayı - min_sayı):
        print("O kadar hak veremem.")
        exit()
    try:
        oyuncu_sayı = int(input(f"{min_sayı} ile {max_sayı} arasında bir sayı seç: "))
    except:
        harf_kullanma += 1
        match harf_kullanma:
            case 1:
                print("Bir daha harf kullanırsan oyun biter.")
            case 2:
                print("Son bir şans daha veriyorum bir daha harf yazarsan oyunu bitiririm!")
            case 3:
                print("Bunu sen istedin...")
                exit()
        continue
    if bilgisayar_sayı != oyuncu_sayı:
        print(f"Yanlış seçtin, kalan canın: {kalan_hak}")
        kalan_hak -= 1
        if kalan_hak == 0:
            print(f"Oyun bitti, {max_hak - kalan_hak} denemede doğru sayıyı tutturamadın.")
            print(f"Doğru sayı {bilgisayar_sayı} olacaktı...")
            exit()
    else:
        print("Tebrikler, bilgisayar ile aynı sayıyı seçtin, ikiniz de", bilgisayar_sayı,
              "sayısını seçtiniz, tam olarak kalan canın :", kalan_hak)
        exit()
