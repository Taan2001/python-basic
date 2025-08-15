# What is exception handling?
# 1. Mechanism to gracefully handle runtime errors and maintain normal program flow.
# 2. Prevents program crashes by managing errors effectively.

# Why use exception handling?
# 1. To identify and manage specific error conditions.
# 2. To ensure cleanup actions (e.g., closing files, releasing resources). 
# 3. To provide meaningful error messages to users or logs

# Syntax:
"""
    try:  the block of code where errors may occur
    except: The block that handles the error if it occur
    else: Optional block executed if no exceptions occur
    finally: Optional block executed no matter what, used for cleanup

    ==> detail:

try:
    # Run this code
except: 
    # Execute this code when there is an exception
else:
    # No exception => run this code
finally:
    # Always run this code
        
"""

# Practice
# 1. 
my_dict = {
    "name": "Taan",
    "age": 20
}

try:
    result = 10 / 0
    my_value = my_dict["address"]
except ZeroDivisionError:
    print("Can't divided")
except AttributeError:
    print("Can't access attribute")


# 2.
try:
    num = int(input("Enter a integer > 0:"))
    result = 1000 / num
except ValueError:
    print("The number is wrong")
except ZeroDivisionError:
    print("The number is 0")
else:
    print(f"result: {result}")
finally:
    print("Completed!")