with open ("Sebelum Enkripsi.txt") as file:
    hurufawal = []
    hurufubah = []
    for kata in file:
        for huruf in kata:
            hurufawal.append(huruf)
    print(hurufawal)
    n = int(input("Silakan Masukkan nilai n :"))
    for data in hurufawal :
            i = ord(data) + n
            hurufubah.append(chr(i))
    with open ("Setelah Enkripsi.txt", 'w+') as f:
        for data in hurufubah :
            f.write(data)
