import streamlit as st
import streamlit.components.v1 as components

# Baca file HTML
with open("index.html", "r", encoding="utf-8") as f:
    html_code = f.read()

# Tampilkan di Streamlit
st.set_page_config(page_title="E-Bisnis", layout="wide")
st.title("Demo E-Bisnis - HTML di Streamlit")
components.html(html_code, height=800, scrolling=True)
