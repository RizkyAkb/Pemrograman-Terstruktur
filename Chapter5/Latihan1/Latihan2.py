bhsind = int(input('Nilai B.Indonesia: '))
ipa = int(input   ('Nilai IPA        : '))
mtk = int(input   ('Nilai Matematika : '))

if (bhsind > 100) or (bhsind < 0) or (ipa > 100) or (ipa < 0) or (mtk > 100) or (mtk < 0):
    print ('Input anda tidak valid')
elif (bhsind >= 60) and (ipa >= 60) and (mtk > 70):
    print ('Status kelulusan : Selamat anda LULUS')
else:
    print ('Status kelulusan : TIDAK LULUS')

