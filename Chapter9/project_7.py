mhs = ['K001:ROSIHAN ARI:1979-09-01:SOLO', 
       'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
       'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']

print("=============================================================")
print("NIM    NAMA MAHASISWA           TGL LAHIR       TEMPAT LAHIR")
print("=============================================================")

for i in mhs:
    data = i.split(':')
    nim = data[0]
    nama = data[1]
    tgl_lahir = data[2]
    tgl_split = tgl_lahir.split('-')
    tgl = tgl_split[2]
    bln = tgl_split[1]
    thn = tgl_split[0]
    tmp_lahir = data[3]
    
    print(nim.ljust(6),
          nama.ljust(24),
          tgl,'/',bln,'/',thn.ljust(5),
          tmp_lahir)
    
    
    
