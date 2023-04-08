import random
import time
import bcrypt
from datetime import datetime
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from openai_api import OpenaiApi


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///main.db'
with app.app_context():
    db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    data_created = db.Column(db.DateTime, default=datetime.utcnow())

    def __repr__(self):
        return '<User %r>' % self.id


@app.route('/sign_up', methods=['POST', 'GET'])
def sign_up():
    if request.method == "POST":
        username = request.form['username']
        email = request.form['email']
        password = request.form['password'].encode('utf-8')
        hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
        username_exists = db.session.query(
            db.session.query(User).filter_by(username=username).exists()
        ).scalar()
        email_exists = db.session.query(
            db.session.query(User).filter_by(email=email).exists()
        ).scalar()

        if not username_exists:
            if not email_exists:
                new_user = User(username=username, password=hashed_password, email=email)
                try:
                    db.session.add(new_user)
                    db.session.commit()
                    return redirect('/select_period')
                except():
                    return "error creating user"
            return render_template('sign_up.html', error="Email already used.")
        return render_template('sign_up.html', error="Username already used.")
    return render_template('sign_up.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password'].encode('utf-8')
        user_db_row = User.query.filter_by(username=username).first()

        if user_db_row:
            if bcrypt.checkpw(password, user_db_row.password):
                return redirect('/select_period')
            return render_template('login.html', error="Wrong password!")
        return render_template('login.html', error="Username not existing!")

    return render_template('login.html')


@app.route('/guessing_game/<string:period>')
def guessing_game(period):
    openai_api = OpenaiApi()
    answers = openai_api.get_a_list_of_answers(
        f"Give me 4 major events from {period} without mentioning the period of the event.",
        1,
        1000
    )
    correct_answer = random.choice(answers).strip()
    img_link = openai_api.generate_dall_e_image(f"{correct_answer} sand sculpture, high detail")
    time.sleep(1)
    hints = openai_api.get_a_list_of_answers(
        f"Give me 5 hints about {correct_answer} without mentioning '{correct_answer}'.",
        0,
        1000
    )
    return render_template(
        "guessing_game.html",
        answers=answers,
        correct_answer=correct_answer,
        hints=hints,
        period=period,
        img_link=img_link
    )


@app.route('/submit_guess/<string:user_answer>/<string:correct_answer>/<int:hints>/<string:period>')
def submit_guess(user_answer, correct_answer, hints, period):
    if user_answer == correct_answer:
        return render_template('win.html', hints=hints, period=period)
    return render_template('lose.html', period=period)


@app.route('/selectTypeGame')
def select_type_game():
    return render_template('selectTypeGame.html')


@app.route('/select_period')
def select_period():
    return render_template('select_period.html')


@app.route('/')
def index():
    return redirect('/login')


if __name__ == "__main__":
    app.run(debug=True)