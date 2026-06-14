import faiss
import pickle
import numpy as np

def save_faiss_index(
    embeddings,
    chunks,
    index_path,
    chunks_path):

    embeddings=np.array(
        embeddings,
        dtype=np.float32
    )

    faiss.normalize_L2(embeddings)

    dimension=embeddings.shape[1]

    index=faiss.IndexFlatIP(
        dimension
    )

    index.add(embeddings)

    faiss.write_index(
        index,
        index_path
    )

    with open(chunks_path, 'wb') as f:
        pickle.dump(chunks, f)

    print(
        f'Stored {len(chunks)} chunks'
    )