import math

def addmultiplenumbers(numbers):
    return sum(numbers)

def multiplymultiplenumbers(numbers):
    return math.prod(numbers)

def isiteven(num):
    return isinstance(num, int) and num % 2 == 0

def isitaninteger(num):
    return isinstance(num, int) or (isinstance(num, float) and num.is_integer())

