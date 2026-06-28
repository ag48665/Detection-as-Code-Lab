import sqlite3

# Connect to the database
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# User input
username = input("Username: ")
password = input("Password: ")

# Vulnerable SQL query (SQL Injection)
query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"

cursor.execute(query)

user = cursor.fetchone()

if user:
    print("Login successful!")
else:
    print("Invalid username or password.")

conn.close()