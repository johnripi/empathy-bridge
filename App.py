import streamlit as st

st.set_page_config(page_title="EmpathyBridge AI", page_icon="🤝", layout="centered")

st.title("🤝 EmpathyBridge AI")
st.subheader("Ο Μεταφραστής σου είναι Σχεδόν Έτοιμος!")

st.info("Η εφαρμογή σου είναι ζωντανή στο ίντερνετ! Στο επόμενο βήμα θα συνδέσουμε το 'μυαλό' της AI και το ταμείο πληρωμών.")

text = st.text_area("Γράψε ένα μήνυμα για δοκιμή:", placeholder="Πληκτρολόγησε εδώ...")
tone = st.selectbox("Επίλεξε Τόνο:", ["Επαγγελματικός", "Φιλικός", "Ενσυναίσθητος"])

if st.button("Δοκιμαστική Μετάφραση"):
    st.success(f"Το κουμπί δουλεύει! Επιλέξατε τον τόνο: {tone}")
  
