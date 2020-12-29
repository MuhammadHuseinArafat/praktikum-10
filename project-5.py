#py 5
file = open("data2.txt")
akhir = []
for data in file:
    x = data.split('|')
    hasil = int(x[0]) + int (x[1][:-1])
    akhir.append(str (hasil))
file.close()
with open('Hasiljumlahdata.txt', 'w+') as f :
    for data in akhir :
        f.write(data + '\n')

