import streamlit as st
import os

‎# إعدادات الصفحة
st.set_page_config(
    page_title="حكايا أجدادنا",
    page_icon="🧓🏻",
    layout="centered"
)

‎# تخصيص التصميم (ألوان + خط + لوقو)
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
        h1, h2, h3, h4, p, label, div, span {
            color: #4b2e1e !important; /* بني غامق */
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

‎# عرض الشعار
st.image("logo.png", width=100)

‎# عنوان التطبيق
st.title("حكايا أجدادنا")

‎# العبارة التراثية
st.markdown("### نحفظ تراثنا.. بصوت أجدادنا 🎤")

‎# واجهة المستخدم
st.subheader("أضف حكايتك أو استعرض الحكايات")

‎# مجلد الحكايات
folder = "حكايات"
os.makedirs(folder, exist_ok=True)

‎# اختيار العملية
option = st.radio("اختر ما ترغب بفعله:", ["إضافة حكاية", "عرض الحكايات"])

if option == "إضافة حكاية":
    title = st.text_input("عنوان الحكاية")
    content = st.text_area("نص الحكاية")
    password = st.text_input("كلمة السر", type="password")

    if st.button("حفظ"):
        if password == "Raedah112233434":
            if title and content:
                with open(f"{folder}/{title}.txt", "w", encoding="utf-8") as f:
                    f.write(content)
                st.success(f"✅ تم حفظ الحكاية: {title}")
            else:
                st.warning("يرجى كتابة عنوان ونص الحكاية.")
        else:
            st.error("❌ كلمة السر غير صحيحة.")

elif option == "عرض الحكايات":
    stories = os.listdir(folder)
    if not stories:
        st.info("لا توجد حكايات محفوظة بعد.")
    else:
        selected = st.selectbox("اختر الحكاية", stories)
        with open(f"{folder}/{selected}", "r", encoding="utf-8") as f:
            st.text(f.read())
