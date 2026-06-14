def decide_tool(user_query: str):

    query=user_query.lower()

    if 'quiz' in query or 'test' in query:
        return 'quiz'

    elif 'roadmap' in query or 'path' in query:
        return 'roadmap'

    elif 'recommend' in query:
        return 'recommendation'

    else:
        return 'notes'