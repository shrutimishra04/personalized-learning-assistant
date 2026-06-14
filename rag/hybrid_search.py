import pickle

from rank_bm25 import BM25Okapi
from rag.retriever import retrieve_context

def bm25_search(
    query,
    chunks_path,
    top_k=3):
    with open(
        chunks_path,
        'rb'
        
    ) as f:
        chunks=pickle.load(f)
        tokenized_chunks=[
            chunk.lower().split()
            for chunk in chunks
        ]
        bm25=BM25Okapi(tokenized_chunks)

        scores=bm25.get_scores(
            query.lower().split()
        )

        ranked= sorted(
            zip(chunks, scores),
            key=lambda x: x[1],
            reverse=True
        )
        results=[chunk for chunk, score in ranked[:top_k]]

        return results

def hybrid_search(
    query,
    index_path,
    chunks_path,
    top_k=5
):

    faiss_results = retrieve_context(
        query=query,
        index_path=index_path,
        chunks_path=chunks_path,
        top_k=top_k
    )

    bm25_results = bm25_search(
        query=query,
        chunks_path=chunks_path,
        top_k=top_k
    )

    combined = []

    seen = set()

    for chunk in (
        faiss_results +
        bm25_results
    ):

        if chunk not in seen:
            combined.append(chunk)
            seen.add(chunk)

    return combined[:top_k]