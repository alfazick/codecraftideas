
# Use assertions to check for conditions that should never occur. 
# Assertions can catch programming errors that are not supposed to happen 
# during normal execution, aiding in early detection of logic errors.

# Example 1 Basic: Checking Function Input

def calculate_square_root(number):
    # Assert that the input is a positive number 
    assert number > 0, "Number must be positive"
    return number ** 0.5 

# Correct usage
print(calculate_square_root(4))

# This will raisee an AssertionError 

# print(calculate_square_root(-1))

# Example 2 Medium-Easy: Ensuring List Non-emptiness

def get_first_element(elements):
    assert len(elements) > 0, "List cannot be empty"
    return elements[0]

# Correct usage
print(get_first_element([1, 2, 3]))

# This will raise an AssertionError
#print(get_first_element([]))


# Example 3: Medium Example: Chceking State Consistency

class BankAccount:
    def __init__(self, balance:float) -> None:
        assert balance >= 0, "Innitial balance cannot be negative"
        self.balance = balance

    def deposit(self, amount):
        assert amount > 0, "Deposit amount must be positive"
        self.balance += amount

    def withdraw(self, amount):
        assert amount > 0, "Withdrawl amount must be positive"
        assert amount <= self.balance, "Insufficient funds"
        self.balance -= amount

account = BankAccount(100)
account.deposit(50)
account.withdraw(20)
# This will raise an AssertionError due to insufficient funds
# account.withdraw(200)

# Example 4: Medium-UP: Verifying Preconditions for Calculating Median

def calculate_median(sorted_numbers):
    assert len(sorted_numbers) > 0, "Input list must not be empty"

    # Assert that the list is sorted
    assert (all(sorted_numbers[i] <= sorted_numbers[i+1] for i in range(len(sorted_numbers)-1))), "List must be sorted"

    n = len(sorted_numbers)

    mid = n//2

    if n % 2 == 0:
        return (sorted_numbers[n-1] + sorted_numbers[n])/2
    else:
        return sorted_numbers[mid]
    
# Correct usage with a sorted list
print(calculate_median([1, 2, 3, 4, 5]))

# This will raise an AssertionError because the list is not sorted
#print(calculate_median([5, 3, 1, 2, 4]))

# This will raise an AssertionError because the list is empty
#print(calculate_median([]))

# Example 5 Hard: Enforcing API Contract

def process_data(data):
    # Precondition: data must be a dictionary with specific keys

    assert isinstance(data,dict), "Input must be a dictionary"
    assert "name" in data and "age" in data, "Dictionary must contain 'name' and 'age'"

    # Simulate processing
    processed_data = {"processed_name": data["name"].upper(), "processed_age": data["age"] + 10}

    assert "processed_name" in processed_data and "processed_age" in processed_data, "Processing failed to meet requirements"

    return processed_data


# Correct usage
print(process_data({"name": "John", "age": 25}))

# This will raise an AssertionError
# print(process_data({"name": "John"}))


# Systems Programming Related Examples

# Example #1 Checking File Existence Before Processing

import os

def process_file(filepath):
    # Assert that the file exists
    assert os.path.exists(filepath), f"File {filepath} does not exist"

    with open(filepath, 'r') as file:
        print(file.read())

    

# If the file does not exist, this will raise an AssertionError
# process_file('nonexistent.txt')

# Example #2 Ensuring Adequate Permissions for File Opertaions

def modify_file(filepath):
    # Check read/write permissions
    assert os.access(filepath, os.R_OK), "File cannot be read"
    assert os.access(filepath, os.W_OK), "File cannot be written to"

    with open(filepath, 'a') as file:
        file.write("\nAdditional data.")

# # Assuming 'example.txt' exists and has proper permissions
# modify_file('app.log')

# # If the file cannot be written to, this will raise an AssertionError
# modify_file('readonly.txt')
        
# Example #3 Validating Process Execution Status
        
import subprocess

def run_command(command):
    # Run a system command and assert its success 
    result = subprocess.run(command,shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    assert result.returncode == 0, f"Command failed with error: {result.stderr.decode('utf-8')}"

    print(f"Command output:\n{result.stdout.decode('utf-8')}")

# Correct usage: assuming 'ls' is a valid command
run_command('ls')

# If the command fails, this will raise an AssertionError. Assuming 'some_nonexistent_command' does not exist.
# run_command('some_nonexistent_command')