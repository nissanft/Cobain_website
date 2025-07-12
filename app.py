import streamlit as st
from PIL import Image

# Konfigurasi halaman
st.set_page_config(page_title="Chemistry Side ⚗️", page_icon="🧪", layout="centered")

# Judul utama
st.title("Welcome to Chemistry Side ⚗️")

# Sidebar untuk menu navigasi
st.sidebar.markdown("📁 Homepage")

# Sidebar selectbox
menu = st.sidebar.selectbox("Pilih Halaman", ["Home", "About", "Contact"])

# Konten berdasarkan pilihan menu
if menu == "Home":
    st.header("🏠 Home")
    st.write("This is your website's homepage. Let's explore the magic of chemistry!")
elif menu == "About":
    st.header("ℹ️ About")
    st.write("This website is created to fulfill a project assignment. Chemistry is fascinating!")
elif menu == "Contact":
    st.header("📞 Contact")
    st.write("Contact us: LPK's Group – we’re always up for a good science chat.")

# Sidebar next selectbox 1
fitur = st.sidebar.selectbox("🔬 Chem Elements", ["Periodic Table"])

# For Sidebar next selectbox 1
elif fitur == "Periodic Table":
    st.header("🧪 Periodic Table")
    st.write("Here's The Periodic Table – all elements")
    
# Footer
st.markdown("---")
st.markdown("<p style='text-align: center;'>© 2025 Chemistry Side ⚗️ Created with 💙 and Python.</p>", unsafe_allow_html=True)
