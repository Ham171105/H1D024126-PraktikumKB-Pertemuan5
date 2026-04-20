def diagnosa_tht(): 
    basis_pengetahuan = {
        "Tonsilitis": ["G37", "G12", "G5", "G27", "G6", "G21"],
        "Sinusitis Maksilaris": ["G37", "G12", "G27", "G17", "G33", "G36", "G29"],
        "Sinusitis Frontalis": ["G37", "G12", "G27", "G17", "G33", "G36", "G21", "G26"],
        "Sinusitis Edmoidalis": ["G37", "G12", "G27", "G17", "G33", "G36", "G21", "G30", "G13", "G26"],
        "Sinusitis Sfenoidalis": ["G37", "G12", "G27", "G17", "G33", "G36", "G29", "G7"],
        "Abses Peritonsiler": ["G37", "G12", "G6", "G15", "G2", "G29", "G10"],
        "Faringitis": ["G37", "G5", "G6", "G7", "G15"],
        "Kanker Laring": ["G5", "G27", "G6", "G15", "G2", "G19", "G1"],
        "Deviasi Septum": ["G37", "G17", "G20", "G8", "G18", "G25"],
        "Laringitis": ["G37", "G5", "G15", "G16", "G32"],
        "Kanker Leher & Kepala": ["G5", "G22", "G8", "G28", "G3", "G11"],
        "Otitis Media Akut": ["G37", "G20", "G35", "G31"],
        "Contact Ulcers": ["G5", "G2"],
        "Abses Parafaringeal": ["G5", "G16"],
        "Barotitis Media": ["G12", "G20"],
        "Kanker Nafasoring": ["G17", "G8"],
        "Kanker Tonsil": ["G6", "G29"],
        "Neuronitis Vestibularis": ["G35", "G24"],
        "Meniere": ["G20", "G35", "G14", "G4"],
        "Tumor Syaraf Pendengaran": ["G12", "G34", "G23"],
        "Kanker Leher Metastatik": ["G29"],
        "Osteosklerosis": ["G34", "G9"],
        "Vertigo Postular": ["G24"]
    }
 
    gejala_list = {
        "G1": "Nafas abnormal", "G2": "Suara serak", "G3": "Perubahan kulit",
        "G5": "Nyeri bicara menelan", "G6": "Nyeri tenggorokan", "G8": "Pendarahan hidung",
        "G12": "Sakit kepala", "G17": "Hidung tersumbat", "G20": "Nyeri telinga",
        "G29": "Benjolan di leher", "G37": "Demam" 
    }

    print("=== Sistem Pakar Diagnosa Penyakit THT ===")
    print("Jawablah pertanyaan berikut dengan (y/n):")
    
    gejala_user = []
    for kode, info in gejala_list.items():
        tanya = input(f"Apakah Anda mengalami {info} ({kode})? ").lower()
        if tanya == 'y':
            gejala_user.append(kode)

    hasil_diagnosa = []
    for penyakit, gejala_penyakit in basis_pengetahuan.items():
        match_count = len(set(gejala_user) & set(gejala_penyakit))
        if match_count > 0:
            persentase = (match_count / len(gejala_penyakit)) * 100
            hasil_diagnosa.append((penyakit, persentase))

    print("\n--- Hasil Diagnosa ---")
    if not hasil_diagnosa:
        print("Penyakit tidak ditemukan berdasarkan gejala yang diberikan.")
    else:
        hasil_diagnosa.sort(key=lambda x: x[1], reverse=True)
        for p, skor in hasil_diagnosa:
            print(f"- {p}: Tingkat kecocokan {skor:.2f}%")

if __name__ == "__main__":
    diagnosa_tht()