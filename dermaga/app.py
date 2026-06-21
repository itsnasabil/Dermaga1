"""
DERMAGA – Dashboard Elektronik Magang BPS Kota Semarang
Entry point: jalankan dengan  streamlit run app.py
"""

# Streamlit multipage: halaman pertama otomatis dari Halaman_Muka.py
# File ini hanya sebagai entry alias jika user ingin run dari root folder

import subprocess, sys, os
<meta name="google-site-verification" content="ttRf-6fP_HKFr5CiFzOukh_ibe-x5pReEmNwvau6ung" />

if __name__ == "__main__":
    # Ensure we run Halaman_Muka.py from this package directory
    base = os.path.dirname(__file__)
    halaman = os.path.join(base, "Halaman_Muka.py")
    subprocess.run([sys.executable, "-m", "streamlit", "run", halaman])
