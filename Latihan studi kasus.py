print('''
Kode jurusan |      Nama jurusan             |        Harga            |
------------------------------------------------------------------------
    SI         Sistem informasi                  Rp2.400.000
    SIA        Sistem informasi Akuntansi        Rp2.400.000
------------------------------------------------------------------------
''')


nis = int(input("Masukkan nis : "))
nama = input("Masukkan nama : ")
jurusan = input("Masukkan kode jurusan[SI],[SIA] : ")
if jurusan == 'SI'or'si':
    print('''
Kode jurusan |      Nama jurusan             |        Harga            |
------------------------------------------------------------------------
    SI         Sistem informasi                  Rp2.400.000
------------------------------------------------------------------------
''')
elif jurusan == 'SIA'or'sia':
    print('''
Kode jurusan |      Nama jurusan             |        Harga            |
------------------------------------------------------------------------
    SIA        Sistem informasi Akuntansi        Rp2.400.000
------------------------------------------------------------------------
''')
else:
    print("jurusuan tidak tersedia")

