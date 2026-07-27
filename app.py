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

# Sidebar for API Key input and info
with st.sidebar:
    st.header("⚙️ Configuration")
    api_key_input = st.text_input("Enter Gemini API Key:", type="password", help="Enter your Google AI Studio API key here.")
    st.markdown("---")
    st.subheader("📌 Key Modules")
    st.markdown("- **Surgical Instrument Guide**")
    st.markdown("- **Tray Setup & OR Workflows**")
    st.markdown("- **CSSD & Sterilization Protocols**")
    st.markdown("- **Patient Case Summarizer**")

# System Prompt Definition
SYSTEM_PROMPT = """
You are 'AI Surgical Assistant', an expert AI advisor specialized in Surgical Technology, Operating Theater (OT) protocols, Surgical Instruments, Sterilization (CSSD), and Clinical Workflows.
Your task is to provide accurate, concise, and highly professional clinical assistance to surgical technologists, OT nurses, and medical students.

Guidelines:
1. Provide clear, structured, and easy-to-read answers (use bullet points and bold headers).
2. Detail proper sterilization parameters, tray assembly procedures, and surgical steps when asked.
3. Always include standard safety precautions for OT environments.
4. Maintain a supportive, professional healthcare tone.
"""

# Get API Key from environment or input
api_key = api_key_input or os.environ.get("GEMINI_API_KEY")

if not api_key:
    st.warning("⚠️ Please enter your Gemini API Key in the sidebar to start using the assistant.")
else:
    try:
        genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash-latest')

        # Chat interface
        st.subheader("💬 Ask AI Surgical Assistant")
        
        # Quick Prompt Buttons
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("✂️ Major Laparotomy Tray Setup"):
                st.session_state['user_prompt'] = "What are the essential instruments required for a Major Laparotomy tray setup?"
        with col2:
            if st.button("🧼 CSSD Autoclave Parameters"):
                st.session_state['user_prompt'] = "Explain standard steam sterilization time, temperature, and pressure parameters in CSSD."
        with col3:
            if st.button("📋 Patient Case Summary Template"):
                st.session_state['user_prompt'] = "Generate a standard OT preoperative surgical checklist and patient case summary template."

        user_query = st.text_input("Enter your surgical query or clinical topic:", value=st.session_state.get('user_prompt', ''))

        if st.button("Ask Assistant", type="primary"):
            if user_query:
                with st.spinner("Analyzing clinical request..."):
                    full_prompt = f"{SYSTEM_PROMPT}\n\nUser Query: {user_query}"
                    response = model.generate_content(full_prompt)
                    st.success("Analysis Complete!")
                    st.markdown("### 💡 Response:")
                    st.markdown(response.text)
            else:
                st.info("Please enter a query or select a quick topic above.")

    except Exception as e:
        st.error(f"Error connecting to AI service: {e}")
