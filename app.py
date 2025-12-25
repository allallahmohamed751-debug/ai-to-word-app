import streamlit as st
from docx import Document
import io

st.set_page_config(page_title="FormatFixer AI", page_icon="📄")
st.title("FormatFixer AI 🚀")
st.write("حول نصوص AI إلى ملفات Word منسقة")

text_input = st.text_area("ألصق النص هنا:", height=300)

if st.button("تحويل إلى Word"):
    if text_input:
        doc = Document()
        for line in text_input.split('\n'):
            doc.add_paragraph(line)
        bio = io.BytesIO()
        doc.save(bio)
        st.download_button(label="تحميل الملف 📥", data=bio.getvalue(), file_name="AI_Document.docx")
    else:
        st.error("الرجاء لصق النص أولاً")
