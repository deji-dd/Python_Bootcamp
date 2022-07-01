# Create a generator that generates the squares of numbers up to some number N.
def gensquares(n):
    for y in range(n):
        yield y ** 2


for x in gensquares(10):
    print(x)
print('\n')

# Create a generator that yields "n" random numbers between a low and high number (that are inputs).
def rand_num(low, high, n):
    import random
    for y in range(n):
        yield random.randint(low, high)


for num in rand_num(1, 10, 12):
    print(num)
print('\n')

# Use the iter() function to convert the string below into an iterator:
s = 'hello'
s = iter(s)
print(next(s))
