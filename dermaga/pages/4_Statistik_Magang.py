import streamlit as st
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from utils import set_page_config, render_header, render_footer
from assets import LOGO_DERMAGA_B64

set_page_config()

st.markdown("""
<style>
.email-hero { background:linear-gradient(135deg,#003F88 0%,#0058BF 50%); padding:22px; border-radius:14px; color:white; margin-bottom:18px; }
.email-hero h1{ margin:0; font-size:1.5rem; }
.email-hero p{ margin:4px 0 0; opacity:0.9 }
.assistant-card{ background:white; border-radius:12px; padding:16px; box-shadow:0 6px 20px rgba(2,6,23,0.06); }
.field-label{ font-weight:700; color:#0B3B6F; margin-bottom:6px; }
.checklist-item{ margin:6px 0; }
</style>
""", unsafe_allow_html=True)

render_header()

st.markdown(f"""
<div class="email-hero">
  <div style="display:flex; gap:14px; align-items:center;">
    <div style="font-size:2rem;">📧</div>
    <div>
      <h1>Email Submission Assistant</h1>
      <p>Buat subject & body email pendaftaran magang. Copy → Paste → Kirim manual via Gmail.</p>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="assistant-card">', unsafe_allow_html=True)

with st.form('email_assistant_form'):
    st.markdown('**Masukkan data Anda**')
    col1, col2 = st.columns([2,2])
    with col1:
        nama = st.text_input('Nama lengkap', placeholder='Contoh: Budi Santoso')
        prodi = st.text_input('Program Studi / Prodi', placeholder='Contoh: Teknologi Informasi')
    with col2:
        universitas = st.text_input('Universitas / Institusi', placeholder='Contoh: Universitas Diponegoro')
        kontak_opsional = st.text_input('Email pengirim (opsional)', placeholder='contoh@mail.com')

    # Generate subject
    def _clean(s: str):
        return "_".join(s.strip().split()) if s and s.strip() else ''

    subject = f"Permohonan Magang {_clean(nama)}_{_clean(prodi)}_{_clean(universitas)}" if nama or prodi or universitas else ''

    st.markdown('\n')
    st.markdown('**Subject email (otomatis)**')
    st.code(subject or 'Isi nama / prodi / universitas untuk melihat subject otomatis')

    # Template email body
    template = f"""Yth. Tim Magang BPS Kota Semarang,

Perkenalkan, saya {nama if nama else '[Nama Anda]'}, mahasiswa Program Studi {prodi if prodi else '[Prodi Anda]'} di {universitas if universitas else '[Universitas Anda]'}. Saya bermaksud mengajukan permohonan magang di BPS Kota Semarang.

Sebagai lampiran bersama email ini, saya sertakan dokumen yang diperlukan sesuai ketentuan:
- KTM / Surat Keterangan Kuliah Aktif
- Surat Pengantar
- Formulir Permohonan Magang
- Daftar Riwayat Hidup (CV)
- Portofolio / Karya (jika ada)
- Karya Infografis / Videografi Statistik (jika ada)
- Bukti follow akun media sosial BPS Kota Semarang

Demikian permohonan ini saya sampaikan. Besar harapan saya dapat diterima untuk mengikuti program magang. Atas perhatian dan kesempatan yang diberikan, saya ucapkan terima kasih.

Hormat saya,
{nama if nama else '[Nama Anda]'}
{prodi if prodi else '[Prodi / Program Studi]'}
{universitas if universitas else '[Universitas / Institusi]'}
"""

    st.markdown('\n')
    st.markdown('**Isi email (siap diedit sebelum copy)**')
    body = st.text_area('Template isi email', value=template, height=260)

    st.markdown('\n')
    st.markdown('**Checklist lampiran (centang sebelum mengirim)**')
    check_items = [
        'KTM atau Surat Keterangan Kuliah Aktif',
        'Surat Pengantar (dokumen resmi)',
        'Formulir Permohonan Magang (diisi & ditandatangani)',
        'Daftar Riwayat Hidup (CV)',
        'Portofolio (aplikasi / infografis / video)',
        'Karya Infografis / Videografi Statistik (jika diminta)',
        'Screenshot bukti follow media sosial BPS Kota Semarang'
    ]
    checks = []
    for idx, item in enumerate(check_items):
        checks.append(st.checkbox(item, key=f'chk_{idx}'))

    st.markdown('\n')
    submit = st.form_submit_button('Siapkan & Tampilkan Output')

if submit:
    st.success('Template siap. Silakan copy subject & isi email, lalu paste di Gmail dan kirim secara manual.')
    st.markdown('**Subject (copy):**')
    st.code(subject)
    st.markdown('**Isi email (copy):**')
    st.text_area('Isi email (untuk copy)', value=body, height=260)

    all_ok = all(checks)
    if all_ok:
        st.success('Semua checklist tercentang — lampiran lengkap.')
    else:
        missing = [it for it, ok in zip(check_items, checks) if not ok]
        st.warning(f'Checklist belum lengkap: {len(missing)} item belum dicentang.')

st.markdown('</div>', unsafe_allow_html=True)

render_footer()
