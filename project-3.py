#py 3
file = open ("data1.txt")
mhs = {'nama' : '', 'nim' : '', 'asal' : ''}
for data in file :
    splitdulu = data.split('|')
    for key in mhs :
        mhs['nama'] = splitdulu[0]
        mhs['nim'] = splitdulu[1]
        mhs['asal'] = splitdulu[2]
    print(mhs)
file.close()
