from flask import Flask, render_template, request, session
from openai import OpenAI

client = OpenAI(api_key="your_openai_api_key")

# Create a Flask web app
app = Flask(__name__)

# Set the secret key for sessions (REQUIRED for using session)
app.secret_key = "a9b8c7d6-super-secret-key-8888"  # CHANGE this string to anything you like

@app.route("/", methods=["GET", "POST"])
def index():
    # Initialize chat history in the session if it doesn't exist
    if "history" not in session:
        session["history"] = []
    response = ""
    if request.method == "POST":
        user_input = request.form.get("user_input")
        if user_input:
            session["history"].append({"role": "user", "content": user_input})
            messages = [{"role": "system", "content": "You are an assistant that only answers math questions."}] + session["history"]
            reply = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages
            )
            response = reply.choices[0].message.content
            session["history"].append({"role": "assistant", "content": response})
            session.modified = True  # Tell Flask session has changed
    return render_template("index.html", history=session.get("history", []), response=response)

if __name__ == "__main__":
    app.run(debug=True)