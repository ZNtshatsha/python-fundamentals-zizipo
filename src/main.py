from src.document_processor import display_documents, load_documents

if __name__ == "__main__":
    docs = load_documents("data/documents.json")
    display_documents(docs)
