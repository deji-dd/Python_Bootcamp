mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in mylist:  # basic for loop example
    print(num)
print('\n')
for num in mylist:  # for loop to return only even numbers
    if num % 2 == 0:
        print(f'{num} is an even number')
    else:
        print(f'{num} is an odd number')
print('\n')
list_sum = 0
for num in mylist:  # for loop to return the total value in a list
    list_sum = list_sum + num
print(f'total value in mylist is {list_sum}')
print('\n')
mystring = 'Hello World'
for letter in mystring:
    print(letter)
print('\n')
tup = (1, 2, 3)
for n in tup:
    print(n)
print('\n')
mylist = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
for a, b in mylist:
    print(a)
    print(b)
    print(f'{a} + {b} = {a + b}')
print('\n')
d = {'k1': 1, 'k2': 2, 'k3': 3}
for key, value in d:
    print(key)
