"""practice with functions"""

from random import randint

print(randint(1, 10))


# Definition of function
def sum(num1: int, num2: int) -> int:
    """Return the sum of num1 and num 2"""
    return num1 + num2


# Calling of Function
print(sum(num1=4, num2=3))  # <- arguments
