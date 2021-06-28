""" Helpful math functions """

f_cache = {}
def factorial(n):
    """ Recursive algorithm to calculate factorial n! """
    if n in f_cache:
        return f_cache[n]
    if n == 0 or n == 1:
        return 1
    value = n*factorial(n-1)
    '''
    if n>2:
        del f_cache[n-1]
    '''
    return value

d_cache = {}
def derangement(n):
    """ Memoization algorithm to calculate derangement !n """
    if n in d_cache:
        return d_cache[n]
    if n == 1:
        return 0
    if n == 2:
        return 1
    value = (n-1)*(derangement(n-2) + derangement(n-1))
    d_cache[n] = value
    '''
    if n>4:
        del d_cache[n-2]
    '''
    return value

w_cache = {}
def weird_derangement(n):
    """ Memoization algorithm to calculate derangement !n """
    if n in w_cache:
        return w_cache[n]
    if n == 1:
        return 1
    if n == 2:
        return 2
    value = (n-1)*(weird_derangement(n-2) + weird_derangement(n-1))
    w_cache[n] = value
    return value