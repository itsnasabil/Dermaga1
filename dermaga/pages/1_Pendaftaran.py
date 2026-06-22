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
    background: linear-gradient(135deg, #001A4D 0%, #003F88 50%, #006BB3 100%);
    padding:38px 36px 34px; margin-bottom:26px;
    box-shadow:0 8px 36px rgba(0,41,102,0.25);
    display:flex; align-items:center; gap:22px; min-height:130px;
}
.page-hero-bg { position:absolute; right:-30px; top:50%; transform:translateY(-50%);
                opacity:0.1; filter:brightness(10); width:180px; }
.page-hero-icon { font-size:3.2rem; z-index:1; }
.page-hero-text { z-index:1; }
.page-hero-text h1 { color:white; margin:0 0 6px; font-size:1.9rem; font-weight:900; }
.page-hero-text p { color:rgba(255,255,255,0.82); margin:0; font-size:0.9rem; }

.section-title {
    font-size:1.2rem; font-weight:800; color:#002966; margin:8px 0 16px;
    display:flex; align-items:center; gap:10px;
}
.section-title::after {
    content:''; flex:1; height:2.5px;
    background:linear-gradient(90deg,#003F88 0%,#F97316 50%,transparent 100%); border-radius:2px;
}

/* action cards */
.act-card {
    background:white; border-radius:18px; padding:28px 22px;
    box-shadow:0 5px 22px rgba(0,63,136,0.09);
    border-top:5px solid; text-align:center; height:100%;
    transition:all 0.25s;
}
.act-card:hover { transform:translateY(-4px); box-shadow:0 10px 34px rgba(0,63,136,0.16); }
.act-icon { font-size:2.8rem; margin-bottom:12px; }
.act-title { font-size:1rem; font-weight:800; margin:0 0 8px; }
.act-desc { font-size:0.81rem; color:#555; margin:0 0 18px; line-height:1.65; }
.act-btn {
    display:block; width:100%; padding:12px 18px; border-radius:10px;
    font-weight:700; font-size:0.87rem; text-decoration:none;
    text-align:center; color:white !important; transition:all 0.2s;
    box-shadow:0 3px 10px rgba(0,0,0,0.15);
}
.act-btn:hover { opacity:0.9; transform:translateY(-1px); color:white !important; }

/* requirement card */
.req-card {
    background:white; border-radius:13px; padding:18px 18px;
    box-shadow:0 3px 14px rgba(0,0,0,0.06); border-left:5px solid; margin-bottom:12px;
}
.req-card h4 { margin:0 0 8px; font-size:0.92rem; font-weight:800; }
.req-card ul { margin:0; padding-left:18px; color:#444; font-size:0.82rem; line-height:1.85; }

/* step row */
.step-row {
    display:flex; align-items:flex-start; gap:12px;
    padding:12px 14px; background:white; border-radius:10px;
    margin-bottom:8px; box-shadow:0 2px 8px rgba(0,0,0,0.05);
}
.step-dot {
    width:28px; height:28px; min-width:28px;
    background:#003F88; color:white; border-radius:50%;
    display:flex; align-items:center; justify-content:center;
    font-size:0.78rem; font-weight:800;
}
.step-text { font-size:0.85rem; color:#333; line-height:1.5; padding-top:3px; }

/* rekap highlight */
.rekap-hl {
    background:linear-gradient(135deg,#EFF6FF,#DBEAFE);
    border:2px solid #93C5FD; border-radius:14px; padding:22px; text-align:center;
}
.rekap-hl-icon { font-size:2.4rem; margin-bottom:8px; }
.rekap-hl-title { font-weight:800; color:#1D4ED8; margin:0 0 6px; font-size:0.98rem; }
.rekap-hl-desc { color:#2563EB; font-size:0.8rem; margin:0 0 14px; }

.contact-card { background:white; border-radius:12px; padding:16px 18px;
                box-shadow:0 2px 10px rgba(0,0,0,0.06); }
.contact-card h4 { color:#003F88; margin:0 0 6px; font-size:0.88rem; font-weight:800; }
.contact-card p { margin:0; color:#444; font-size:0.82rem; line-height:1.6; }
</style>
""", unsafe_allow_html=True)

render_header()

# ── HERO ─────────────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="page-hero">
  <img class="page-hero-bg" src="data:image/png;base64,{LOGO_DERMAGA_B64}" alt="" />
  <div class="page-hero-icon">📝</div>
  <div class="page-hero-text">
    <h1>Pendaftaran Magang</h1>
    <p>Informasi pendaftaran, persyaratan, formulir online, berkas, dan hasil seleksi peserta magang BPS Kota Semarang</p>
  </div>
</div>
""", unsafe_allow_html=True)

# ── 3 ACTION CARDS ────────────────────────────────────────────────────────────
st.markdown('<div class="section-title">🚀 Aksi Pendaftaran</div>', unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)
cards = [
    (c1, "#003F88", "📋", "Form Pendaftaran Online",
     "Isi formulir pendaftaran magang secara online. Pastikan semua data diisi dengan benar dan lengkap.",
     "linear-gradient(135deg,#003F88,#0058BF)", "📋 Isi Form Sekarang",
     "https://docs.google.com/forms/d/e/1FAIpQLSdJDOqp1zJ_PdT5zmrFBVnTbFLvqCAsWH2RJSDF4xjmF9l_iQ/viewform"),
    (c2, "#059669", "📁", "Berkas Pendaftaran",
     "Download surat pengantar, form permohonan, dan daftar riwayat hidup yang wajib dilengkapi.",
     "linear-gradient(135deg,#059669,#10B981)", "📁 Unduh Berkas",
     "/Berkas_Pendaftaran"),
    (c3, "#D97706", "📊", "Hasil Seleksi Pendaftar",
     "Pantau rekapitulasi data dan hasil seleksi pendaftar magang secara real-time.",
     "linear-gradient(135deg,#D97706,#F59E0B)", "📊 Lihat Hasil Seleksi",
     "https://docs.google.com/spreadsheets/d/1s7NPjiOSzcJmf083jb_VqVCK6QTjAJceobzsGhkdzvQ/edit?gid=160746663"),
]
for col, color, icon, title, desc, grad, btnlabel, url in cards:
    with col:
        target = '_self' if url.startswith('/') else '_blank'
        st.markdown(f"""
        <div class="act-card" style="border-top-color:{color};">
          <div class="act-icon">{icon}</div>
          <div class="act-title" style="color:{color};">{title}</div>
          <div class="act-desc">{desc}</div>
          <a class="act-btn" style="background:{grad};" href="{url}" target="{target}">{btnlabel}</a>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── PERSYARATAN + LANGKAH ─────────────────────────────────────────────────────
cl, cr = st.columns(2)

with cl:
    st.markdown('<div class="section-title">📌 Persyaratan Pendaftaran</div>', unsafe_allow_html=True)
    reqs = [
        ("#003F88", "📄 Dokumen Wajib", [
            "Surat pengantar dari perguruan tinggi",
            "Formulir permohonan magang yang telah diisi & ditanda tangani",
            "Daftar riwayat hidup (CV) sesuai template",
            "Portofolio sesuai ketentuan (utama + pendukung)",
            "Kartu Tanda Mahasiswa (KTM)",
        ]),
        ("#059669", "🎓 Persyaratan", [
            "Mahasiswa aktif D3 / D4 / S1",
            "Prodi yang diutamakan(Statistik, Ekonomi, Administrasi, Akuntansi, Teknik Informatika, Mtematika, Ilmu Komunikasi)",
            "Tidak sedang magang di instansi lain",
            "Menguasai MS Office dengan baik, terutama MS Excel",
            "Kemampuan Dasar Desain dan Editing (Canva dll)",
            "Kemampuan komunikasi & manajemen waktu dengan baik",
            "Khusus Jurusan Teknik Informatika, Menguasai RPL Pengembangan Aplikasi Andoroid, Pengembangan Aplikasi Berbasis Website, Pemanfaatan Kecerdasan Buatan, dan siap menerima surat kesepakatan yang menyerahkan source code aplikasi.",
        ]),
        ("#D97706", "⏰ Ketentuan Waktu", [
            "Durasi magang minimal 1 (satu) bulan",
            "Hari kerja Senin s.d. Jumat",
            "Jam kerja 07.30 – 16.00 WIB",
            "Menyesuaikan kalender kerja BPS Kota Semarang",
            "Pendaftaran paling lambat 2 minggu sebelum mulai",
        ]),
    ]
    for color, title, items in reqs:
        bullets = "".join(f"<li>{i}</li>" for i in items)
        st.markdown(f"""
        <div class="req-card" style="border-left-color:{color};">
          <h4 style="color:{color};">{title}</h4>
          <ul>{bullets}</ul>
        </div>
        """, unsafe_allow_html=True)

with cr:
    st.markdown('<div class="section-title">📍 Langkah Pendaftaran</div>', unsafe_allow_html=True)
    steps = [
        ("1", "📥 Unduh Berkas", "Download surat pengantar, form permohonan, dan CV dari halaman Berkas Pendaftaran."),
        ("2", "✏️ Lengkapi Dokumen", "Isi dan tanda tangani semua dokumen. Pastikan data sesuai KTP dan KTM."),
        ("3", "🖨️ Cetak & Scan", "Cetak dokumen yang sudah diisi, tanda tangani, lalu scan dalam format PDF."),
        ("4", "📋 Isi Form Online", "Daftarkan diri melalui Google Form pendaftaran dan lampirkan semua berkas PDF."),
        ("5", "⏳ Tunggu Hasil Seleksi", "Pantau hasil seleksi melalui spreadsheet yang tersedia. BPS akan menghubungi peserta lolos."),
        ("6", "✅ Konfirmasi & Mulai", "Setelah konfirmasi dari BPS, persiapkan diri untuk memulai magang sesuai jadwal."),
    ]
    for num, title, desc in steps:
        st.markdown(f"""
        <div class="step-row">
          <div class="step-dot">{num}</div>
          <div class="step-text"><strong>{title}</strong><br>{desc}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"""
    <div class="rekap-hl">
      <div class="rekap-hl-icon">📊</div>
      <div class="rekap-hl-title">Hasil Seleksi Tersedia</div>
      <div class="rekap-hl-desc">Cek data dan status seluruh pendaftar magang secara real-time</div>
      <a class="act-btn" style="background:linear-gradient(135deg,#1D4ED8,#3B82F6);"
         href="https://docs.google.com/spreadsheets/d/1s7NPjiOSzcJmf083jb_VqVCK6QTjAJceobzsGhkdzvQ/edit?gid=160746663"
         target="_blank">📊 Lihat Hasil Seleksi Pendaftar</a>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── KONTAK ────────────────────────────────────────────────────────────────────
st.markdown('<div class="section-title">📞 Informasi Kontak BPS Kota Semarang</div>', unsafe_allow_html=True)
k1, k2, k3, k4, k5 = st.columns(5)
contacts = [
    ("🏛️", "Alamat", "Jl. Inspeksi Kali Semarang No.1, Sekayu,Semarang-Jawa Tengah"),
    ("📞", "Telepon", "(024) 3546413"),
    ("🌐", "Website Resmi", "https://semarangkota.bps.go.id/id"),
    ("💬", "WhatsApp", "085117113374"),
    ("✉️", "Email", "bps3374@bps.go.id"),
]
for col, (icon, title, val) in zip([k1,k2,k3,k4,k5], contacts):
    with col:
        st.markdown(f"""
        <div class="contact-card">
          <h4>{icon} {title}</h4>
          <p>{val}</p>
        </div>
        """, unsafe_allow_html=True)

render_footer()
