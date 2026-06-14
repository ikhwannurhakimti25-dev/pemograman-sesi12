import json

def lihat_pemilih():
    try:
        with open("data/pemilih.json", "r") as file:
            data = json.load(file)

        print("\n=== DATA PEMILIH ===")

        for pemilih in data:
            print(
                f"{pemilih['id']} - {pemilih['nama']} - {pemilih['jurusan']}"
            )

    except Exception as e:
        print("Terjadi kesalahan:", e)