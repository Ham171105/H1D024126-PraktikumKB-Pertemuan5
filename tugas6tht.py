import tkinter as tk
from tkinter import messagebox, ttk

class AppSistemPakarTHT:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistem Pakar Diagnosa THT - Berbasis Modul")
        self.root.geometry("600x700")

        self.basis_pengetahuan = {
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
            "Kanker Nasofaring": ["G17", "G8"],
            "Kanker Tonsil": ["G6", "G29"],
            "Neuronitis Vestibularis": ["G35", "G24"],
            "Meniere": ["G20", "G35", "G14", "G4"],
            "Tumor Syaraf Pendengaran": ["G12", "G34", "G23"],
            "Kanker Leher Metastatik": ["G29"],
            "Osteosklerosis": ["G34", "G9"],
            "Vertigo Postular": ["G24"]
        }

        self.gejala_info = {
            "G1": "Nafas abnormal", "G2": "Suara serak", "G3": "Perubahan kulit", "G4": "Telinga penuh",
            "G5": "Nyeri bicara menelan", "G6": "Nyeri tenggorokan", "G7": "Nyeri leher", "G8": "Pendarahan hidung",
            "G9": "Telinga berdenging", "G10": "Airliur menetes", "G11": "Perubahan suara", "G12": "Sakit kepala",
            "G13": "Nyeri pinggir hidung", "G14": "Serangan vertigo", "G15": "Getah bening", "G16": "Leher bengkak",
            "G17": "Hidung tersumbat", "G18": "Infeksi sinus", "G19": "Beratbadan turun", "G20": "Nyeri telinga",
            "G21": "Selaput lendir merah", "G22": "Benjolan leher", "G23": "Tubuh tak seimbang", "G24": "Bolamata bergerak",
            "G25": "Nyeri wajah", "G26": "Dahi sakit", "G27": "Batuk", "G28": "Tumbuh dimulut", "G29": "Benjolan dileher",
            "G30": "Nyeri antara mata", "G31": "Radang gendang telinga", "G32": "Tenggorokan gatal", "G33": "Hidung meler",
            "G34": "Tuli", "G35": "Mual muntah", "G36": "Letih lesu", "G37": "Demam"
        }

        self.vars = {}
        self.setup_ui()

    def setup_ui(self):
        header = tk.Frame(self.root, bg="#3498db", pady=10)
        header.pack(fill="x")
        tk.Label(header, text="Sistem Pakar Diagnosa THT", font=("Arial", 16, "bold"), bg="#3498db", fg="white").pack()
        tk.Label(header, text="Centang gejala yang Anda rasakan di bawah ini:", bg="#3498db", fg="white").pack()

        main_frame = tk.Frame(self.root)
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        canvas = tk.Canvas(main_frame)
        scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        for kode in sorted(self.gejala_info.keys(), key=lambda x: int(x[1:])):
            nama = self.gejala_info[kode]
            var = tk.BooleanVar()
            cb = tk.Checkbutton(scrollable_frame, text=f"[{kode}] {nama}", variable=var, font=("Arial", 10))
            cb.pack(anchor="w", pady=2)
            self.vars[kode] = var

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        btn_frame = tk.Frame(self.root, pady=10)
        btn_frame.pack(fill="x")
        
        btn_diagnosa = tk.Button(btn_frame, text="DIAGNOSA SEKARANG", command=self.proses_diagnosa, 
                                 bg="#2ecc71", fg="white", font=("Arial", 12, "bold"), pady=10)
        btn_diagnosa.pack(fill="x", padx=20)

    def proses_diagnosa(self):
        gejala_user = [kode for kode, var in self.vars.items() if var.get()]
        
        if not gejala_user:
            messagebox.showwarning("Peringatan", "Silakan pilih minimal satu gejala untuk memulai diagnosa!")
            return

        hasil = []
        for penyakit, list_gejala in self.basis_pengetahuan.items():
            cocok = set(gejala_user) & set(list_gejala)
            if cocok:
                persentase = (len(cocok) / len(list_gejala)) * 100
                hasil.append((penyakit, persentase))

        hasil.sort(key=lambda x: x[1], reverse=True)

        if not hasil:
            messagebox.showinfo("Hasil Diagnosa", "Maaf, gejala yang Anda pilih tidak cocok dengan data penyakit kami.")
        else:
            teks_hasil = "Kemungkinan Diagnosa Anda:\n\n"
            for p, s in hasil[:5]: # Ambil 5 teratas
                teks_hasil += f"• {p}: {s:.2f}%\n"
            
            teks_hasil += "\n*Segera periksa ke dokter jika gejala berlanjut."
            messagebox.showinfo("Hasil Analisis Sistem Pakar", teks_hasil)

if __name__ == "__main__":
    root = tk.Tk()
    app = AppSistemPakarTHT(root)
    root.mainloop()