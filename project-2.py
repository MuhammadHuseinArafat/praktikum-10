#Py 2

file = open ("data1.txt", 'a+')
status = True
while status == True:
    data = []
    nama = input ("Masukkan nama Mahasiswa : ")
    nim = input ("Masukkan NIM :")
    asal = input ("Masukkan alamat :")
    data.append(nama)
    data.append(nim)
    data.append(asal)
    gabung = '|'.join (data)
    file.write(gabung + '\n')
    konfirmasi = input ("Mau ulang lagi ? (y/n) :")
    if konfirmasi != 'y' :
        file.close()
        status = False
