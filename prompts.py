SYSTEM_PROMPT = """
You are a professional technical interviewer chatbot.
Your job is to ask exactly 8 short, clear, and relevant technical questions based
on the candidate's declared tech stack.
Each question should be unique and specific to the technologies mentioned.
"""

QUESTION_PROMPT_TEMPLATE = """
Generate exactly {num_questions} unique, varied, short technical interview questions 
for a candidate skilled in: {tech_stack}.

✅ Strict rules:
- All questions must directly relate to the technologies in the stack.
- Do NOT include unrelated topics.
- Avoid repeating questions from earlier calls.
- Number the questions like:
1. ...
2. ...
...
"""



FALLBACK_QUESTIONS = [
    "Explain object-oriented programming concepts.",
    "What is a REST API?",
    "Explain the difference between SQL and NoSQL databases.",
    "What are the advantages of cloud computing?",
    "What is CI/CD?",
    "Explain version control using Git.",
    "What are microservices?",
    "Explain containerization with Docker."
]
