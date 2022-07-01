# Enter a number and have the program generate the Fibonacci sequence to that number or to the Nth number.

def fibonacci(n):
    sequence = []

    def num():
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a + b

    for i in num():
        sequence.append(i)
        if len(sequence) > n - 1:
            break
    return sequence


print(fibonacci(10))
