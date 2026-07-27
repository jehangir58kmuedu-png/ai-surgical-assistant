import streamlit as st
import google.generativeai as genai
import os

st.set_page_config(page_title="AI Surgical Assistant", page_icon="🏥", layout="wide")

st.title("🏥 AI Surgical Assistant")
st.markdown("### Smart Clinical & Surgical Technology Guidance System")
st.write("An intelligent assistant designed for Surgical Technologists, Operating Theater (OT) staff, and healthcare professionals.")

SYSTEM_PROMPT = "You are 'AI Surgical Assistant', an expert AI designed specifically to guide Surgical Technologists and OT staff. Your task is to provide accurate, concise, and highly relevant clinical information."

api_key = st.secrets.get("GEMINI_API_KEY", os.getenv("GEMINI_API_KEY"))

if not api_key:
    st.error("⚠️ Please enter your Gemini API Key in Streamlit Secrets!")
else:
    genai.configure(api_key=api_key)
    
    st.header("💬 Ask AI Surgical Assistant")

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("✂️ Major Laparotomy Tray Setup"):
            st.session_state['user_prompt'] = "What are the essential instruments required for a Major Laparotomy setup?"
    with col2:
        if st.button("🧼 CSSD Autoclave Parameters"):
            st.session_state['user_prompt'] = "What are the standard time, temperature, and pressure requirements for steam autoclaving in CSSD?"
    with col3:
        if st.button("📋 Patient Case Summary Template"):
            st.session_state['user_prompt'] = "Provide a standard OT case presentation summary template for a surgical technologist."

    default_prompt = st.session_state.get('user_prompt', '')
    user_query = st.text_input("Enter your surgical query or clinical topic:", value=default_prompt)

    if st.button("Ask Assistant", type="primary"):
        if user_query:
            with st.spinner("Analyzing clinical request..."):
                try:
                    # Directly using standard model without extra beta paths
                    model = genai.GenerativeModel('gemini-1.5-flash')
                    full_prompt = f"{SYSTEM_PROMPT}\n\nUser Question: {user_query}"
                    response = model.generate_content(full_prompt)
                    
                    st.markdown("---")
                    st.subheader("💡 Assistant Response:")
                    st.write(response.text)
                except Exception:
                    try:
                        # Fallback for 2.0
                        model = genai.GenerativeModel('gemini-2.0-flash')
                        full_prompt = f"{SYSTEM_PROMPT}\n\nUser Question: {user_query}"
                        response = model.generate_content(full_prompt)
                        st.markdown("---")
                        st.subheader("💡 Assistant Response:")
                        st.write(response.text)
                    except Exception as err:
                        st.error(f"Error connecting to AI service: {err}")
        else:
            st.warning("Please enter a query or select a preset option above.")
