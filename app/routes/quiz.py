from fastapi import APIRouter
from app.services.quiz_service import generate_quiz
from app.memory.short_term import get_last_topic


router=APIRouter()

@router.post("/followup")
def followup_quiz(user_id: str):

    topic = get_last_topic(user_id)

    if not topic:
        return {
            "error": "No previous topic found"
        }

    quiz = generate_quiz(user_id, topic)

    return {
        "user_id": user_id,
        "topic": topic,
        "difficulty": quiz["difficulty"],
        "quiz": quiz["quiz"]
    }