import requests
from src.config import MODEL_NAME, OLLAMA_URL

def generate_response(query, context):
    prompt = f"""
You are a helpful assistant.

Use the provided context to answer the question.

Context:
{context}

Question:
{query}

Answer:
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