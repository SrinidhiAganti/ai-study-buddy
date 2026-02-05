from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Home page
@app.route("/", methods=["GET", "POST"])
def index():
    answer = ""
    summary = ""
    mcqs = []

    if request.method == "POST":
        text = request.form.get("text")

        if text:
            # Simple AI placeholders (replace later with Kiro / LLM)

            # Answer (dummy)
            answer = "This is a sample AI answer based on your input."

            # Summary
            summary = "Summary: " + text[:150] + "..."

            # MCQ Generator
            mcqs = generate_mcq(text)

    return render_template("index.html", answer=answer, summary=summary, mcqs=mcqs)

# Simple MCQ generator
def generate_mcq(text):
    words = text.split()
    mcq_list = []

    if len(words) > 5:
        key = words[0]

        question = f"What is related to '{key}'?"

        options = random.sample(words, min(4, len(words)))
        mcq_list.append({
            "q": question,
            "options": options,
            "answer": options[0]
        })

    return mcq_list

if __name__ == "__main__":
    app.run(debug=True)
