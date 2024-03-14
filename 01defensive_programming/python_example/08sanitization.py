
# Sanitization: 
# Sanitize data by cleaning or escaping it to ensure that it does not contain harmful content, 
# especially when inserting into databases, generating HTML content, or executing system commands.

#1 Easy: Basic Input Sanitization for Database Queries
# => Objective: Prevent SQL Injection by sanitazing user inputs used in a database queries
# => Technique: Use parametrized queries with placeholders.

# import sqlite3

# conn = sqlite3.connect("example.db")
# c = conn.cursor()

# # Create a table
# c.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, age INTEGER)''')

# # User Input
# username = input("Enter username: ")
# age = input("Enter age: ")

# # Sanitize inputs by using parametrized queries
# c.execute("INSERT INTO users (username, age) VALUES (?, ?)", (username,age))

# # commit and close
# conn.commit()

# print(conn.execute("SELECT * FROM users").fetchall())

# conn.close()


# #2 Medium: Escaping HTML Content to Prevent XSS

# # Objective: Sanitize user input to be safely displayed as HTML,
# # preventing Cross-Site Scripting(XSS) attacks

# # Technique: Escape special HTML characters

# from html import escape

# # User input
# user_comment = input("Enter your comment")

# # simple ex : <script>alert('XSS Attack!');</script>
# sanitized_comment = escape(user_comment)
# print(f"Sanitized comment for HTML: {sanitized_comment}")

# print(user_comment)


# 3. Advanced: Validating and Sanitzining File Paths for Secure File Operations

# Objective: Prevent directory traversal attacks by sanitizing file paths received as input

# Technique: Use "os.path" and "os.path.abspath" to validate paths

# import os

# # User input
# user_file_path = input("Enter the path to the file you want to read: ").strip()

# # Base directory to restrict file operations
# BASE_DIR = os.path.abspath("/safe/directory/")

# # Join and normalize the path to prevent directory traversal
# safe_path = os.path.normpath(os.path.join(BASE_DIR, user_file_path))

# print(safe_path)
# # Check if the resolved path starts with the base directory
# if not safe_path.startswith(BASE_DIR):
#     print("Access denied: Attempted directory traversal.")
# else:
#     try:
#         with open(safe_path, 'r') as file:
#             print(file.read())
#     except FileNotFoundError:
#         print(f"File not found: {safe_path}")

# 4. Challenging: Sanitzing Shell Commands to Prevent Command Injection
        
# Objective: Safely execute system commands with user inputs by avoiding command injection.
# Technique: Use subprocess with a list of command arguments.

# import subprocess


# # User input
# user_input = input("Enter the file name to check its size: ")

# # Sanitize and execute command safely 

# result = subprocess.run(["ls", "-l", user_input], capture_output=True, text=True)

# print(result.stdout)

# Bonus: 
# secrets.compare_digest enhances security:

# When comparing secret values, such as API keys or passwords, in a straightforward manner 
# (e.g., using == in Python), the comparison typically stops as soon as a mismatch is found. 
# This means that comparisons of strings that are incorrect earlier will usually take less 
# time than comparisons for strings that are only incorrect at a later position. 
# An attacker can use these timing differences to gradually guess the correct value, 
# character by character.

# Constant-Time Execution: 
# By ensuring the comparison operation takes the same amount of time regardless of 
# the input, it prevents attackers from gaining useful information from timing 
# how long the comparison takes.

# Prevents Side-Channel Attacks: 
# Timing attacks are a type of side-channel attack. 
# By neutralizing the timing side-channel, secrets.compare_digest makes 
# these attacks impractical against the comparison operation.

# Useful for Secret Comparisons: This function is particularly useful for 
# comparing sensitive information like passwords, tokens, or API keys, 
# where preventing leaks of secret information is critical.

import os
import secrets

# Generate a secure API key
api_key = secrets.token_hex(20)  # Generates a 40-character hexadecimal string

# Set the generated API key as an environment variable
os.environ["API_KEY"] = api_key
print("API key generated and set successfully.")
print(os.environ["API_KEY"])

import secrets

# Example user input for an environment variable value
user_env_value = input("Enter the API key: ")

# Secure comparison
if secrets.compare_digest(user_env_value, os.environ["API_KEY"]):
    print("API key matches.")
else:
    print("Invalid API key.")

