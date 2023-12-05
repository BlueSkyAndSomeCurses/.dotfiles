"""
Module with recursive functoins
"""


def create_table(n: int, m: int) -> list:
    """
    Create a number table, n x m size. Numbers under in row or column with index 0 equals to 1.
    All other elements calculated according to A[i][j] = A[i-1][j] + A[i][j-1].

    >>> create_table(4,6)
    [[1, 1, 1, 1, 1, 1], [1, 2, 3, 4, 5, 6], [1, 3, 6, 10, 15, 21], [1, 4, 10, 20, 35, 56]]
    """

    lst = []

    def creater(row=0, column=0):
        if row == n:
            return
        if column == m:
            creater(row + 1, 0)
            return
        if not column:
            lst.append([1])
            creater(row, column + 1)
            return
        if not row:
            lst[-1].append(1)
            creater(row, column + 1)
            return

        lst[-1].append(lst[row - 1][column] + lst[row][column - 1])
        creater(row, column + 1)

    creater()

    return lst

def flatten(lst: list) -> list:
    """
    Function which takes a list of lists of lists of lists of ... (of lists) * n, 
    where n -> rotated(8).
    
    >>> flatten([1,[2]]) -> returns [1,2]
    >>> flatten([1,2,[3,[4,5],6],7]) -> returns [1,2,3,4,5,6,7]
    >>> flatten(['wow', [2,[[]]], [True]]) -> returns ['wow', 2, True]
    >>> flatten([]) -> returns []
    >>> flatten([[]]) -> returns []
    >>> flatten(3) -> returns 3 (not a list)
    """

if __name__ == "__main__":
    import doctest

    print(doctest.testmod())
