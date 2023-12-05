"""
module with algorithms
"""


def linear_search(list_of_values: list, value: any) -> int:
    """
    Implementation of linear search
    >>> linear_search([5,3,9,2], 9)
    2
    >>> linear_search([5,3,9,2], 90)
    -1
    """

    for i, el in enumerate(list_of_values):
        if el == value:
            return i
    return -1


def merge_sort(lst: list) -> list:
    """
    Implementation of merge sort
    >>> merge_sort([5,1,7,2,5,0,3,6,4])
    [0, 1, 2, 3, 4, 5, 5, 6, 7]
    >>> merge_sort([])
    []
    """
    if len(lst) <= 1:
        return lst

    sorted_lst = []
    right = merge_sort(lst[len(lst) // 2 :])
    left = merge_sort(lst[: len(lst) // 2])
    while len(right) or len(left):
        if len(right) == 0:
            sorted_lst.append(left.pop(0))
        elif len(left) == 0:
            sorted_lst.append(right.pop(0))
        elif left[0] > right[0]:
            sorted_lst.append(right.pop(0))
        else:
            sorted_lst.append(left.pop(0))

    return sorted_lst


def binary_search(list_of_values: list, value: any) -> int:
    """
    Implementation of binary search
    >>> binary_search([2,3,5,9,1], 9)
    3
    >>> binary_search([2,3,5,9,1], 99)
    -1
    >>> binary_search([10, 40, 68, 100, 194, 274, 550, 4000], 10)
    0
    """

    left = 0
    right = len(list_of_values) - 1

    while right - 1 != left:
        center = (left + right) // 2
        if list_of_values[center] == value:
            return center
        if list_of_values[center] < value:
            left = center
        elif list_of_values[center] > value:
            right = center
            

    return -1


def selection_sort(lst: list) -> list:
    """
    Implementation of selection sort sort
    >>> selection_sort([5,1,7,2,5,0,3,6,4])
    [0, 1, 2, 3, 4, 5, 5, 6, 7]
    """

    for i, _ in enumerate(lst[:-1]):
        min_ = i
        for j, el_j in enumerate(lst[i + 1 :]):
            if el_j < lst[min_]:
                min_ = j + i + 1
        lst[i], lst[min_] = lst[min_], lst[i]

    return lst


def quick_sort(lst: list) -> list:
    """
    Implementation of quick sort sort
    >>> quick_sort([5,1,7,2,5,0,3,6,4])
    [0, 1, 2, 3, 4, 5, 5, 6, 7]
    """
    if len(lst) <= 1:
        return lst

    pivot = lst[-1]

    return (
        quick_sort([i for i in lst[::-1] if i < pivot])
        + [i for i in lst if i == pivot]
        + quick_sort([i for i in lst[::-1] if i > pivot])
    )


if __name__ == "__main__":
    import doctest

    print(doctest.testmod())
