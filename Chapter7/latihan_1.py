try:
    nama_file = input("Masukkan nama file: ")
    file = open(nama_file, "r")
    print(file.read())
except FileNotFoundError:
    print("File tidak ditemukan")
except UnicodeDecodeError:
    print("File tidak bisa terbuka di Shell")
