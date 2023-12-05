"""
Module with recursive and iterative function for fibonacci sequnce and factorial
"""

def factorial_recursive(n: int):
    """
    Recursively calculates factorial

    >>> factorial_recursive(23)
    25852016738884976640000
    """

    if not n:
        return 1
    return n * factorial_recursive(n - 1)

def factorial_iterative(n: int):
    """
    Iteratively calculates factorial

    >>> factorial_iterative(23)
    25852016738884976640000
    """
    
    prod = 1

    for num in range(2, n+1):
        prod *= num 
        
    return prod

def fibonacci_recursive(n: int) -> int:
    """ 
    Recursively calculates fibonacci

    fibonacci_recursive(7)
    21
    """

    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def fibonacci_iterative(n: int):
    """ 
    Iteratively calculates fibonacci
    
    >>> fibonacci_iterative(7)
    21

    """

    first_n = 1
    second_n = 1
    for _ in range(n):
        tmp = second_n
        second_n = first_n + second_n
        first_n = tmp
        
    return second_n


if __name__ == "__main__":
    import doctest

    print(doctest.testmod())
