def hitung_luas(panjang, lebar, satuan):
    # Menghitung luas
    luas = panjang * lebar
    return luas, satuan

panjang = float(input("Masukkan panjang ruangan: "))
lebar = float(input("Masukkan lebar ruangan: "))

print("Pilih satuan (m untuk meter, in untuk inci): ")
satuan = input("Masukkan satuan (m/in): ").lower()

if satuan == "m":
    luas, satuan = hitung_luas(panjang, lebar, "meter")
    print(f"Luas ruangan adalah {luas} meter persegi.")
elif satuan == "in":
    luas, satuan = hitung_luas(panjang, lebar, "inci")
    print(f"Luas ruangan adalah {luas} inci persegi.")
else:
    print("Satuan tidak valid. Gunakan 'm' untuk meter atau 'in' untuk inci.")