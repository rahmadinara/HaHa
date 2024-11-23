from banner import tampilkan_banner
from input_kondisi import input_data
from analisis_kesehatan import hitung_bmi, hitung_berat_ideal, cek_air, cek_tidur, cek_kesehatan, tampilkan_analisis
from klinik import tampilkan_klinik
from utils import validasi_input

def menu_utama():
    data_kesehatan = None
    while True:
        print("\nSilahkan Pilih Menu di Bawah Ini!")
        print("1. Pendataan Kondisi Tubuh dan Kegiatan")
        print("2. Analisis Kondisi Tubuh dan Kesehatan")
        print("3. Bantuan Profesional")
        print("4. Keluar")
        
        menu = validasi_input(input("Masukkan pilihan menu: "), int)
        
        if menu == 1:
            data_kesehatan = input_data()
        elif menu == 2:
            if data_kesehatan:
                tampilkan_analisis(data_kesehatan)
            else:
                print("Silakan input kondisi kesehatan terlebih dahulu (Opsi 1).")
        elif menu == 3:
            tampilkan_klinik()
        elif menu == 4:
            print("Keluar dari aplikasi. Tetap sehat!")
            break
        else:
            print("Menu tidak valid. Coba lagi.")

if __name__ == "__main__":
    tampilkan_banner()
    username = input("Masukkan nama Anda: ")
    print("Halo " + username + ", Selamat datang di Health Analytics and Habit Assistance")
    menu_utama()
