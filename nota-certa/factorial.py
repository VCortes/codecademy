import math


def factorial(n):
    """
    Calculate the factorial of a given number.
    Parameters:
    n (int): The number to calculate the factorial for. Must be a non-negative integer.
    Returns:
    int: The factorial of the number if n is between 0 and 100.
    str: An error message if n is negative or greater than 100.
    """
    if n < 0:
        return "Negative numbers do not have a factorial"
    if n > 100:
        return "Number too large to calculate factorial"
    if n == 0:
        return 1
    return math.factorial(n)


if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print(factorial(n))
