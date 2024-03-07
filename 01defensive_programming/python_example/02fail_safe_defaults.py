
# Use safe default values that system remains 
# in a secure and non-critical state if something goes wrong
 
# Example #1 Basic: Default Argument in Function

def safe_division(num,denom=1):
    """Performs safe division, ensuring the denominator is not zero."""
    if denom == 0:
        print("Denominator was zero. Defaulted to 1.")
        denom = 1
    return num/denom


# Examples
print(safe_division(10, 2))  # Regular division
print(safe_division(10))    # Uses fail-safe default
print(safe_division(10, 0)) # Avoids division by zero with fail-safe

# Example #2 Medium: Configuration Defaults

import json 

def load_configuration(file_path):
    """Loads configuration from a file, defaults if necessary."""
    default_config = {"timeout": 30, "retry_attempts":3,"log_level":"INFO"}
    try:
        with open(file_path, 'r') as config_file:
            config = json.load(config_file)
            # ensure all necessary configurations are present
            for key,value in default_config.items():
                config.setdefault(key,value)

    except:
        print("Configuration file not found. Using default configs.")
        config = default_config

    return config 

# Assume we have a configuration file. In a real scenario, this path might be dynamic or incorrect.
config = load_configuration('path/to/nonexistent/config.json')
print(config)

# Example #3 Medium Up: Safe API Call with Timeout Default

import requests

def safe_api_call(url, timeout = 5):
    """Make a safe API call with a specified timeout"""
    try:
        response = requests.get(url, timeout=timeout)
        return response.json()
    except requests.exceptions.Timeout:
        print(f"Request timed out after {timeout} seconds. Using fail-safe response.")
        return {'status': 'fail', 'data': 'Request timed out'}
    except requests.exceptions.RequestException as e:
        print(f"An error occured: {e}")
        return {"status":"fail", "data":"Error in request"}
    

# Example API call
result = safe_api_call('https://api.example.com/data')
print(result)

# Example #4  Database Connection with Fail-Safe Read Option and Parametrized Queries

import sqlite3

def get_user_data(user_id, default_data = {}):
    """Attempts to retrieve user data from the database, defaults to cached data on failure, using parameterized SQL queries for safety."""
    conn = None
    try:
        conn = sqlite3.connect("example.db", timeout=10)
        cursor = conn.cursor()
        # Using a parametrized query for security

        # UNSAFE: Using string formatting to include user input directly into the SQL command
        # query = f"SELECT * FROM users WHERE id='{user_id}'"
        # cursor.execute(query)
        cursor.execute("SELECT * FROM users WHERE id=?", (user_id,))
        data = cursor.fetchone()
        if data:
            return data
        else:
            print("User not found. Using default data.")
            return default_data
    except (sqlite3.OperationalError, sqlite3.DatabaseError) as e:
        print(f"Database error: {e}. Using fail-safe default data.")
        return default_data
    finally:
        if conn:
            conn.close()

# Assume there's a user ID and default data as a fail-safe
user_data = get_user_data('123', {'name': 'Unknown', 'email': 'no-reply@example.com'})
print(user_data)


# Note Important:
# The line cursor.execute("SELECT * FROM users WHERE id=?", (user_id,)) in Python, 
# when using the sqlite3 library, demonstrates the use of a parameterized query. 
# Parameterized queries are a fundamental aspect of writing secure SQL code because 
# they help prevent SQL injection attacks. Here's a breakdown of what this line does:

# cursor.execute(): This method executes an SQL statement. 
# The cursor object is used to interact with the database, 
# allowing you to execute SQL queries and fetch data.

# SQL Query: "SELECT * FROM users WHERE id=?" is the SQL query being executed. 
# This query selects all columns (*) from the users table where the id column matches a specific value.

# Parameter ?: The question mark (?) is a placeholder for a parameter in the SQL query. 
# Using placeholders instead of directly concatenating values into the SQL string prevents 
# SQL injection, a common security vulnerability where an attacker can execute arbitrary 
# SQL commands by manipulating the input.

# Parameters (user_id,): The parameters for the SQL query are passed as a tuple. 
# In this case, (user_id,) is the tuple containing the user_id value that will 
# replace the placeholder (?) in the query. Even if there's only one parameter, 
# it should be passed as a tuple (hence the comma after user_id).

# By using parameterized queries, the database driver automatically 
# handles escaping of the parameters, ensuring that the input is treated as a 
# data value rather than part of the SQL command. This mechanism effectively mitigates 
# the risk of SQL injection, making your database interactions safer.