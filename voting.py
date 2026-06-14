import json

def proses_voting():

    with open("data/pemilih.json", "r") as file:
        pemilih = json.load(file)

    with open("data/calon.json", "r") as file:
        calon = json.load(file)

    id_pemilih = input("Masukkan ID Pemilih : ")
    id_calon = input("Masukkan ID Calon : ")

    pemilih_ditemukan = None
    calon_ditemukan = None

    for p in pemilih:
        if p["id"] == id_pemilih:
            pemilih_ditemukan = p

    for c in calon:
        if c["id"] == id_calon:
            calon_ditemukan = c

    if pemilih_ditemukan is None:
        print("ID Pemilih tidak ditemukan!")
        return

    if calon_ditemukan is None:
        print("ID Calon tidak ditemukan!")
        return

    if pemilih_ditemukan["sudah_memilih"]:
        print("Pemilih sudah melakukan voting!")
        return

    calon_ditemukan["jumlah_suara"] += 1
    pemilih_ditemukan["sudah_memilih"] = True

    with open("data/pemilih.json", "w") as file:
        json.dump(pemilih, file, indent=4)

    with open("data/calon.json", "w") as file:
        json.dump(calon, file, indent=4)

    print("Voting berhasil!")