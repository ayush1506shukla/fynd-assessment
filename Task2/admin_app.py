import streamlit as st
import json

DATA_FILE = "Task2/data.json"

def load_data():
    with open(DATA_FILE, "r") as f:
        return json.load(f)

st.title("🔐 Admin Dashboard")
st.write("Live view of all user submissions.")

data = load_data()

if len(data) == 0:
    st.info("No submissions yet.")
else:
    for entry in data:
        st.subheader(f"⭐ Rating: {entry['rating']}")
        st.write(f"**Review:** {entry['review']}")
        st.write(f"**AI Summary:** {entry['summary']}")
        st.write(f"**Recommended Actions:** {entry['actions']}")
        st.markdown("---")
