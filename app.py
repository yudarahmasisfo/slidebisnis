# import streamlit as st
# import streamlit.components.v1 as components

# # Baca file HTML
# with open("index.html", "r", encoding="utf-8") as f:
#     html_code = f.read()

# # Tampilkan di Streamlit
# st.set_page_config(page_title="E-Bisnis", layout="wide")
# st.title("Demo E-Bisnis - HTML di Streamlit")
# components.html(html_code, height=800, scrolling=True)

import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(page_title="E-Bisnis App", layout="wide")

st.sidebar.title("📑 Navigasi")
st.sidebar.write("Pilih halaman untuk ditampilkan")

# Cari semua file html di folder
html_files = [f for f in os.listdir() if f.endswith(".html")]

# Buat menu otomatis dari nama file
menu = st.sidebar.selectbox("Halaman:", html_files)

# Baca file HTML yang dipilih
with open(menu, "r", encoding="utf-8") as f:
    html_content = f.read()

# Tampilkan file HTML
st.title(f"Halaman: {menu.replace('.html', '').capitalize()}")
components.html(html_content, height=800, scrolling=True)
