import json

def lihat_calon():

    with open("data/calon.json", "r") as file:
        data = json.load(file)

    print("\n=== DATA CALON ===")

    for calon in data:
        print(
            f"{calon['id']} - {calon['nama']}"
        )