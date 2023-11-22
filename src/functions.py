# This file is to teach you about functions in Python

# A simple function
def greet():
    print("Hello, World!")

# Call the function
greet()

# Function with parameters
def greet_person(name):
    print(f"Hello, {name}!")

# Call the function with an argument
greet_person("Alice")

# Function with default parameters
def greet_person_with_message(name, message="Good day"):
    print(f"{message}, {name}!")

# Call the function with one argument
greet_person_with_message("Bob")
# Call the function with two arguments
greet_person_with_message("Charlie", "Good evening")

# Function with return value
def add_numbers(num1, num2):
    return num1 + num2

# Call the function and print the return value
print(add_numbers(3, 4))

# Function with variable number of arguments
def print_args(*args):
    for arg in args:
        print(arg)

# Call the function with three arguments
print_args("one", "two", "three")

# Function with variable number of keyword arguments
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Call the function with three keyword arguments
print_kwargs(first="one", second="two", third="three")