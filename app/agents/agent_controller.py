from langchain.agents import(
    AgentExecutor,
    create_openai_tools_agent
)

from langchain import hub
from langchain_openai import ChatOpenAI

from app.agents.tools import (
    notes_tool, 
    roadmap_tool, 
    recommendation_tool, 
    quiz_tool
)

llm=ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0
)

tools=[
    notes_tool,
    roadmap_tool,
    recommendation_tool,
    quiz_tool
]

prompt= hub.pull("hwchase17/openai-tools-agent")

agent=create_openai_tools_agent(
    llm=llm,
    tools=tools,
    prompt=prompt
)

agent_executor=AgentExecutor(
    agent=agent, 
    tools=tools, 
    verbose=True
)

def run_agent(user_query: str):
    response=agent_executor.invoke(
        {
            "input": user_query
        }
    )
    return response