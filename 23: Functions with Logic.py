def check_even(num):  # checks if a number is even
    return num % 2 == 0
def even_check(num_list):  # checks if a number in a list is even
    for number in num_list:
        if number % 2 == 0:
            return True
        else:
            pass
    return False
def even_num(num_list):  # returns the even numbers in a list
    even_numbers = []  # a placeholder
    for number in num_list:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            pass
    if not even_numbers:
        return 'There are no even numbers'
    else:
        return even_numbers




print(check_even(10345678))
print(even_check([5, 3, 2, 9]))
print(even_num([1, 3, 6, 4, 2]))
print(even_num([1, 3, 5, 7, 9]))
