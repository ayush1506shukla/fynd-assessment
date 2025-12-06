import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

# Configure Gemini API Key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_user_response(review, rating):
    prompt = f"""
    A user gave a rating of {rating} stars and wrote this review:
    "{review}"

    1. Generate a friendly AI response to the user.
    2. Create a short summary of their review.
    3. Suggest recommended actions for the business.

    Return in JSON with keys: response, summary, actions.
    """

    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)

    # Safe extraction
    try:
        import json
        return json.loads(response.text)
    except:
        return {
            "response": "Thank you for your feedback!",
            "summary": "User provided feedback.",
            "actions": "Review and improve accordingly."
        }
