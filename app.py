import streamlit as st
import google.generativeai as genai
import os

# Page Configuration
st.set_page_config(
    page_title="AI Surgical Assistant",
    page_icon="🏥",
    layout="wide"
)

# Title & Description
st.title("🏥 AI Surgical Assistant")
st.markdown("### Smart Clinical & Surgical Technology Guidance System")
st.write("An intelligent assistant designed for Surgical Technologists, Operating Theater (OT) staff, and healthcare professionals.")

# System Prompt
SYSTEM_PROMPT = """
You are 'AI Surgical Assistant', an expert AI designed specifically to guide Surgical Technologists and OT staff.
Your task is to provide accurate, concise, and highly relevant clinical information.

Guidelines:
1. Provide clear, structured, step-by-step guidance.
2. Detail pre-operative, intra-operative, and post-operative procedures accurately.
3. Always include relevant safety precautions, infection control measures, and instrument specifics.
4. Maintain a professional, helpful, and concise tone.
"""

# Get API Key from Secrets or Environment
api_key = st.secrets.get("GEMINI_API_KEY", os.getenv("GEMINI_API_KEY"))

if not api_key:
    st.error("⚠️ Please enter your Gemini API Key in Streamlit Secrets!")
else:
    genai.configure(api_key=api_key)
    
    # UI Interface
    st.header("💬 Ask AI Surgical Assistant")

    # Prompt Buttons
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

    # User Input Field
    default_prompt = st.session_state.get('user_prompt', '')
    user_query = st.text_input("Enter your surgical query or clinical topic:", value=default_prompt)

    if st.button("Ask Assistant", type="primary"):
        if user_query:
            with st.spinner("Analyzing clinical request..."):
                # Try recommended Gemini 2.5/2.0 models first
                models_to_try = [
                    'gemini-2.5-flash',
                    'gemini-2.0-flash',
                    'gemini-1.5-flash-8b'
                ]
                
                response_text = None
                last_error = None

                for model_name in models_to_try:
                    try:
                        model = genai.GenerativeModel(model_name)
                        full_prompt = f"{SYSTEM_PROMPT}\n\nUser Question: {user_query}"
                        res = model.generate_content(full_prompt)
                        response_text = res.text
                        break
                    except Exception as e:
                        last_error = e
                        continue

                if response_text:
                    st.markdown("---")
                    st.subheader("💡 Assistant Response:")
                    st.write(response_text)
                else:
                    st.error(f"Error connecting to AI service: {last_error}")
        else:
            st.warning("Please enter a query or select a preset option above.")
