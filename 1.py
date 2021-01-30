# Deklarasi semua type rumah dan harga rumah!!
semuaTypeRumah = ['Rose', 'Gold', 'Platinum']
semuaHargaRumah = {
    semuaTypeRumah[0]: 120000000,
    semuaTypeRumah[1]: 300000000,
    semuaTypeRumah[2]: 360000000
}

# Display input
print(".------------------->")
print("| 1. Rose\t120.000.000")
print("| 2. Gold\t300.000.000")
print("| 3. Platinum\t360.000.000")
print("`------------------->")

# Pencarian type rumah berdasarkan input user (1-3)
rumahTerpilih = input("|Pilih Rumah, option 1-3 ----> ")
try:
    typeRumah = semuaTypeRumah[int(rumahTerpilih)-1] # ---------------> TYPE RUMAH
except:
    print("Only 1-3 ;>")
    exit()

# Pencarian lama kredit berdasarkan input user (1-3)
kreditTerpilih = input("Lama Kredit (\n1. 12 Bulan,\n2. 18 Bulan,\n3. 24 Bulan\n)`option 1-3 ----> ")
if kreditTerpilih == '1':
    lamaKredit = 12 # LAMA KREDIT 12 BULAN
elif kreditTerpilih == '2':
    lamaKredit = 18 # LAMA KREDIT 18 BULAN
elif kreditTerpilih == '3':
    lamaKredit = 24 # LAMA KREDIT 24 BULAN
else:
    print("Only 1-3")
    exit()
# ----------------------------------- ^^LAMA KREDIT^^



# Fixed variabel berdasarkan input
hargaRumah = semuaHargaRumah[typeRumah]
uangMuka = int(hargaRumah * 0.2)
sisa = hargaRumah - uangMuka
angsuran = int(sisa / lamaKredit)

# Display user!
input('Sukses!') # Menunggu user sebelum data ditampilkan
print('\n\n.----------------------------->')
print('Detail Pembelian')
print('.----------------------------->')
print(f'Type Rumah:\t{typeRumah}')
print(f'Harga Rumah:\t{hargaRumah}')
print(f'Uang Muka:\t{uangMuka}')
print(f'Sisa:\t\t{sisa}')
print(f'Lama Kredit\t{lamaKredit}')
print(f'Angsuran:\t{angsuran}')


# Display tabel angsuran!!
input('\n\nDisplay tabel angsuran!') # menggunggu user sebelum data ditampilkan
print('\n.----------------------------->')
print('|Tabel Angsuran')
print('|----------------------------->')
print('|Bulan ke\t| Angsuran\t| Sisa')
print('|----------------------------------------------|<')
for no in range(lamaKredit):
    sisa -= angsuran
    print(f'|\t{no+1}\t| {angsuran}\t| {sisa} ')