# Learning from following video : https://youtu.be/kj850Y8y8FI

# def is_even(n):
#   return n%2 == 0

# def update(n):
#   return(n*2)

# def add_all(a,b):
#   return a+b

from functools import reduce

nums = [3, 2, 6, 8, 4, 6, 2, 9]

evens = list(filter(lambda n : n%2==0 ,nums))

doubles = list(map(lambda n : n*2,evens))

sum = reduce(lambda a,b: a+b, doubles)

print(evens)
print(doubles)
print(sum)