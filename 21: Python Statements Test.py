# Use for, .split(), and if to create a Statement that will print out words that start with 's':
st = 'Print only the words that start with s in this sentence'
st = st.split()
for x in st:
    if x[0] == 's':
        print(x)
print('\n')
# Use range() to print all the even numbers from 0 to 10.
for x in range(0, 11):
    if x % 2 == 0:
        print(x)
print('\n')
# Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
num = [x for x in range(0, 51) if x % 3 == 0]
print(num)
print('\n')
# Go through the string below and if the length of a word is even print "even!"
st = 'Print every word in this sentence that has an even number of letters'
st = st.split()
for x in st:
    if len(x) % 2 == 0:
        print(f'{x} is even!')
print('\n')
# Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number,
# and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
for x in range(1, 101):
    if x % 3 == 0 and x % 5 == 0:
        print('FizzBuzz')
    elif x % 3 == 0:
        print('Fizz')
    elif x % 5 == 0:
        print('Buzz')
    else:
        print(x)
print('\n')
# Use List Comprehension to create a list of the first letters of every word in the string below:
st = 'Create a list of the first letters of every word in this string'
st = st.split()
st = [x[0] for x in st]
print(st)
