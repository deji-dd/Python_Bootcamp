def myfunc(*args):  # *args allows multiple arguments to be taken in
    return sum(args) * 0.05
def my_func(**kwargs):
    if 'fruit' in kwargs:
        print(f"My fruit of choice is {kwargs['fruit']}")
    else:
        print('I did not find any fruit here')


print(myfunc(40, 60, 80, 90, 50, 100))
my_func(fruit='apple', veggies='lettuce')
def myfunc(*args, **kwargs):
    print(f"I would like {args[0]} {kwargs['food']}")


myfunc(10, 20, 30, 40, fruit='orange', food='eggs', animal='dog')
