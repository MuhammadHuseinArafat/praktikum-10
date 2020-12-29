#py 1
with open ("data.txt") as file:
    angka = []
    i = 0
    j = 0
    for data in file:
        angka.append (int(data))
    for data in angka:
        if data % 2 == 0:
            i += 1
        else:
            j +=1
    print("Banyak Bilangan Genap adalah :", i, "\nBanyak Bilangan Ganjil adalah :", j)
