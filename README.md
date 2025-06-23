Assignment 3 – Web Application with Database Integration and Selenium Automation
👨‍💻 Developed by:
Dhyey Patel
📝 Objective
Create a simple Flask web application with a login form, integrate it with a MySQL database, and automate login testing using Selenium.


🚀 Setup Instructions
🐳 Step 1: Start MySQL using Docker Compose
Run the following command in your terminal:
docker compose -f up.yml up --build
Use Adminer at http://localhost:8080 to manage your database if needed.
🛠️ Step 2: Create MySQL Table
Run this SQL in Adminer or MySQL CLI:

CREATE DATABASE IF NOT EXISTS test;
USE test;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);

🌐 Step 3: Install Requirements
Run this command:
pip install -r requirements.txt
Contents of requirements.txt:

flask
mysql-connector-python
selenium

🔧 Step 4: Run Flask App
Command:
python app.py
Visit: http://localhost:5000
🧪 Step 5: Run Selenium Test
Install dependencies (Codespaces):

sudo apt update
sudo apt install -y chromium-browser chromium-chromedriver

Then run the test:
python test_login.py
Expected output:
Selenium Test Passed: User found in database.
 Features
- HTML login form
- Flask backend inserts form data into MySQL
- Selenium fills out the form, submits it, and verifies via DB query

