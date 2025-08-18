import streamlit as st

st.set_page_config(page_title="Landing Page", page_icon="🌐", layout="centered")

st.title("Selamat Datang di Landing Page!")
st.subheader("Website Demo dengan Streamlit")

st.write("""
Ini adalah contoh landing page sederhana menggunakan Streamlit.
Silakan eksplorasi fitur-fitur yang tersedia di website ini.
""")

st.image("https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png", width=300)

st.button("Mulai Sekarang")