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
                try:
                    # Dynamically get active models for this API Key
                    active_models = []
                    for m in genai.list_models():
                        if 'generateContent' in m.supported_generation_methods:
                            active_models.append(m.name)

                    # List of stable models to attempt in order
                    target_models = [
                        'models/gemini-2.5-flash',
                        'models/gemini-1.5-flash',
                        'models/gemini-1.5-pro'
                    ]

                    chosen_model = None
                    for tm in target_models:
                        if tm in active_models:
                            chosen_model = tm
                            break

                    # Fallback to any model in active list if specific match not found
                    if not chosen_model and active_models:
                        chosen_model = active_models[0]

                    if not chosen_model:
                        st.error("No active Gemini models found for this API key.")
                    else:
                        model = genai.GenerativeModel(chosen_model)
                        full_prompt = f"{SYSTEM_PROMPT}\n\nUser Question: {user_query}"
                        response = model.generate_content(full_prompt)
                        
                        st.markdown("---")
                        st.subheader("💡 Assistant Response:")
                        st.write(response.text)

                except Exception as e:
                    st.error(f"Error connecting to AI service: {e}")
        else:
            st.warning("Please enter a query or select a preset option above.")
        '
