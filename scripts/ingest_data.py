from rag.ingestion import extract_text
from rag.chunking import create_chunks
from rag.embeddings import create_embeddings
from rag.vector_store import save_faiss_index

pdf_path='data/raw_pdfs/sample.pdf'

text=extract_text(pdf_path)

chunks=create_chunks(text)

embeddings=create_embeddings(chunks)

save_faiss_index(
    embeddings,
    chunks,
    'data/vector_db/faiss.index',
    'data/vector_db/chunks.pkl'
)

print('Index created successfully')