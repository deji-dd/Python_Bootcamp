# Enter a number and have the program generate π (pi) up to that many decimal places. Keep a limit to how far the program will go.
from math import pi

def n_pi(n):
    if n <= 15:
        return round(pi, n)
    else:
        return "Sorry that number is too big."


print(n_pi(16))
