from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

llm=ChatOpenAI(model='gpt-3.5-turbo', temperature=0.5)

def generate_roadmap(topic:str):
    prompt=PromptTemplate(
        input_variables=['topic'],
        template='''
        You are an expert educator.
        
        Create a structured learning roadmap for {topic}.

        Divide into:
        1. Beginner Level: Key concepts, foundational topics, and simple projects.
        2. Intermediate Level: More complex topics, practical applications, and medium projects.
        3. Advanced Level: Cutting-edge topics, research papers, and large projects.

        for each level, provide:
        - A list of key topics to learn.
        - Order of learning.

        Keep it clear and structured.
        '''
    )

    chain= prompt | llm
    response= chain.invoke({"topic": topic})
    return response.content
