# Have the program find prime numbers until the user chooses to stop asking for the next one.
def next_prime(n):
    prime_n = []
    for x in range(2, n + 1):
        if x > 1:
            for y in range(2, x):
                if x % y == 0:
                    break
            else:
                prime_n.append(x)
    result = 0
    question = 'rip'
    while True:
        if question == 'Y':
            try:
                print(f"The next prime number is: {prime_n[result]}\n")
                result += 1
            except IndexError:
                return 'That is all the prime numbers in this range.'
        if question == 'N':
            return "The operation has ended."
        else:
            question = input("Do you want the next prime number in this range?(Y or N): ")
            if question not in ['Y', 'N']:
                print("Please pick (Y or N)\n")



print(next_prime(100))
