import streamlit as st

# Judul utama
st.title("Welcome to Chemistry Side⚗️")

# Sidebar untuk menu navigasi
menu = st.sidebar.selectbox("Homepage", ["Home", "About", "Contact"])

# Konten berdasarkan pilihan menu
if menu == "Home":
    st.header("🏠 Home")
    st.write("This is your website's.")
elif menu == "About":
    st.header("ℹ️ Tentang")
    st.write("This website is created to fulfill a project assignment.")
elif menu == "Contact":
    st.header("📞 Contact")
    st.write("Contact us : lpk's group")

menu = st.sidebar.selectbox (["Periodik Unsur"])

if menu == "Periodik Unsur":
    st.header("The Elements of The Periodic Table 🧪 ˗ˏˋ꒰𖦹｡")
    st.write("Here's The Periodic Table")
