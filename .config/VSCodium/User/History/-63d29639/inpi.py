# Complete all of the following functions. Currently they all just
# 'pass' rather than explicitly return value, which means that they
# implicitly return None.
"""
Module with functions to work with function
"""
from typing import Callable


def find_max_1(f: Callable, points: list) -> int:
    """
    (function, list(int)) -> int

    Find and return maximal value of function f in points.

    >>> find_max_1(lambda x: x ** 2 + x, [1, 2, 3, -1])
    12
    """

    return max(f(i) for i in points)


def find_max_2(f: Callable, points: list) -> list:
    """
    (function, list(number)) -> (number)

    Find and return list of points where function f has the maximal value.

    >>> find_max_2(lambda x: x ** 2 + x, [1, 2, 3, -1])
    [3]
    """

    max_value = find_max_1(f, points)

    return [x for x in points if f(x) == max_value]


def compute_limit(seq: Callable) -> float:
    """
    (function) -> (float)

    Compute and return limit of a convergent sequence.

    >>> compute_limit(lambda n: (n ** 2 + n) / n ** 2)
    1.0
    """
    lst = []  # the list sequence elements

    i = 0

    while True:
        n = 10**i  # the number of element
        lst.append(seq(n))  # adding new element

        # check the difference between elements
        if i != 0 and abs(lst[i] - lst[i - 1]) < 0.001:
            return float(f"{lst[i]:.2f}")
        i += 1


def compute_derivative(f: Callable, x_0: float) -> float:
    """
    (function, number) -> (number)

    Compute and return derivative of function f in the point x_0.

    >>> compute_derivative(lambda x: x ** 2 + x, 2)
    5.0
    """

    aprox = []

    i = 0

    while True:
        dx = 10**-i

        x = x_0 + dx
        df = f(x)  # dF = f(x_0 + dx)

        x = x_0
        df -= f(x)  # dF = f(x_0 + dx) - f(x_0)

        der = df / dx  # der = (f(x_0 + dx) - f(x_0))/ dx

        aprox.append(der)

        if i != 0 and abs(aprox[i] - aprox[i - 1]) < 0.001:
            return float(f"{aprox[i]:.2f}")
        i += 1


def get_tangent(f: Callable, x_0: float) -> str:
    """
    (function, number) -> (str)

    Compute and return tangent line to function f in the point x_0.

    >>> get_tangent(lambda x: x ** 2 + x, 2)
    '5.0 * x - 4.0'
    >>> get_tangent(lambda x: - x ** 2 + x, 2)
    '-3.0 * x + 4.0'
    """

    f_x_d = float(f"{compute_derivative(f, x_0):.2f}")
    f_x = float(f"{f(x_0):.2f}") + float(f"{(-x_0) * f_x_d:.2f}")

    if f_x < 0:
        return f"{f_x_d} * x - {abs(f_x)}"

    return f"{f_x_d} * x + {f_x}"


def get_root(f: Callable, a: float, b: float, counter=0) -> float:
    """
    (function, number, number) -> (number)

    Compute and return root of the function f in the interval (a, b).

    >>> get_root(lambda x: x, -1, 1)
    0.0
    >>> get_root(lambda x: 2 * x**3 - 10, 1, 2)
    0.0
    """

    center = (a + b) / 2

    counter += 1

    if float(f"{f(center):.8f}") == 0 or counter == 30:
        return float(f"{center:.2f}")

    if f(a) < 0 < f(b) or f(b) < 0 < f(a):
        return get_root(f, a, center, counter)

    return get_root(f, center, b, counter)


if __name__ == "__main__":
    # import doctest

    # print(doctest.testmod())

    print(get_root(lambda x: 2 * x**3 - 10, 1, 2))