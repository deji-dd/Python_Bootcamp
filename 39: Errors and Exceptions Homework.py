# Handle the exception thrown by the code below by using try and except blocks.
try:
    for i in ['a', 'b', 'c']:
        print(i ** 2)
except TypeError:
    print("Sorry, you can only perform this operation on integers.")


# Handle the exception thrown by the code below by using try and except blocks.
# Then use a finally block to print 'All Done.'
try:
    x = 5
    y = 0
    z = x / y
except ZeroDivisionError:
    print("Sorry, you can not divide by zero.")
finally:
    print("All Done.")


# Write a function that asks for an integer and prints the square of it. Use a while loop with a
# try, except, else block to account for incorrect inputs.
def ask():
    while True:
        try:
            num = int(input("Please put in an integer: "))
        except ValueError:
            print("An error occurred! Please try again!\n")
            continue
        else:
            print(f"Thank you, your number squared is: {num ** 2}")
            break


ask()
