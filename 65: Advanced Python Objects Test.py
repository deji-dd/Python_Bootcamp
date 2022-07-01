# Convert 1024 to binary and hexadecimal representation
print(bin(1024))
print(hex(1024))

# Round 5.23222 to two decimal places
print('\n')
print(round(5.23222, 2))

# Check if every letter in the string s is lower case
print('\n')
s = 'hello how are you Mary, are you feeling okay?'
print(s.islower())

# How many times does the letter 'w' show up in the string below?
print('\n')
s = 'twywywtwywbwhsjhwuwshshwuwwwjdjdid'
print(s.count('w'))

# Find the elements in set1 that are not in set2
print('\n')
set1 = {2, 3, 1, 5, 6, 8}
set2 = {3, 1, 7, 5, 6, 8}
print(set1.difference(set2))

# Find all elements that are in either set
print('\n')
print(set1.union(set2))

# Create this dictionary: {0: 0, 1: 1, 2: 8, 3: 27, 4: 64} using a dictionary comprehension.
print('\n')
print({x: x ** 3 for x in range(0, 5)})

# Reverse the list below
print('\n')
list1 = [1, 2, 3, 4]
list1.reverse()
print(list1)

# Sort the list below
print('\n')
list2 = [3, 4, 2, 5, 1]
list2.sort()
print(list2)
