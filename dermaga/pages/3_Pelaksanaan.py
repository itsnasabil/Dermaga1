import streamlit as st
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from utils import set_page_config, render_header, render_footer
from assets import LOGO_DERMAGA_B64

set_page_config()

st.markdown("""
<style>
.page-hero {
    position:relative; border-radius:20px; overflow:hidden;
    background:linear-gradient(135deg,#3B0764 0%,#6D28D9 50%,#8B5CF6 100%);
    padding:38px 36px 34px; margin-bottom:26px;
    box-shadow:0 8px 36px rgba(109,40,217,0.28);
    display:flex; align-items:center; gap:22px; min-height:130px;
}
.page-hero-bg { position:absolute; right:-20px; top:50%; transform:translateY(-50%);
                opacity:0.1; filter:brightness(10); width:170px; }
.page-hero-text h1 { color:white; margin:0 0 6px; font-size:1.9rem; font-weight:900; z-index:1; position:relative; }
.page-hero-text p { color:rgba(255,255,255,0.82); margin:0; font-size:0.9rem; z-index:1; position:relative; }

.section-title {
    font-size:1.2rem; font-weight:800; color:#002966; margin:8px 0 16px;
    display:flex; align-items:center; gap:10px;
}
.section-title::after {
    content:''; flex:1; height:2.5px;
    background:linear-gradient(90deg,#003F88 0%,#F97316 50%,transparent 100%); border-radius:2px;
}

/* feature card */
.fc {
    background:white; border-radius:18px; padding:26px 20px;
    box-shadow:0 5px 22px rgba(0,0,0,0.08); border-top:5px solid;
    text-align:center; transition:all 0.25s; height:100%;
}
.fc:hover { transform:translateY(-4px); box-shadow:0 10px 36px rgba(0,0,0,0.13); }
.fc-num {
    width:32px; height:32px; border-radius:50%;
    display:inline-flex; align-items:center; justify-content:center;
    font-size:0.82rem; font-weight:800; color:white;
    margin-bottom:10px;
}
.fc-icon { font-size:2.8rem; margin-bottom:8px; display:block; }
.fc-badge {
    display:inline-block; padding:3px 10px; border-radius:20px;
    font-size:0.7rem; font-weight:700; margin-bottom:12px;
}
.fc-title { font-size:1rem; font-weight:800; margin:0 0 8px; }
.fc-desc { font-size:0.8rem; color:#555; margin:0 0 16px; line-height:1.65; }
.fc-btn {
    display:block; width:100%; padding:11px 16px; border-radius:10px;
    font-weight:700; font-size:0.84rem; text-decoration:none;
    text-align:center; color:white !important; transition:all 0.2s;
    box-shadow:0 3px 10px rgba(0,0,0,0.14);
}
.fc-btn:hover { opacity:0.9; transform:translateY(-1px); color:white !important; }

/* doc link */
.doc-lnk {
    display:flex; align-items:center; gap:12px;
    background:white; border-radius:12px; padding:14px 16px; margin-bottom:10px;
    box-shadow:0 2px 10px rgba(0,0,0,0.06); text-decoration:none; color:#222;
    transition:all 0.2s; border-left:4px solid;
}
.doc-lnk:hover { transform:translateX(4px); }
.doc-lnk-icon { font-size:1.5rem; }
.doc-lnk-title { font-weight:700; font-size:0.88rem; margin:0 0 2px; }
.doc-lnk-desc { font-size:0.76rem; color:#666; margin:0; }
.doc-lnk-arrow { margin-left:auto; color:#aaa; }

/* tata tertib */
.tt-item {
    background:white; border-radius:10px; padding:11px 14px;
    margin-bottom:8px; display:flex; gap:12px; align-items:flex-start;
    box-shadow:0 2px 8px rgba(0,0,0,0.05); border-left:4px solid;
}
.tt-num {
    width:26px; height:26px; min-width:26px; border-radius:50%;
    display:flex; align-items:center; justify-content:center;
    font-size:0.76rem; font-weight:800; color:white;
}
.tt-text { font-size:0.84rem; color:#333; line-height:1.5; padding-top:3px; }

/* info alert */
.ia {
    border-radius:12px; padding:15px 18px; margin-bottom:12px;
    display:flex; gap:12px; align-items:flex-start;
}
.ia-icon { font-size:1.4rem; }
.ia-title { font-weight:700; margin:0 0 3px; font-size:0.88rem; }
.ia-body { margin:0; font-size:0.8rem; line-height:1.55; }
</style>
""", unsafe_allow_html=True)

render_header()

# ── HERO ─────────────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="page-hero">
  <img class="page-hero-bg" src="data:image/png;base64,{LOGO_DERMAGA_B64}" alt="" />
  <div style="font-size:3.2rem; z-index:1;">🗂️</div>
  <div class="page-hero-text">
    <h1>Pelaksanaan Magang</h1>
    <p>Absensi harian, folder laporan, laporan kegiatan harian, rekap kegiatan, laporan akhir & dokumentasi magang</p>
  </div>
</div>
""", unsafe_allow_html=True)

# ── 6 FITUR (urutan sesuai link asli) ────────────────────────────────────────
# Urutan dari link pelaksanaan:
# 1. Form Absensi  2. Folder Laporan  3. Laporan Kegiatan Harian (Form Penilaian)
# 4. Rekap Kegiatan Harian  5. Laporan Akhir Magang (Panduan)  6. Sheets Kegiatan Magang Mahasiswa  7. Folder Dokumentasi
# → 7 fitur, baris 3+3+1

st.markdown('<div class="section-title">🎯 Fitur Pelaksanaan Magang</div>', unsafe_allow_html=True)

features = [
    # (nomor, warna, grad, icon, badge_bg, badge_color, label_badge, title, desc, btn_label, url)
    ("1","#003F88","linear-gradient(135deg,#003F88,#0058BF)","✅",
     "#EFF6FF","#1D4ED8","HARIAN",
     "Absensi Harian",
     "Isi absensi kehadiran setiap hari kerja. Wajib diisi setiap pagi sebelum memulai kegiatan magang.",
     "✅ Isi Absensi Sekarang",
     "https://docs.google.com/forms/d/e/1FAIpQLSfy37MhTvDVGGCklo_QNwgvut4g2xwo4jLEPIjQAn23QTTpRw/viewform"),
    ("2","#059669","linear-gradient(135deg,#059669,#10B981)","📂",
     "#ECFDF5","#166534","LAPORAN",
     "Folder Laporan Magang",
     "Upload dan akses laporan harian magang melalui Google Drive yang telah disediakan oleh BPS.",
     "📂 Buka Folder Laporan",
     "https://drive.google.com/drive/folders/1kpU5Quxk2dmevFnaKqw9ryvzKyCz5weL"),
    ("3","#D97706","linear-gradient(135deg,#D97706,#F59E0B)","📓",
     "#FFFBEB","#92400E","HARIAN",
     "Laporan Kegiatan Harian",
     "Form laporan kegiatan harian yang wajib diisi peserta magang sebagai bukti aktivitas dan progress setiap hari.",
     "📓 Isi Laporan Kegiatan",
     "https://docs.google.com/forms/d/e/1FAIpQLSdLIjIjeB_gZqv9CbkIEqku6jpEZpyPNjInTecm9uk3GfK_vQ/viewform"),
    ("4","#DC2626","linear-gradient(135deg,#DC2626,#EF4444)","📊",
     "#FEF2F2","#B91C1C","REKAP",
     "Rekap Kegiatan Harian",
     "Spreadsheet rekapitulasi kegiatan harian dan evaluasi seluruh peserta magang BPS Kota Semarang.",
     "📊 Lihat Rekap Kegiatan",
     "https://docs.google.com/spreadsheets/d/15v0VIzoLXIH0ub3HKd17vNlq-b6gOqtM4m6QiMin0oM/edit?usp=sharing"),
    ("5","#7C3AED","linear-gradient(135deg,#7C3AED,#8B5CF6)","📄",
     "#F5F3FF","#6D28D9","AKHIR",
     "Laporan Akhir Magang",
     "Dokumen laporan akhir magang yang wajib diselesaikan dan dikumpulkan oleh peserta di akhir periode.",
     "📄 Buka Laporan Akhir",
     "https://docs.google.com/document/d/1SpKCjlPpXwIlmsC3XmGBjXpeBCl01hx4/edit?usp=sharing"),
    ("6","#0891B2","linear-gradient(135deg,#0891B2,#06B6D4)","📋",
     "#ECFEFF","#164E63","SHEETS",
     "Sheets Kegiatan Magang Mahasiswa",
     "Spreadsheet kegiatan magang mahasiswa yang mencatat seluruh aktivitas dan progress selama magang berlangsung.",
     "📋 Buka Sheets Kegiatan",
     "https://docs.google.com/spreadsheets/d/1h10vFhh64ecM8-_pQCAMFly3YwdvrN2hchbivnr-v4o/edit?gid=17043618#gid=17043618"),
    ("7","#BE185D","linear-gradient(135deg,#BE185D,#EC4899)","📸",
     "#FDF2F8","#9D174D","DOKUMENTASI",
     "Folder Dokumentasi",
     "Kumpulan foto dan dokumentasi kegiatan magang BPS Kota Semarang sepanjang periode berlangsung.",
     "📸 Buka Dokumentasi",
     "https://drive.google.com/drive/folders/1lczKeEN6xRNihyNVNnql3MSX1DTu63e4"),
]

# Row 1: fitur 1-3
r1c1, r1c2, r1c3 = st.columns(3)
for col, (num, color, grad, icon, bkgb, bkgc, badge, title, desc, btn, url) in zip([r1c1,r1c2,r1c3], features[:3]):
    with col:
        st.markdown(f"""
        <div class="fc" style="border-top-color:{color};">
          <div class="fc-num" style="background:{color};">{num}</div>
          <span class="fc-icon">{icon}</span>
          <span class="fc-badge" style="background:{bkgb}; color:{bkgc};">{badge}</span>
          <div class="fc-title" style="color:{color};">{title}</div>
          <div class="fc-desc">{desc}</div>
          <a class="fc-btn" style="background:{grad};" href="{url}" target="_blank">{btn}</a>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Row 2: fitur 4-6
r2c1, r2c2, r2c3 = st.columns(3)
for col, (num, color, grad, icon, bkgb, bkgc, badge, title, desc, btn, url) in zip([r2c1,r2c2,r2c3], features[3:6]):
    with col:
        st.markdown(f"""
        <div class="fc" style="border-top-color:{color};">
          <div class="fc-num" style="background:{color};">{num}</div>
          <span class="fc-icon">{icon}</span>
          <span class="fc-badge" style="background:{bkgb}; color:{bkgc};">{badge}</span>
          <div class="fc-title" style="color:{color};">{title}</div>
          <div class="fc-desc">{desc}</div>
          <a class="fc-btn" style="background:{grad};" href="{url}" target="_blank">{btn}</a>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Row 3: fitur 7 centered
_, r3c, _ = st.columns([1, 1, 1])
num, color, grad, icon, bkgb, bkgc, badge, title, desc, btn, url = features[6]
with r3c:
    st.markdown(f"""
    <div class="fc" style="border-top-color:{color};">
      <div class="fc-num" style="background:{color};">{num}</div>
      <span class="fc-icon">{icon}</span>
      <span class="fc-badge" style="background:{bkgb}; color:{bkgc};">{badge}</span>
      <div class="fc-title" style="color:{color};">{title}</div>
      <div class="fc-desc">{desc}</div>
      <a class="fc-btn" style="background:{grad};" href="{url}" target="_blank">{btn}</a>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── TATA TERTIB + LINK CEPAT ──────────────────────────────────────────────────
cl, cr = st.columns([1, 1])

with cl:
    st.markdown('<div class="section-title">📋 Tata Tertib Magang</div>', unsafe_allow_html=True)
    rules = [
        ("Hadir tepat waktu sesuai jam kerja BPS (07.30 – 16.00 WIB)", "#003F88"),
        ("Berpakaian rapi dan sopan sesuai ketentuan instansi", "#059669"),
        ("Mengisi absensi harian sebelum memulai kegiatan magang", "#D97706"),
        ("Mengisi laporan kegiatan harian setiap hari kerja", "#DC2626"),
        ("Menjaga kerahasiaan data dan dokumen BPS", "#7C3AED"),
        ("Tidak meninggalkan kantor tanpa izin pembimbing lapangan", "#0891B2"),
        ("Membuat laporan akhir magang sesuai format yang ditetapkan", "#BE185D"),
        ("Berlaku sopan dan profesional kepada seluruh pegawai BPS", "#D97706"),
        ("Upload laporan & dokumentasi ke folder Drive yang disediakan", "#059669"),
        ("Menyelesaikan semua tugas dan administrasi sebelum akhir periode", "#003F88"),
    ]
    colors_cycle = [r[1] for r in rules]
    for i, (rule, color) in enumerate(rules, 1):
        st.markdown(f"""
        <div class="tt-item" style="border-left-color:{color};">
          <div class="tt-num" style="background:{color};">{i}</div>
          <div class="tt-text">{rule}</div>
        </div>
        """, unsafe_allow_html=True)

with cr:
    st.markdown('<div class="section-title">🔗 Semua Tautan Pelaksanaan</div>', unsafe_allow_html=True)
    doclinks = [
        ("✅","#003F88","Absensi Harian",
         "Isi setiap hari kerja — WAJIB!",
         "https://docs.google.com/forms/d/e/1FAIpQLSfy37MhTvDVGGCklo_QNwgvut4g2xwo4jLEPIjQAn23QTTpRw/viewform"),
        ("📂","#059669","Folder Laporan Magang",
         "Simpan laporan harian & mingguan di sini",
         "https://drive.google.com/drive/folders/1kpU5Quxk2dmevFnaKqw9ryvzKyCz5weL"),
        ("📓","#D97706","Laporan Kegiatan Harian",
         "Form laporan kegiatan wajib diisi harian",
         "https://docs.google.com/forms/d/e/1FAIpQLSdLIjIjeB_gZqv9CbkIEqku6jpEZpyPNjInTecm9uk3GfK_vQ/viewform"),
        ("📊","#DC2626","Rekap Kegiatan Harian",
         "Spreadsheet rekap kegiatan seluruh peserta",
         "https://docs.google.com/spreadsheets/d/15v0VIzoLXIH0ub3HKd17vNlq-b6gOqtM4m6QiMin0oM/edit?usp=sharing"),
        ("📄","#7C3AED","Laporan Akhir Magang",
         "Dokumen laporan akhir wajib dikumpulkan",
         "https://docs.google.com/document/d/1SpKCjlPpXwIlmsC3XmGBjXpeBCl01hx4/edit?usp=sharing"),
        ("📋","#0891B2","Sheets Kegiatan Magang Mahasiswa",
         "Rekap lengkap kegiatan magang mahasiswa",
         "https://docs.google.com/spreadsheets/d/1h10vFhh64ecM8-_pQCAMFly3YwdvrN2hchbivnr-v4o/edit?gid=17043618#gid=17043618"),
        ("📸","#BE185D","Folder Dokumentasi",
         "Upload foto & dokumentasi kegiatan magang",
         "https://drive.google.com/drive/folders/1lczKeEN6xRNihyNVNnql3MSX1DTu63e4"),
    ]
    for icon, color, title, desc, url in doclinks:
        st.markdown(f"""
        <a class="doc-lnk" href="{url}" target="_blank" style="border-left-color:{color};">
          <div class="doc-lnk-icon">{icon}</div>
          <div>
            <div class="doc-lnk-title" style="color:{color};">{title}</div>
            <div class="doc-lnk-desc">{desc}</div>
          </div>
          <div class="doc-lnk-arrow">→</div>
        </a>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── INFO PENTING ──────────────────────────────────────────────────────────────
st.markdown('<div class="section-title">⚠️ Informasi Penting Pelaksanaan</div>', unsafe_allow_html=True)
ia1, ia2 = st.columns(2)
infos_l = [
    ("#EFF6FF","#93C5FD","#1D4ED8","#1E40AF","📅",
     "Absensi Wajib Setiap Hari",
     "Peserta wajib mengisi form absensi setiap hari kerja (Senin–Jumat). Ketidakhadiran tanpa keterangan memengaruhi penilaian akhir."),
    ("#ECFDF5","#86EFAC","#166534","#14532D","📓",
     "Laporan Kegiatan Harian",
     "Isi form laporan kegiatan setiap hari. Upload laporan ke folder Drive yang disediakan paling lambat setiap akhir minggu."),
]
infos_r = [
    ("#FFFBEB","#FDE68A","#92400E","#78350F","📄",
     "Laporan Akhir Magang",
     "Susun laporan akhir sesuai format yang ditetapkan dan kumpulkan sebelum akhir periode magang. Merupakan syarat penyelesaian magang."),
    ("#F5F3FF","#C4B5FD","#6D28D9","#5B21B6","📸",
     "Dokumentasi Kegiatan",
     "Upload foto dokumentasi kegiatan magang ke folder Drive yang disediakan. Dokumentasi mendukung kelengkapan laporan akhir Anda."),
]
for col, infos in [(ia1, infos_l), (ia2, infos_r)]:
    with col:
        for bg, border, htc, bc, icon, title, body in infos:
            st.markdown(f"""
            <div class="ia" style="background:{bg}; border:1px solid {border};">
              <div class="ia-icon">{icon}</div>
              <div>
                <div class="ia-title" style="color:{htc};">{title}</div>
                <div class="ia-body" style="color:{bc};">{body}</div>
              </div>
            </div>
            """, unsafe_allow_html=True)

render_footer()
