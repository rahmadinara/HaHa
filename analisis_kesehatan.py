# Fungsi untuk menghitung BMI
def hitung_bmi(berat, tinggi):
    bmi = berat / ((tinggi / 100) ** 2)
    if bmi < 18.5:
        return bmi, "Underweight"
    elif 18.5 <= bmi < 24.9:
        return bmi, "Normal"
    else:
        return bmi, "Overweight"

# Fungsi untuk menghitung berat badan ideal
def hitung_berat_ideal(gender, tinggi):
    if gender == "perempuan":
        berat_ideal = (tinggi - 100) - ((tinggi - 100) * 0.15)
    elif gender == "laki-laki" or "laki" or "laki laki":
        berat_ideal = (tinggi - 100) - ((tinggi - 100) * 0.10)
    else:
        return None  # Jika gender tidak valid
    return berat_ideal

# Fungsi untuk mengecek konsumsi air harian
def cek_air(air, berat):
    air_diperlukan = berat * 0.033
    if air >= air_diperlukan:
        return "Cukup", 0  
    else:
        return "Kurang", air_diperlukan - air

# Fungsi untuk mengecek durasi tidur
def cek_tidur(tidur):
    if 7 <= tidur <= 9:
        return "Cukup"
    else:
        return "Kurang"

# Fungsi untuk mengecek Kesehatan secara keseluruhan
def cek_kesehatan(status_bmi, status_air, status_tidur, status_kegiatan):
    # Hitung jumlah kondisi yang memenuhi syarat
    kondisi_tercukupi = 0
    
    if status_air == "Cukup":
        kondisi_tercukupi += 1
    if status_tidur == "Cukup":
        kondisi_tercukupi += 1
    if status_kegiatan >= 3:
        kondisi_tercukupi += 1

    if status_bmi == "Normal":
        return "Fit" if kondisi_tercukupi >= 2 else "Tidak Fit"
    elif status_bmi == "Overweight":
        return "Fit" if kondisi_tercukupi == 3 else "Tidak Fit"
    elif status_bmi == "Underweight":
        return "Tidak Fit" if kondisi_tercukupi <= 2 and status_kegiatan >= 3 else "Fit"
    else:
        return "Bingung"

#Fungsi untuk menampilkan analisis kesehatan
def tampilkan_analisis(data):
    print("\n=== Analisis Kondisi Kesehatan ===")
    bmi, status_bmi = hitung_bmi(data["berat"], data["tinggi"])
    berat_ideal = hitung_berat_ideal(data["gender"], data["tinggi"])
    selisih_berat = data["berat"] - berat_ideal if status_bmi == "Underweight" else berat_ideal - data["berat"]
    status_air, kekurangan_air = cek_air(data["air"], data["berat"])
    status_tidur = cek_tidur(data["tidur"])
    status_kesehatan = cek_kesehatan(status_bmi, status_air, status_tidur, data["kegiatan"])
    
    print(f"Nama: {data['nama']}")
    print(f"Umur: {data['umur']} tahun")
    print(f"Jenis Kelamin: {data['gender']}")
    print(f"BMI: {bmi:.2f} ({status_bmi})")
    print(f"Konsumsi Air: {status_air}")
    print(f"Durasi Tidur: {status_tidur}")
    print(f"Kesehatan Keseluruhan: {status_kesehatan}")

    print("\n=== Saran ===")
    if status_bmi == "Normal":
        print("1. Pertahankan berat badan Anda yang ideal.")
    elif status_bmi == "Underweight":
        print(f"1. Naikkan berat badan Anda sebanyak {abs(selisih_berat)} kg.")
    else:
        print(f"1. Turunkan berat badan Anda sebanyak {abs(selisih_berat)} kg.")

    if status_air == "Cukup":
        print("2. Keep going, tetap jaga minum Anda.")
    else:
        print(f"2. Tambahkan jumlah konsumsi air Anda sebanyak {kekurangan_air:.2f} liter.")

    if status_tidur == "Cukup":
        print("3. Tetap pertahankan jam tidur Anda.")
    elif status_tidur == "Kurang":
        print("3. Kurang tidur tidak baik untuk kesehatan.")
    else:
        print("3. Terlalu banyak tidur akan membuat Anda tidak fit.")

    print("== Tetap jaga kondisi Anda agar Anda tetap fit ==")