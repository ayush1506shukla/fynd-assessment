import streamlit as st
import json
import pandas as pd
from ai import generate_user_response, generate_summary, generate_recommendation

DATA_FILE = "Task2/data.json"

def load_data():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

st.title("⭐ User Review Dashboard")

rating = st.slider("Select Rating", 1, 5)
review = st.text_area("Write your review")

if st.button("Submit"):
    if review.strip() == "":
        st.warning("Please enter a review")
    else:
        user_response = generate_user_response(rating, review)
        summary = generate_summary(review)
        recommendation = generate_recommendation(review)

        new_entry = {
            "rating": rating,
            "review": review,
            "ai_response": user_response,
            "summary": summary,
            "recommendation": recommendation
        }

        data = load_data()
        data.append(new_entry)
        save_data(data)

        st.success("Your review was submitted!")
        st.subheader("AI Response:")
        st.write(user_response)


