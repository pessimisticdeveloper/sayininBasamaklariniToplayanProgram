#girilen sayının basamaklarını toplayan program

top = 0
sayi = int(input("bir sayı girin:"))
while(sayi != 0):
    top = top + sayi % 10
    sayi = sayi // 10

print(top)