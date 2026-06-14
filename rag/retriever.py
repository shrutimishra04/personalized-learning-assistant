# rag/retriever.py

import faiss
import pickle
import numpy as np

from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "BAAI/bge-small-en-v1.5"
)


def retrieve_context(
    query,
    index_path,
    chunks_path,
    top_k=3
):

    index = faiss.read_index(
        index_path
    )

    with open(
        chunks_path,
        "rb"
    ) as f:
        chunks = pickle.load(f)

    query_embedding = model.encode(
        [query]
    )

    query_embedding = np.array(
        query_embedding,
        dtype=np.float32
    )

    faiss.normalize_L2(
        query_embedding
    )

    scores, indices = index.search(
        query_embedding,
        top_k
    )

    results = []

    for idx in indices[0]:
        results.append(
            chunks[idx]
        )

    return results