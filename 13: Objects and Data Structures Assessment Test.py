# Numbers: normal numbers without decimal points (e.g. 100)
# Strings: text or numbers wrapped in single or double quotes (e.g. 'string')
# Lists: multiple object types separated by commas and wrapped in braces. they are mutable (e.g. [1, 2, five])
# Tuples: multiple object types separated by commas and wrapped in parentheses. they are immutable (e.g. (1, 2, five))
# Dictionaries: these are used to store object types using a 'key: value' syntax and are wrapped in curly braces (e.g. {apple: 5.00})
print(((((100.25 - 50) + 50) * 2) / 2) ** 1)
print(4 * (6 + 5))  # 44
print(4 * 6 + 5)  # 29
print(4 + 6 * 5)  # 34
print(type(3 + 1.5 + 4))  # float
print(9 ** 0.5)  # square root
print(3 ** 2)  # squared
s = 'hello'
print(s[1])  # returns 'e'
print(s[::-1])  # reverses the string
print(s[-1])  # returns 'o'
print(s[4])  # returns 'o'
lst = [0, 0, 0]
print(lst)  # returns the list [0, 0, 0]
lst = []
lst.append(0)
lst.append(0)
lst.append(0)
print(lst)  # returns the list [0, 0, 0]
list3 = [1, 2, [3, 4, 'hello']]
list3[2][2] = 'goodbye'
print(list3)  # returns the list [1, 2, [3, 4, 'goodbye']]
list4 = [5, 3, 4, 6, 1]
list4.sort()
print(list4)  # returns a sorted list
d = {'simple_key': 'hello'}
print(d['simple_key'])  # grabs 'hello'
d = {'k1': {'k2': 'hello'}}
print(d['k1']['k2'])  # grabs 'hello'
d = {'k1': [{'nest_key': ['this is deep', ['hello']]}]}
print(d['k1'][0]['nest_key'][1][0])  # grabs hello
d = {'k1': [1, 2, {'k2': ['this is tricky', {'tough': [1, 2, ['hello']]}]}]}
print(d['k1'][2]['k2'][1]['tough'][2][0])  # grabs hello
# you can sort a dictionary using the 'Sorted()' function
# tuples are immutable and use parentheses while lists are mutable and use braces
# you create a tuple by assigning it to a keyword
# sets can only contain one of a particular number
list5 = [1, 2, 2, 33, 4, 4, 11, 22, 3, 3, 2]
print(set(list5))
print(2 > 3)  # False
print(3 <= 2)  # False
print(3 == 2.0)  # False
print(3.0 == 3)  # True
print(4**0.5 != 2)  # False
l_one = [1, 2, [3, 4]]
l_two = [1, 2, {'k1': 4}]
print(l_one[2][0] >= l_two[2]['k1'])  # False
