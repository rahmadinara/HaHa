klinik_jogja = {
    "jogja": [
        ("RSUD Kota Yogyakarta", "Jl. Ki Ageng Pemanahan No.1-6, Sorosutan, Kec. Umbulharjo, Kota Yogyakarta"),
        ("RS Bethesda", "Jl. Jend. Sudirman No.70, Kotabaru, Kec. Gondokusuman, Kota Yogyakarta"),
        ("RS Panti Rapih", "Jl. Cik Di Tiro No.30, Samirono, Terban, Kec. Gondokusuman, Kota Yogyakarta"),
        ("RS PKU Muhammadiyah", "Jl. KH. Ahmad Dahlan No.20, Ngupasan, Kec. Gondomanan, Kota Yogyakarta"),
        ("RS DKT Dr. Soetarto", "Jl. Juadi No.19, Kotabaru, Kec. Gondokusuman, Kota Yogyakarta")
    ],
    "bantul": [
        ("RSUD Panembahan Senopati", "Jl. Raya Janti Blok O Banguntapan, Kab. Bantul"),
        ("RSPAU Dr. Suhardi Harjolukito", "Jl. Dr. Wahidin Sudiro Husodo, Kab. Bantul"),
        ("RSU PKU Muhammadiyah Bantul", "Jl. Jenderal Sudirman 124, Kab. Bantul"),
        ("RS Universitas Islam Indonesia", "Jl. Srandakan KM 5,5 Wijirejo, Pandak, Kab. Bantul"),
        ("RSU Rachma Husada", "Jl Parangtritis Km.16 Gerselo, Patalan, Jetis, Kab. Bantul")
    ],
    "sleman": [
        ("RSUD Kabupaten Sleman", "Jl. Jl. Bhayangkara No.48, Temulawak, Triharjo, Kec. Sleman, Kab. Sleman"),
        ("RSUP Dr. Sardjito", "Jl. Kesehatan Sendowo No.1, Sendowo, Sinduadi, Kec. Mlati, Kab. Sleman"),
        ("RS JIH", "Jl. Ring Road Utara No.160, Perumnas Condong Catur, Kec. Depok, Kab. Sleman"),
        ("RS Akademik UGM", "Jl. Kabupaten, Kranggahan I, Trihanggo, Kec. Gamping, Kab. Sleman"),
        ("RSUD Prambanan", "Jl. Raya Piyungan - Prambanan No.KM. 7, Delegan, Sumberharjo, Kec. Prambanan, Kab. Sleman ")
    ],
    "gunungkidul": [
        ("RSUD Wonosari", "Jalan Taman Bhakti No. 6 Wonosari, Kab. Gunungkidul"),
        ("RSU Pelita Husada", "Jl. Raya Semanu Km 3. Sambirejo Semanu, Kab. Gunungkidul"),
        ("RSUD Saptosari", "Karang, Jetis, Saptosari, Kab. Gunungkidul"),
        ("RS Panti Rahayu", "Jl. Wonosari-Ponjong Km 7, Kelor, Karangmojo, Kab. Gunungkidul "),
        ("RS Nur Rohmah", "Jl. Wonosari-Jogja Km 7, Bandung, Playen, Kab. Gunungkidul")
    ],
    "kulonprogo": [
        ("RSUD Wates", "Jl. Tentara Pelajar KM 1 No 5, Beji, Kelurahan Wates, Kapanewon Wates, Kab. Kulon Progo"),
        ("RSU Santo Yusup Boro", "Boro, Kalurahan Banjarasri RT 001/RW 001, Kapanewon Kalibawang, Kab. Kulon Progo"),
        ("RS Umum Daerah Nyi Ageng Serang", "Jl. Sentolo Nanggulan, Bantar Kulon, Kalurahan Banguncipto, Kapanewon Sentolo, Kab. Kulon Progo"),
        ("RS Umum Kharisma Paramedika", "Jl. Khudori № 34, Dipan, Kelurahan Wates, Kapanewon Wates, Kab. Kulon Progo"),
        ("RS Umum Pura Raharja Medika", "Jl. Raya Brosot № 18, Bangeran, Kalurahan Bumirejo, Kapanewon Lendah, Kab. Kulon Progo")
    ]
}

def tampilkan_klinik():
    print("=== Pilih Lokasi ===")
    print("1. Jogja")
    print("2. Bantul")
    print("3. Sleman")
    print("4. Gunungkidul")
    print("5. Kulonprogo")
    
    pilihan = int(input("Masukkan pilihan lokasi: "))
    lokasi = None

    if pilihan == 1:
        lokasi = "jogja"
    elif pilihan == 2:
        lokasi = "bantul"
    elif pilihan == 3:
        lokasi = "sleman"
    elif pilihan == 4:
        lokasi = "gunungkidul"
    elif pilihan == 5:
        lokasi = "kulonprogo"
    else:
        print("Pilihan tidak valid!")
        return

    print(f"\n=== 5 Klinik Terbaik di {lokasi.capitalize()} ===")
    for klinik, alamat in klinik_jogja[lokasi]:
        print(f"- {klinik}\n  Alamat: {alamat}")