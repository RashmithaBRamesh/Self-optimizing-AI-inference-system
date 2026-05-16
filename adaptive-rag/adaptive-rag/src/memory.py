conversation_history = []

def add_to_memory(query, answer):
    conversation_history.append({
        "query": query,
        "answer": answer
    })

    # Keep only recent memory
    if len(conversation_history) > 5:
        conversation_history.pop(0)

def get_memory_context():
    context = ""

    for item in conversation_history:
        context += f"""
Previous Query: {item['query']}
Previous Answer: {item['answer']}
"""

    return context