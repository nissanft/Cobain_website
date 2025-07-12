import streamlit as st

# Judul utama
st.title("Selamat Datang di Website Nissa 💻")

# Sidebar untuk menu navigasi
menu = st.sidebar.selectbox("Pilih Menu", ["Beranda", "Tentang", "Kontak"])

# Konten berdasarkan pilihan menu
if menu == "Beranda":
    st.header("🏠 Beranda")
    st.write("Ini adalah halaman utama website kamu.")
elif menu == "Tentang":
    st.header("ℹ️ Tentang")
    st.write("Website ini dibuat menggunakan Python dan Streamlit.")
elif menu == "Kontak":
    st.header("📞 Kontak")
    st.write("Hubungi saya di: nissa@example.com")
