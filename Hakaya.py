import streamlit as st
import os

# إعدادات الصفحة
st.set_page_config(
    page_title="حكايا أجدادنا",
    page_icon="🧓🏻",
    layout="centered"
)

# تخصيص الستايل
st.markdown("""
    <style>
        body {
            background-color: #f5f0e6;
        }
        .block-container {
            background-color: #fffdf7;
            padding: 2rem;
            border-radius: 15px;
            border: 2px solid #c8b28e;
        }
        h1, h2, h3, h4 {
            color: #5c4328;
            font-family: 'Cairo', sans-serif;
        }
        .logo {
            position: absolute;
            top: 15px;
            right: 15px;
            width: 100px;
        }
        footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# عرض الشعار
st.image("logo.png", width=100)

# ✅ عنوان التطبيق
st.title("حكايا أجدادنا")

# ✅ العبارة التراثية
st.markdown("### نحفظ تراثنا.. بصوت أجدادنا 🎤")
