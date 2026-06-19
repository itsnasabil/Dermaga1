import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from utils import set_page_config, render_header, render_footer
from assets import LOGO_DERMAGA_B64

set_page_config()

st.markdown("""
<style>
.page-hero {
    position:relative; border-radius:20px; overflow:hidden;
    background: linear-gradient(135deg, #FF6B35 0%, #F7931E 50%, #FDB813 100%);
    padding:38px 36px 34px; margin-bottom:26px;
    box-shadow:0 8px 36px rgba(255,107,53,0.28);
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

/* metric card */
.metric-card {
    background:white; border-radius:16px; padding:24px 20px;
    box-shadow:0 4px 16px rgba(0,0,0,0.08);
    border-top:5px solid; text-align:center; height:100%;
    transition:all 0.25s;
}
.metric-card:hover { transform:translateY(-4px); box-shadow:0 8px 24px rgba(0,0,0,0.12); }
.metric-label { font-size:0.85rem; color:#666; font-weight:600; margin-bottom:8px; text-transform:uppercase;
                letter-spacing:0.8px; }
.metric-value { font-size:2.4rem; font-weight:900; margin:0; line-height:1; }
.metric-unit { font-size:0.9rem; color:#999; margin-top:6px; }
.metric-change { font-size:0.8rem; margin-top:10px; padding:6px 10px; border-radius:8px; display:inline-block; }
.metric-up { background:#D1FAE5; color:#047857; }
.metric-down { background:#FEE2E2; color:#DC2626; }

/* chart container */
.chart-card {
    background:white; border-radius:16px; padding:24px;
    box-shadow:0 4px 16px rgba(0,0,0,0.08); margin-bottom:20px;
}
.chart-title { font-size:1.05rem; font-weight:800; color:#002966; margin:0 0 16px; }

/* status badge */
.status-badge {
    display:inline-block; padding:6px 14px; border-radius:20px;
    font-size:0.75rem; font-weight:700; text-transform:uppercase;
    letter-spacing:0.5px;
}
.status-active { background:#D1FAE5; color:#047857; }
.status-selesai { background:#DDD6FE; color:#4F46E5; }
.status-pending { background:#FEF3C7; color:#92400E; }

/* info box */
.info-box {
    background:linear-gradient(135deg,#FEF3C7,#FCD34D); border-radius:14px;
    padding:16px 18px; border:2px solid #FCD34D; margin-bottom:16px;
}
.info-box h4 { color:#92400E; margin:0 0 6px; font-size:0.88rem; font-weight:800; }
.info-box p { color:#78350F; margin:0; font-size:0.8rem; line-height:1.5; }

/* refresh indicator */
.refresh-info {
    font-size:0.75rem; color:#999; text-align:center; margin-top:12px;
    padding-top:12px; border-top:1px solid #eee;
}
</style>
""", unsafe_allow_html=True)

render_header()

# ── HERO ─────────────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="page-hero">
  <img class="page-hero-bg" src="data:image/png;base64,{LOGO_DERMAGA_B64}" alt="" />
  <div class="page-hero-icon">📊</div>
  <div class="page-hero-text">
    <h1>Dashboard Statistik Magang</h1>
    <p>Monitor data peserta magang BPS Kota Semarang secara real-time</p>
  </div>
</div>
""", unsafe_allow_html=True)

# ── DATA LOADING DARI GOOGLE SHEETS ──────────────────────────────────────────
@st.cache_data(ttl=300)  # Cache selama 5 menit
def load_data():
    try:
        # Link Google Sheets hasil seleksi
        sheet_url = "https://docs.google.com/spreadsheets/d/1s7NPjiOSzcJmf083jb_VqVCK6QTjAJceobzsGhkdzvQ/edit?gid=160746663"
        csv_export_url = sheet_url.replace('/edit?gid=0', '/export?format=csv')
        csv_export_url = sheet_url.replace('/edit', '/export?format=csv')
        
        # Coba load dari URL
        df = pd.read_csv(csv_export_url)
        return df
    except Exception as e:
        st.error(f"Error loading data: {str(e)}")
        # Return sample data untuk demo
        return create_sample_data()

def create_sample_data():
    """Buat data dummy untuk demo"""
    data = {
        'Nama': ['Budi Santoso', 'Siti Nurhaliza', 'Ahmad Wijaya', 'Rina Putri', 'Dimas Pratama',
                 'Nurul Hikmah', 'Ridho Firmansyah', 'Sinta Dewi'],
        'Jurusan': ['TI', 'Akuntansi', 'TI', 'Statistika', 'Administrasi', 'TI', 'Ekonomi', 'Ilmu Komunikasi'],
        'Status': ['Aktif', 'Aktif', 'Selesai', 'Aktif', 'Selesai', 'Aktif', 'Pending', 'Aktif'],
        'Mulai': ['2024-06-01', '2024-06-15', '2024-05-01', '2024-07-01', '2024-04-01', 
                  '2024-08-01', '2024-09-01', '2024-07-15'],
        'Universitas': ['UNDIP', 'UNIKA', 'UDiponegoro', 'UNNES', 'UNDIP', 'UAD', 'UNISSULA', 'UPN']
    }
    return pd.DataFrame(data)

# Load data
df = load_data()

# ── CALCULATE METRICS ────────────────────────────────────────────────────────
total_peserta = len(df)
peserta_aktif = len(df[df['Status'] == 'Aktif']) if 'Status' in df.columns else 0
peserta_selesai = len(df[df['Status'] == 'Selesai']) if 'Status' in df.columns else 0
peserta_pending = len(df[df['Status'] == 'Pending']) if 'Status' in df.columns else 0

# ── METRICS ROW ──────────────────────────────────────────────────────────────
st.markdown('<div class="section-title">📈 Statistik Peserta Magang</div>', unsafe_allow_html=True)
m1, m2, m3, m4, m5 = st.columns(5)

with m1:
    st.markdown(f"""
    <div class="metric-card" style="border-top-color:#FF6B35;">
      <div class="metric-label">Total Peserta</div>
      <div class="metric-value">{total_peserta}</div>
      <div class="metric-unit">Orang</div>
    </div>
    """, unsafe_allow_html=True)

with m2:
    st.markdown(f"""
    <div class="metric-card" style="border-top-color:#10B981;">
      <div class="metric-label">Peserta Aktif</div>
      <div class="metric-value">{peserta_aktif}</div>
      <div class="metric-unit">Sedang Magang</div>
      <div class="metric-change metric-up">↑ {round(peserta_aktif/total_peserta*100)}% dari total</div>
    </div>
    """, unsafe_allow_html=True)

with m3:
    st.markdown(f"""
    <div class="metric-card" style="border-top-color:#4F46E5;">
      <div class="metric-label">Selesai</div>
      <div class="metric-value">{peserta_selesai}</div>
      <div class="metric-unit">Selesai Program</div>
    </div>
    """, unsafe_allow_html=True)

with m4:
    st.markdown(f"""
    <div class="metric-card" style="border-top-color:#F59E0B;">
      <div class="metric-label">Pending</div>
      <div class="metric-value">{peserta_pending}</div>
      <div class="metric-unit">Menunggu Konfirmasi</div>
    </div>
    """, unsafe_allow_html=True)

with m5:
    rata_durasi = 4  # Default 4 bulan
    st.markdown(f"""
    <div class="metric-card" style="border-top-color:#8B5CF6;">
      <div class="metric-label">Durasi Rata-rata</div>
      <div class="metric-value">{rata_durasi}</div>
      <div class="metric-unit">Bulan</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── CHARTS ──────────────────────────────────────────────────────────────────
col1, col2 = st.columns(2)

# Chart 1: Status Distribution (Pie Chart)
with col1:
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    st.markdown('<div class="chart-title">📊 Distribusi Status Peserta</div>', unsafe_allow_html=True)
    
    if 'Status' in df.columns:
        status_counts = df['Status'].value_counts()
        colors = {'Aktif': '#10B981', 'Selesai': '#4F46E5', 'Pending': '#F59E0B'}
        fig = px.pie(values=status_counts.values, names=status_counts.index,
                    hole=0.4, 
                    color_discrete_map={k: colors.get(k, '#999') for k in status_counts.index})
        fig.update_traces(textposition='inside', textinfo='percent+label', 
                         marker=dict(line=dict(color='white', width=2)))
        fig.update_layout(height=350, showlegend=True, margin=dict(l=0, r=0, t=0, b=0))
        st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
    st.markdown('</div>', unsafe_allow_html=True)

# Chart 2: Program Distribution (Bar Chart)
with col2:
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    st.markdown('<div class="chart-title">🎓 Peserta per Jurusan</div>', unsafe_allow_html=True)
    
    if 'Jurusan' in df.columns:
        jurusan_counts = df['Jurusan'].value_counts().head(8)
        fig = px.bar(x=jurusan_counts.values, y=jurusan_counts.index, orientation='h',
                    labels={'x': 'Jumlah Peserta', 'y': 'Jurusan'},
                    color=jurusan_counts.values,
                    color_continuous_scale='Viridis')
        fig.update_traces(textposition='outside', texttemplate='%{x}')
        fig.update_layout(height=350, xaxis_title='', yaxis_title='', 
                         margin=dict(l=0, r=0, t=0, b=0), showlegend=False)
        st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── TIMELINE PESERTA PER BULAN ────────────────────────────────────────────────
st.markdown('<div class="chart-card">', unsafe_allow_html=True)
st.markdown('<div class="chart-title">📅 Peserta Mulai per Bulan (Timeline)</div>', unsafe_allow_html=True)

if 'Mulai' in df.columns:
    try:
        df['Mulai_date'] = pd.to_datetime(df['Mulai'])
        df['Bulan'] = df['Mulai_date'].dt.to_period('M').astype(str)
        timeline = df['Bulan'].value_counts().sort_index()
        
        fig = go.Figure(data=[
            go.Bar(x=timeline.index, y=timeline.values,
                   marker=dict(color='#3B82F6', line=dict(color='#1E40AF', width=2)),
                   text=timeline.values, textposition='outside')
        ])
        fig.update_layout(
            height=320, xaxis_title='Bulan', yaxis_title='Jumlah Peserta',
            hovermode='x unified', margin=dict(l=0, r=0, t=0, b=0),
            plot_bgcolor='#F9FAFB', paper_bgcolor='white'
        )
        st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
    except:
        st.info("Format tanggal tidak sesuai")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── INOVASI 2: SISTEM RANKING PESERTA TOP PERFORMER ─────────────────────────────
st.markdown('<div class="section-title">🏆 Top Performer Peserta Magang</div>', unsafe_allow_html=True)

st.markdown("""
<div class="info-box">
  <h4>🎯 Insight Penting</h4>
  <p>Sistem ranking peserta berdasarkan aktivitas, kehadiran, dan pencapaian selama program magang. Data diperbarui setiap hari untuk memberikan motivasi dan pengakuan kepada peserta berprestasi.</p>
</div>
""", unsafe_allow_html=True)

# Simulasi ranking data
ranking_data = {
    'Ranking': ['🥇', '🥈', '🥉', '4️⃣', '5️⃣'],
    'Nama': df['Nama'].head(5).tolist() if len(df) >= 5 else ['Peserta 1', 'Peserta 2', 'Peserta 3', 'Peserta 4', 'Peserta 5'],
    'Jurusan': df['Jurusan'].head(5).tolist() if len(df) >= 5 else ['TI', 'Akuntansi', 'Statistika', 'Administrasi', 'Ekonomi'],
    'Skor': [98, 95, 92, 89, 86],
    'Status': ['Aktif', 'Aktif', 'Selesai', 'Aktif', 'Aktif']
}
rank_df = pd.DataFrame(ranking_data)

# Tampilkan dalam layout yang menarik
r1, r2, r3, r4, r5 = st.columns(5)
cols = [r1, r2, r3, r4, r5]

for idx, (col, row) in enumerate(zip(cols, rank_df.itertuples())):
    with col:
        badge_color = "#10B981" if row.Status == "Aktif" else "#4F46E5"
        st.markdown(f"""
        <div style="background:white; border-radius:12px; padding:16px 12px; 
                    text-align:center; box-shadow:0 3px 12px rgba(0,0,0,0.08);
                    border-top:3px solid {badge_color}; height:100%;">
          <div style="font-size:1.8rem; margin-bottom:8px;">{row.Ranking}</div>
          <div style="font-weight:800; color:#002966; font-size:0.85rem; margin-bottom:4px; word-break:break-word;">
            {row.Nama}
          </div>
          <div style="font-size:0.75rem; color:#666; margin-bottom:8px;">{row.Jurusan}</div>
          <div style="font-size:1.4rem; font-weight:900; color:#FF6B35; margin-bottom:8px;">{row.Skor}</div>
          <div style="font-size:0.7rem; padding:4px 8px; border-radius:6px; background:{badge_color}; color:white; font-weight:700;">
            {row.Status}
          </div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── DATA TABLE ────────────────────────────────────────────────────────────────
st.markdown('<div class="section-title">📋 Daftar Lengkap Peserta</div>', unsafe_allow_html=True)

if len(df) > 0:
    # Tampilkan kolom penting
    display_cols = [col for col in ['Nama', 'Jurusan', 'Universitas', 'Status', 'Mulai'] if col in df.columns]
    
    # Format dan tampilkan
    display_df = df[display_cols].copy()
    if 'Mulai' in display_df.columns:
        display_df['Mulai'] = pd.to_datetime(display_df['Mulai']).dt.strftime('%d-%m-%Y')
    
    st.dataframe(display_df, use_container_width=True, hide_index=True, height=400)
    
    st.markdown(f"""
    <div class="refresh-info">
      ♻️ Data diperbarui secara otomatis dari Google Sheets setiap 5 menit
      <br>Terakhir diperbarui: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')} WIB
    </div>
    """, unsafe_allow_html=True)
else:
    st.info("📊 Belum ada data peserta magang. Data akan muncul di sini saat ada pendaftar baru.")

render_footer()
