import random
import sqlite3
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__, static_folder="static", template_folder="templates")
app.secret_key = "replace_this_with_a_secure_key"
DB_NAME = "database.db"


def get_db_connection():
    """Open a SQLite connection and return rows as dictionaries."""
    connection = sqlite3.connect(DB_NAME)
    connection.row_factory = sqlite3.Row
    return connection


def init_db():
    """Create the tables needed for users and questions."""
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            email TEXT UNIQUE
        )
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            option1 TEXT NOT NULL,
            option2 TEXT NOT NULL,
            option3 TEXT NOT NULL,
            option4 TEXT NOT NULL,
            answer TEXT NOT NULL
        )
        """
    )
    connection.commit()
    connection.close()


@app.route("/")
def index():
    """Render the login page or redirect if already logged in."""
    init_db()
    if session.get("user_email"):
        return redirect(url_for("quiz"))
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def login():
    """Process login form and store user details in the database."""
    username = request.form.get("username", "").strip()
    email = request.form.get("email", "").strip().lower()

    if not username or not email:
        return render_template(
            "index.html",
            error="Both username and email are required.",
            username=username,
            email=email,
        )

    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
    user = cursor.fetchone()

    if user:
        cursor.execute("UPDATE users SET username = ? WHERE email = ?", (username, email))
    else:
        cursor.execute(
            "INSERT INTO users (username, email) VALUES (?, ?)",
            (username, email),
        )
    connection.commit()
    connection.close()

    session["user_email"] = email
    session["username"] = username

    return redirect(url_for("quiz"))


@app.route("/quiz")
def quiz():
    """Show the quiz page only if the user is logged in."""
    if not session.get("user_email"):
        return redirect(url_for("index"))

    init_db()
    connection = get_db_connection()
    questions = connection.execute("SELECT * FROM questions").fetchall()
    connection.close()

    if not questions:
        return render_template(
            "index.html",
            error="No quiz questions are available yet. Please initialize the database.",
        )

    question_list = list(questions)
    random.shuffle(question_list)

    return render_template(
        "quiz.html",
        username=session.get("username"),
        questions=question_list,
    )


@app.route("/submit", methods=["POST"])
def submit():
    """Handle submitted quiz answers and generate the result page."""
    if not session.get("user_email"):
        return redirect(url_for("index"))

    connection = get_db_connection()
    questions = connection.execute("SELECT * FROM questions").fetchall()
    connection.close()

    score = 0
    correct = 0
    wrong = 0
    results = []

    for question in questions:
        field_name = f"q_{question['id']}"
        user_answer = request.form.get(field_name, "")
        is_correct = user_answer == question["answer"]

        if is_correct:
            score += 1
            correct += 1
        else:
            wrong += 1

        results.append(
            {
                "question": question["question"],
                "selected": user_answer or "No answer",
                "correct_answer": question["answer"],
                "is_correct": is_correct,
            }
        )

    return render_template(
        "result.html",
        username=session.get("username"),
        score=score,
        total=len(questions),
        correct=correct,
        wrong=wrong,
        results=results,
    )


@app.route("/logout")
def logout():
    """Clear the session and return to the login page."""
    session.clear()
    return redirect(url_for("index"))


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
