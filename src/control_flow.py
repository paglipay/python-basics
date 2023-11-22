# This is a Python script that demonstrates control flow tools in Python

# Conditional statements
def test_conditional_statements(x):
    if x < 0:
        return 'Negative'
    elif x == 0:
        return 'Zero'
    else:
        return 'Positive'

# Loops
def test_loops():
    # For loop
    for i in range(5):
        print(f"For loop iteration: {i}")

    # While loop
    i = 0
    while i < 5:
        print(f"While loop iteration: {i}")
        i += 1

# Error handling
def test_error_handling(x):
    try:
        return 10 / x
    except ZeroDivisionError:
        return "Error: Division by zero"
    finally:
        print("This is the finally block. It always executes.")

# Test the functions
print(test_conditional_statements(-5))
print(test_conditional_statements(0))
print(test_conditional_statements(5))

test_loops()

print(test_error_handling(2))
print(test_error_handling(0))