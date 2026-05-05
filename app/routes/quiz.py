from fastapi import APIRouter
from app.services.quiz_service import generate_quiz

router=APIRouter()

@router.post('/')
def get_quiz(topic: str):
    quiz= generate_quiz(topic)
    return {'topic': topic, 'quiz': quiz}
