# Learning from https://www.geeksforgeeks.org/python/descriptor-in-python/ and https://chatgpt.com/share/69ce9c4c-47f0-8320-ac0a-3968bc216061
# In general, a descriptor is an attribute value that has one of the methods in the descriptor protocol. Basically helps adding checks/conditions/logging.

# Descriptor Protocol Methods :
# __get__(self, obj, objtype=None) # Runs when attribute is read
# __set__(self, obj, value) # Runs when attribute is assigned
# __delete__(self, obj) Runs  # when attribute is deleted
# __set_name__(self, owner, name) # optional 

class Age:
    def __get__(self, instance, owner):
        return instance._age

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        instance._age = value


class Person:
    age = Age()   # descriptor

    def __init__(self, age):
        self.age = age   # calls __set__


p = Person(20)
print(p.age)   # 20

p.age = 30     # calls __set__
print(p.age)   # 30
