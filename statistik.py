import json

def tampilkan_statistik():

    with open("data/pemilih.json", "r") as file:
        pemilih = json.load(file)

    with open("data/calon.json", "r") as file:
        calon = json.load(file)

    total_pemilih = len(pemilih)

    sudah_memilih = 0

    for p in pemilih:
        if p["sudah_memilih"]:
            sudah_memilih += 1

    belum_memilih = total_pemilih - sudah_memilih

    if total_pemilih > 0:
        partisipasi = (sudah_memilih / total_pemilih) * 100
    else:
        partisipasi = 0

    pemenang = max(calon, key=lambda x: x["jumlah_suara"])

    print("\n=== STATISTIK VOTING ===")
    print(f"Total Pemilih : {total_pemilih}")
    print(f"Sudah Memilih : {sudah_memilih}")
    print(f"Belum Memilih : {belum_memilih}")
    print(f"Partisipasi : {partisipasi:.2f}%")
    print(
        f"Pemenang Sementara : {pemenang['nama']} ({pemenang['jumlah_suara']} suara)"
    )