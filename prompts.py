# System prompt for Mistral
SYSTEM_PROMPT = """
You are TalentScout's AI Interviewer.
You greet candidates, collect their details, and ask relevant technical questions.
You stay polite, concise, and professional.
"""

# Template for generating questions
QUESTION_PROMPT_TEMPLATE = """
Generate 8 short, numbered technical interview questions 
for a candidate skilled in: {tech_stack}.
Format strictly as:
1. Question
2. Question
3. Question
...
Do not add explanations, only questions.
"""


# Fallback generic questions
FALLBACK_QUESTIONS = [
    "What is Object-Oriented Programming?",
    "Explain the difference between a compiler and an interpreter.",
    "What are REST APIs?",
    "What is the difference between SQL and NoSQL databases?",
    "Explain the concept of cloud computing."
]
