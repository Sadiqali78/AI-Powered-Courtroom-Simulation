import streamlit as st
from interface.ui import setup_ui
from utils.file_handler import extract_text
from agents.client_agent import handle_client_input
from agents.law_research_agent import retrieve_laws
from agents.logic_analyzer import analyze_logic
from agents.legal_advisor import provide_legal_advice
from agents.opponent_lawyer import generate_counter_arguments
from agents.ai_judge import give_verdict

st.set_page_config(page_title="AI-Virtual Courtroom Simulation", layout="wide")
st.title("⚖️ AI-Virtual Courtroom Simulation")

setup_ui()

st.markdown("### 👨‍💼 Step 1: Upload Your Case File")
uploaded_file = st.file_uploader("Upload Legal Document", type=["pdf", "txt", "png", "jpg", "jpeg"])

if uploaded_file:
    case_text = extract_text(uploaded_file)
    st.success("✅ Case document processed successfully!")
    st.markdown("### 📄 Extracted Case Text:")
    st.write(case_text)

    st.markdown("### 🧑‍⚖️ Step 2: Click Below to Begin the Courtroom Simulation")
    if st.button("Start Courtroom Simulation"):
        with st.spinner("Processing as Client Agent..."):
            client_input = handle_client_input(case_text)
            st.markdown("#### 👨‍💼 Client Agent")
            st.write(client_input)

        with st.spinner("Researching relevant laws..."):
            laws = retrieve_laws(client_input)
            st.markdown("#### 📚 Law Research Agent")
            st.write(laws)

        with st.spinner("Analyzing logic and consistency..."):
            logic_report = analyze_logic(client_input, laws)
            st.markdown("#### 🔍 Logic Analyzer")
            st.write(logic_report)

        with st.spinner("Generating legal advice..."):
            legal_advice = provide_legal_advice(logic_report, laws)
            st.markdown("#### 👨‍⚖️ Legal Advisor")
            st.write(legal_advice)

        with st.spinner("Generating opposing arguments..."):
            counter_args = generate_counter_arguments(client_input)
            st.markdown("#### 🗣️ Opponent Lawyer")
            st.write(counter_args)

        with st.spinner("Delivering final verdict..."):
            verdict = give_verdict(client_input, legal_advice, counter_args)
            st.markdown("#### 🏛️ AI Judge Verdict")
            st.success(verdict)
