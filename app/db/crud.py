from app.db.database import get_connection

def save_performance(user_id:str, topic:str,score:int):
    topic=topic.strip().lower()

    if topic.endswith('s'):
        topic=topic[:-1]

    conn=get_connection()
    cursor=conn.cursor()

    cursor.execute(
        "INSERT INTO performance (user_id, topic, score) VALUES (?, ?, ?)",
        (user_id, topic, score)
    )

    conn.commit()
    conn.close()

def get_user_performance(user_id:str):
    conn=get_connection()
    cursor=conn.cursor()

    cursor.execute(
        "SELECT topic, score FROM performance WHERE user_id= ?",
        (user_id,)
    )

    data=cursor.fetchall()
    conn.close()

    return data