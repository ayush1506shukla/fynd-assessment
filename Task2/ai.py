import random

def summarize_review(review):
    return f"Summary: {review[:60]}..."

def recommend_action(stars):
    if stars <= 2:
        return "Apologize and offer support."
    elif stars == 3:
        return "Request clarification."
    else:
        return "Thank customer and highlight strengths."

def ai_response(review, stars):
    return f"Thanks for your {stars}-star review! We appreciate your feedback."
