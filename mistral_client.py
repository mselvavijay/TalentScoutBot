import os
import requests
from prompts import SYSTEM_PROMPT, QUESTION_PROMPT_TEMPLATE, FALLBACK_QUESTIONS

# Load API key

OPENROUTER_API_KEY ="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"
BASE_URL = "https://openrouter.ai/api/v1/chat/completions"

def generate_questions_with_mistral(tech_stack):
    """
    Generates 8 varied technical questions based on the candidate's tech stack.
    Falls back to default questions if API fails.
    """

    if not OPENROUTER_API_KEY:
        print("⚠️ No API key found. Using fallback questions.")
        return "\n".join(FALLBACK_QUESTIONS)

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "mistralai/mistral-7b-instruct:free",
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {
                "role": "user",
                "content": QUESTION_PROMPT_TEMPLATE.format(
                    tech_stack=tech_stack,
                    num_questions=8
                )
            }
        ]
    }

    try:
        # Debug: show outgoing request
        print("🔍 DEBUG: Sending payload:", payload)

        response = requests.post(BASE_URL, headers=headers, json=payload)
        print("🔍 DEBUG: API raw response:", response.text)

        response.raise_for_status()
        data = response.json()

        if "choices" in data and len(data["choices"]) > 0:
            questions_text = data["choices"][0]["message"]["content"].strip()
            return questions_text if questions_text else "\n".join(FALLBACK_QUESTIONS)
        else:
            print("⚠️ No choices returned in API response.")
            return "\n".join(FALLBACK_QUESTIONS)

    except Exception as e:
        print(f"⚠️ API Error: {e}")
        return "\n".join(FALLBACK_QUESTIONS)
