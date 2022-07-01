my_dict = {'key1': 'value1', 'key2': 'value2'}  # syntax for a dictionary
print(my_dict)
print(my_dict['key1'])
prices_lookup = {'apple': 2.99, 'oranges': 1.99, 'milk': 5.89}
print(prices_lookup['apple'])
d = {'k1': 123, 'k2': [0, 1, 2], 'k3': {'insideKey': 100}}  # dictionaries are very flexible; they can hold multiple data types
print(d['k2'])
print(d['k3']['insideKey'])
# an example to grab an element in a dictionary and use the .upper() function
d = {'key1': ['a', 'b', 'c']}
print(d)
mylist = d['key1']
print(mylist)
letter = mylist[2]
print(letter)
print(letter.upper())
# an example to the same thing in one step
print(d['key1'][2].upper())
d = {'k1': 100, 'k2': 200}
d['k3'] = 300  # creating a new entry in the dictionary
print(d)
d['k1'] = 'NEW VALUE'  # replacing an existing value in the dictionary with a new one
print(d)
d = {'k1': 100, 'k2': 200, 'k3': 300}
print(d.keys())  # returns all the keys in a dictionary
print(d.values())  # returns all the values in a dictionary
print(d.items())  # returns all the pairings in a dictionary
