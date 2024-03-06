
# Intro Example#1
def process_positive_integer(number):
    if not isinstance(number,int):
        raise TypeError("Expected an integer")
    if number <= 0:
        raise ValueError("The number must be positive")
    
    # Process the positive integer here
    print(f"Processing number: {number}")


# Example usage
try:
    user_input = input("Please enter a positive integer: ")
    user_input = int(user_input)  # Convert input to integer
    process_positive_integer(user_input)
except ValueError as e:
    print(f"Invalid input: {e}")
except TypeError as e:
    print(f"Type error: {e}")

print("Reached that line without crushing the program")
# The isinstance function checks if the input is an integer.
# The program then checks if the number is positive.
# If the input fails any of these checks, the function raises an appropriate exception.
# The try block is used to catch and handle these exceptions, providing feedback to the user.

# Medium Example#2: Validate User Profile

import re

def is_valid_email(email):
    """Validate email using a simple regex"""
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None 

def validate_user_profile(profile):
    # Validate that profile is a dictionary
    if not isinstance(profile, dict):
        raise ValueError("Profile must be a dictionary.")
    
    # Validate that required keys exist
    required_keys = ["username", "age", "email"]
    for key in required_keys:
        if key not in profile:
            raise ValueError(f"Missing required fields: {key}")
        
    # Validate username
    if not isinstance(profile["username"], str):
        raise ValueError("Username must be a string.")
    if not profile["username"]:
        raise ValueError("Username cannot be empty")
    
    # Validate age
    if not isinstance(profile["age"], int):
        raise ValueError("Age must be an integer")
    if not 18 <= profile["age"] <= 120:
        raise ValueError("Age must be between 18 and 120.")
    
    # Validate email
    if not isinstance(profile["email"],str) or not is_valid_email(profile["email"]):
        raise ValueError("Invalid email address.")
    
    # If all validataions pass
    print("User profile is valid")


# Example usage
    
try:
    user_profile = {
        "username": "john_doe",
        "age": 25,
        "email": "john.doe@example.com"
    }

    validate_user_profile(user_profile)
except ValueError as e:
    print(f"Validation error: {e}")

# Type checking for each field to ensure they are of the expected type.
# Presence checking to ensure all required fields are provided.
# Value checking for the age to be within a specified range.
# Format validation using a regular expression to validate the email address format.
    
# Medium UP Example#3:
    
# The input validation must ensure that:

# The username is a non-empty string containing only 
# letters, numbers, and underscores, and is between 5 to 15 characters long.
    
# 1) The password is at least 8 characters long, containing at least 
# 2) one uppercase letter, one lowercase letter, one digit, and one special character.
# 3) The email is valid (using the same validation as our previous example).
# 4) The age is an integer within the range of 18 to 100.
# We'll use a combination of regular expressions and custom logic to validate this input.


import re

def is_valid_email(email):
    """Validate email using a simple regex."""
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

def is_valid_username(username):
    """Validate username."""
    return re.match(r'^\w{5,15}$',username) is not None 

def is_valid_password(password):
    """Validate password."""
    if len(password) < 8:
        return False
    has_upper = re.search(r'[A-Z]',password) is not None
    has_lower = re.search(r'[a-z]',password) is not None
    has_digit = re.search(r'\d',password) is not None 
    has_special = re.search(r'[\W_]', password) is not None 
    return has_digit and has_lower and has_special and has_upper

def validate_new_user(data):
    if not isinstance(data, dict):
        raise ValueError("Data must be a dictionary.")
    
    # Validate username
    if "username" not in data or not is_valid_username(data["username"]):
        raise ValueError("Invalid username")
    
    if "password" not in data or not is_valid_password(data["password"]):
        raise ValueError("Invalid password")
    
    if "email" not in data or not is_valid_email(data["email"]):
        raise ValueError("Invalid email")
    
    if "age" not in data:
        raise ValueError("Age is required")
    if not isinstance(data["age"],int) or not 18 <= data["age"] <= 100:
        raise ValueError("Invalid age.")
    
    print("User data is valid. Proceeding with account creation")

    # Example Input

user_data = {
    "username": "validUser_123",
    "password": "Passw0rd!",
    "email": "user@example.com",
    "age": 25
}

try:
    validate_new_user(user_data)
except ValueError as e:
    print(f"Validation error: {e}")


# Advanced Scenario Example #4
    
# Scenario Overview
# Imagine we're creating a user profile that includes:

# Personal Details: Username, password, email, and age, with the validation criteria previously defined.
# Addresses: A list of address objects, where each address must have a street, city, state (2 uppercase letters), and zip code (5 digits).
# Social Media Links (optional): Valid URLs for Facebook and Twitter.

# This example will introduce:

# Nested data structure validation.
# List validation where each item must meet certain criteria.
# Optional field validation with specific format requirements.

import re

def is_valid_email(email):
    return re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email) is not None

def is_valid_username(username):
    return re.match(r'^\w{5,15}$', username) is not None 

def is_valid_password(password):
    criteria = [
        lambda s: any(x.isupper() for x in s), # at least one uppercase letter
        lambda s: any(x.islower() for x in s), # at least one lowercase letter
        lambda s: any(x.isdigit() for x in s), # at least one digit
        lambda s: len(s) >= 8, # at least 8 characters long 
        lambda s: re.search(r'[\W_]',s) is not None # at least one special character
    ]

    return all(criterion(password) for criterion in criteria)

def is_valid_address(address):
    if not all(key in address for key in ["street","city", "state", "zip_code"]):
        return False
    if not re.match(r'^[A-Z]{2}$', address["state"]):
        return False
    if not re.match(r'^\d{5}$', address["zip_code"]):
        return False
    return True 

def is_valid_social_media(links):
    patterns = {
        "facebook": r'^(https?:\/\/)?(www\.)?facebook\.com\/[a-zA-Z0-9(\.\?)?]',
        "twitter": r'^(https?:\/\/)?(www\.)?twitter\.com\/[a-zA-Z0-9(\.\?)?]'
    }

    for key,url in links.items():
        if key in patterns and not re.match(patterns[key], url):
            return False
        
    return True 

def validate_user_profile(data):
    # Basic validations
    if not is_valid_username(data.get('username', '')):
        raise ValueError("Invalid username.")
    if not is_valid_password(data.get('password', '')):
        raise ValueError("Invalid password.")
    if not is_valid_email(data.get('email', '')):
        raise ValueError("Invalid email.")
    if not isinstance(data.get('age', 0), int) or not 18 <= data['age'] <= 100:
        raise ValueError("Invalid age.")
    
    #  Address validations

    if not isinstance(data.get("address",[]),list) or not all(is_valid_address(addr) for addr in data['addresses']):
        raise ValueError("Invalid address information")
    
    # Social media validations (optional fields)
    if 'social_media' in data and not is_valid_social_media(data['social_media']):
        raise ValueError("Invalid social media links.")

    print("User profile is valid. Proceeding with account creation.")



# Example input
user_profile = {
    "username": "validUser_123",
    "password": "Passw0rd!",
    "email": "user@example.com",
    "age": 30,
    "addresses": [
        {"street": "123 Main St", "city": "Anytown", "state": "NY", "zip_code": "12345"}
    ],
    "social_media": {
        "facebook": "https://www.facebook.com/validUser_123",
        "twitter": "https://twitter.com/validUser_123"
    }
}

try:
    validate_user_profile(user_profile)
except ValueError as e:
    print(f"Validation error: {e}")

