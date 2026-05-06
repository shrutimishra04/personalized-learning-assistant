from fastapi import APIRouter
from app.db.crud import save_performance
from app.services.recommendation_service import get_weak_topics

router=APIRouter()

@router.post('/submit-performance')
def submit_performance(user_id:str, topic:str, score:int):
    save_performance(user_id, topic, score)

    return {
        "message": "Performance data saved successfully",
        "user_id": user_id,
        "topic": topic,
        "score": score
    }

@router.get("/weak-topics")
def weak_topics(user_id:str):
    topics=get_weak_topics(user_id)

    return {
        "user_id": user_id,
        "weak_topics": topics
    }
