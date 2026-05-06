from fastapi import FastAPI
from app.routes import notes, quiz, roadmap, user
from app.db.database import init_db

app=FastAPI(title="Personalized Learning Assistant")

init_db()

app.include_router(notes.router, prefix='/notes', tags=['Notes'])
app.include_router(quiz.router, prefix='/quiz', tags=['Quiz'])
app.include_router(roadmap.router, prefix='/roadmap', tags=['Roadmap'])
app.include_router(user.router, prefix="/user", tags=["User"])


@app.get('/')
def root():
    return {'message':'Learning Assistant API is running'}
    