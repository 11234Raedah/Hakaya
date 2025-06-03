import streamlit as st

# عنوان التطبيق
st.title("حكايا أجدادنا")

# قائمة الحكايات (مخزنة مؤقتاً في الجلسة)
if "حكايات" not in st.session_state:
    st.session_state["حكايات"] = {}

# إضافة حكاية جديدة
st.header("أضف حكاية جديدة")
عنوان = st.text_input("ادخل عنوان الحكاية")
نص = st.text_area("ادخل نص الحكاية")

if st.button("حفظ الحكاية"):
    if عنوان.strip() == "" or نص.strip() == "":
        st.error("يرجى إدخال العنوان والنص معًا.")
    else:
        st.session_state["حكايات"][عنوان] = نص
        st.success(f"تم حفظ الحكاية بعنوان: {عنوان}")

# عرض الحكايات المحفوظة
st.header("الحكايات المحفوظة")
if st.session_state["حكايات"]:
    for عناوين, نصوص in st.session_state["حكايات"].items():
        st.subheader(عناوين)
        st.write(نصوص)
else:
    st.write("لا توجد حكايات محفوظة بعد.")
