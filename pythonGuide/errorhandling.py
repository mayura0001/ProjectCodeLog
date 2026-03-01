"""
PYTHON ERROR HANDLING - COMPLETE GUIDE
Author: Your Name
Purpose: Teach Python error handling from beginner → advanced level

Error handling prevents your program from crashing when unexpected
situations occur.

Instead of crashing, your program can:
- show proper message
- recover safely
- continue execution
"""

# ============================================================
# SECTION 1: BASIC ERROR EXAMPLE (WITHOUT ERROR HANDLING)
# ============================================================

print("\n--- SECTION 1: Basic error example ---")

# This will crash if user enters non-number
# Uncomment to test crash behavior

# number = int(input("Enter a number: "))
# print("You entered:", number)

# Problem: if user enters "abc"
# Python throws ValueError and program stops


# ============================================================
# SECTION 2: TRY and EXCEPT (Basic error handling)
# ============================================================

print("\n--- SECTION 2: try and except ---")

try:
    number = int(input("Enter a number: "))
    print("You entered:", number)

except:
    print("Error: You must enter a valid number.")

# Explanation:
# try = code that may cause error
# except = runs if error occurs


# ============================================================
# SECTION 3: CATCH SPECIFIC ERRORS (Best practice)
# ============================================================

print("\n--- SECTION 3: specific exception handling ---")

try:
    num = int(input("Enter number: "))
    result = 10 / num
    print("Result:", result)

except ValueError:
    print("Error: Invalid number format.")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

# Why specific exceptions?
# Better debugging and control


# ============================================================
# SECTION 4: USING else (runs if NO error occurs)
# ============================================================

print("\n--- SECTION 4: try, except, else ---")

try:
    num = int(input("Enter number: "))
except ValueError:
    print("Invalid input.")
else:
    print("Success! Number is:", num)

# else runs ONLY if try succeeds


# ============================================================
# SECTION 5: USING finally (always runs)
# ============================================================

print("\n--- SECTION 5: finally block ---")

try:
    file = open("example.txt", "r")
    content = file.read()
    print(content)

except FileNotFoundError:
    print("File not found.")

finally:
    print("This always runs (cleanup code).")

# finally is used for:
# - closing files
# - releasing resources
# - cleanup


# ============================================================
# SECTION 6: FULL PROFESSIONAL EXAMPLE
# ============================================================

print("\n--- SECTION 6: professional example ---")

def divide_numbers():
    """
    Function that safely divides two numbers
    """

    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        result = a / b

    except ValueError:
        print("Error: Please enter valid numbers.")

    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

    else:
        print("Result is:", result)

    finally:
        print("Division operation complete.")


divide_numbers()


# ============================================================
# SECTION 7: CATCH MULTIPLE ERRORS IN ONE EXCEPT
# ============================================================

print("\n--- SECTION 7: multiple exception handling ---")

try:
    x = int(input("Enter integer: "))
    result = 100 / x

except (ValueError, ZeroDivisionError):
    print("Invalid input or division by zero.")


# ============================================================
# SECTION 8: GETTING ERROR DETAILS
# ============================================================

print("\n--- SECTION 8: getting error details ---")

try:
    num = int(input("Enter number: "))

except ValueError as error:
    print("Error occurred:", error)

# "as error" gives error message


# ============================================================
# SECTION 9: RAISING YOUR OWN ERRORS
# ============================================================

print("\n--- SECTION 9: raising custom exception ---")

def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")

    print("Age is valid:", age)

try:
    check_age(-5)

except ValueError as error:
    print("Custom error caught:", error)


# ============================================================
# SECTION 10: COMPLETE REAL-WORLD EXAMPLE
# ============================================================

print("\n--- SECTION 10: real-world login simulation ---")

def login_system():
    correct_password = "python123"

    try:
        password = input("Enter password: ")

        if password != correct_password:
            raise Exception("Wrong password")

    except Exception as error:
        print("Login failed:", error)

    else:
        print("Login successful")

    finally:
        print("Login attempt finished")

login_system()


# ============================================================
# SUMMARY
# ============================================================

"""
KEY CONCEPTS:

try:
    risky code

except:
    handles error

else:
    runs if no error

finally:
    runs always

raise:
    create custom error

BEST PRACTICE:
Always use specific exceptions, not bare except.
"""


print("\nProgram finished safely.")