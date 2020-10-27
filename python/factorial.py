from functools import reduce

def factorial(n):
    return reduce(lambda a, b: a*b, [x for x in range(n,0,-1)])