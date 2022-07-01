# formatting with the .format() method
print('This is a string {}'.format('INSERTED'))
print('The {} {} {}'.format('fox', 'brown', 'quick'))
print('The {2} {1} {0}'.format('fox', 'brown', 'quick'))  # using indexing
print('The {q} {b} {f}'.format(f='fox', b='brown', q='quick'))  # using variables
# float formatting == "{value:width.precision f}"
result = 100/777
print(result)
print('The result was {}'.format(result))
print('The result was {r:1.3f}'.format(r=result))
# formatting with f-string literals
name = 'Deji_Package'
age = 19
print(f'Hello, his name is {name} and he is {age} years old.')
