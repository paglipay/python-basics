# This is a Python script that introduces the basics of Python

# Variables and Data Types
# In Python, you don't need to declare the data type of a variable. 
# Python automatically determines the data type based on the value you assign.

# This is an integer
num = 10
print(type(num))  # <class 'int'>

# This is a float
pi = 3.14
print(type(pi))  # <class 'float'>

# This is a string
greeting = "Hello, World!"
print(type(greeting))  # <class 'str'>

# This is a boolean
is_python_fun = True
print(type(is_python_fun))  # <class 'bool'>

# Operators
# Python supports a variety of operators, such as arithmetic operators, comparison operators, and logical operators.

# Arithmetic operators
sum = num + pi
print(sum)  # 13.14

# Comparison operators
is_equal = num == pi
print(is_equal)  # False

# Logical operators
result = is_python_fun and is_equal
print(result)  # False