def terpintar(x):
    global tertinggi
    tertinggi = 0
    data = {}
    for i in x:
        mid = i.get('mid')
        uas = i.get('uas')
        nakhir = (mid + (2*uas))/3
        if nakhir > tertinggi:
            tertinggi = nakhir
            data['nim'] = i.get('nim')
            data['nama'] = i.get('nama')
    print('Mahasiswa dengan nilai akhir tertinggi adalah',data['nama'],
          'Nim',data['nim'],'dengan nilai',round(tertinggi,3)        )
    return data
                  
nilaiMhs = [{'nim' : 'A01', 'nama' : 'Amir', 'mid' : 50, 'uas' : 80},
            {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90},       
            {'nim' : 'A03', 'nama' : 'Cici', 'mid' : 50, 'uas' : 50}, 
            {'nim' : 'A04', 'nama' : 'Dedi', 'mid' : 20, 'uas' : 30}, 
	    {'nim' : 'A05', 'nama' : 'Fifi', 'mid' : 70, 'uas' : 40}]

terpintar(nilaiMhs)


