import google.generativeai as genai
import os

# Load your API Key from environment variable
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_user_response(rating, review):
    prompt = f"""
    A user gave a rating of {rating} and wrote the review:
    '{review}'.
    Write a friendly AI-generated response of 3-4 lines.
    """
    
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    return response.text


def generate_summary(review):
    prompt = f"""
    Summarize the following review in 2 lines:
    '{review}'
    """

    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    return response.text


def generate_recommendation(review):
    prompt = f"""
    Based on this review:
    '{review}'
    Recommend 2-3 next actions for the business.
    """

    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    return response.text
