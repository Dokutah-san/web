import streamlit as st
import os

# Konfigurasi Halaman
st.set_page_config(page_title="Reggy Feraldin - CV", page_icon="📄", layout="centered")

# Inisialisasi foto profil default jika belum ada yang di-upload
if 'photo_path' not in st.session_state:
    st.session_state.photo_path = "https://via.placeholder.com/150"

# --- SIDEBAR UNTUK UPLOAD FOTO ---
with st.sidebar:
    st.header("🖼️ Settings")
    uploaded_file = st.file_uploader("Upload Foto Profil Baru", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        # Simpan file sementara atau langsung tampilkan dari bytes
        st.session_state.photo_path = uploaded_file
        st.success("Foto berhasil diperbarui!")

# --- HEADER / PROFIL ---
col_img, col_text = st.columns([1, 2])

with col_img:
    # Menampilkan foto profil (bisa dari URL atau file yang di-upload)
    st.image(st.session_state.photo_path, width=150)

with col_text:
    st.title("Reggy Feraldin")
    st.subheader("Electronic Systems Engineering Student & Developer")
    st.write("📍 Pekanbaru, Riau, Indonesia")
    st.write("✉️ email@example.com | 🌐 [LinkedIn](https://linkedin.com) | 💻 [GitHub](https://github.com)")

st.markdown("---")

# --- TENTANG SAYA ---
st.header("👤 About Me")
st.write("""
I am an Electronic Systems Engineering student focusing on embedded systems development, 
microcontroller programming, and software development using Python. 
I enjoy solving technical problems and building projects that bridge the gap between hardware and software.
""")

st.markdown("---")

# --- RIWAYAT PENDIDIKAN ---
st.header("🎓 Education")
c1, c2 = st.columns([3, 1])
with c1:
    st.markdown("**Caltex Riau Polytechnic**")
    st.write("Bachelor of Applied Science (D4) in Electronic Systems Engineering")
with c2:
    st.write("2024 - Present")

st.markdown("---")

# --- KEAHLIAN / SKILLS ---
st.header("🛠️ Technical Skills")
sk1, sk2 = st.columns(2)
with sk1:
    st.markdown("**Programming & Software:**")
    st.write("- Python, C / C++, HTML, CSS, MySQL")
with sk2:
    st.markdown("**Electronics & Hardware:**")
    st.write("- Raspberry Pi, ATmega328p, Z80, Proteus")

st.markdown("---")

# --- PROYEK ---
st.header("🚀 Featured Projects")
st.markdown("**1. Modern Audio Encryption System (AES-256 GCM)**")
st.write("Python implementation of AES-256 GCM algorithm to secure cryptographic operations for .wav audio tracks.")

st.markdown("**2. DC Motor Speed Control via PWM (Raspberry Pi)**")
st.write("Developing precise embedded automation using Raspberry Pi GPIO lines to generate constant PWM frequency signals.")
