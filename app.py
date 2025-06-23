from flask import Flask, request, render_template
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",       # Use "mysql" if running via Docker Compose
        user="root",
        password="password",    # Replace with your MySQL password
        database="test"
    )

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        conn.commit()
        cursor.close()
        conn.close()

        return "Login submitted and saved to database!"
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
