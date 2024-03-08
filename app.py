from flask import Flask, render_template, request, session
from flask_session import Session

app = Flask(__name__)
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = 'your_secret_key'  

Session(app)

@app.route('/', methods=["GET", "POST"])
def index():
    if 'notes' not in session:
        session['notes'] = []

    if request.method == "POST":
        note = request.form.get("note")
        if note:
            session['notes'].append(note)

    return render_template("home.html", notes=session['notes'])

if __name__ == '__main__':
    app.run(debug=True)

