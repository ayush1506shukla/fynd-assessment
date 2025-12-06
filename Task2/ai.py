def summarize_review(review):
    return f"Summary: {review[:70]}..."

def recommend_action(stars):
    if stars <= 2:
        return "Apologize and offer help."
    elif stars == 3:
        return "Ask user for more details."
    else:
        return "Thank user and encourage repeat visit."

def ai_response(review, stars):
    return f"Thanks for your {stars}-star review! We appreciate your feedback: {review[:50]}..."
