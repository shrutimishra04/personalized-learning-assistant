from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate


llm=ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)


def generate_notes(topic:str):
    prompt=PromptTemplate(
        input_variables=['topic'],
        template="Explain {topic} in simple terms with examples"
    )

    chain= prompt | llm
    response= chain.invoke({'topic': topic})

    return response.content