import streamlit as st
import os

# المجلد اللي تنحفظ فيه الحكايات
FOLDER = "hikayat"

# إنشاء المجلد إذا ما كان موجود
if not os.path.exists(FOLDER):
    os.makedirs(FOLDER)

# واجهة التطبيق
st.title("📚 حكايا أجدادنا")
st.write("منصة لتوثيق ومشاركة قصص الأجداد")

# تبويب الحكايات
tab1, tab2 = st.tabs(["✍️ أرسل حكايتك", "📖 عرض الحكايات"])

with tab1:
    title = st.text_input("عنوان الحكاية")
    story = st.text_area("اكتب الحكاية هنا")
    if st.button("حفظ الحكاية"):
        if title and story:
            with open(f"{FOLDER}/{title}.txt", "w", encoding="utf-8") as f:
                f.write(story)
            st.success("✅ تم حفظ الحكاية بنجاح!")
        else:
            st.warning("⚠️ الرجاء كتابة عنوان ونص الحكاية.")

with tab2:
    files = os.listdir(FOLDER)
    if not files:
        st.info("لا توجد حكايات محفوظة بعد.")
    else:
        for filename in files:
            with open(f"{FOLDER}/{filename}", "r", encoding="utf-8") as f:
                content = f.read()
            st.subheader(f"📌 {filename.replace('.txt', '')}")
            st.write(content)
