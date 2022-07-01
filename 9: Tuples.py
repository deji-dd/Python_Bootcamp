t = (1, 2, 3)  # tuples are like lists except they are immutable and use parenthesis
mylist = [1, 2, 3]
print(type(t))
print(type(mylist))
print(len(t))
t = ('one', 2)  # they can contain different data types
print(t[0])
t = ('a', 'a', 'b')
print(t.count('a'))  # returns how many times an object appears in a tuple
print(t.index('a'))  # returns the index position of an object the first time it appears
