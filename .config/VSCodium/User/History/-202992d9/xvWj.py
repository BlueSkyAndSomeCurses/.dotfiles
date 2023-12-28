"""
Catalan
"""
import functools
import time


# обчислює кількість способів з`єднати верхній лівий і нижній правий кут матриці n x n (числа Каталана).
# Крок може бути лише вправо або вниз.
# кількість шляхів до будь-якої точки у матриці можна розрахувати
# якщо використати кількість шляхів до двох попередніх точок - верхньої і лівої
def ways_to_dot(n_elem):
    """
    Returns how many ways you can find in nxn matrix
    """
    matrix = [
        [0] * (n_elem + 1) for _ in range(n_elem + 1)
    ]  # створення матриці (n+1) x (n+1) (не булевої) , заповнення її нулями

    for i in range(
        n_elem + 1
    ):  # перший рядок і перший стовпчик - 1, бо інсує лише 1 спосіб дістатися до них. Вниз або вправо.
        matrix[i][0] = 1
    for j in range(n_elem + 1):
        matrix[0][j] = 1
    for i in range(
        1, n_elem + 1
    ):  # рахуємо для кожної точки, це буде сума двох точок, верхньої і лівої
        for j in range(1, n_elem + 1):
            matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]
    return (
        (matrix[n_elem][n_elem]) // (n_elem + 1)
    )  # повертаємо кількість у нижній правій точці і ділимо на n-1, щоб була відповідність до чисел Каталана


# приймає на вхід число діаголаней для n для 2n-кутника
def diagonal_counting(diagonal):
    """
    Return a number of diagonals in Polygon
    """
    if (
        diagonal == 0
    ):  # Якщо n_elem дорівнює 0, то функція повертає 1. Коли немає жодної вершини, отже, немає діагоналей
        return 1
    catalan = [0] * (
        diagonal + 1
    )  # створюємо список, в який будемо додавати числа каталана
    catalan[0] = 1  # перше число каталана
    # обчислюємо число каталана за допомогою двох попередніх членів.
    for i in range(
        1, diagonal + 1
    ):  # ітерується в рамках від 1 до половини введеного числа
        for j in range(i):  # попереднє за i число
            catalan[i] += catalan[j] * catalan[i - 1 - j]
    return catalan[diagonal]


@functools.lru_cache(maxsize=1000)
def catalan_recursive(n: int):
    match n:
        case 0:
            return 1
        case 1:
            return 1
        case 2:
            return 2
        case 3:
            return 5

    catalan = 0
    for k in range(n):
        catalan += catalan_recursive(k) * catalan_recursive(n - k - 1)

    return catalan


def recursive_definition(n):
    for i in range(n + 1):
        print(i, ":", catalan_recursive(i))


# def factorial_recursive(number):
#     '''
#     Recursive function, returns a factorial of number
#     '''
#     factorial = 1
#     if number != 1:
#         factorial *= (number * (factorial_recursive(number - 1)))
#     else:
#         return 1
#     return factorial


# def ways_to_dot(n_elem):
#     '''
#     Returns number of ways from (0,0) to (n,n)
#     '''
#     result = (factorial_recursive(2* n_elem) // \
# (factorial_recursive(n_elem) * factorial_recursive(2* n_elem - n_elem))) // (n_elem + 1)
#     return result


@functools.lru_cache(maxsize=1000)
def catalan_powers(x, numb):
    def factorial(m):
        """
        factorial
        """
        if m == 0:
            return 1
        return m * factorial(m - 1)

    def ceshka(n, k):
        """
        Counts number of nth number by ceshka
        """
        return factorial(n) // (factorial(k) * factorial(n - k))

    def counted_catalan_number(n):
        """
        Counts by fromula of counting C(n) = (1/(n+1)) * C(2 * n, n)
        """
        return ceshka(2 * n, n) // (n + 1)

    def catalan_power_series_method(x, numb_of_first_terms):
        """
        Finds sum of n terms.
        """
        series = [
            counted_catalan_number(n) * (x**n) for n in range(numb_of_first_terms)
        ]
        return series

    return catalan_power_series_method(x, numb)


def parentheses(n: int) -> list[str]:
    res = []

    def dfs(left, right, s):
        if len(s) == n * 2:
            res.append(s)
            return
        if left < n:
            dfs(left + 1, right, s + "(")
        if right < left:
            dfs(left, right + 1, s + ")")

    dfs(0, 0, "")
    return res


if __name__ == "__main__":
    """ diagonal_counting(4)
    ways_to_dot(10)
    print(diagonal_counting(20))
    print(ways_to_dot(10))

    start = time.time()
    recursive_definition(1000)
    print(time.time())

    for i in range(10):
        print(len(parentheses(i)))
 """
    print(catalan_powers(1, 1000))
