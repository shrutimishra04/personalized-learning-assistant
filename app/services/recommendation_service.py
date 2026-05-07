from app.db.crud import get_user_performance

def get_weak_topics(user_id:str):
    data=get_user_performance(user_id)

    topic_scores={}

    for topic, score in data:
        if topic not in topic_scores:
            topic_scores[topic]=[]

        topic_scores[topic].append(score)

    weak_topics=[]

    for topic,scores in topic_scores.items():
        avg_score=sum(scores)/len(scores)

        if avg_score<50:
            weak_topics.append(topic)

    return weak_topics


def get_recommendations(user_id:str):
    data=get_user_performance(user_id)
    
    topic_scores={}

    for topic, score in data:
        if topic not in topic_scores:
            topic_scores[topic]=[]

        topic_scores[topic].append(score)

    recommendations=[]

    for topic, scores in topic_scores.items():
        avg_score=sum(scores)/len(scores)

        if avg_score < 40:
            level='Beginner'

        elif avg_score < 70:
            level='Intermediate'
        
        else:
            level='Advanced'

        recommendations.append({
            'topic': topic,
            'average_score': avg_score,
            'recommended_level': level
        })

    return recommendations