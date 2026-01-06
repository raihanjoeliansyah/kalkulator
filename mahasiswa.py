# Program Menu Pengelolaan Mahasiswa

data_mahasiswa = []

def tampilkan_menu():
    print("\n===== MENU PENGELOLAAN MAHASISWA =====")
    print("1. Tambah Mahasiswa")
    print("2. Tampilkan Semua Mahasiswa")
    print("3. Cari Mahasiswa (NIM)")
    print("4. Hapus Mahasiswa")
    print("5. Keluar")

def tambah_mahasiswa():
    nim = input("Masukkan NIM: ")
    nama = input("Masukkan Nama: ")
    prodi = input("Masukkan Program Studi: ")

    mahasiswa = {
        "nim": nim,
        "nama": nama,
        "prodi": prodi
    }

    data_mahasiswa.append(mahasiswa)
    print("Data mahasiswa berhasil ditambahkan.")

def tampilkan_semua_mahasiswa():
    if len(data_mahasiswa) == 0:
        print("Belum ada data mahasiswa.")
    else:
        print("\nDAFTAR MAHASISWA:")
        for mhs in data_mahasiswa:
            print(f"NIM   : {mhs['nim']}")
            print(f"Nama  : {mhs['nama']}")
            print(f"Prodi : {mhs['prodi']}")
            print("-" * 30)

def cari_mahasiswa():
    nim_cari = input("Masukkan NIM yang dicari: ")
    ditemukan = False

    for mhs in data_mahasiswa:
        if mhs["nim"] == nim_cari:
            print("Data Mahasiswa Ditemukan:")
            print(f"NIM   : {mhs['nim']}")
            print(f"Nama  : {mhs['nama']}")
            print(f"Prodi : {mhs['prodi']}")
            ditemukan = True
            break

    if not ditemukan:
        print("Data mahasiswa tidak ditemukan.")

def hapus_mahasiswa():
    nim_hapus = input("Masukkan NIM yang akan dihapus: ")

    for mhs in data_mahasiswa:
        if mhs["nim"] == nim_hapus:
            data_mahasiswa.remove(mhs)
            print("Data mahasiswa berhasil dihapus.")
            return

    print("Data mahasiswa tidak ditemukan.")

def main():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            tambah_mahasiswa()
        elif pilihan == "2":
            tampilkan_semua_mahasiswa()
        elif pilihan == "3":
            cari_mahasiswa()
        elif pilihan == "4":
            hapus_mahasiswa()
        elif pilihan == "5":
            print("Terima kasih. Program selesai.")
            break
        else:
            print("Pilihan tidak valid.")


main()
