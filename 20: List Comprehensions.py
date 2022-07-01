mystring = 'hello'
mylist = []
for letter in mystring:
    mylist.append(letter)
print(mylist)
# using list comprehension, this can be written on one line as:
mystring1 = 'goodbye'
mylist = [letter for letter in mystring1]  # this uses the syntax: element 'for' element 'in' iterable_object
print(mylist)
mylist = [x for x in 'word']
print(mylist)
mylist = [x for x in range(0, 11)]
print(mylist)
mylist = [num ** 2 for num in range(0, 11)]  # you can begin to run operations on the first element
print(mylist)
mylist = [x for x in range(0, 11) if x % 2 == 0]  # you can include an if statement at the end
print(mylist)
celsius = [0, 10, 20, 34.5]
fahrenheit = [((9 / 5) * temp + 32) for temp in celsius]  # you can do more complex operations
print(fahrenheit)
results = [x if x % 2 == 0 else 'ODD' for x in range(0, 11)]  # you can include else statements with if statements
print(results)
mylist = []
for x in [2, 4, 6]:  # this is a nested loop
    for y in [100, 200, 300]:
        mylist.append(x * y)
print(mylist)
mylist = [x * y for x in [2, 4, 6] for y in [1, 10, 1000]]  # nested loops using list comprehension
print(mylist)
