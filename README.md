# Math Chatbot Website

A simple web-based chatbot that answers math questions, powered by OpenAI's GPT API and built with Flask.  
All previous questions and answers are saved and displayed, creating a chat-like experience.

---

## Setup Instructions

1. **Clone or Download This Project**

git clone https://github.com/luomi16/math_ai_chatbot
cd math_ai_chatbot-main

2. **Install Required Python Packages**

```
pip install flask openai
```


## Features

- Ask any math question and get an instant answer.
- Conversation history is shown on the page.
- Clean and easy-to-understand web interface.
- Easily customizable for teaching or demos.


## Project Structure

```
math-chatbot-website/
│
├── app.py
└── templates/
└── index.html
```

- `app.py`: Main Python code for the Flask web app.
- `templates/index.html`: The web page layout (HTML).

---

## How It Works

- Enter your math question and click **Ask**.
- The bot will reply with an answer, and the conversation will appear as a chat history.
- To clear the history, simply refresh the browser tab.

---


## Customization Tips

- **Change the Assistant's Personality:**  
  Edit the `system` message in `app.py` to customize what kind of bot you want.

---