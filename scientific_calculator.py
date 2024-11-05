import math

def sin(x):
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be a number")
    return math.sin(x)
def cos(x):
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be a number")
    return math.cos(x)

def tan(x):
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be a number")
    return math.tan(x)

def sqrt(x):
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be a number")
    if x < 0:
        raise ValueError("Cannot calculate square root of a negative number")
    return math.sqrt(x)

def log(x):
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be a number")
    if x <= 0:
        raise ValueError("Cannot calculate logarithm of zero or negative number")
    return math.log(x)

def exp(x):
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be a number")
    return math.exp(x)
