# Functions with multiple inputs
# def show_info(name, age):
#     print(f"{name} is {age} years old.")

# show_info("Subham", 18)


# Functions with Return Values
# def square(number):
#     return number * number

# result = square(5)
# print(f"The square of 5 is {result}")


# Functions with Default Parameters
# def greeting(name="Guest"):
#     print(f"Welcome, {name}!")

# greeting()
# greeting("Subham")


# Global vs Local Variables
# x = 10 # Global

# def my_func():
#     y = 5 # Local
#     print(f"Inside function: x={x}, y={y}")

# my_func()
# print(f"Outside function: x={x}")
# # print(y) # Error! 'y' only exists inside the function


# Lambda Functions
# Syntax: lambda arguments : expression
# add = lambda a, b: a + b
# print(f"Lambda Addition: {add(10, 20)}")

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error! Can't divide by zero."
    return a / b

# Testing our functions
num1 = 10
num2 = 5

print("Results : ")
print(f"Add: {addition(num1, num2)}")
print(f"Subtract: {subtraction(num1, num2)}")
print(f"Multiply: {multiplication(num1, num2)}")
print(f"Divide: {division(num1, num2)}")
print(f"Divide by zero: {division(num1, 0)}")
