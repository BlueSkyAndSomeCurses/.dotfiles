"""
Module with recursive and iterative function for fibonacci sequnce and factorial
"""
import time


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

    for num in range(2, n + 1):
        prod *= num

    return prod


def fibonacci_recursive(n: int) -> int:
    """
    Recursively calculates fibonacci

    >>> fibonacci_recursive(7)
    21
    """

    if n in (0, 1):
        return 1

    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_iterative(n: int):
    """
    Iteratively calculates fibonacci

    >>> fibonacci_iterative(7)
    21

    """

    first_n = 1
    second_n = 1
    for _ in range(n - 1):
        tmp = second_n
        second_n = first_n + second_n
        first_n = tmp
    return second_n


def time_test(function: callable, verbose=False):
    """
    Function to evalute time of function work

    It doesn't have doctests, because time may vary depending on your hardware and circumstances.
    """

    if verbose:
        if function is factorial_recursive:

            def test(n: int, depth=1):
                if not n:
                    print("This function's depth:", depth)
                    return 1
                return n * test(n - 1, depth + 1)

        elif function is factorial_iterative:

            def test(n: int):
                prod = 1

                for num in range(2, n + 1):
                    print(prod)
                    prod *= num

                return prod

        elif function is fibonacci_recursive:
            brances_depth = []

            def test(n: int, depth=1):
                if n in (0, 1):
                    brances_depth.append(depth)
                    return 1

                return test(n - 1, depth + 1) + test(n - 2, depth + 1)


        print(test(17))
        print(len(brances_depth))

    start_p = time.time()
    function(31)
    return f"Time is: {time.time() - start_p}"


if __name__ == "__main__":
    import doctest

    print(doctest.testmod())

    # print(time_test(factorial_recursive, True))
    # print(time_test(factorial_iterative, True))
    print(time_test(fibonacci_recursive, True))
