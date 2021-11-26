nilai = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80}, 
         {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90}, 
         {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50}, 
         {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100}, 
         {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]

print("=================================================")
print("NIM    NAMA         MID   UAS   N.AKHIR   STATUS")
print("=================================================")

for i in nilai:
    akhir = (i['mid'] + (2 * i['uas']))/3
    i['akhir'] = round(akhir,2)
    if i['akhir'] >= 60:
        i['stat'] = 'LULUS'
    else:
        i['stat'] = 'TIDAK LULUS'
    
    print(i['nim'].ljust(6),
          i['nama'].ljust(12),
          str(i['mid']).ljust(5),
          str(i['uas']).ljust(5),
          str(i['akhir']).ljust(9),
          i['stat'])
    
    
    
