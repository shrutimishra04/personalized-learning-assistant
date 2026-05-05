from fastapi import APIRouter
from app.services.roadmap_service import generate_roadmap

router=APIRouter()

@router.post('/')
def get_roadmap(topic: str):
    roadmap=generate_roadmap(topic)
    return {'topic': topic, 'roadmap': roadmap}
    