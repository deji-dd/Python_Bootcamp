x = 0
while x < 5:  # basic while loop. MAKE SURE TO AVOID INFINITE WHILE LOOPS!!
    print(f'The current value of x is {x}')
    x = x + 1
else:
    print('X is not less than 5')
print('\n')
x = [1, 2, 3]
for item in x:
    pass  # this makes the loop do nothing at all
mystring = 'Deji_Package'
for ltr in mystring:
    if ltr == 'e':
        continue  # goes back to the top of the closest enclosing loop
    if ltr == 'i':
        break  # breaks out of the current closest enclosing loop
    print(ltr)
print('\n')
x = 0
while x < 5:
    if x == 2:
        break
    print(x)
    x += 1
