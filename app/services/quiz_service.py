# app/services/quiz_service.py

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

from app.db.crud import get_user_performance
from app.memory.short_term import save_context

llm = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0.7
)


def get_difficulty_level(user_id: str, topic: str):

    data = get_user_performance(user_id)

    scores = []

    for saved_topic, score in data:

        if saved_topic == topic.lower():
            scores.append(score)

    if not scores:
        return "Beginner"

    avg_score = sum(scores) / len(scores)

    if avg_score < 40:
        return "Beginner"

    elif avg_score < 70:
        return "Intermediate"

    else:
        return "Advanced"


def generate_quiz(user_id: str, topic: str):

    save_context(user_id, topic)

    difficulty = get_difficulty_level(user_id, topic)

    prompt = PromptTemplate(
        input_variables=["topic", "difficulty"],
        template="""
        Generate 5 {difficulty}-level multiple choice questions on {topic}.

        Rules:
        - Each question must have 4 options
        - Include correct answer
        - Questions should match difficulty level
        - Keep formatting clean
        """
    )

    chain = prompt | llm

    response = chain.invoke({
        "topic": topic,
        "difficulty": difficulty
    })

    return {
        "difficulty": difficulty,
        "quiz": response.content
    }