Warna_Gelang = {
    "hitam" : 0,
    "coklat" : 1,
    "merah" : 2,
    "oranye" : 3,
    "kuning" : 4,
    "hijau" : 5,
    "biru" : 6,
    "violet" : 7,
    "abu-abu" : 8,
    "putih" : 9
}

Warna_Gelang_Pengali = {
    "silver" : 0.01,
    "emas" : 0.1,
    "hitam" : 1,
    "coklat" : 10,
    "merah" : 100,
    "oranye" : 1000,
    "kuning" : 10000,
    "hijau" : 100000,
    "biru" : 1000000,
    "violet" : 10000000,
    "abu-abu" : 100000000,
    "putih" : 1000000000
}

print("=== Kalkulator Resistor 4 Gelang ===")
print("Ketik Sesuai dengan Template di Bawah ini!")
print("hitam, coklat, merah, oranye, kuning, hijau, biru, violet, abu-abu, putih. silver dan emas (tambahan warna pengali)")

print("======================================")
Gelang1 = input("\nMasukkan Warna Gelang 1 = ").lower()
Gelang2 = input("Masukkan Warna Gelang 2 = ").lower()
Gelang3 = input("Masukkan Warna Gelang 3 (Pengali) = ").lower()

Angka1 = Warna_Gelang[Gelang1]
Angka2 = Warna_Gelang[Gelang2]
Pengali = Warna_Gelang_Pengali[Gelang3]

Nilai_Resistor = ((Angka1 * 10) + Angka2) * Pengali
print("==============================================")
print("Nilai Resistor adalah", Nilai_Resistor, "Ohm")
