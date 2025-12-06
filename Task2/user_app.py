import streamlit as st
import json
import os
from ai import generate_user_response

DATA_FILE = "Task2/data.json"

# Ensure file exists
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump([], f)

# Load existing data
def load_data():
    with open(DATA_FILE, "r") as f:
        return json.load(f)

# Save new entry
def save_data(new_entry):
    data = load_data()
    data.append(new_entry)
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# ----------------------------------------
# STREAMLIT USER DASHBOARD
# ----------------------------------------
st.title("⭐ User Feedback Portal")
st.write("Submit your review and get an instant AI-generated response.")

# User Inputs
rating = st.selectbox("Select Rating (1-5 Stars)", [1, 2, 3, 4, 5])
review = st.text_area("Write your review here")

if st.button("Submit"):
    if review.strip() == "":
        st.error("Please enter a review before submitting.")
    else:
        # Generate AI response
        ai_response = generate_user_response(review, rating)

        # Save data
        entry = {
            "rating": rating,
            "review": review,
            "ai_response": ai_response["response"],
            "summary": ai_response["summary"],
            "actions": ai_response["actions"]
        }
        save_data(entry)

        st.success("Review submitted successfully!")
        st.subheader("AI Response:")
        st.write(ai_response["response"])
