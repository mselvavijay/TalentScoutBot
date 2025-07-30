import streamlit as st
import csv
from mistral_client import generate_questions_with_mistral
from prompts import FALLBACK_QUESTIONS

CSV_FILE = "candidates.csv"

def save_candidate(candidate_data):
    try:
        with open(CSV_FILE, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(candidate_data.values())
    except Exception as e:
        st.error(f"Error saving candidate data: {e}")

st.set_page_config(page_title="TalentScout - Hiring Assistant", layout="centered")
st.title("😀 TalentScout - Hiring Assistant")

if "step" not in st.session_state:
    st.session_state.step = "greeting"
if "questions" not in st.session_state:
    st.session_state.questions = []
if "answers" not in st.session_state:
    st.session_state.answers = {}
if "current_q" not in st.session_state:
    st.session_state.current_q = 0

# Step 1: Greeting
if st.session_state.step == "greeting":
    st.subheader("👋 Welcome!")
    st.write("Hello! Welcome to **TalentScout**, your smart hiring assistant.")
    st.write("I’ll collect your details and then ask technical questions based on your tech stack.")
    if st.button("Start"):
        st.session_state.step = "form"
        st.rerun()

# Step 2: Candidate details form
elif st.session_state.step == "form":
    with st.form("candidate_form"):
        st.subheader("📝 Candidate Details")
        name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        phone = st.text_input("Phone Number")
        experience = st.text_input("Years of Experience")
        position = st.text_input("Desired Position(s)")
        location = st.text_input("Current Location")
        tech_stack = st.text_input("Tech Stack (comma separated)")

        submit_btn = st.form_submit_button("Submit Details")

        if submit_btn:
            # Exit keyword check
            if any(exit_word in [name, email, phone, experience, position, location, tech_stack] for exit_word in ["exit", "quit"]):
                st.session_state.step = "end"
                st.rerun()

            st.session_state.candidate_data = {
                "Name": name,
                "Email": email,
                "Phone": phone,
                "Experience": experience,
                "Position": position,
                "Location": location,
                "Tech Stack": tech_stack
            }
            save_candidate(st.session_state.candidate_data)

            # Call Mistral API
            questions_text = generate_questions_with_mistral(tech_stack)

            # Debug: Show raw questions
            st.write("🔍 Debug: Questions returned by API/fallback")
            st.code(questions_text)

            st.session_state.questions = [q.strip() for q in questions_text.split("\n") if q.strip()]
            st.session_state.step = "questions"
            st.success("✅ Candidate details saved!")
            st.rerun()

# Step 3: Questions
elif st.session_state.step == "questions":
    if st.session_state.current_q < len(st.session_state.questions):
        q_text = st.session_state.questions[st.session_state.current_q]
        st.subheader(f"Question {st.session_state.current_q + 1}:")
        st.write(q_text)

        answer = st.text_area("Your Answer", key=f"answer_{st.session_state.current_q}")
        next_btn = st.button("Next")

        if next_btn:
            if answer.lower().strip() in ["exit", "quit"]:
                st.session_state.step = "end"
                st.rerun()
            st.session_state.answers[q_text] = answer
            st.session_state.current_q += 1
            st.rerun()
    else:
        st.success("✅ All questions completed!")
        st.write("### Candidate Answers:")
        for q, a in st.session_state.answers.items():
            st.write(f"**{q}**")
            st.write(f"Answer: {a}")
        st.subheader("🙏 Thank You!")
        st.write("Thank you for your time. Your responses have been recorded. We will review them and contact you shortly.")
        if st.button("Finish"):
            st.session_state.clear()
            st.rerun()

# Step 4: End conversation
elif st.session_state.step == "end":
    st.subheader("👋 Conversation Ended")
    st.write("Thank you for visiting TalentScout. Have a great day!")
    if st.button("Restart"):
        st.session_state.clear()
        st.rerun()
