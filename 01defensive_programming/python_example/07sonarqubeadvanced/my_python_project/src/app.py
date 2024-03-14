# Introducing a code smell: unnecessary complexity and hardcoded password
def complex_function(a, b):
    password = "admin"  # Hardcoded password
    if a > b:
        return a
    elif a < b:
        return b
    else:
        for i in range(5):
            print(i)
        return a

# Duplicate code - a code smell
def duplicate_code():
    for i in range(5):
        print(i)

def another_duplicate():
    for i in range(5):
        print(i)
