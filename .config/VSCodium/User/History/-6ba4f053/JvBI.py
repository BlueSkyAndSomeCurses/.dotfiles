"""
Aliens 
"""


def quick_sort(lst: list, key: int) -> int:
    """
    Function for sorting
    """

    if len(lst) <= 1:
        return lst

    pivot = [lst.pop()]
    smaller = []
    bigger = []

    if key:
        for person in lst:
            if person[key] > pivot[0][key]:
                smaller.append(person)
            elif person[key] < pivot[0][key]:
                bigger.append(person)
            else:
                pivot.append(person)
    else:
        for person in lst:
            if person[key] < pivot[0][key]:
                smaller.append(person)
            elif person[key] > pivot[0][key]:
                bigger.append(person)
            else:
                pivot.append(person)

    return quick_sort(smaller, 1) + quick_sort(pivot, 0) + quick_sort(bigger, 1)


def read_file(file_path: str) -> dict:
    """
    Function reads a file, and returns dictionary
    key: name surname
    value: int(IQ)

    >>> import tempfile
    >>> with tempfile.NamedTemporaryFile(mode = "w", delete = False)as tmpfile:
    ...    _ = tmpfile.write('google.com\\n')
    ...    _ = tmpfile.write('Elon Musk,165\\n')
    ...    _ = tmpfile.write('Mark Zuckerberg,152\\n')
    ...    _ = tmpfile.write('Will Smith,157\\n')
    ...    _ = tmpfile.write('Marilyn vos Savant,186\\n')
    >>> read_file(tmpfile.name)
    {'Elon Musk': 165, 'Mark Zuckerberg': 152, 'Will Smith': 157, 'Marilyn vos Savant': 186}
    """

    with open(file_path, "r", encoding="utf-8") as file:
        smart_people = {}
        file.readline()
        for line in file:
            line = line.strip().split(",")
            smart_people[line[0]] = int(line[1])

    return smart_people


def rescue_people(smarties: dict, limit_iq: int) -> list:
    """
    return amount of flies, and what people will be evacuated each time.


    >>> rescue_people({"Steve Jobs": 160, "Albert Einstein": 160,\
    "Sir Isaac Newton": 195, "Nikola Tesla": 189},500)
    (2, [['Sir Isaac Newton', 'Nikola Tesla'], ['Albert Einstein', 'Steve Jobs']])
    >>> rescue_people({"Alice": 100, "Bob": 80, "Charlie": 90}, 180)
    (2, [['Alice', 'Bob'], ['Charlie']])
    """
    smarties = quick_sort(list(smarties.items()), 1)
    print(smarties)

    flies = [0, []]
    if limit_iq < smarties[0][1]:
        return flies

    smarties_copy = smarties[:]

    while len(smarties) > 0:
        tmp = limit_iq
        flies[0] += 1
        flies[-1].append([])
        for i, pers in enumerate(smarties_copy):
            if tmp >= pers[1]:
                flies[-1][-1].append(pers[0])
                tmp -= pers[1]
                smarties.pop(i)

        smarties_copy = smarties[:]

    # while len(smarties) > 0:
    #     tmp = limit_iq
    #     flies[-1].append([])
    #     flies[0] += 1
    #     count = 0
    #     while count != len(smarties):
    #         if tmp >= smarties[count][1]:
    #             flies[-1][-1].append(smarties[count][0])
    #             tmp -= smarties[count][1]
    #             smarties.pop(count)
    #             count -= 1
    #
    #         count += 1

    return tuple(flies)


if __name__ == "__main__":
    import doctest

    print(doctest.testmod())
    print(rescue_people(read_file("smart_people.txt"), 500))
