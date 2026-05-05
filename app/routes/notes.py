from fastapi import APIRouter
from app.services.llm_service import generate_notes


router=APIRouter()

@router.post('/')
def get_notes(topic:str):
    notes=generate_notes(topic)
    return {'topic': topic, 'notes': notes}