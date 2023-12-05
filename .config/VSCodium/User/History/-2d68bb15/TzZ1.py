"""
Module with a function to check game table of puzzle for validity
https://github.com/BlueSkyAndSomeCurses/valihurskyi-anton-lab8-task2
"""


def validate_board(board: list) -> bool:
    """
    Function takes a list of string as argument and returns whether it is valid or invalid
    >>> validate_board(\
    ["**** ****",\
     "***1 ****",\
     "**  3****",\
     "* 4 1****",\
     "     9 5 ",\
     " 6  83  *",\
     "3   1  **",\
     "  8  2***",\
     "  2  ****"])
    False
    >>> validate_board(\
    ["**** ****",\
     "***1 ****",\
     "**  3****",\
     "* 4 1****",\
     "     9 5 ",\
     " 6  83  *",\
     "3   7  **",\
     "  8  2***",\
     "  2  ****"])
    True 
    """

    for row in board:
        characters = set(row)
        for char in characters:
            if char not in "123456789* " or row.count(char) > 1 or len(row) != 9:
                return False

    for column in range(9):
        elemnts = set()
        for el in board:
            el = el[column]
            if el.isdigit() and el in elemnts:
                return False
            elemnts.add(el)

    for st_point in range(5):
        elem_set = set()
        for row in range(4 - st_point, 10 - st_point):
            elem = board[row][st_point]
            if elem.isdigit() and elem in elem_set:
                return False
        for col in range(st_point, st_point + 5):
            elem = board[9 - st_point][col]
            if elem.isdigit and elem in elem_set:
                return False


if __name__ == "__main__":
    # import doctest

    # print(doctest.testmod())

    print(validate_board(\
    ["**** ****",\
     "***1 ****",\
     "**  3****",\
     "* 4 1****",\
     "     9 5 ",\
     " 6  83  *",\
     "3   7  **",\
     "  8  2***",\
     "  2  ****"])
)