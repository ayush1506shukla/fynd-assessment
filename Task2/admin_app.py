from flask import Flask, render_template_string
import json
from ai import summarize_review, recommend_action

app = Flask(__name__)

ADMIN_HTML = """
<h2>Admin Dashboard</h2>

<table border="1" cellpadding="8">
<tr>
  <th>Stars</th>
  <th>Review</th>
  <th>Summary</th>
  <th>Recommended Action</th>
</tr>

{% for row in data %}
<tr>
  <td>{{ row.stars }}</td>
  <td>{{ row.review }}</td>
  <td>{{ row.summary }}</td>
  <td>{{ row.action }}</td>
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
