'''
Nama : Dhea Febrianti
NIM : 2602997
Kelas : 1A
'''

buah = ['apel', 'jeruk', 'ceri', 'durian', 'apel', 'mangga']
buah[2] = 'cherry'
nomor = int(input('Masukkan index yang akan ditambahkan : '))
tambahanbuah = input('Masukkan nama buah : ')
buah.insert(nomor, tambahanbuah)
buah.sort()
print(buah)