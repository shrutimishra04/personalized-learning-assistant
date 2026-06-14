from fastapi import APIRouter
from app.services.rag_service import answer_question

router=APIRouter()

@router.post('/')
def ask_document(question: str):
    result=answer_question(question)
    return result