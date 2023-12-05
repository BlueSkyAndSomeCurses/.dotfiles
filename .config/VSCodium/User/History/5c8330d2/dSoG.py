"""
https://github.com/BlueSkyAndSomeCurses/valihurskyi-anton-lab8-task1 
"""
from calendar import TextCalendar


def calendar(year: int, month: int):
    """
    Function which generate a calendar for one month with usage of calendar module

    >>> calendar(2014, 3)
    'March 2014\nMo Tu We Th Fr Sa Su\n                1  2\n 3  4  5  6  7  8  9\n10 11 12 13 14 15
16\n17 18 19 20 21 22 23\n24 25 26 27 28 29 30\n31'
    """

    return TextCalendar().formatmonth(year, month).strip()


def transform_calendar(calendar: str):
    pass


if __name__ == "__main__":
    import doctest

    print(doctest.testmod())
