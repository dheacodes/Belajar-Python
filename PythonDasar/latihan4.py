''''
Nama : Dhea Febrianti
NIM : 2602997
Kelas : 1A
'''

JumlahPeserta = int(input('Masukkan jumlah peserta : '))
BiayaSewaTempat = int(input('Masukkan biaya sewa tempat : Rp. '))
BiayaDokumentasi = int(input('Masukkan biaya dokumentasi Rp. '))

# Perhitungan biaya konsumsi
HargaKonsumsi = 35000
JumlahKonsumsi = int(int(JumlahPeserta)*1.1)
TotalHargaKonsumsi = JumlahKonsumsi*HargaKonsumsi

print(f'a. Perhitungan Biaya Konsumsi \n Jumlah konsumsi : {JumlahKonsumsi} \n Total biaya konsumsi : Rp. {TotalHargaKonsumsi}')

# Perhitungan Kebutuhan Cetak Sertifikat
HargaRIM = 65000
JumlahSertifikat = JumlahKertas = round(int(JumlahPeserta)*1.05)
JumlahRIM = (JumlahKertas+499)//500
TotalHargaKertas = JumlahRIM*HargaRIM

print(f'b. Perhitungan Kebutuhan cetak sertifikat \n Jumlah sertifikat yang perlu dicetak : {JumlahSertifikat} \n Jumlah lembar kertas yang dibutuhkan : {JumlahKertas} \n Perkiraan jumlah rim kertas yang dibutuhkan : {JumlahRIM} \n Total biaya pembelian kertas : Rp. {TotalHargaKertas}')

# Perhitungan Biaya Pendaftaran Peserta
HargaCetakSertifikat = HargaRIM//500
TotalBiayaPenyelenggaraan = BiayaDokumentasi + BiayaSewaTempat+ TotalHargaKertas + TotalHargaKonsumsi
DanaCadangan = round(TotalBiayaPenyelenggaraan*0.1)
TotalDana = DanaCadangan + TotalBiayaPenyelenggaraan
BiayaPendaftaran = TotalDana//JumlahPeserta 

print(f'c. Perhitungan Biaya Pendaftaran peserta \n Total Biaya penyelenggaraan acara : Rp. {TotalBiayaPenyelenggaraan} \n Besar dana cadangan : Rp. {DanaCadangan} \n Total dana yang harus dikumpulkan : Rp. {TotalDana} \n Biaya pendaftaran : Rp. {BiayaPendaftaran}')