# Timeouts and Resource Limits: Implement timeouts and set resource limits for operations 
# that may hang or consume excessive amounts of resources 
# (e.g., file operations, network requests, and database queries). 
# This prevents denial-of-service conditions and helps ensure system responsiveness.

# Easy: Implementing a Timeout for a Network Request

# import requests 
# def fetch_data(url):
#     try:
#         response = requests.get(url,timeout=5) # Timeout after 5 seconds
#         return response.text 
#     except requests.Timeout:
#         return "Request timed out"

# # Example usage
# url = "http://example.com"
# print(fetch_data(url))

# Introducing shlex
# import shlex
# text = 'command "argument with spaces" \'another one\' an\\ escaped\\ space'
# print(text.split(" "))
# arguments = shlex.split(text)
# print(arguments)

# # Medium: Setting Resource Limits for a Subprocess

# import subprocess
# import shlex # shell like parser

# def run_command_with_timeout(command,timeout):
#     try:
#         result = subprocess.run(shlex.split(command), timeout = timeout, capture_output = True)
#         return result.stdout 
#     except subprocess.TimeoutExpired:
#         return "Command timed out"

# # Example usage
# command = "sleep 10"
# print(run_command_with_timeout(command, 5))

# Hard: Implementing Timeouts for File Operations

# import threading

# def read_file_with_timeout(filename, timeout):
#     content = [None]

#     def read_file():
#         try:
#             with open(filename, 'r') as file:
#                 content[0] = file.read()
#         except FileNotFoundError:
#             return "Non exist"


#     thread = threading.Thread(target = read_file)
#     thread.start()
#     thread.join(timeout = timeout)
#     if thread.is_alive():
#         return "Reading file timed out"
#     else:
#         return content[0]


# # Example usage
# filename = "app.log"
# print(read_file_with_timeout(filename, 5))

# Challenging: Limiting Memory usage of a Python Script

# Limiting memory usage directly in Python is complex because Python does not offer 
# built-in mechanisms for setting strict memory limits on a script. 
# However, you can use the resource module (Unix-based systems only) to set 
# soft and hard limits on memory usage.

import resource
import os 

def set_memory_limit(memory_in_mb):
    soft, hard = memory_in_mb * 1024 * 1024, memory_in_mb * 1024 * 1024
    resource.setrlimit(resource.RLIMIT_AS, (soft,hard))

def allocate_memory():
    a = []
    while True:
        a.append(" " *10 ** 6) # Try to allocate a lot of memory, malloc will be called 


try:
    set_memory_limit(100) # Limit memoru usage to 100 mb
    allocate_memory()
except MemoryError:
    print("Memory limit reached!")

# This will work only on unix-based systems
    