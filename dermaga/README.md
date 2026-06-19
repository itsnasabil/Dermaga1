# ⚓ DERMAGA
**Dashboard Elektronik Magang BPS Kota Semarang**

Website berbasis Streamlit yang mereplikasi dan meningkatkan fitur dari [situs resmi DERMAGA](https://sites.google.com/view/dermaga-bps-kota-semarang/halaman-muka).

---

## 🗂️ Struktur Halaman

| Halaman | Deskripsi |
|---|---|
| 🏠 Halaman Muka | Beranda, pengumuman, alur magang |
| 📝 Pendaftaran | Form pendaftaran, persyaratan, langkah daftar, rekap |
| 📁 Berkas Pendaftaran | Download surat pengantar, form permohonan, CV |
| 🗂️ Pelaksanaan | Absensi, folder laporan, penilaian, rekap nilai, panduan, dokumentasi |

---

## 🚀 Cara Menjalankan

### 1. Siapkan lingkungan Python

```bash
cd dermaga
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Jalankan aplikasi

```bash
streamlit run Halaman_Muka.py
```

Aplikasi akan terbuka otomatis di browser: `http://localhost:8501`

---

## 📁 Struktur File

```
dermaga/
├── Halaman_Muka.py          # Halaman utama (entry point)
├── utils.py                 # Komponen & CSS bersama
├── app.py                   # Entry alias
├── requirements.txt
├── .streamlit/
│   └── config.toml          # Konfigurasi tema
└── pages/
    ├── 1_Pendaftaran.py     # Halaman pendaftaran
    ├── 2_Berkas_Pendaftaran.py  # Download berkas
    └── 3_Pelaksanaan.py     # Pelaksanaan magang
```

---

## 🔗 Tautan Eksternal Terintegrasi

Semua tautan dari website asli terintegrasi dalam aplikasi ini:

- 📋 Form Pendaftaran (Google Form)
- 📊 Rekap Data Pendaftar (Google Sheets)
- 📁 Berkas Pendaftaran (Google Docs)
- ✅ Absensi Harian (Google Form)
- 📂 Folder Laporan (Google Drive)
- ⭐ Form Penilaian (Google Form)
- 📊 Rekap Nilai (Google Sheets)
- 📖 Panduan Magang (Google Docs)
- 📸 Dokumentasi (Google Drive)
- 📊 Rekap Absensi (Google Sheets)

---

## 🎨 Desain

- Warna utama: Biru BPS (#003F88)
- Sidebar navigasi interaktif
- Responsive & mobile-friendly
- Kartu interaktif dengan hover effects
- Konsisten dengan identitas BPS Kota Semarang

---

*© 2025 BPS Kota Semarang. Dibuat untuk program DERMAGA.*
