from flask import Flask, render_template_string
import json
from ai import summarize_review, recommend_action

app = Flask(__name__)

ADMIN_HTML = """
<h2>Admin Dashboard</h2>

<table border="1" cellpadding="8">
<tr>
    <th>Rating</th>
    <th>Review</th>
    <th>AI Summary</th>
    <th>Next Action</th>
</tr>

{% for item in data %}
<tr>
  <td>{{ item.stars }}</td>
  <td>{{ item.review }}</td>
  <td>{{ item.summary }}</td>
  <td>{{ item.action }}</td>
</tr>
{% endfor %}
</table>
"""

@app.route("/")
def home():
    with open("data.json") as f:
        entries = json.load(f)

    processed = []
    for e in entries:
        processed.append({
            "stars": e["stars"],
            "review": e["review"],
            "summary": summarize_review(e["review"]),
            "action": recommend_action(e["stars"])
        })

    return render_template_string(ADMIN_HTML, data=processed)

if __name__ == "__main__":
    app.run(debug=True, port=5002)
