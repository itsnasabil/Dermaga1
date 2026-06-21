import streamlit as st
from utils import set_page_config, render_header, render_footer
from assets import LOGO_DERMAGA_B64


st.markdown(
    '<meta name="google-site-verification" content="ttRf-6fP_HKFr5CiFzOukh_ibe-x5pReEmNwvau6ung" />',
    unsafe_allow_html=True
)

set_page_config()

# ── PAGE CSS ─────────────────────────────────────────────────────────────────
st.markdown("""
<style>
/* ── Hero ── */
.hero-wrap {
    position: relative;
    border-radius: 22px;
    overflow: hidden;
    margin-bottom: 28px;
    box-shadow: 0 12px 48px rgba(0,41,102,0.28);
    min-height: 320px;
    display: flex; align-items: center; justify-content: center;
    background: linear-gradient(135deg, #001A4D 0%, #003F88 45%, #0058BF 75%, #0070E0 100%);
}
.hero-bg-logo {
    position: absolute; inset: 0;
    display: flex; align-items: center; justify-content: center;
    pointer-events: none; z-index: 0;
}
.hero-bg-logo img {
    width: 55%; max-width: 420px;
    opacity: 0.13; filter: brightness(10);
}
.hero-content {
    position: relative; z-index: 1;
    text-align: center; padding: 48px 32px;
    width: 100%;
}
.hero-tagline {
    font-size: 0.82rem; color: rgba(255,255,255,0.6);
    letter-spacing: 2px; text-transform: uppercase;
    font-weight: 600; margin-bottom: 10px;
}
.hero-main-title {
    font-size: 2.5rem; font-weight: 900;
    color: white; margin: 0 0 4px;
    letter-spacing: 1px;
    text-shadow: 0 3px 16px rgba(0,0,0,0.25);
}
.hero-main-title span { color: #F97316; }
.hero-subtitle {
    font-size: 1rem; color: rgba(255,255,255,0.8);
    font-weight: 500; margin: 0 0 22px;
}
.hero-badges {
    display: flex; gap: 10px; justify-content: center; flex-wrap: wrap;
}
.hbadge {
    background: rgba(255,255,255,0.15);
    border: 1px solid rgba(255,255,255,0.28);
    color: white; padding: 5px 14px; border-radius: 20px;
    font-size: 0.76rem; font-weight: 600;
    backdrop-filter: blur(6px);
}

/* ── Stat cards ── */
.stat-card {
    background: white; border-radius: 16px;
    padding: 20px 16px; text-align: center;
    box-shadow: 0 4px 18px rgba(0,63,136,0.09);
    border-bottom: 4px solid;
}
.stat-emoji { font-size: 2rem; margin-bottom: 6px; }
.stat-label { font-size: 0.78rem; color: #555; font-weight: 600; margin: 0; }

/* ── Nav cards ── */
.nav-card {
    background: white; border-radius: 18px;
    padding: 30px 22px; text-align: center;
    box-shadow: 0 5px 22px rgba(0,63,136,0.09);
    border-top: 5px solid;
    transition: all 0.25s; height: 100%;
    text-decoration: none; display: block;
}
.nav-card:hover { transform: translateY(-5px); box-shadow: 0 10px 36px rgba(0,63,136,0.18); }
.nav-card-icon { font-size: 3.2rem; margin-bottom: 12px; }
.nav-card-title { font-size: 1.05rem; font-weight: 800; margin: 0 0 8px; }
.nav-card-desc { font-size: 0.81rem; color: #666; margin: 0; line-height: 1.6; }

/* ── Announcement ── */
.ann-box {
    border-radius: 12px; padding: 15px 18px;
    margin-bottom: 12px; display: flex; gap: 12px; align-items: flex-start;
}
.ann-icon { font-size: 1.4rem; }
.ann-title { font-weight: 700; margin: 0 0 3px; font-size: 0.88rem; }
.ann-body { margin: 0; font-size: 0.81rem; line-height: 1.55; }

/* ── Timeline ── */
.tl-item { display:flex; gap:14px; margin-bottom:18px; align-items:flex-start; }
.tl-dot {
    width:38px; height:38px; min-width:38px;
    background: linear-gradient(135deg,#003F88,#0070CC);
    border-radius:50%; display:flex; align-items:center; justify-content:center;
    font-size:0.9rem; color:white; font-weight:800;
    box-shadow: 0 4px 12px rgba(0,63,136,0.3);
}
.tl-title { font-weight:700; color:#002966; margin:0 0 3px; font-size:0.9rem; }
.tl-desc { color:#555; font-size:0.81rem; margin:0; line-height:1.5; }

/* ── Quick access ── */
.qa-link {
    display:flex; align-items:center; gap:10px;
    background:white; border-radius:12px; padding:13px 16px; margin-bottom:10px;
    text-decoration:none; color:#222; border-left:4px solid;
    box-shadow:0 2px 10px rgba(0,0,0,0.06); transition:all 0.2s;
    font-size:0.86rem; font-weight:600;
}
.qa-link:hover { transform:translateX(4px); color:#003F88; }
.qa-icon { font-size:1.3rem; }
</style>
""", unsafe_allow_html=True)

render_header()

# ── HERO ─────────────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="hero-wrap">
  <div class="hero-bg-logo">
    <img src="data:image/png;base64,{LOGO_DERMAGA_B64}" alt="Logo DERMAGA" />
  </div>
  <div class="hero-content">
    <div class="hero-tagline">🚢 Badan Pusat Statistik Kota Semarang</div>
    <div class="hero-main-title">DER<span>MAGA</span></div>
    <div class="hero-subtitle">Dashboard ElektRonik MAGAng BPS Kota Semarang</div>
    <div class="hero-badges">
      <span class="hbadge">📍 Kota Semarang</span>
      <span class="hbadge">🏛️ BPS Resmi</span>
      <span class="hbadge">📊 Program Magang</span>
      <span class="hbadge">🎓 Untuk Mahasiswa</span>
      <span class="hbadge">💡 BerAKHLAK</span>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ── STAT ROW ──────────────────────────────────────────────────────────────────
c1, c2, c3, c4 = st.columns(4)
stats = [
    ("📝", "Form Pendaftaran Online", "#003F88"),
    ("📁", "Berkas & Dokumen", "#059669"),
    ("✅", "Absensi Harian Digital", "#7C3AED"),
    ("⭐", "Penilaian Magang", "#D97706"),
]
for col, (emoji, label, color) in zip([c1,c2,c3,c4], stats):
    with col:
        st.markdown(f'<div class="stat-card" style="border-bottom-color:{color};"><div class="stat-emoji">{emoji}</div><div class="stat-label">{label}</div></div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── NAVIGATION ───────────────────────────────────────────────────────────────
st.markdown('<div class="section-title">🗺️ Menu Utama</div>', unsafe_allow_html=True)

nc1, nc2, nc3, nc4 = st.columns(4)
navs = [
    ("/", "🏠", "Halaman Muka", "Beranda, pengumuman & alur program magang BPS Kota Semarang", "#003F88"),
    ("/Pendaftaran", "📝", "Pendaftaran", "Form pendaftaran online, persyaratan, rekap & hasil seleksi pendaftar", "#059669"),
    ("/Statistik_Magang", "📧", "Asisten Email Pendaftaran", "Bantuan pembuatan subject & isi email pendaftaran (Copy+Paste)", "#F59E0B"),
    ("/Pelaksanaan", "🗂️", "Pelaksanaan", "Absensi, laporan kegiatan, penilaian, rekap nilai & dokumentasi", "#7C3AED"),
]
for col, (href, icon, title, desc, color) in zip([nc1,nc2,nc3,nc4], navs):
    with col:
        st.markdown(f"""
        <a href="{href}" target="_self" class="nav-card" style="border-top-color:{color};">
          <div class="nav-card-icon">{icon}</div>
          <div class="nav-card-title" style="color:{color};">{title}</div>
          <div class="nav-card-desc">{desc}</div>
        </a>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── PENGUMUMAN + AKSES CEPAT ──────────────────────────────────────────────────
left, right = st.columns([3, 2])

with left:
    st.markdown('<div class="section-title">📢 Pengumuman</div>', unsafe_allow_html=True)
    announcements = [
        ("#EFF6FF","#BFDBFE","#1D4ED8","#1E40AF","🔔","Pendaftaran Magang Dibuka!",
         "Program magang BPS Kota Semarang kini membuka pendaftaran. Segera lengkapi berkas dan daftarkan diri Anda melalui menu Pendaftaran."),
        ("#ECFDF5","#86EFAC","#166534","#14532D","📋","Cek Hasil Seleksi Pendaftar",
         "Rekapitulasi data dan hasil seleksi peserta magang tersedia secara real-time. Pantau status pendaftaran melalui menu Pendaftaran."),
        ("#FFFBEB","#FDE68A","#92400E","#78350F","📌","Wajib Absensi Harian",
         "Seluruh peserta magang wajib mengisi absensi harian dan laporan kegiatan melalui form yang tersedia di menu Pelaksanaan setiap hari kerja."),
    ]
    for bg, border, htc, bc, icon, title, body in announcements:
        st.markdown(f"""
        <div class="ann-box" style="background:{bg}; border:1px solid {border};">
          <div class="ann-icon">{icon}</div>
          <div>
            <div class="ann-title" style="color:{htc};">{title}</div>
            <div class="ann-body" style="color:{bc};">{body}</div>
          </div>
        </div>
        """, unsafe_allow_html=True)

with right:
    st.markdown('<div class="section-title">⚡ Akses Cepat</div>', unsafe_allow_html=True)
    quick_links = [
        ("📧", "#F59E0B",
         "Asisten Email Pendaftaran",
         "/Statistik_Magang"),
        ("📋", "#003F88",
         "Form Pendaftaran",
         "https://docs.google.com/forms/d/e/1FAIpQLSdJDOqp1zJ_PdT5zmrFBVnTbFLvqCAsWH2RJSDF4xjmF9l_iQ/viewform"),
        ("📊", "#059669",
         "Hasil Seleksi Pendaftar",
         "https://docs.google.com/spreadsheets/d/1s7NPjiOSzcJmf083jb_VqVCK6QTjAJceobzsGhkdzvQ/edit?gid=160746663"),
        ("✅", "#7C3AED",
         "Absensi Harian",
         "https://docs.google.com/forms/d/e/1FAIpQLSfy37MhTvDVGGCklo_QNwgvut4g2xwo4jLEPIjQAn23QTTpRw/viewform"),
        ("📓", "#D97706",
         "Laporan Kegiatan Harian",
         "https://docs.google.com/forms/d/e/1FAIpQLSdLIjIjeB_gZqv9CbkIEqku6jpEZpyPNjInTecm9uk3GfK_vQ/viewform"),
        ("📊", "#DC2626",
         "Rekap Kegiatan Harian",
         "https://docs.google.com/spreadsheets/d/15v0VIzoLXIH0ub3HKd17vNlq-b6gOqtM4m6QiMin0oM/edit?usp=sharing"),
    ]
    for icon, color, label, url in quick_links:
        is_internal = url.startswith("/")
        target = "_self" if is_internal else "_blank"
        st.markdown(f"""
        <a class="qa-link" href="{url}" target="{target}" style="border-left-color:{color};">
          <span class="qa-icon">{icon}</span>
          <span style="color:{color};">{label}</span>
          <span style="margin-left:auto; font-size:0.85rem; color:#aaa;">→</span>
        </a>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── ALUR MAGANG ───────────────────────────────────────────────────────────────
st.markdown('<div class="section-title">📍 Alur Program Magang</div>', unsafe_allow_html=True)

steps_l = [
    ("1","📥 Unduh Berkas Pendaftaran",
     "Download surat pengantar, form permohonan, dan daftar riwayat hidup dari halaman Berkas Pendaftaran."),
    ("2","✏️ Lengkapi & Tanda Tangani",
     "Isi semua dokumen dengan data yang benar dan tanda tangani sesuai ketentuan."),
    ("3","📋 Isi Form Pendaftaran Online",
     "Daftarkan diri melalui Google Form pendaftaran dan upload semua berkas yang sudah dilengkapi."),
]
steps_r = [
    ("4","⏳ Tunggu Hasil Seleksi",
     "Pantau hasil seleksi melalui spreadsheet yang tersedia. BPS akan menghubungi peserta yang lolos."),
    ("5","✅ Pelaksanaan Magang",
     "Ikuti kegiatan magang, isi absensi harian, dan buat laporan kegiatan sesuai format."),
    ("6","⭐ Penilaian & Penyelesaian",
     "Proses penilaian oleh pembimbing dan penyelesaian administrasi akhir magang."),
]
cl, cr = st.columns(2)
for col, steps in [(cl, steps_l), (cr, steps_r)]:
    with col:
        for num, title, desc in steps:
            st.markdown(f"""
            <div class="tl-item">
              <div class="tl-dot">{num}</div>
              <div>
                <div class="tl-title">{title}</div>
                <div class="tl-desc">{desc}</div>
              </div>
            </div>
            """, unsafe_allow_html=True)

render_footer()
