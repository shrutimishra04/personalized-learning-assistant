from langchain.tools import tool

from app.services.llm_service import generate_notes
from app.services.quiz_service import generate_quiz
from app.services.roadmap_service import generate_roadmap
from app.services.recommendation_service import get_recommendations


@tool
def notes_tool(topic: str):
    """
    Generate learning notes for a topic.
    """
    return generate_notes(topic)

@tool
def roadmap_tool(topic: str):
    """
    Generate learning roadmap for a topic.
    """
    return generate_roadmap(topic)

@tool
def recommendation_tool(user_id: str):
    """
    Get personalized recommendations for a user and a topic.
    """
    return str(get_recommendations(user_id))


@tool
def quiz_tool(input_text: str):
    """
    Generate adaptive quiz.

    Input format:
    user_id,topic

    Example:
    user1,recursion
    """
    user_id, topic = input_text.split(',')

    result= generate_quiz(
        user_id=user_id.strip(),
        topic=topic.strip()
    )

    return str(result)