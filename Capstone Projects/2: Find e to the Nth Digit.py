# Enter a number and have the program generate e up to that many decimal places. Keep a limit to how far the program will go.
from math import e

def n_e(n):
    if n <= 15:
        return round(e, n)
    else:
        return "Sorry that number is too big."


print(n_e(16))
