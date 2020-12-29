#py 4
file = open ("data1.txt", 'r')
nim = input ("Silakan masukkan NIM mahasiswa yang ingin anda cari :")
daftar = []
for data in file:
    identitas = data.split('|')
    daftar.append(identitas[0])
    daftar.append(identitas[1])
    daftar.append(identitas[2])
if nim not in daftar:
    print ("NIM tidak ditemukan")
else:
    print("\nNIM\t:",daftar[daftar.index(nim)])
    print("\nNama\t:",daftar[daftar.index(nim)-1])
    print("\nAsal\t:",daftar[daftar.index(nim)+1])

file.close()
