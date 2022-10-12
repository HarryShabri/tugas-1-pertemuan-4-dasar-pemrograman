gaji_pokok = int(300000)
nama = input("Masukkan nama : ")
golongan_jabatan = int(input("Masukkan golongan jabatan :"))
if golongan_jabatan == 1 :
    gaji_jabatan =int(gaji_pokok*5/100)
elif golongan_jabatan == 2 :
    gaji_jabatan = int(gaji_pokok*10/100)
elif golongan_jabatan == 3 :
    gaji_jabatan = int(gaji_pokok*15/100)
else:
    print("Golongan tidak tersedia")
pendidikan = input("Masukkan pendidikkan : ")
if pendidikan == 'sma' or "SMA":
    gaji_pendidikan = int(gaji_pokok*2.5/100)
elif pendidikan == 'd1' or 'D1':
    gaji_pendidikan = int(gaji_pokok*5/100)
elif pendidikan == 'd3' or 'D3':
    gaji_pendidikan = int(gaji_pokok*20/100)
elif pendidikan == 's1' or 'S1':
    gaji_pendidikan = int(gaji_pokok*30/100)
else:
    print("Pendidikan tidak tersedia")
jam_kerja = int(input("Masukkan jam kerja :"))
if jam_kerja > 8:
    honor_lembur = int((jam_kerja- 8)* 3500)
else:
    print("tidak ada uang lembur")
total = gaji_jabatan + gaji_pendidikan + honor_lembur + gaji_pokok
print("\nKaryawan yang bernama  : ", nama)
print("Honor yang diterima ")
print("Gaji pokok               : Rp ", gaji_pokok)
print("Tunjangan Jabatan        : Rp ", gaji_jabatan)
print("Tunjangan Pendidikan     : Rp ", gaji_pendidikan)
print("Honor Lembur             : Rp ", honor_lembur)
print('------------------------------------------------+')
print("Total gaji yang diterima : Rp ", total )
