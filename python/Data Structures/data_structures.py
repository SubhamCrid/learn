# list = ["Subham", 25, 28, 12, "Chocolate", True, 12.5, "Subham"]
# tuple = ("Subham", 25, 28, 12, "Chocolate", True, 12.5)
# dictionary = {"name": "Subham", "age": 18.2}
# set = {"Subham", 25, 28, 12, "Chocolate", True, 12.5}
# string = "Subham"

# print(f"{list} : {type(list)}\n {tuple} : {type(tuple)}\n {dictionary} : {type(dictionary)}\n {set} : {type(set)}\n {string} : {type(string)}")

# Everything with lists that I know.
# list = ["Subham", 25, 28, 12, "Chocolate", True, 12.5, "Subham"]
# list.append("noice")
# print(list)
# list.pop()
# print(list)
# print(list[3:1:-1])
# print(list.index("Subham"))
# print(list.count("Subham"))
# print(list[::-1])
# list.extend(["noice", "Subham"])
# print(list)
# # list.clear()
# # print(list)
# print(list)
# list.sort()
# print(list)

# For tuple its mostly similar its just an immutable list. It can do everthing a list can do with the sole exception of modifying itself.
# tuple = ("Subham", 25, 28, 12, "Chocolate", True, 12.5)
# print(tuple)
# print(tuple[3:1:-1])
# print(tuple.index("Subham"))
# print(tuple.count("Subham"))
# print(tuple[::-1])
# # tuple.extend(["noice", "Subham"])
# # print(tuple)
# # tuple.clear()
# # print(tuple)
# # print(tuple)
# # tuple.sort()
# # print(tuple)

# Everything I can do with dictionaries
# my_dict = {"name": "Subham", "age": 18, "is_noice": True}
# print(my_dict["name"])
# my_dict["location"] = "Earth"
# print(my_dict)
# my_dict.update({"food": "Chocolate", "drinks": "Water"})
# print(my_dict)
# print(my_dict.keys())
# print(my_dict.values())
# print(my_dict.items())
# my_dict.pop("age")
# print(my_dict)
# my_dict.clear()
# print(my_dict)

# Everything in Sets with python (Mainly : Duplicates not allowed that's about it)
# my_set = {"Subham", 25, 28, 12, "Chocolate", True, 12.5}
# print(my_set)
# my_set.add("Subham")
# print(my_set)
# my_set.remove("Subham")
# print(my_set)
# my_set.pop()
# print(my_set)
# my_set.clear()
# print(my_set)

# Everything with strings in python
string = "Subham"
print(string[0])
print(string[3:6])
print(string[::-1])
print(len(string))
print(string.upper())
print(string.lower())
print(string.strip()) # remove spaces
print(string.replace("S", "Z"))
print(string.split("u")) # split into a list
print(string.find("a")) # find index
print(string.count("h")) # count
name = "Subham"
hobby = "Coding"
print(f"Hi, I'm {name} and I love {hobby}!")
print("Subham" + " " + "Coding")
print("noice " * 5)
print("a" in string)
print(string.isnumeric())
story = """Multi
line
string"""
print(story)
