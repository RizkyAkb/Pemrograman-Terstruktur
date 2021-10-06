harga_perhari = 200000
harga_perjam = 10000

print('Masukkan waktu mengembalikan')
jam_kembali = int(input('Jam = '))
menit_kembali = int(input('Menit = '))

print('Masukkan waktu menyewa')
jam_sewa = int(input('Jam = '))
menit_sewa = int(input('Menit = '))

lama_sewa = (jam_kembali * 60 + menit_kembali) - (jam_sewa * 60 + menit_sewa)
lama_sewa = lama_sewa / 60
print ('Lama menyewa adalah', round(lama_sewa,2), 'Jam')

if (lama_sewa <= 12):
    harga_total = harga_perhari
    print ('Jumlah yang harus dibayarkan adalah Rp.', harga_total)
    print ('Silahkan melakukan pembayaran')
    
elif(lama_sewa >= 12):
    jam_lebih = lama_sewa - 12
    jam_lebih = jam_lebih * harga_perjam
    jam_lebih = jam_lebih + harga_perhari
    harga_total = round(jam_lebih)
    print ('Jumlah yang harus dibayarkan adalah', harga_total)

uang_penyewa = int(input('Pembayaran = '))
uang_kembali = uang_penyewa - harga_total
uang_kembali = round(uang_kembali)
if (uang_kembali > 0):
    print ('Uang kembalian anda adalah Rp.',uang_kembali, '. Terima kasih :)')
elif (uang_kembali == 0):
    print ('Uang anda pas ya. Terima kasih :)')
else :
    print ('Uang anda kurang, mohon ulangi proses dari awal')
