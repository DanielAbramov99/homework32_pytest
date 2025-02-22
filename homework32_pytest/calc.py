import math


# a
def power(number, exponent):
    return number ** exponent


# b
def sqrt(number):
    return math.sqrt(number)


# c
def factorial(number):
    if number < 0:
        raise ValueError("Cannot compute the factorial of a negative number.")
    elif number == 0 or number == 1:
        return 1
    else:
        result = 1
        for i in range(2, number + 1):
            result *= i
        return result

# d
