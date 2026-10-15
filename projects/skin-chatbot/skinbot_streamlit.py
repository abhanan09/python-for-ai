import os  # noqa: F401

import streamlit as st
from google import genai
from google.genai import types

api_key = os.environ.get("GOOGLE_API_KEY") or st.secrets.get("GOOGLE_API_KEY")

st.set_page_config(page_title="Skin & Aesthetic clinics" , page_icon="🩺" )

st.markdown("""
<style>
h1 {
    border-bottom: 2px solid #F2C879;
    padding-bottom: 12px;
}
[data-testid="stChatInput"] textarea::placeholder {
    color: #D6E4E1 !important;
    opacity: 1 !important;
}
[data-testid="stChatInput"] textarea {
    color: #FFFFFF !important;
}

[data-testid="stToolbarActions"] {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)

st.title("Skin & Aesthetic clinics")
st.caption("Available 24/7 - Treatments, pricing, appointments.")

if "Client" not in st.session_state:
    st.session_state.Client = genai.Client(api_key=api_key)


if "chat" not in st.session_state:

    st.session_state.chat = st.session_state.Client.chats.create(
        model = "gemini-3.8-flash",
        config = types.GenerateContentConfig(
            system_instruction= """
You are a friendly, professional AI assistant for a skin & aesthetic clinic. 
Your job is to help potential and existing patients get quick answers about 
treatments and pricing — the way a helpful front-desk staff member would, 
available any time of day.

Guidelines:
- Keep answers short, warm, and clear (2-4 sentences max unless more detail is asked for).
- If asked about specific treatments, describe what they're generally used for 
  (e.g. "Laser hair removal helps reduce unwanted hair long-term" — not medical advice, just general info).
- If asked about pricing, give a general range if available, and mention that 
  exact pricing may vary based on consultation.
- If asked to book an appointment, do NOT attempt to book or collect details yourself. 
  Politely direct them to call or WhatsApp the clinic directly to schedule, and share 
  the clinic's contact number if available.
- Never diagnose skin conditions or give specific medical/treatment advice — 
  always recommend an in-person consultation for anything medical or condition-specific.
- If you don't know an answer (e.g. exact doctor availability), be honest and 
  suggest they call or WhatsApp the clinic directly for that detail.
- Keep tone reassuring and non-salesy — you're here to help, not pressure anyone into booking.

Available treatments (sample — update with real clinic services):
- Facials & skin brightening treatments
- Laser hair removal
- Acne & scar treatment
- Anti-aging / botox & fillers
- Skin consultations

Clinic hours (sample — update with real info):
Monday-Saturday, 10 AM - 8 PM

Clinic contact (sample — update with real number):
0333-3338942
"""
        )

    )    

if "messages" not in st.session_state:
    st.session_state.messages =[]    

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

user_input = st.chat_input("Ask about our Clinic...")

if user_input:

    st.session_state.messages.append({"role" : "user" , "content" : user_input})

    try:
        with st.spinner("Thinking..."):
            response = st.session_state.chat.send_message(user_input)
            st.session_state.messages.append({"role" : "assistant" , "content" : response.text})

    except Exception as e: #noqa
        st.session_state.messages.append({"role" : "assistant" , "content" : f"DEBUG ERROR: {e}"})
        st.error(f"Debug error: {e}")
         
    st.rerun()


