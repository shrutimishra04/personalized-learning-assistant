user_memory={}

def save_context(user_id: str, topic: str):
    user_memory[user_id]={
        'last_topic': topic
    }

def get_last_topic(user_id: str):
    if user_id not in user_memory:
        return None

    return user_memory[user_id]['last_topic']