# strings are immutable, therefore they do not support item assignment
name = 'Sam'
print(name)
last_letters = name[1:]
print(last_letters)
new_name = 'P' + last_letters  # string concatenation (merging)
print(new_name)
letter = 'z'
print(letter * 10)
x = 'Hello World'
print(x.upper())  # string methods
print(x.lower())
print(x.split())
x = 'Hi this is a string'
print(x.split('i'))
