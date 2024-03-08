# Error Handling: Implement comprehensive error handling that catches and, 
# if possible, recovers from errors gracefully. 
# Logging errors for later analysis can also help with identifying and fixing underlying issues.


# Example #1 Basic: Try-Except Block

def divide_numbers():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1/num2 
        print("The result is: ", result)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    

# divide_numbers()


# Example #2 Medium: Handling Multiple Exceptions

def read_file_content(filename):
    try:
        with open(filename, 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print("The file does not exist")
    except IsADirectoryError:
        print("The specified path is a directory, not a file.")

read_file_content("example.txt")

# Example #3 Medium-UP: Exception Chaining

def confugure_system(path):
    try:
        if path == "/forbidden":
            raise PermissionError("Access to the path is forbidden.")
    except PermissionError as e:
        raise RuntimeError("System configuration failed") from e
    

try:
    confugure_system("/forbidden")
except RuntimeError as e:
    print(e)
    print("Original cause: ", e.__cause__)


# Example #4 Medium-UP: Logging errors
    
import requests
import logging

logging.basicConfig(filename="app.log",filemode="w", format='%(name)s - %(levelname)s - %(message)s')


def fetch_data_from_api(url):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        logging.error(f"HTTPError: {e} for URL {url}")
        return None 
    except requests.exceptions.ConnectionError:
        logging.error(f"ConnectionError: Failed to connect to {url}")
        return None
    except requests.exceptions.Timeout:
        logging.error(f"Timeout: The request to {url} timed out.")
        return None
    except requests.exceptions.RequestException as e:
        logging.error(f"RequestException: An error occurred while handling the request to {url}. Error: {e}")
        return None
    else:
        # process the response
        try:
            data = response.json()
            return data 
        except ValueError:
            logging.error(f"JSONDecodeError: Failed to decode JSON response from {url}")
            return None
        
url = "https://api.example.com/data"
data = fetch_data_from_api(url)
if data:
    print("Data fetched successfully!")
else:
    print("Failed to fetch data. Check the log for errors.")



# Example 5: Hard : Custom Exceptions
    
class NetworkError(Exception):
    """Base class for network-related errors"""
    pass 

class ServerUnreachableError(NetworkError):
    """Exception raised when the server is unreachable"""
    def __init__(self, server):
        self.server = server
        self.message = f"Cannot connect to server {server}. Server is unreachable."
        super().__init__(self.message)

class ConnectionTimeoutError(NetworkError):
    """Exception raised when the connection to the server times out."""
    def __init__(self, server, timeout):
        self.server = server
        self.timeout = timeout
        self.message = f"Connection to server {server} timed out after {timeout} seconds."
        super().__init__(self.message)


def connect_to_server(server):
    if server == "server_unreachable":
        raise ServerUnreachableError(server)
    elif server == "connection_timeout":
        raise ConnectionTimeoutError(server, 5)
    else:
        print(f"Succesfully connected to server {server}")


try:
    connect_to_server("server_unreachable")
except ServerUnreachableError as e:
    print(f"Error: {e}")
except ConnectionTimeoutError as e:
    print(f"Error: {e}")
except NetworkError:
    print("A general network error occurred.")
else:
    print("Connection successful.")
finally:
    print("Attempt to connect to server has completed.")

    