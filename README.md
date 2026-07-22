# 🏥 AI Surgical Assistant

An intelligent, real-time clinical decision-support application built for **Surgical Technologists, Operating Theater (OT) Technicians, and Healthcare Students**. This application helps OT staff quickly access surgical instrument guides, tray setup procedures, CSSD sterilization guidelines, and preoperative checklists.

---

## 🔗 Live Application & Links

* **Live Deployed App:** *(Deployment ke baad live link yahan aayega)*
* **Public GitHub Repository:** `https://github.com/jehangir58kmuedu-png/ai-surgical-assistant`

---

## ✨ Features List

1. **Surgical Tray & Setup Guide:** Detailed list of required instruments for major procedures (e.g., Laparotomy, Orthopedic, Vascular)[span_0](start_span)[span_0](end_span).
2. **CSSD & Sterilization Protocols:** Precise guidelines on steam autoclaving, ETO sterilization, washer-disinfector parameters, and biological indicators[span_1](start_span)[span_1](end_span).
3. **Preoperative & OT Checklist Assistant:** Generates standardized safety checklists compliant with WHO surgical safety standards[span_2](start_span)[span_2](end_span).
4. **Interactive AI Clinical Search:** Accepts custom clinical queries and generates structured, professional healthcare advice instantly[span_3](start_span)[span_3](end_span).
5. **Quick One-Tap Prompts:** Instant presets for high-frequency surgical technician workflows[span_4](start_span)[span_4](end_span).

---

## 🤖 The AI Feature & System Prompt

The application utilizes **Google Gemini 1.5 Flash AI** model integrated via the `google-generativeai` SDK[span_5](start_span)[span_5](end_span). 

### System Prompt Behind the AI:
```text
You are 'AI Surgical Assistant', an expert AI advisor specialized in Surgical Technology, Operating Theater (OT) protocols, Surgical Instruments, Sterilization (CSSD), and Clinical Workflows.
Your task is to provide accurate, concise, and highly professional clinical assistance to surgical technologists, OT nurses, and medical students.

Guidelines:
1. Provide clear, structured, and easy-to-read answers (use bullet points and bold headers).
2. Detail proper sterilization parameters, tray assembly procedures, and surgical steps when asked.
3. Always include standard safety precautions for OT environments.
4. Maintain a supportive, professional healthcare tone.
