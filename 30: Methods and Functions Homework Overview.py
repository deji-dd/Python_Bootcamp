# Write a function that computes the volume of a sphere given its radius.
from math import pi


def vol(rad):
    return (rad ** 3) * pi * (4 / 3)


print(vol(2))
print('\n')


# Write a function that checks whether a number is in a given range (inclusive of high and low)
def ran_check(num, low, high):
    if num in range(low, high + 1):
        return f'{num} is in the range between {low} and {high}'


print(ran_check(5, 2, 7))
print('\n')


# If you only wanted to return a boolean:
def ran_bool(num, low, high):
    return num in range(low, high + 1)


print(ran_bool(3, 1, 10))
print('\n')


# Write a Python Bootcamp function that accepts a string and calculates the number of upper case letters and lower case letters.
def up_low(st):
    upper = []
    lower = []
    for x in st:
        if x.isupper():
            upper.append(x)
        elif x.islower():
            lower.append(x)
        else:
            pass
    return f'No. of Upper case characters :  {len(upper)} \nNo. of Lower case Characters :  {len(lower)}'


s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
print(up_low(s))
print('\n')


# Write a Python Bootcamp function that takes a list and returns a new list with unique elements of the first list.
def unique_list(lst):
    return list(set(lst))


print(unique_list([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5]))
print('\n')
# Write a Python Bootcamp function to multiply all the numbers in a list.
def multiply(numbers):
    from math import prod
    return prod(numbers)


print(multiply([1, 2, 3, -4]))
print('\n')
# Write a Python Bootcamp function that checks whether a word or phrase is palindrome or not.
def palindrome(st):
    st = str(st).replace(' ', '')
    return st == st[::-1]


print(palindrome('helleh'))
print(palindrome("nurses run"))
print('\n')
# Write a Python Bootcamp function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)
import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    str1 = str(str1).replace(' ', '').lower()
    str1 = list(set(str1))
    str1.sort()
    alphabet = list(alphabet)
    return str1 == alphabet


print(ispangram("The quick brown fox jumps over the lazy dog"))
