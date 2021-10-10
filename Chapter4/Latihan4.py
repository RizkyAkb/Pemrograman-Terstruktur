jrk_AB = 125
jrk_BC = 256
kec_AB = 62
kec_BC = 70

jambrkt = 6
mntbrkt = 00

mntistirahat = 45 / 60

waktu_AB = round(jrk_AB / kec_AB, 2)
waktu_BC = round(jrk_BC / kec_BC, 2)

totalwaktu = waktu_AB + waktu_BC + mntistirahat
totalwaktu = round(totalwaktu, 2)

totaljam = totalwaktu // 1
jamsampai = totaljam + jambrkt

totalmnt = totalwaktu % 1
totalmnt = round(totalmnt * 60, 1)
mntsampai = round(totalmnt + mntbrkt, 1)

print('Waktu yang diperlukan dari kota A ke B adalah', waktu_AB, 'jam')
print('Waktu yang diperlukan dari kota B ke C adalah', waktu_BC, 'jam')
print('Total waktu perjalanan + istirahat 45 menit adalah', totalwaktu, 'jam')
print('Atau', round(totaljam), "jam", totalmnt, 'menit')
print('Jika pak Amir berangkat pada jam', jambrkt, 'lebih', mntbrkt, 'menit')
print('Maka pak Amir akan sampai pada jam', round(jamsampai), 'lebih', mntsampai, 'menit')
