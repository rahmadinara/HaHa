from utils import validasi_input

def validasi_input(input_value, expected_type, error_message="Input salah"):
    try:
        return expected_type(input_value)
    except ValueError:
        print(error_message)
        return None

# Fungsi menu 1 input data
def input_data():
    print("=== Form Input Kondisi Kesehatan ===")
    
    # Input Nama
    nama = input("Nama: ")
    
    # Input Umur
    while True:
        umur = validasi_input(input("Umur: "), int)
        if umur is not None and 0 <= umur <= 100:
            break
        print("Umur harus berupa angka yang valid (0-100).")

    # Input Gender
    while True:
        gender = validasi_input(input("Jenis Kelamin (Laki-laki/Perempuan): "), str)
        if gender is not None and gender in ["laki-laki", "laki laki", "laki", "perempuan"]:
            break
        else:
            print("Jenis kelamin harus valid (Laki-laki atau Perempuan).")
    
    # Validasi tinggi badan
    while True:
        tinggi = validasi_input(input("Tinggi Badan (cm): "), float)
        if tinggi is not None and 140 <= tinggi <= 200:
            break
        else:
            print("Input tinggi badan harus valid (140-200 cm).")

    # Validasi berat badan
    while True:
        berat = validasi_input(input("Berat Badan (kg): "), float)
        if berat is not None and 30 <= berat <= 150:
            break
        else:
            print("Input berat badan harus valid (30-150 kg).")

    # Input Konsumsi Air
    while True:
        air = validasi_input(input("Konsumsi Air Harian (liter): "), float)
        if air is not None and 0 <= air <= 20:
            break
        print("Konsumsi air harus valid")

    # Input Intensitas Kegiatan
    while True:
        print("1. Tidak Intens")
        print("2. Kurang Intens")
        print("3. Sedang")
        print("4. Cukup Intens")
        print("5. Sangat Intens")
        kegiatan = validasi_input(input("Tingkat Intensitas Kegiatan (1-5): "), int)
        if kegiatan is not None and 1 <= kegiatan <= 5:
            break
        print("Intensitas kegiatan harus berupa angka antara 1 hingga 5.")
    
    # Input Durasi Tidur
    while True:
        tidur = validasi_input(input("Durasi Tidur (jam): "), float)
        if tidur is not None and 0 <= tidur <= 24:
            break
        print("Durasi tidur harus berupa angka.")
    
    # Return data kesehatan jika semua input valid
    return {
        "nama": nama,
        "umur": umur,
        "gender": gender,
        "tinggi": tinggi,
        "berat": berat,
        "air": air,
        "kegiatan": kegiatan,
        "tidur": tidur
    }
