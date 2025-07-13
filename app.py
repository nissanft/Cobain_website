import streamlit as st
from PIL import Image

#=====================================================================================
# HALAMAN UTAMA
#=====================================================================================

#Konfigurasi halaman
st.set_page_config(page_title="Chemistry Side ⚗️", page_icon="🧪", layout="centered")

#Judul utama
st.title("Welcome to Chemistry Side ⚗️")
st.write("This is your website's homepage. Let's explore the magic of chemistry!")

#Sidebar untuk menu navigasi
st.sidebar.markdown("📁 Dashboard")

#Sidebar selectbox
menu = st.selectbox (["Homepage", "About", "Contact"])

#Konten berdasarkan pilihan menu
if menu == "About":
    st.header("ℹ️ About")
    st.write("This website is created to fulfill a project assignment. Chemistry is fascinating!")
elif menu == "Contact":
    st.header("📞 Contact")
    st.write("Contact us: LPK's Group – we’re always up for a good science chat.")


# Daftar halaman yang tersedia
pages = ["Periodic Table", "Calculator Mass"]

# Validasi dan set default halaman
if 'page' not in st.query_params or st.query_params.page not in pages:
    st.query_params.page = "Periodic Table"

default_index = pages.index(st.query_params.page)

# Komponen radio di sidebar untuk navigasi halaman
page = st.sidebar.radio(
    "🔬 Chem Elements",
    pages,
    key="page_selector",
    index=default_index
)

# Tampilkan konten berdasarkan pilihan halaman
if page == "Periodic Table":
    st.header("🧪 Periodic Table")
    st.markdown("Here's The Periodic Table – all elements")

elif page == "Calculator Mass":
    st.header("🧮 Calculator Mass")
    st.write("Masukkan data untuk menghitung massa molar.")

# Jika terjadi perubahan halaman, perbarui query dan bersihkan parameter lainnya
if st.query_params.page != page:
    st.query_params.page = page
    keys_to_clear = [k for k in st.query_params if k != 'page']
    for k in keys_to_clear:
        del st.query_params[k]
    st.rerun()

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center;'>© 2025 Chemistry Side ⚗️ Created with 💙 and Python.</p>", unsafe_allow_html=True)
