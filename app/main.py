from fastapi import FastAPI
from app.routes import notes, quiz, roadmap

app=FastAPI(title="Personalized Learning Assistant")

app.include_router(notes.router, prefix='/notes', tags=['Notes'])
app.include_router(quiz.router, prefix='/quiz', tags=['Quiz'])
app.include_router(roadmap.router, prefix='/roadmap', tags=['Roadmap'])

@app.get('/')
def root():
    return {'message':'Learning Assistant API is running'}
    