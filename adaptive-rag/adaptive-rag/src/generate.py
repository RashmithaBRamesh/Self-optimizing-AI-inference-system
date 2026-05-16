import requests
from src.config import MODEL_NAME, OLLAMA_URL
from src.memory import get_memory_context

def generate_response(query, context):
    memory_context = get_memory_context()

    prompt = f"""
    You are an AI assistant.

    Use the conversation history and provided context to answer accurately.

    Conversation History:
    {memory_context}

    Retrieved Context:
    {context}

    Current Question:
    {query}

    Answer clearly and concisely:
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