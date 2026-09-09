''''Dhea Febrianti / 2602997 / 1A'''
jumlahprodukterjual = [120, 150, 135, 180, 160]
jumlahprodukterjual[2] = 140
jumlahprodukterjual.append(175)
jumlahprodukterjual.insert(2, 155)
jumlahprodukterjual.pop(1)
totalprodukterjual = sum(jumlahprodukterjual)
pendapatankotor = totalprodukterjual*75000
biayaplatform = int(pendapatankotor*0.5)
pendapatanbersih = int(pendapatankotor-biayaplatform)
penjualantertinggi = max(jumlahprodukterjual)
penjualanterendah = min(jumlahprodukterjual)
selisih = penjualantertinggi - penjualanterendah

print(f' Total yang terjual : {totalprodukterjual} \n Total pendapatan kotor : {pendapatankotor} \n Biaya platform (5%) : {biayaplatform} \n Pendapatan bersih : {pendapatanbersih} \n Penjualan tertinggi : {penjualantertinggi} \n Penjualan terendah : {penjualanterendah} \n Selisih penjualan tertinggi dan terendah : {selisih}')