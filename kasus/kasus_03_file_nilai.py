
try:
    with open("data/nilai.txt", "r", encoding="utf-8") as file:
        nilai = float(file.read().strip())
        print(f"Nilai yang dibaca: {nilai}")

except FileNotFoundError:
    print("File nilai.txt tidak ditemukan.")

except ValueError:
    print("Isi file harus berupa angka.")
