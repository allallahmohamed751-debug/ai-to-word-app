import streamlit as st
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from openai import OpenAI
import io

# إعدادات واجهة المستخدم
st.set_page_config(page_title="FormatFixer AI Pro", page_icon="🚀")
st.title("FormatFixer AI Pro 🚀")

# شريط جانبي لإدخال المفتاح
with st.sidebar:
    st.header("إعدادات الطاقة ⚙️")
    api_key = st.text_input("OpenAI API Key:", type="password")
    st.markdown("---")
    st.write("بناء: @allallahmohamed751")

# منطقة العمل الرئيسية
topic = st.text_input("ماذا تريد أن نكتب اليوم؟", placeholder="مثلاً: تقرير عن فوائد الذكاء الاصطناعي في الطب")

if st.button("توليد وتنسيق الملف 🪄"):
    if not api_key:
        st.error("الرجاء إدخال الـ API Key أولاً في القائمة الجانبية.")
    elif not topic:
        st.warning("أدخل موضوعاً لنبدأ العمل!")
    else:
        try:
            client = OpenAI(api_key=api_key)
            with st.spinner('جاري العصف الذهني وتنسيق الملف...'):
                # 1. طلب المحتوى من AI
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": f"اكتب موضوعاً كاملاً ومنسقاً عن {topic}. استخدم العناوين والجداول إذا لزم الأمر."}]
                )
                content = response.choices[0].message.content

                # 2. تحويل المحتوى إلى ملف Word منسق
                doc = Document()
                for line in content.split('\n'):
                    p = doc.add_paragraph(line)
                    # ميزة المليون دولار: دعم اتجاه النص العربي تلقائياً
                    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT 
                
                # 3. تجهيز الملف للتحميل
                bio = io.BytesIO()
                doc.save(bio)
                
                st.success("تم تجهيز مستندك باحترافية!")
                st.download_button(
                    label="تحميل ملف Word المنسق 📥",
                    data=bio.getvalue(),
                    file_name=f"{topic}.docx",
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                )
                
                st.markdown("### معاينة سريعة للمحتوى:")
                st.write(content)
        except Exception as e:
            st.error(f"حدث خطأ فني: {e}")
