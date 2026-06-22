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
    background:linear-gradient(135deg,#064E3B 0%,#059669 55%,#10B981 100%);
    padding:38px 36px 34px; margin-bottom:26px;
    box-shadow:0 8px 36px rgba(5,150,105,0.28);
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

/* berkas card */
.berkas-card {
    background:white; border-radius:18px; padding:30px 24px;
    text-align:center; box-shadow:0 6px 26px rgba(0,0,0,0.08);
    border-top:5px solid; transition:all 0.25s; height:100%;
}
.berkas-card:hover { transform:translateY(-4px); box-shadow:0 12px 38px rgba(0,0,0,0.13); }
.berkas-icon { font-size:3.2rem; margin-bottom:12px; }
.berkas-title { font-size:1.05rem; font-weight:800; margin:0 0 8px; }
.berkas-desc { font-size:0.81rem; color:#555; margin:0 0 12px; line-height:1.7; }
.berkas-contents {
    background:#F8FAFF; border-radius:10px; padding:10px 14px;
    text-align:left; margin-bottom:16px;
}
.berkas-contents-title { font-size:0.75rem; font-weight:700; color:#666; text-transform:uppercase;
                          letter-spacing:0.8px; margin-bottom:6px; }
.berkas-contents ul { margin:0; padding-left:16px; font-size:0.79rem; color:#333; line-height:1.9; }
.berkas-badge {
    display:inline-block; padding:3px 10px; border-radius:20px;
    font-size:0.7rem; font-weight:700; margin-bottom:14px;
}
.dl-btn {
    display:block; width:100%; padding:12px 18px; border-radius:10px;
    font-weight:700; font-size:0.87rem; text-decoration:none;
    text-align:center; color:white !important; transition:all 0.2s;
    box-shadow:0 3px 12px rgba(0,0,0,0.15);
}
.dl-btn:hover { opacity:0.9; transform:translateY(-1px); color:white !important; }
.dl-btn-outline {
    display:block; width:100%; padding:11px 18px; border-radius:10px;
    font-weight:700; font-size:0.85rem; text-decoration:none;
    text-align:center; transition:all 0.2s; margin-top:8px;
    border:2px solid;
}
.dl-btn-outline:hover { opacity:0.85; transform:translateY(-1px); }

/* checklist */
.ck-item {
    display:flex; align-items:flex-start; gap:10px;
    padding:11px 14px; background:white; border-radius:10px;
    margin-bottom:8px; box-shadow:0 2px 8px rgba(0,0,0,0.05); font-size:0.85rem;
}
.ck-icon { font-size:1.2rem; min-width:26px; }
.ck-body strong { display:block; color:#002966; font-size:0.86rem; margin-bottom:2px; }
.ck-body span { color:#555; font-size:0.78rem; line-height:1.4; }

/* notice */
.notice {
    border-radius:12px; padding:16px 18px; margin-bottom:12px;
}
.notice h4 { margin:0 0 6px; font-size:0.88rem; font-weight:800; }
.notice p { margin:0; font-size:0.81rem; line-height:1.6; }

/* lampiran card */
.lampiran-card {
    background:white; border-radius:14px; padding:18px 16px;
    box-shadow:0 3px 12px rgba(0,0,0,0.08); border-left:4px solid;
    margin-bottom:12px; transition:all 0.25s;
}
.lampiran-card:hover { transform:translateX(4px); box-shadow:0 5px 16px rgba(0,0,0,0.12); }
.lampiran-num { 
    display:inline-block; width:28px; height:28px; background:#003F88;
    color:white; border-radius:50%; text-align:center; line-height:28px;
    font-weight:800; font-size:0.9rem; margin-right:10px;
}
.lampiran-title { font-weight:800; color:#002966; font-size:0.92rem; margin-bottom:6px; }
.lampiran-desc { color:#555; font-size:0.8rem; line-height:1.5; margin-bottom:8px; }
.lampiran-sub { color:#666; font-size:0.75rem; font-style:italic; margin-left:4px; }

/* social media icons */
.social-section {
    background:linear-gradient(135deg,#F0F9FF,#E0F2FE); border-radius:14px;
    padding:20px 18px; border:2px solid #93C5FD;
}
.social-title { font-weight:800; color:#0C4A6E; font-size:0.95rem; margin:0 0 12px; }
.social-icons {
    display:flex; gap:10px; flex-wrap:wrap;
}
.social-icon {
    width:44px; height:44px; border-radius:10px; 
    display:flex; align-items:center; justify-content:center;
    font-size:1.4rem; text-decoration:none; transition:all 0.2s;
    box-shadow:0 2px 8px rgba(0,0,0,0.1);
}
.social-icon:hover { transform:translateY(-3px); box-shadow:0 4px 12px rgba(0,0,0,0.15); }
.social-ig { background:#E1306C; }
.social-tiktok { background:#000000; }
.social-fb { background:#1877F2; }
.social-yt { background:#FF0000; }

/* email submission */
.email-box {
    background:linear-gradient(135deg,#ECFDF5,#DCFCE7); border-radius:14px;
    padding:18px 16px; border:2px solid #86EFAC; margin-top:16px;
}
.email-label { font-weight:800; color:#166534; font-size:0.88rem; margin-bottom:8px; display:block; }
.email-content { background:white; border-radius:10px; padding:12px 14px;
                 font-family:monospace; font-size:0.78rem; color:#333;
                 word-break:break-all; box-shadow:0 2px 6px rgba(0,0,0,0.05); }
.copy-btn {
    display:inline-block; padding:6px 12px; background:#10B981; color:white;
    border-radius:6px; font-size:0.75rem; font-weight:700; cursor:pointer;
    text-decoration:none; margin-top:8px; transition:all 0.2s;
}
.copy-btn:hover { background:#059669; transform:scale(1.05); }
</style>
""", unsafe_allow_html=True)

render_header()

# ── HERO ─────────────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="page-hero">
  <img class="page-hero-bg" src="data:image/png;base64,{LOGO_DERMAGA_B64}" alt="" />
  <div style="font-size:3.2rem; z-index:1;">📁</div>
  <div class="page-hero-text">
    <h1>Berkas Pendaftaran</h1>
    <p>Unduh dan lengkapi semua berkas yang diperlukan untuk pendaftaran magang BPS Kota Semarang</p>
  </div>
</div>
""", unsafe_allow_html=True)

# ── URL berkas (masing-masing berkas memiliki link sendiri) ───────────────────
BERKAS_URLS = {
    "Surat Pengantar": "https://docs.google.com/document/d/1bwLc-43FbTMj7ndqobIJUNa1DauTPZBRDBTgjh6Alc4/edit?usp=sharing",
    "Formulir Permohonan Magang": "https://docs.google.com/document/d/1rSmrYk8mRX_e7SGyqRri5Oq8fkpisx_Rqpy9pbRDUC0/edit?usp=sharing",
    "Daftar Riwayat Hidup (CV)": "https://docs.google.com/document/d/1YrkwcDeVr_q3NcFFs7lXmBh6XhmJlvIVWgJ8YcZqeMY/edit?usp=sharing"
}

# ── 3 BERKAS CARDS ────────────────────────────────────────────────────────────
st.markdown('<div class="section-title">📥 Berkas yang Harus Diunduh</div>', unsafe_allow_html=True)
b1, b2, b3 = st.columns(3)

berkas = [
    (b1, "#003F88", "linear-gradient(135deg,#003F88,#0058BF)",
     "📩", "Surat Pengantar", "#EFF6FF", "#1D4ED8", "WAJIB",
     "Surat pengantar resmi yang digunakan sebagai kelengkapan berkas pendaftaran magang BPS Kota Semarang.",
     [
         "Kop surat dari BPS Kota Semarang",
         "Ditujukan kepada Pimpinan Instansi",
         "Memuat nama & periode magang",
         "Ditanda tangani pemohon",
     ]),
    (b2, "#059669", "linear-gradient(135deg,#059669,#10B981)",
     "📋", "Formulir Permohonan Magang", "#ECFDF5", "#166534", "WAJIB",
     "Formulir permohonan yang harus diisi dengan lengkap, ditanda tangani, dan dilampirkan saat pendaftaran.",
     [
         "Data diri lengkap (nama, NIM, jurusan)",
         "Asal perguruan tinggi & program studi",
         "Periode magang yang diinginkan",
         "Tanda tangan pemohon & materai",
     ]),
    (b3, "#D97706", "linear-gradient(135deg,#D97706,#F59E0B)",
     "👤", "Daftar Riwayat Hidup (CV)", "#FFFBEB", "#92400E", "WAJIB",
     "Template CV resmi untuk mempermudah penulisan informasi diri. Sertakan foto dan lengkapi seluruh kolom.",
     [
         "Foto 3×4 cm terbaru",
         "Riwayat pendidikan",
         "Pengalaman organisasi / kerja",
         "Kemampuan & keahlian relevan",
     ]),
]

for col, color, grad, icon, title, bgbadge, colorbadge, badge, desc, contents in berkas:
    with col:
        bullets = "".join(f"<li>{c}</li>" for c in contents)
        doc_url = BERKAS_URLS.get(title, "#")
        st.markdown(f"""
        <div class="berkas-card" style="border-top-color:{color};">
          <div class="berkas-icon">{icon}</div>
          <span class="berkas-badge" style="background:{bgbadge}; color:{colorbadge};">{badge}</span>
          <div class="berkas-title" style="color:{color};">{title}</div>
          <div class="berkas-desc">{desc}</div>
          <div class="berkas-contents">
            <div class="berkas-contents-title">Isi Dokumen:</div>
            <ul>{bullets}</ul>
          </div>
          <a class="dl-btn" style="background:{grad};" href="{doc_url}" target="_blank">
            📥 Download {title}
          </a>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── DOWNLOAD ALL + PETUNJUK ───────────────────────────────────────────────────
cl, cr = st.columns([1.2, 1])

with cl:
    st.markdown('<div class="section-title">📌 Petunjuk Pengisian Berkas</div>', unsafe_allow_html=True)
    checklists = [
        ("📥", "Unduh File", "Klik tombol download di atas untuk membuka dokumen Google Docs."),
        ("📋", "Salin ke Drive", "Klik 'File → Buat salinan' agar bisa diedit di Google Drive Anda."),
        ("✏️", "Isi Semua Kolom", "Lengkapi setiap kolom dengan data yang benar. Gunakan huruf kapital pada nama."),
        ("🖨️", "Cetak & Tanda Tangan", "Cetak dokumen, tanda tangani (+ materai jika diperlukan)."),
        ("📷", "Scan ke PDF", "Scan dokumen yang sudah ditanda tangani dalam format PDF."),
        ("📎", "Upload ke Form", "Upload semua berkas PDF saat mengisi formulir pendaftaran online."),
    ]
    for icon, title, desc in checklists:
        st.markdown(f"""
        <div class="ck-item">
          <span class="ck-icon">{icon}</span>
          <div class="ck-body"><strong>{title}</strong><span>{desc}</span></div>
        </div>
        """, unsafe_allow_html=True)

with cr:
    st.markdown('<div class="section-title">ℹ️ Informasi Penting</div>', unsafe_allow_html=True)

    st.markdown(f"""
    <div class="notice" style="background:#EFF6FF; border:1px solid #93C5FD;">
      <h4 style="color:#1D4ED8;">📦 Berkas Terpisah, Mudah Diakses</h4>
      <p style="color:#1E40AF;">Setiap berkas tersedia dalam dokumen Google Docs terpisah. Klik tombol Download masing-masing di atas untuk membuka berkas yang Anda butuhkan. Semua berkas dapat diakses dan disalin ke Google Drive Anda.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="notice" style="background:#FFF7ED; border:1px solid #FED7AA; margin-top:12px;">
      <h4 style="color:#C2410C;">⚠️ Perhatian</h4>
      <p style="color:#9A3412;">Pastikan <strong>semua berkas sudah lengkap</strong> sebelum diunggah ke formulir pendaftaran. Berkas yang tidak lengkap atau tidak jelas dapat menyebabkan proses pendaftaran Anda tertunda atau gugur seleksi.</p>
    </div>

    <div class="notice" style="background:#F5F3FF; border:1px solid #C4B5FD; margin-top:12px;">
      <h4 style="color:#6D28D9;">💡 Tips</h4>
      <p style="color:#5B21B6;">Simpan salinan berkas Anda di Google Drive pribadi agar mudah diakses kembali jika diperlukan di kemudian hari.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── LAMPIRAN DAN PENGIRIMAN ──────────────────────────────────────────────────
st.markdown('<div class="section-title">📎 Daftar Lampiran yang Harus Dikirimkan</div>', unsafe_allow_html=True)

lampiran_data = [
    ("KTM atau Surat Keterangan Kuliah Aktif", 
     "Kartu Tanda Mahasiswa atau surat dari perguruan tinggi yang membuktikan status kuliah aktif"),
    
    ("Surat Pengantar", 
     "Surat resmi dari perguruan tinggi Anda sebagai kelengkapan berkas pendaftaran"),
    
    ("Formulir Permohonan Magang", 
     "Formulir yang sudah diisi dengan lengkap, ditanda tangani, dan bermaterai"),
    
    ("Daftar Riwayat Hidup (CV)", 
     "CV lengkap dengan foto terbaru 3×4 cm dan pengalaman relevan"),
    
    ("Portofolio", 
     "Portofolio Utama : Semua Projek yang pernah dikerjakan (website/perhitungan statistik/dll)<br>Portofolio Pendukung : <br>Mahasiswa TI: Program atau Aplikasi yang pernah dibuat<br>Mahasiswa non TI: Infografis atau videografi dengan data BPS Kota Semarang (sumber: semarangkota.bps.go.id - tabel statistik, berita resmi statistik, publikasi). *catatan keduanya wajib."),
    
    ("Karya Infografis/Videografi Statistik", 
     "Menyertakan karya infografis, videografi, atau content statistik menggunakan data statistik Kota Semarang terbaru dari publikasi/tabel statistik di semarangkota.bps.go.id. Karya harus 100% hasil sendiri (bukan dari orang lain)"),
    
    ("Screenshot Bukti Follow Media Sosial", 
     "Screenshot yang membuktikan Anda sudah follow akun resmi BPS Kota Semarang di semua platform (Instagram, Facebook, TikTok, YouTube)"),
]

for i, (title, desc) in enumerate(lampiran_data, 1):
    st.markdown(f"""
    <div class="lampiran-card" style="border-left-color:#059669;">
      <span class="lampiran-num">{i}</span>
      <div class="lampiran-title">{title}</div>
      <div class="lampiran-desc">{desc}</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── IKUTI MEDIA SOSIAL ─────────────────────────────────────────────────────────
st.markdown('<div class="section-title">📱 Ikuti Media Sosial Resmi BPS Kota Semarang</div>', unsafe_allow_html=True)

st.markdown("""
<div class="social-section">
    <div class="social-title">🔔 Jangan lupa untuk follow semua akun resmi kami!</div>
    <div class="social-icons">
        <a href="https://www.instagram.com/bpskotasemarang/" target="_blank" class="social-icon social-ig" title="Instagram @bpskotasemarang">📷</a>
        <a href="https://www.tiktok.com/@bps.kota.semarang" target="_blank" class="social-icon social-tiktok" title="TikTok @bps.kota.semarang">🎵</a>
        <a href="https://www.facebook.com/BPS-Kota-Semarang" target="_blank" class="social-icon social-fb" title="Facebook BPS Kota Semarang">f</a>
        <a href="https://www.youtube.com/@bpskotasemarang8647" target="_blank" class="social-icon social-yt" title="YouTube @bpskotasemarang8647">▶</a>
    </div>
    <div style="font-size:0.8rem; color:#0C4A6E; margin-top:12px; line-height:1.6;">
        <strong>Instagram:</strong> @bpskotasemarang<br>
        <strong>TikTok:</strong> @bps.kota.semarang<br>
        <strong>Facebook:</strong> BPS Kota Semarang<br>
        <strong>YouTube:</strong> @bpskotasemarang8647
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── PENGIRIMAN EMAIL ──────────────────────────────────────────────────────────
st.markdown('<div class="section-title">✉️ Cara Pengiriman Berkas</div>', unsafe_allow_html=True)

col1, col2 = st.columns([1.2, 1])

with col1:
    st.markdown("""
    <div class="notice" style="background:#FEF3C7; border:2px solid #FCD34D;">
      <h4 style="color:#92400E;">📧 Email Pengiriman</h4>
      <p style="color:#78350F; font-size:0.85rem; margin-bottom:10px;">Kirimkan semua berkas lampiran yang sudah lengkap ke alamat email resmi BPS Kota Semarang</p>
      <div style="background:white; border-radius:8px; padding:10px 12px; font-family:monospace; font-size:0.85rem; color:#333; word-break:break-all;">
        <strong>magangbps3374@bps.go.id</strong>
      </div>
    </div>
    
    <div class="notice" style="background:#DBEAFE; border:2px solid #93C5FD; margin-top:14px;">
      <h4 style="color:#1E40AF;">📝 Format Subjek Email</h4>
      <p style="color:#1E40AF; font-size:0.82rem; line-height:1.7;">Gunakan format berikut untuk subjek email agar mudah diidentifikasi:</p>
      <div style="background:#F0F9FF; border-radius:8px; padding:10px 12px; font-family:monospace; font-size:0.78rem; color:#1E40AF; word-break:break-word; border-left:3px solid #0284C7;">
        <strong>Permohonan Magang [Nama Mahasiswa]_[Jurusan]_[Fakultas]_[Universitas/Perguruan Tinggi]</strong>
      </div>
      <p style="color:#1E40AF; font-size:0.8rem; margin-top:8px; margin-bottom:0;"><strong>Contoh:</strong></p>
      <div style="background:white; border-radius:8px; padding:8px 10px; font-family:monospace; font-size:0.77rem; color:#333; margin-top:6px;">
        Permohonan Magang Budi Santoso_Teknik Informatika_Fakultas Teknik_Universitas Diponegoro
      </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="notice" style="background:#F3E8FF; border:2px solid #D8B4FE;">
      <h4 style="color:#6D28D9;">⚡ Poin Penting</h4>
      <ul style="color:#5B21B6; font-size:0.8rem; margin:0; padding-left:18px; line-height:1.8;">
        <li>Pastikan <strong>semua lampiran lengkap</strong> sebelum dikirim</li>
        <li>Gunakan format subjek email dengan benar</li>
        <li>Lampirkan file dalam format <strong>PDF</strong> atau <strong>ZIP</strong></li>
        <li>Jangan lupa screenshot bukti follow media sosial</li>
        <li>Email akan diproses dalam 5-7 hari kerja</li>
        <li>Periksa email secara berkala untuk respon dari kami</li>
      </ul>
    </div>

    <div class="notice" style="background:#FEE2E2; border:2px solid #FCA5A5; margin-top:14px;">
      <h4 style="color:#991B1B;">⚠️ Catatan Penting</h4>
      <p style="color:#7F1D1D; font-size:0.8rem; margin:0;">Berkas yang tidak lengkap, format subjek email yang salah, atau tidak menyertakan screenshot bukti follow akan ditolak dan diminta untuk dikirim ulang.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── NAVIGASI LANJUT ───────────────────────────────────────────────────────────
st.markdown('<div class="section-title">🔗 Langkah Selanjutnya</div>', unsafe_allow_html=True)
n1, n2 = st.columns(2)
with n1:
    st.markdown("""
    <a href="/Pendaftaran" target="_self"
       style="display:block; background:white; border:2px solid #003F88; color:#003F88;
              padding:14px 20px; border-radius:12px; text-align:center;
              font-weight:700; font-size:0.9rem; text-decoration:none; transition:all 0.2s;">
      ← Kembali ke Pendaftaran
    </a>
    """, unsafe_allow_html=True)
with n2:
    st.markdown("""
    <a href="https://docs.google.com/forms/d/e/1FAIpQLSdJDOqp1zJ_PdT5zmrFBVnTbFLvqCAsWH2RJSDF4xjmF9l_iQ/viewform"
       target="_blank"
       style="display:block; background:linear-gradient(135deg,#003F88,#0058BF); color:white;
              padding:14px 20px; border-radius:12px; text-align:center;
              font-weight:700; font-size:0.9rem; text-decoration:none;
              box-shadow:0 4px 14px rgba(0,63,136,0.3);">
      📋 Isi Form Pendaftaran Online →
    </a>
    """, unsafe_allow_html=True)

render_footer()
