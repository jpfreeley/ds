def fib(n):
    '''
    >>> fib(1)
    1
    >>> fib(2)
    1
    >>> fib(3)
    2
    >>> fib(4)
    3
    >>> fib(5)
    5
    >>> fib(6)
    8
    >>> fib(12)
    144
    '''
    
    
    if type(n) != int:
        raise TypeError("ints only, chumps!")
    if n < 0:
        raise ValueError("stop ruining recursion!")
    elif n == 0:
        return(0)
    elif n in set([1,2]):
        return 1
    else: 
        return fib(n-1) + fib(n-2)

if __name__ == "__main__":
    import doctest
    doctest.testmod()