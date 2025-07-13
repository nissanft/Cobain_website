import streamlit as st
from PIL import Image

#=====================================================================================
# HALAMAN UTAMA
#=====================================================================================

"""Konfigurasi halaman"""
st.set_page_config(page_title="Chemistry Side ⚗️", page_icon="🧪", layout="centered")

"""Judul utama"""
st.title("Welcome to Chemistry Side ⚗️")
st.write("This is your website's homepage. Let's explore the magic of chemistry!")

placeholder = st.empty()

"""Sidebar untuk menu navigasi"""
st.sidebar.markdown("📁 Dashboard")

"""Sidebar selectbox"""
menu = st.sidebar.selectbox("Homepage", ["Homepage", "About", "Contact"])
fitur = st.sidebar.selectbox("🔬 Chem Elements", ["Element", "Periodic Table"])

"""Konten berdasarkan pilihan menu"""
def tampilkan_menu(menu):
    if menu == "About":
        st.header("ℹ️ About")
        st.write("This website is created to fulfill a project assignment. Chemistry is fascinating!")
    elif menu == "Contact":
        st.header("📞 Contact")
        st.write("Contact us: LPK's Group – we’re always up for a good science chat.")

"""For Sidebar next selectbox 1"""
def tampilkan_fitur(fitur):
    if fitur == "Periodic Table":
        st.header("🧪 Periodic Table")
        st.write("Here's The Periodic Table – all elements")

# Ambil query params
query = st.query_params
menu = query.get("menu", "About")
fitur = query.get("fitur", "Periodic Table")

# Sidebar interaktif
selected_menu = st.sidebar.selectbox("Pilih Menu", ["About", "Contact"], index=["About", "Contact"].index(menu))
selected_fitur = st.sidebar.selectbox("Pilih Fitur", ["Periodic Table"], index=0)

# Update query params jika ada perubahan
if selected_menu != menu or selected_fitur != fitur:
    st.query_params.update({
        "menu": selected_menu,
        "fitur": selected_fitur
    })

# Tampilkan konten
tampilkan_menu(selected_menu)
tampilkan_fitur(selected_fitur)


# Footer
st.markdown("---")
st.markdown("<p style='text-align: center;'>© 2025 Chemistry Side ⚗️ Created with 💙 and Python.</p>", unsafe_allow_html=True)
