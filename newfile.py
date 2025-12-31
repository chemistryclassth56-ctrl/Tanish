from flask import Flask, render_template_string, request

app = Flask(__name__)

# Aapka naam yahan set hai
MY_NAME = "Tansu"

# Quiz Questions
quiz_data = [
    {"question": "Python ke creator kaun hain?", "options": ["Elon Musk", "Guido van Rossum", "Mark Zuckerberg", "Tansu"], "answer": "Guido van Rossum"},
    {"question": "Flask kis kaam aata hai?", "options": ["Web Dev", "Game Dev", "AI", "Designing"], "answer": "Web Dev"},
    {"question": "Tansu ki website kaisi hai?", "options": ["Bekaar", "Theek hai", "Zabardast", "Pata nahi"], "answer": "Zabardast"}
]

# HTML Template (Single File Setup)
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ name }}'s Quiz</title>
    <style>
        body { font-family: sans-serif; background-color: #f0f2f5; padding: 20px; }
        .card { background: white; padding: 20px; border-radius: 15px; shadow: 0 4px 8px rgba(0,0,0,0.1); max-width: 500px; margin: auto; }
        h1 { color: #1a73e8; text-align: center; }
        .q-box { margin-bottom: 20px; padding: 10px; border-bottom: 1px solid #eee; }
        .btn { background: #1a73e8; color: white; border: none; padding: 10px 20px; width: 100%; border-radius: 5px; font-size: 18px; }
    </style>
</head>
<body>
    <div class="card">
        <h1>{{ name }}'s Quiz Portal</h1>
        <form action="/result" method="post">
            {% for i in range(questions|length) %}
            <div class="q-box">
                <p><strong>{{ i+1 }}. {{ questions[i].question }}</strong></p>
                {% for opt in questions[i].options %}
                <input type="radio" name="q{{i}}" value="{{opt}}" required> {{opt}}<br>
                {% endfor %}
            </div>
            {% endfor %}
            <button type="submit" class="btn">Submit Results</button>
        </form>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE, name=MY_NAME, questions=quiz_data)

@app.route('/result', methods=['POST'])
def result():
    score = 0
    for i, q in enumerate(quiz_data):
        ans = request.form.get(f"q{i}")
        if ans == q['answer']:
            score += 1
    
    return f"""
    <div style="text-align:center; padding:50px; font-family:sans-serif;">
        <h2>Shabash!</h2>
        <p style="font-size:20px;">{MY_NAME} ki website par aapka score: <b>{score}/{len(quiz_data)}</b></p>
        <a href="/">Wapas Jayein</a>
    </div>
    """

if __name__ == '__main__':
    # Pydroid ke liye host='0.0.0.0' zaroori hai
    app.run(host='0.0.0.0', port=5000, debug=True)
