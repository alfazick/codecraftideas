# Code Reviews and Static Analysis: 
# Regularly review code manually and use static analysis tools to detect 
# potential security vulnerabilities, bugs, and bad practices early in the development cycle.



# Easy: flake8 check your code against PEP 8 and programming errors

# pip install flake8

# bad_style.py

def calculate(a,b):
    result=a+b
    print("The result is:",result)
    return result


# in command line 
# flake8 bad_style.py


# Medium : mypy to identify type issues 

# pip install mypy 

#type_issue.py

def greet(name:str) -> str:
    return "Hello " + name 

try:
    greet(123) # not good 
except:
    pass 

# mypy type_issue.py 

# Advanced: Using 'bandit' to Identify Security Issues

# pip install bandit 

# security_risk.py 

user_input = input("Enter your name: ")
print(eval(user_input))

