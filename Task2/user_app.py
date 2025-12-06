from flask import Flask, render_template_string, request
import json
from ai import ai_response

app = Flask(__name__)

HTML = """
<h2>User Review Submission</h2>

<form method="post">
  Rating (1-5): <input name="stars" /><br><br>

  Review:<br>
  <textarea name="review" rows="5" cols="40"></textarea><br><br>

  <button type="submit">Submit</button>
</form>

{% if reply %}
<h3>AI Response:</h3>
<p>{{ reply }}</p>
{% endif %}
"""

def save_data(entry):
    with open("data.json", "r") as f:
        old = json.load(f)

    old.append(entry)

    with open("data.json", "w") as f:
        json.dump(old, f, indent=2)

@app.route("/", methods=["GET", "POST"])
def home():
    reply = None

    if request.method == "POST":
        stars = int(request.form["stars"])
        review = request.form["review"]

        ai_reply = ai_response(review, stars)

        save_data({
            "stars": stars,
            "review": review,
            "ai_reply": ai_reply
        })

        reply = ai_reply

    return render_template_string(HTML, reply=reply)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
