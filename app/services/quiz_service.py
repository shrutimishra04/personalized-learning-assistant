from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

llm=ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)


def generate_quiz(topic: str):
    prompt=PromptTemplate(
        input_variables=['topic'],
        template='''
        Generate 5 multiple choice questions on {topic}.
        Each question should have 4 options and 1 correct answer.
        Format the response as a list of dictionaries with keys: question, options, correct_answer.
        '''
    )
    chain=prompt | llm
    response=chain.invoke({'topic': topic})

    return response.content
    