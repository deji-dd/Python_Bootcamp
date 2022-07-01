def sqr(num):
    return num ** 2


my_nums = [1, 2, 3, 4, 5]
for item in map(sqr, my_nums):  # the map function can run a defined function through a list instead of using a for loop
    print(item)
print(list(map(sqr, my_nums)))  # you can return it as a list
def splicer(mystring):
    if len(mystring) % 2 == 0:
        return 'Even'
    else:
        return mystring[0]


names = ['Andy', 'Eve', 'Sally']
print(list(map(splicer, names)))
def check_even(num):
    return num % 2 == 0


mynums = [1, 2, 3, 4, 5, 6]
print(list(filter(check_even, mynums)))  # returns only the elements in a list for which the function used returns True
# lambda expressions are known as anonymous expressions as they are intended for functions with only one time use
sqr = lambda num: num ** 2  # a lambda expression


print(sqr(3))
print(list(map(lambda num: num ** 2, mynums)))
print(list(filter(lambda num: num % 2 == 0, mynums)))
print(list(map(lambda name: name[::-1], names)))
