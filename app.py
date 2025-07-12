import streamlit as st

# Judul utama
st.title("Welcome to Chemistry Side⚗️")

# Sidebar untuk menu navigasi
select menu = st.sidebar.selectbox("Select Menu", ["Home", "About", "Contact"])

# Konten berdasarkan pilihan menu
if select menu == "Home":
    st.header("🏠 Home")
    st.write("This is your website's.")
elif select menu == "About":
    st.header("ℹ️ Tentang")
    st.write("This website is created to fulfill a project assignment.")
elif select menu == "Contact":
    st.header("📞 Contact")
    st.write("Contact us : lpk's group")
