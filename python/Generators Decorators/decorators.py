# learning from https://youtu.be/vAFl6tvrxOo

# def log_deco(func):
#   def wrap(*args):
#     print("values", args)
#     result = func(*args)
#     print("Result", result)
#     return result
#   return wrap

# def greater_first(func):
#   def wrap(a,b):
#     if a<b:
#       a,b=b,a
#     return func(a,b)
#   return wrap
# @log_deco
# @greater_first
# def divide(a, b):
#   return a / b
# @log_deco
# @greater_first
# def sub (a,b):
#   return a-b

# @log_deco
# def add(a,b,c):
#   return a+b+c

# # sub = greater_first(sub)
# # divide = greater_first(divide) # same thing as @greater_first in old way

# print(divide(2,4))
# print(sub(2,4))
# print (add(5,7,6))

def log_deco(func):
  def wrap():
    print("Before")
    func()
    print("After")
  return wrap
@log_deco
def greet():
  print("Hello, World!")
greet()

#Real life reason : For adding conditions before calling an existing functions Eg : Logging
