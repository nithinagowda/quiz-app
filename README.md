# Quiz Application

A dynamic web-based quiz application built with Flask and SQLite. Users can register, log in, take quizzes, and view their results.

## Features

- **User Registration & Login**: Create an account with a username and email
- **Quiz System**: Answer multiple-choice questions across various topics
- **Score Tracking**: View quiz results and performance
- **Database Storage**: User data and quiz questions stored in SQLite
- **Responsive UI**: Clean and intuitive web interface

## Project Structure

```
quiz-app/
├── app.py                 # Main Flask application
├── init_db.py            # Database initialization with sample questions
├── database.db           # SQLite database (auto-created)
├── templates/
│   ├── index.html        # Login page
│   ├── quiz.html         # Quiz page
│   └── result.html       # Results page
├── static/
│   ├── script.js         # JavaScript for interactivity
│   └── style.css         # Styling
└── .venv/                # Virtual environment
```

## Technologies Used

- **Backend**: Flask (Python)
- **Database**: SQLite3
- **Frontend**: HTML5, CSS3, JavaScript
- **Python Version**: 3.x

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd quiz-app
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1  # Windows PowerShell
# or
source .venv/bin/activate      # macOS/Linux
```

3. Install dependencies:
```bash
pip install flask
```

4. Initialize the database:
```bash
python init_db.py
```

5. Run the application:
```bash
python -m flask run
```

6. Open your browser and navigate to `http://localhost:5000`

## Usage

1. Register a new account with a username and email
2. Log in with your credentials
3. Start the quiz and answer the questions
4. View your final score and results

## Database Schema

### Users Table
- `id`: Primary key
- `username`: User's username
- `email`: User's email (unique)

### Questions Table
- `id`: Primary key
- `question`: Question text
- `option1-4`: Multiple choice options
- `answer`: Correct answer

## Features to Add

- Password encryption
- Leaderboard
- Question categories
- Timer for quizzes
- User performance analytics

## License

MIT License
