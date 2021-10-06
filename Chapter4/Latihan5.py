print('Grafik jumlah mahasiswa laki-laki dan perempuan PTIK UNS')
mhs_laki = int(input('Masukkan jumlah mahasiswa laki laki = '))
lk_puluh = mhs_laki // 10
lk_puluh = '$' * lk_puluh
lk_satuan = mhs_laki % 10
lk_satuan = '@' * lk_satuan 

mhs_pr = int(input('Masukkan jumlah mahasiswa perempuan = '))
pr_puluh = mhs_pr // 10
pr_puluh = '$' * pr_puluh
pr_satuan = mhs_pr % 10
pr_satuan = '@' * pr_satuan 

print (lk_puluh,lk_satuan,(mhs_laki))
print (pr_puluh,pr_satuan,(mhs_pr))

print('$ berarti puluhan @ berarti satuan')
