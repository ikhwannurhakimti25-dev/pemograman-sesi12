from modul.pemilih import lihat_pemilih
from modul.calon import lihat_calon
from modul.voting import proses_voting
from modul.statistik import tampilkan_statistik

while True:

    print("\n=== SISTEM E-VOTING MAHASISWA ===")
    print("1. Lihat Data Pemilih")
    print("2. Lihat Data Calon")
    print("3. Voting")
    print("4. Statistik")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        lihat_pemilih()

    elif pilihan == "2":
        lihat_calon()

    elif pilihan == "3":
        proses_voting()

    elif pilihan == "4":
        tampilkan_statistik()

    elif pilihan == "5":
        print("Program selesai")
        break

    else:
        print("Pilihan tidak valid!")