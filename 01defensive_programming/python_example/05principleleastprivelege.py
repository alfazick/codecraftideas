
# The Principle of Least Privilege is a fundamental concept in computer security, 
# advocating for minimal user and process permissions to perform required tasks, 
# thus limiting the impact of a security breach. 

# In programming, this principle can be implemented in various ways, 
# including operating system-level permission controls, 
# database access restrictions, and limited use of high-privilege accounts in code.

# Example #1 Basic: File Access with Minimal Permissions

# try:
#     with open('config.txt', 'r') as config_file:
#         config = config_file.read()
#         print("Config file sucessfully read.")
# except FileNotFoundError:
#     print("Error: The confugartion file does not exist")
# except PermissionError:
#     print("Error: Insufficient permissions to read the configuration file.")


# Example #2 Medium:  Dropping Privileges
    
import os
import subprocess

def drop_priveleges():
    if os.getuid() == 0:
        # Assuming a non-root user with UID 1000 exists
        os.seteuid(1000)
        print("Priveleges dropped, running as a non-root user.")

drop_priveleges()
# Continue with logic
# to check run as sudo python3 script_name.py 


# Example #3 Medium-Up: Secure Temporary File Creation

import tempfile

with tempfile.NamedTemporaryFile(mode='w+t', delete=True) as temp_file:
    temp_file.write('Some sensitive data')
    temp_file.seek(0)
    # Process the file
    print(temp_file.read())

# File is automatically deleted, minimizing exposure


# Using secure temporary files is essential in many scenarios, especially where 
# data security and integrity are paramount. 
# Here are three different scenarios where the approach demonstrated 
# with tempfile.NamedTemporaryFile is essential

# Scenario 1: Processing Sensitive User Data

import tempfile

def reverse_text(text):
    """Simple function to reverse text."""
    return text[::-1]

def process_user_upload(uploaded_text):
    """Process uploaded text document securely."""
    with tempfile.NamedTemporaryFile(mode='w+t', delete=True) as temp_file:
        temp_file.write(uploaded_text)
        temp_file.seek(0) # Go back to the start of the file for reading

        content = temp_file.read()
        processed_content = reverse_text(content) # Example processing

        print(f"Processed Content: {processed_content}")

# Simulate user uploading a document
uploaded_document = "Sensitive information here."
process_user_upload(uploaded_document)

#Scenario 2: Generating and Using Temporary Credentials

import tempfile
import secrets

def generate_api_key():
    """Generate a secure, random API key."""
    return secrets.token_hex(16)

def use_temporary_credentials():
    """Generate and use temporary credentials securely."""
    api_key = generate_api_key()
    with tempfile.NamedTemporaryFile(mode='w+t', delete=True) as temp_file:
        temp_file.write(f"Api_key={api_key}")
        temp_file.seek(0)

        # Simulate reading the API key back from the file for use
        credentials = temp_file.readline().strip()
        print(f"Using credentials: {credentials} for temporary access.")


use_temporary_credentials()

import tempfile
import json

def cache_and_process_data(data):
    """Cache data temporarily and process it in a background job."""
    with tempfile.NamedTemporaryFile(mode='w+t', delete=True) as temp_file:
        # Cache the data
        json.dump(data, temp_file)
        temp_file.seek(0)
        
        # Simulate a background job reading and processing the data
        processed_data = json.load(temp_file)
        print(f"Background job processed data: {processed_data}")

# Example data to cache and process
user_data = {"id": 123, "name": "Alice", "email": "alice@example.com"}
cache_and_process_data(user_data)



