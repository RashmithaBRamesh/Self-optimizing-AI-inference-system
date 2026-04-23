import requests
from src.config import MODEL_NAME, OLLAMA_URL

def generate_response(query, context):
    prompt = f"""
You are an AI assistant.

Use ONLY the provided context to answer the question clearly and accurately.
If the answer is not in the context, say "Not enough information".

Context:
{context}

Question:
{query}

Answer in 2-3 sentences:
"""

    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL_NAME,
                "prompt": prompt,
                "stream": False
            }
        )

        data = response.json()

        if "response" in data:
            return data["response"].strip()
        else:
            return f"[Model Error] {data}"

    except Exception as e:
        return f"[System Error] {str(e)}"