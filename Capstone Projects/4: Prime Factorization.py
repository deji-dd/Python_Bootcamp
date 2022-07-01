# Have the user enter a number and find all Prime Factors (if there are any) and display them.
def prime(n):
    prime_n = []
    num = n + 1
    for x in range(2, num):
        if n % x == 0:
            for y in range(2, x):
                if x % y == 0:
                    break
            else:
                prime_n.append(x)
    if n <= 1:
        return 'Sorry that number is too small.'
    return prime_n


print(prime(100))
