def kalkulator():
    while True:
        print("\nMENU KALKULATOR")
        print("1. Penjumlahan")
        print("2. Pengurangan")
        print("3. Perkalian")
        print("4. Pembagian")
        print("5. Keluar")

        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "5":
            print("Terima kasih, program selesai.")
            break

        a = float(input("Masukkan bilangan pertama: "))
        b = float(input("Masukkan bilangan kedua: "))

        if pilihan == "1":
            print("Hasil penjumlahan:", a + b)
        elif pilihan == "2":
            print("Hasil pengurangan:", a - b)
        elif pilihan == "3":
            print("Hasil perkalian:", a * b)
        elif pilihan == "4":
            if b != 0:
                print("Hasil pembagian:", a / b)
            else:
                print("Error: pembagian dengan nol tidak diperbolehkan.")
        else:
            print("Pilihan tidak valid, coba lagi.")

kalkulator()