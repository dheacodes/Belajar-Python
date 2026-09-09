resep_4_jus = [600, 400, 4] 
jumlah_porsi = 15

hitung = [(bahan / 4) * jumlah_porsi for bahan in resep_4_jus]

print(f"Jumlah buah adalah {int(hitung[0])} gram, dengan susu {int(hitung[1])} ml, dan gula {int(hitung[2])} sendok makan.")