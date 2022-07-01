# Write a function that returns the lesser of two given numbers if both numbers are even,
# but returns the greater if one or both numbers are odd
def lesser_of_two_evens(a, b):
    if a % 2 == 0 and b % 2 == 0:
        if a < b:
            return a
        else:
            return b
    else:
        if a > b:
            return a
        else:
            return b


print(lesser_of_two_evens(2, 4))
print(lesser_of_two_evens(2, 5))
print('\n')


# Write a function that takes a two-word string and returns True if both words begin with the same letter
def animal_crackers(text):
    result = str(text).split()
    return result[0][0] == result[1][0]


print(animal_crackers('Levelheaded Llama'))
print(animal_crackers('Crazy Kangaroo'))
print('\n')


# Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
def makes_twenty(n1, n2):
    return n1 + n2 == 20 or n1 == 20 or n2 == 20


print(makes_twenty(20, 10))
print(makes_twenty(12, 8))
print(makes_twenty(2, 3))
print('\n')


# Write a function that capitalizes the first and fourth letters of a name
def old_macdonald(name):
    return str(name)[0].capitalize() + str(name)[1:3] + str(name)[3].capitalize() + str(name)[4:]


print(old_macdonald('macdonald'))
print('\n')


# Given a sentence, return a sentence with the words reversed
def master_yoda(text):
    text = str(text)
    split = text.split()
    reverse = split[::-1]
    result = " ".join(reverse)
    return result


print(master_yoda('I am home'))
print(master_yoda('We are ready'))
print('\n')


# Given an integer n, return True if n is within 10 of either 100 or 200
def almost_there(n):
    return abs(100 - n) <= 10 or abs(200 - n) <= 10


print(almost_there(90))
print(almost_there(104))
print(almost_there(150))
print(almost_there(209))
print('\n')


# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
def has_33(nums):
    for i in range(0, len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False


print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 9, 3]))
print('\n')


# Given a string, return a string where for every character in the original there are three characters
def paper_doll(text):
    text = list(text)
    result = []
    for x in text:
        result.append(x * 3)
    return ''.join([str(item) for item in result])


print(paper_doll('Hello'))
print(paper_doll('Mississippi'))
print('\n')


# Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum
# exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment)
# exceeds 21, return 'BUST'
def blackjack(a, b, c):
    add = a + b + c
    if add <= 21:
        return add
    elif add > 21 and (a == 11 or b == 11 or c == 11):
        return add - 10
    else:
        return 'BUST'


print(blackjack(5, 6, 7))
print(blackjack(9, 9, 9))
print(blackjack(9, 9, 11))
print('\n')


# Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the
# next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
def summer_69(arr):
    stop = False
    result = 0
    for num in arr:
        if num == 6:
            stop = True
        elif num == 9:
            stop = False
        elif stop is False:
            result += num
        elif arr is []:
            return 0
    return result


print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 6, 7, 8, 9]))
print(summer_69([2, 1, 6, 9, 11]))
print('\n')


# Write a function that takes in a list of integers and returns True if it contains 007 in order
def spy_game(nums):
    for i in range(0, len(nums) - 1):
        if nums[i] == 0:
            nums1 = nums[i + 1:]
            if 0 in nums1:
                ind = nums1.index(0)
                nums2 = nums1[ind + 1:]
                if 7 in nums2:
                    return True
    return False


print(spy_game([1, 2, 4, 0, 0, 7, 5]))
print(spy_game([1, 0, 2, 4, 0, 5, 7]))
print(spy_game([1, 7, 2, 0, 4, 5, 0]))
print('\n')


# Write a function that returns the number of prime numbers that exist up to and including a given number
def count_primes(num):
    primes = [2, 3, 5, 7]
    for i in range(2, num + 1):
        if not i % 2 == 0 and not i % 3 == 0 and not i % 5 == 0 and not i % 7 == 0:
            primes.append(i)
    return len(primes)


print(count_primes(100))
print('\n')
# Write a function that takes in a single letter, and returns a 5x5 representation of that letter
def print_big(letter):
    if letter == 'A' or 'a':
        return "  *  \n * * \n*****\n*   *\n*   *"


print(print_big('a'))
