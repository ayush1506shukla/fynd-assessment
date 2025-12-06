import streamlit as st
import json
import pandas as pd

DATA_FILE = "Task2/data.json"

def load_data():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except:
        return []

st.title("🔐 Admin Dashboard – User Feedback Monitor")

data = load_data()

if len(data) == 0:
    st.info("No submissions yet.")
else:
    df = pd.DataFrame(data)
    st.dataframe(df)

    st.subheader("📊 Analytics")

    avg_rating = df["rating"].mean()
    st.metric("Average Rating", round(avg_rating, 2))

    st.bar_chart(df["rating"].value_counts())
