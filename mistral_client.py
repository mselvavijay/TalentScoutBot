import requests
import os

FALLBACK_QUESTIONS = {
    "django": [
        "Explain Django's MVT architecture.",
        "How does Django ORM work?",
        "What are Django signals and their use cases?",
        "Explain the use of Django middleware.",
        "How to optimize database queries in Django?"
    ],
    "react": [
        "What are React hooks?",
        "Explain the difference between functional and class components.",
        "What is JSX and why is it used?",
        "Explain the concept of virtual DOM in React.",
        "How do you manage state in large React applications?"
    ],
    "ai": [
        "What is the difference between supervised and unsupervised learning?",
        "Explain the architecture of a transformer model.",
        "What is fine-tuning in AI?",
        "Explain the difference between CNN and RNN.",
        "What are embeddings in NLP?"
    ]
}

def call_mistral_api(tech_stack):
    API_KEY = os.getenv("OPENROUTER_API_KEY")
    url = "https://openrouter.ai/api/v1/chat/completions"

    prompt = f"Generate 10 unique technical interview questions for: {tech_stack}. Number them clearly."

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "mistralai/mistral-7b-instruct:free",
        "messages": [
            {"role": "system", "content": "You are an AI technical interviewer."},
            {"role": "user", "content": prompt}
        ]
    }

    try:
        res = requests.post(url, headers=headers, json=payload)
        if res.status_code == 200:
            return res.json()["choices"][0]["message"]["content"].split("\n")
        else:
            return []
    except:
        return []

def generate_questions(tech_stack):
    questions = call_mistral_api(tech_stack)

    # If API fails or returns generic content, use fallback
    if not questions or not any(stack.lower() in " ".join(questions).lower() for stack in tech_stack.split(",")):
        result = []
        for stack in tech_stack.split(","):
            stack = stack.strip().lower()
            if stack in FALLBACK_QUESTIONS:
                result.extend(FALLBACK_QUESTIONS[stack])
        return result
    
    return questions
