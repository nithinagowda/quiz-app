import sqlite3

DB_NAME = "database.db"

sample_questions = [
    ("What is the capital city of Australia?", "Sydney", "Melbourne", "Canberra", "Brisbane", "Canberra"),
    ("Which element has the chemical symbol 'O'?", "Gold", "Oxygen", "Silver", "Iron", "Oxygen"),
    ("What is 8 x 7?", "54", "56", "64", "42", "56"),
    ("Who is known as the father of computers?", "Alan Turing", "Charles Babbage", "Bill Gates", "Steve Jobs", "Charles Babbage"),
    ("Which planet has the most moons?", "Earth", "Mars", "Jupiter", "Venus", "Jupiter"),
    ("What is the boiling point of water at sea level?", "90°C", "100°C", "110°C", "120°C", "100°C"),
    ("What is the largest ocean on Earth?", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean", "Pacific Ocean"),
    ("What is the square root of 144?", "10", "11", "12", "13", "12"),
    ("Who wrote 'Romeo and Juliet'?", "William Wordsworth", "William Shakespeare", "Charles Dickens", "Jane Austen", "William Shakespeare"),
    ("What does CPU stand for?", "Central Processing Unit", "Computer Power Unit", "Central Program Unit", "Control Processing Unit", "Central Processing Unit"),
    ("Which country uses the yen as currency?", "China", "Japan", "South Korea", "Thailand", "Japan"),
    ("What is the chemical formula for table salt?", "H2O", "CO2", "NaCl", "O2", "NaCl"),
    ("Which instrument measures temperature?", "Barometer", "Thermometer", "Hygrometer", "Anemometer", "Thermometer"),
    ("What is the color of the sky on a clear day?", "Blue", "Green", "Red", "Yellow", "Blue"),
    ("How many continents are there on Earth?", "5", "6", "7", "8", "7"),
    ("What is 15% of 200?", "20", "25", "30", "35", "30"),
    ("Which gas do plants absorb from the air?", "Oxygen", "Hydrogen", "Carbon dioxide", "Nitrogen", "Carbon dioxide"),
    ("Which device is used to point and click on a computer screen?", "Keyboard", "Mouse", "Monitor", "Printer", "Mouse"),
    ("What is the main language spoken in Brazil?", "Spanish", "Portuguese", "French", "English", "Portuguese"),
    ("Which number is a prime number?", "4", "6", "9", "17", "17"),
    ("What is the value of pi rounded to two decimals?", "3.12", "3.14", "3.16", "3.18", "3.14"),
    ("Which animal is known as the king of the jungle?", "Tiger", "Lion", "Elephant", "Giraffe", "Lion"),
    ("What is the smallest unit of life?", "Atom", "Molecule", "Cell", "Organ", "Cell"),
    ("Which invention is Thomas Edison famous for?", "Telephone", "Light bulb", "Airplane", "Radio", "Light bulb"),
    ("Which planet is closest to the Sun?", "Venus", "Mars", "Mercury", "Earth", "Mercury"),
    ("Which continent is Egypt part of?", "Asia", "Europe", "Africa", "Australia", "Africa"),
]


def init_db():
    """Create the database tables and insert sample quiz questions."""
    connection = sqlite3.connect(DB_NAME)
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

    cursor.execute("DELETE FROM questions")
    cursor.executemany(
        "INSERT INTO questions (question, option1, option2, option3, option4, answer) VALUES (?, ?, ?, ?, ?, ?)",
        sample_questions,
    )
    connection.commit()
    connection.close()
    print(f"Initialized {DB_NAME} with {len(sample_questions)} questions.")


if __name__ == "__main__":
    init_db()
