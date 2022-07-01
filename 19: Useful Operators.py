from random import shuffle
from random import randint
for num in range(10):
    print(num)
print('\n')
index_count = 0
word = 'abcde'
for ltr in word:
    print('At index {} the letter is {}'.format(index_count, ltr))
    index_count += 1
# you can replicate this with the 'enumerate' function
print('\n')
for item in enumerate(word):
    print(item)
print('\n')
mylist1 = [1, 2, 3]
mylist2 = ['a', 'b', 'c']
mylist3 = [100, 200, 300]
for item in zip(mylist1, mylist2, mylist3):  # the 'zip' function joins two or more lists together
    print(item)
print('\n')
print('x' in [1, 2, 3])  # checks if an element is in an iterable object
print('x' in ['x', 'y', 'z'])
print('\n')
mylist = [10, 20, 30, 40, 100]
print(min(mylist))  # returns the minimum value of a list
print(max(mylist))  # returns the maximum value of a list
print('\n')
shuffle(mylist)  # shuffles any iterable objects
print(mylist)
print('\n')
print(randint(0, 100))  # returns a random integer
print('\n')
result = input('Enter a number here: ')  # takes in user input
print(result)
