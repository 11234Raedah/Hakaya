import streamlit as st
import os

FOLDER = "hikayat"
if not os.path.exists(FOLDER):
    os.makedirs(FOLDER)

st.title("📚 حكايا أجدادنا")
st.write("منصة لتوثيق ومشاركة قصص الأجداد")

tab1, tab2 = st.tabs(["✍️ أرسل حكايتك", "🔒 عرض الحكايات (خاص)"])

with tab1:
    title = st.text_input("عنوان الحكاية", key="title_input")
    story = st.text_area("اكتب الحكاية هنا", key="story_textarea")
    if st.button("حفظ الحكاية", key="save_button"):
        if title and story:
            with open(f"{FOLDER}/{title}.txt", "w", encoding="utf-8") as f:
                f.write(story)
            st.success("✅ تم حفظ الحكاية بنجاح!")
        else:
            st.warning("⚠️ الرجاء كتابة عنوان ونص الحكاية.")

with tab2:
    password = st.text_input("أدخل كلمة المرور لعرض الحكايات", type="password", key="password_input")
    if password == "Raedah112233434":
        files = os.listdir(FOLDER)
        if not files:
            st.info("لا توجد حكايات محفوظة بعد.")
        else:
            for filename in files:
                with open(f"{FOLDER}/{filename}", "r", encoding="utf-8") as f:
                    content = f.read()
                st.subheader(f"📌 {filename.replace('.txt', '')}")
                st.write(content)
    elif password != "":
        st.error("🚫 كلمة المرور خاطئة!")
