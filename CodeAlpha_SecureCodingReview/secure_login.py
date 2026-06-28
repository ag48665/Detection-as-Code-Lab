import sqlite3
import hashlib
import getpass

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

username = input("Username: ").strip()
password = getpass.getpass("Password: ")

hashed_password = hash_password(password)

query = "SELECT * FROM users WHERE username = ? AND password = ?"

cursor.execute(query, (username, hashed_password))

user = cursor.fetchone()

if user:
    print("Login successful!")
else:
    print("Invalid username or password.")

conn.close()