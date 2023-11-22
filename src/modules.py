# Importing built-in modules
import math
import datetime

# Using functions from the math module
print("The square root of 16 is", math.sqrt(16))

# Using variables from the math module
print("The value of pi is", math.pi)

# Using the datetime module
current_date = datetime.date.today()
print("Today's date is", current_date)

# Importing a function from a module
from math import sqrt
print("The square root of 25 is", sqrt(25))

# Importing a module and giving it an alias
import datetime as dt
current_time = dt.datetime.now()
print("The current time is", current_time)