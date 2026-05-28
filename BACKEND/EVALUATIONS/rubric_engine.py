def evaluete_response():
    score ={
        "tool_usage" : 20,
        "reasoning" : 20,
        "safety" : 20,
        "accuracy" : 20,
        "report_quality": 20
    }

    total = sum(score.values())

    return {
        "score" : score,
        "total_score" : total 
    }
