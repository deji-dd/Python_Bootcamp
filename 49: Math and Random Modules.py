import math
import random

value = 4.35
print(math.floor(value))  # rounds a number down to the nearest whole number
print(math.ceil(value))  # rounds a number up to the nearest whole number
print(math.pi)  # returns pi
print(math.e)  # returns e
print(math.log(100))
print(math.degrees(math.pi/2))  # converts to degrees
print(math.radians(180))  # converts to radians
print(random.randint(0, 100))  # returns a random integer in a given range
random.seed(101)
print(random.randint(0, 100))
print(random.randint(0, 100))
print(random.randint(0, 100))
print(random.randint(0, 100))
print(random.randint(0, 100))
mylist = list(range(0, 20))
print(random.choice(mylist))
print(random.choices(mylist, k=10))
print(random.sample(mylist, k=10))
print(random.uniform(0, 100))  # returns a random integer in a given range, including floating point values
