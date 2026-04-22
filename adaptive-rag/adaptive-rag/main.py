from src.ingest import load_docs
from src.retrieve import retrieve
from src.generate import generate_response

def main():
    docs = load_docs("data/docs.txt")

    query = input("Enter query: ")

    results = retrieve(query, docs)
    context = " ".join(results)

    answer = generate_response(query, context)

    print("\nAnswer:\n", answer)

if __name__ == "__main__":
    main()