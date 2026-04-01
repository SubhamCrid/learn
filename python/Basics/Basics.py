# x = 5
# y = "Subham"
# z = ["Drink", 12, True]
# a = ("Shy", 25, False)
# b = {"name": "Subham", "age":18.2}
# # print (f"{x} : {type(x)}\n {y} : {type(y)}\n {z} : {type(z)}\n {a} : {type(a)}\n {b} : {type(b)}")

# z.append("Subham")
# print(z)
# # z.pop()
# # print(z)
# print(z[1:2]) # start included end excluded

# Basic Calculator

while True:
  print ('''
  2 number Basic Calculator
  1. Addition
  2. Substraction
  3. Multiplication
  4. Division
  ''')
  user_input = input("Enter your choice (1-4): ")
  
  try:
    num1 = float(input("Enter 1st number: "))
    num2 = float(input("Enter 2nd number: "))
  except ValueError:
    print("Invalid input! Please try again!")
    continue

  if user_input == "1":
    print(f"Addition of {num1} and {num2} is {num1 + num2}")
  elif user_input == "2":
    print(f"Substraction from {num1} of {num2} is {num1 - num2}")
  elif user_input == "3":
    print(f"Multiplication of {num1} and {num2} is {num1 * num2}")
  elif user_input == "4":
    if num2 != 0:
      print(f"Division of {num1} by {num2} is {num1 / num2}")
    else:
      print("Error: Division by zero is not allowed.")
  else:
    print("Invalid choice! Please select 1, 2, 3, or 4.")
    continue

  choice = input("Enter 'y' to continue, or any other key to exit: ").lower()
  if choice != 'y':
    break

random_list = ["Subham", 25, 28, 12, "Chocolate", True, 12.5]
for i in random_list:
  print(i)