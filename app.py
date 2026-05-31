import streamlit as st
import openai

st.set_page_config(page_title="EmpathyBridge", page_icon="🤝")
st.title("🤝 EmpathyBridge AI")

api_key = st.text_input("Βάλε το OpenAI API Key σου:", type="password")
text = st.text_area("Γράψε το μήνυμα για μετάφραση:")
language = st.selectbox("Γλώσσα:", ["Αγγλικά", "Γερμανικά", "Γαλλικά"])
tone = st.selectbox("Τόνος:", ["Επαγγελματικός", "Φιλικός", "Ενσυναίσθητος"])

if st.button("Μετάφραση"):
    if not api_key:
        st.error("Βάλε πρώτα το κλειδί!")
    else:
        try:
            client = openai.OpenAI(api_key=api_key)
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "Analyse the input, translate to the target language and explain the context."},
                    {"role": "user", "content": f"Translate to {language} with {tone} tone: {text}"}
                ]
            )
            st.success(response.choices.message.content)
        except Exception as e:
            st.error(f"Σφάλμα: {e}")
            
