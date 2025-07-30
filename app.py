import streamlit as st
import os
import csv
from mistral_client import generate_questions

# Candidate details saving function
def save_candidate(candidate_data):
    file_path = "candidates.csv"
    file_exists = os.path.isfile(file_path)
    with open(file_path, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=candidate_data.keys())
        if not file_exists:
            writer.writeheader()
        writer.writerow(candidate_data)

# Initialize session states
if "step" not in st.session_state:
    st.session_state.step = 0
if "candidate_data" not in st.session_state:
    st.session_state.candidate_data = {}
if "questions" not in st.session_state:
    st.session_state.questions = []
if "current_question" not in st.session_state:
    st.session_state.current_question = 0

# Greeting
st.title("🤖 TalentScout Hiring Assistant")
if st.session_state.step == 0:
    st.write("Welcome! I’m here to collect your details and ask you technical questions based on your tech stack.")
    if st.button("Start"):
        st.session_state.step = 1

# Information gathering
elif st.session_state.step == 1:
    st.header("📋 Candidate Information")
    name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    phone = st.text_input("Phone Number")
    exp = st.number_input("Years of Experience", min_value=0, max_value=50)
    position = st.text_input("Desired Position(s)")
    location = st.text_input("Current Location")
    tech_stack = st.text_input("Tech Stack (comma separated e.g., Python, Django, React)")

    if st.button("Submit Details"):
        st.session_state.candidate_data = {
            "Full Name": name,
            "Email": email,
            "Phone": phone,
            "Experience": exp,
            "Position": position,
            "Location": location,
            "Tech Stack": tech_stack
        }
        save_candidate(st.session_state.candidate_data)
        st.session_state.questions = generate_questions(tech_stack)
        st.session_state.step = 2

# Technical Questions
elif st.session_state.step == 2:
    st.header("🛠 Technical Questions")
    if st.session_state.current_question < len(st.session_state.questions):
        question = st.session_state.questions[st.session_state.current_question]
        st.write(f"**Q{st.session_state.current_question+1}:** {question}")
        answer = st.text_area("Your Answer", key=f"answer_{st.session_state.current_question}")
        
        if st.button("Next Question"):
            st.session_state.current_question += 1
            st.experimental_set_query_params()  # Clears text area
    else:
        st.success("✅ Thank you for completing the interview!")
        st.write("Your responses have been saved. We’ll contact you with next steps.")
