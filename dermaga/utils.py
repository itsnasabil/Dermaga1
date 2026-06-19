import streamlit as st
from assets import LOGO_DERMAGA_B64, LOGO_BPS_B64


def set_page_config():
    st.set_page_config(
        page_title="DERMAGA – BPS Kota Semarang",
        page_icon="🚢",
        layout="wide",
        initial_sidebar_state="expanded",
    )


# ── shared CSS injected once per page ───────────────────────────────────────
GLOBAL_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

*, *::before, *::after { box-sizing: border-box; }

html, body, [data-testid="stAppViewContainer"] {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    background: #F0F5FF !important;
}

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #002966 0%, #003F88 55%, #0058BF 100%) !important;
    box-shadow: 4px 0 24px rgba(0,0,0,0.18);
    min-width: 240px !important;
}
[data-testid="stSidebar"] * { color: white !important; }
[data-testid="stSidebarContent"] { padding-top: 0 !important; }

/* ── Hide default streamlit nav labels ── */
[data-testid="stSidebarNav"] { display: none !important; }

/* ── Top bar header ── */
.top-header-bar {
    background: white;
    border-radius: 16px;
    padding: 12px 24px;
    margin-bottom: 20px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    box-shadow: 0 2px 16px rgba(0,63,136,0.07);
    border-bottom: 3px solid #003F88;
}
.top-header-left { display: flex; align-items: center; gap: 14px; }
.top-header-title { font-size: 0.85rem; color: #003F88; font-weight: 700; line-height: 1.3; }
.top-header-sub { font-size: 0.72rem; color: #666; font-weight: 500; }

/* ── Section title ── */
.section-title {
    font-size: 1.2rem; font-weight: 800;
    color: #002966; margin: 4px 0 16px;
    display: flex; align-items: center; gap: 10px;
}
.section-title::after {
    content: ''; flex: 1; height: 2.5px;
    background: linear-gradient(90deg, #003F88 0%, #F97316 50%, transparent 100%);
    border-radius: 2px;
}

/* ── Quick link buttons ── */
.quick-btn {
    display: inline-flex; align-items: center; gap: 8px;
    background: linear-gradient(135deg, #003F88, #0058BF);
    color: white !important;
    padding: 11px 22px; border-radius: 10px;
    font-weight: 700; font-size: 0.87rem;
    text-decoration: none;
    box-shadow: 0 4px 14px rgba(0,63,136,0.3);
    transition: all 0.2s; margin: 4px;
}
.quick-btn:hover { transform: translateY(-2px); color: white !important; box-shadow: 0 6px 20px rgba(0,63,136,0.4); }
.quick-btn-outline {
    display: inline-flex; align-items: center; gap: 8px;
    background: white; color: #003F88 !important;
    padding: 10px 22px; border-radius: 10px;
    font-weight: 700; font-size: 0.87rem;
    text-decoration: none; border: 2px solid #003F88;
    transition: all 0.2s; margin: 4px;
}
.quick-btn-outline:hover { background: #003F88; color: white !important; transform: translateY(-2px); }

/* ── Footer ── */
.footer-bar {
    text-align: center; padding: 20px; color: #888;
    font-size: 0.78rem; margin-top: 44px;
    border-top: 2px solid #e0e0e0;
}
.footer-bar strong { color: #003F88; }
</style>
"""


def render_header():
    """Sidebar + top header bar with logos."""
    st.markdown(GLOBAL_CSS, unsafe_allow_html=True)

    # ── SIDEBAR ──────────────────────────────────────────────────────────────
    with st.sidebar:
        # Dermaga logo
        st.markdown(f"""
        <div style="padding: 18px 16px 0; text-align:center;">
          <img src="data:image/png;base64,{LOGO_DERMAGA_B64}"
               style="width:88%; max-width:200px; border-radius:12px;
                      box-shadow:0 4px 16px rgba(0,0,0,0.25); margin-bottom:6px;" />
          <div style="font-size:0.68rem; color:rgba(255,255,255,0.55); margin-bottom:10px; font-style:italic;">
            Dashboard ElektRonik MAGAng
          </div>
          <hr style="border-color:rgba(255,255,255,0.18); margin:0 0 10px;">
        </div>
        """, unsafe_allow_html=True)

        # Nav
        st.markdown("""
        <style>
        .snav { font-size:0.67rem; color:rgba(255,255,255,0.45);
                font-weight:700; letter-spacing:1.5px; text-transform:uppercase;
                padding:10px 16px 4px; }
        .slink { display:flex; align-items:center; gap:9px;
                 padding:10px 16px; border-radius:10px; margin:2px 8px;
                 font-weight:600; font-size:0.86rem; color:white !important;
                 text-decoration:none; transition:background 0.2s; }
        .slink:hover { background:rgba(255,255,255,0.15) !important; color:white !important; }
        .slink-sub { display:flex; align-items:center; gap:9px;
                     padding:8px 16px 8px 36px; border-radius:10px; margin:2px 8px;
                     font-size:0.8rem; color:rgba(255,255,255,0.82) !important;
                     text-decoration:none; transition:background 0.2s; }
        .slink-sub:hover { background:rgba(255,255,255,0.1) !important; color:white !important; }
        .sdivider { border-color:rgba(255,255,255,0.15); margin:12px 0; }
        </style>

        <div class="snav">Navigasi</div>
        <a href="/" target="_self" class="slink">🏠 Halaman Muka</a>
        <a href="/Pendaftaran" target="_self" class="slink">📝 Pendaftaran</a>
        <a href="/Berkas_Pendaftaran" target="_self" class="slink-sub">📁 Berkas Pendaftaran</a>
        <a href="/Pelaksanaan" target="_self" class="slink">🗂️ Pelaksanaan</a>
        <hr class="sdivider">
        <div class="snav">Akses Cepat</div>
        <a href="https://docs.google.com/forms/d/e/1FAIpQLSdJDOqp1zJ_PdT5zmrFBVnTbFLvqCAsWH2RJSDF4xjmF9l_iQ/viewform"
           target="_blank" class="slink">📋 Form Pendaftaran ↗</a>
        <a href="https://docs.google.com/forms/d/e/1FAIpQLSfy37MhTvDVGGCklo_QNwgvut4g2xwo4jLEPIjQAn23QTTpRw/viewform"
           target="_blank" class="slink">✅ Absensi Harian ↗</a>
        <a href="https://docs.google.com/forms/d/e/1FAIpQLSdLIjIjeB_gZqv9CbkIEqku6jpEZpyPNjInTecm9uk3GfK_vQ/viewform"
           target="_blank" class="slink">📓 Laporan Kegiatan ↗</a>
        <hr class="sdivider">
        <div style="font-size:0.67rem; color:rgba(255,255,255,0.38);
                    text-align:center; padding:6px 0 14px;">
          © 2025 BPS Kota Semarang
        </div>
        """, unsafe_allow_html=True)

    # ── TOP HEADER BAR (logo BPS + BerAKHLAK kanan) ──────────────────────
    st.markdown(f"""
    <div class="top-header-bar">
      <div class="top-header-left">
        <img src="data:image/png;base64,{LOGO_BPS_B64}"
             style="height:52px; object-fit:contain;" />
      </div>
      <div style="font-size:0.8rem; color:#555; font-style:italic; text-align:right; line-height:1.4;">
        <span style="color:#003F88; font-weight:700;">DERMAGA</span> —
        Dashboard ElektRonik MAGAng<br>
        <span style="font-size:0.7rem;">Badan Pusat Statistik Kota Semarang</span>
      </div>
    </div>
    """, unsafe_allow_html=True)


def render_footer():
    st.markdown("""
    <div class="footer-bar">
      <strong>DERMAGA</strong> – Dashboard ElektRonik MAGAng BPS Kota Semarang<br>
            Badan Pusat Statistik Kota Semarang · Jl. Inspeksi Kali Semarang No.1, Sekayu,Semarang-Jawa Tengah<br>
      <span style="font-size:0.7rem;">© 2025 BPS Kota Semarang. All rights reserved.</span>
    </div>
    """, unsafe_allow_html=True)
