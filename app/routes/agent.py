from fastapi import APIRouter
from appp.agents.agent_controller import run_agent

router = APIRouter()

@router.post('/agent')
def agent_chat(user_query: str):
    response=run_agent(user_query)

    return {
        "response": response
    }

    