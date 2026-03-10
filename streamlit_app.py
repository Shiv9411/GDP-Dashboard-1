import streamlit as st
import google.generativeai as genai
from gtts import gTTS

# --- AI SETUP ---
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
APP_PASSWORD = "UP16" 

# --- LOCK ---
if "locked" not in st.session_state:
    st.session_state["locked"] = True

if st.session_state["locked"]:
    st.title("🔐 AI Studio Lock")
    pwd = st.text_input("Password (UP16):", type="password")
    if st.button("Unlock"):
        if pwd == APP_PASSWORD:
            st.session_state["locked"] = False
            st.rerun()
        else:
            st.error("Galat Password!")
    st.stop()

# --- APP ---
st.title("🤖 Titan AI: Avatar Studio")
topic = st.text_input("Topic Likhein:", placeholder="Ex: Futuristic Farming Robot...")

if st.button("🚀 Start Production"):
    if topic:
        model = genai.GenerativeModel('gemini-1.5-flash')
        with st.status("AI Kaam kar raha hai..."):
            st.subheader("🎭 AI Avatar Design")
            res = model.generate_content(f"Describe a unique AI avatar for: {topic}. No real humans.")
            st.info(res.text)
            st.subheader("📝 Script")
            s_res = model.generate_content(f"Write a viral script in Hindi for: {topic}")
            st.write(s_res.text)
            tts = gTTS(text=s_res.text[:300], lang='hi')
            tts.save("v.mp3")
            st.audio("v.mp3")
        st.balloons()
