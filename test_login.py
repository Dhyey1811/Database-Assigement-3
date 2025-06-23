from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import mysql.connector
import time
import tempfile
import os

# Configure Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run without GUI
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument(f"--user-data-dir={tempfile.mkdtemp()}")

# If using Codespaces: set Chromium browser paths
chrome_options.binary_location = "/usr/bin/chromedriver"
driver_path = "/usr/bin/chromedriver"


# Start WebDriver
driver = webdriver.Chrome(service=Service(driver_path), options=chrome_options)

# Target Flask app URL
driver.get("http://localhost:5000/")

# Test credentials
test_username = "seleniumuser"
test_password = "seleniumpass123"

# Fill and submit the form
driver.find_element(By.NAME, "username").send_keys(test_username)
driver.find_element(By.NAME, "password").send_keys(test_password)
driver.find_element(By.NAME, "submit").click()

# Allow Flask to insert into DB
time.sleep(2)

# Connect to MySQL to verify the entry
conn = mysql.connector.connect(
    host="localhost",     # Or 'mysql' if using Docker container name
    user="root",
    password="password",  # Match your DB password
    database="test"
)
cursor = conn.cursor()
cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (test_username, test_password))
result = cursor.fetchone()

# Output result
if result:
    print("✅ Selenium Test Passed: User found in database.")
else:
    print("❌ Selenium Test Failed: User not found in database.")

# Cleanup
cursor.close()
conn.close()
driver.quit()
