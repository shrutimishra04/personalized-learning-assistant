from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

from rag.hybrid_search import hybrid_search

llm=ChatOpenAI(
    model='gpt-4.1-mini',
    temperature=0
)

def answer_question(query: str):
    contexts= hybrid_search(
        query=query,
        index_path='data/vector_db/faiss.index',
        chunks_path='data/vector_db/chunks.pkl',
        top_k=3
    )

    context_text='\n\n'.join(contexts)

    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template="""
        Answer the question using ONLY the provided context.

        Context:
        {context}

        Question:
        {question}

        If the answer is not present in the context,
        say:
        "Information not found in the document."
        """
    )

    chain=prompt | llm

    response= chain.invoke({
        'context': context_text,
        'question': query
    })

    return {
        'answer': response.content,
        'retrieved_chunks': contexts
    }