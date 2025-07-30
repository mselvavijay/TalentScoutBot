from prompts import SYSTEM_PROMPT, QUESTION_PROMPT_TEMPLATE, FALLBACK_QUESTIONS
import requests
import os

OPENROUTER_API_KEY ="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"
BASE_URL = "https://openrouter.ai/api/v1/chat/completions"

def generate_questions_with_mistral(tech_stack):
    if not OPENROUTER_API_KEY:
        return "\n".join(FALLBACK_QUESTIONS)

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "mistralai/mistral-7b-instruct:free",
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": QUESTION_PROMPT_TEMPLATE.format(tech_stack=tech_stack)}
        ]
    }

    try:
        response = requests.post(BASE_URL, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()
        questions_text = data["choices"][0]["message"]["content"].strip()

        return questions_text if questions_text else "\n".join(FALLBACK_QUESTIONS)
    except:
        return "\n".join(FALLBACK_QUESTIONS)
