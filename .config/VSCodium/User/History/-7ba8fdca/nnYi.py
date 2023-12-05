"""
module with functions which generates pictures with symbols
"""


def read_file(path: str) -> dict[str : list[tuple[int, int]]]:
    """
    str -> dict[str: list[tuple[int, int]]]

    Function which takes a txt file, and extract symbol and its according\
    coordinates. Returns a dictinoary with strings as keys, and value is a list of tuples[int, int].

    >>> read_file("example.txt")
    {'♥': [(0, 0), (1, 1), (2, 2)], '%': [(0, 1), (0, 2), (1, 2)]}
    """

    coord_dict = {}
    with open(path, "r", encoding="utf-8") as file:
        ind = 1
        last_symb = ""
        for line in file:
            line = line.replace("\n", "")
            if ind:
                ind = 0
                last_symb = line
                coord_dict[line] = []
                continue
            ind = 1
            coord_dict[last_symb] = line.split(" ")
            for coord in enumerate(coord_dict[last_symb]):
                tmp = coord[1].split("_")
                coord_dict[last_symb][coord[0]] = tuple([int(tmp[0]), int(tmp[1])])

    return coord_dict


def save_pict_to_file(
    symbols: dict[str : list[tuple[int, int]]], textfile: str
) -> None:
    """
    (dict[str : list[tuple[int, int]]], str) -> None

    Function which takes input of dictionary with symbols and assosiated lists of coordinates.
    Writes this symbols to a file according to this coordinates.

    >>> import tempfile
    >>> with tempfile.NamedTemporaryFile(mode = "w") as tmpfile:
    ...    _ = tmpfile.write("")
    >>> save_pict_to_file({'♥': [(2, 2), (1, 1), (0, 0)],\
    '%': [(1, 2), (0, 2), (0, 1)]}, tmpfile.name)
    >>> with open(tmpfile.name, "r", encoding = "utf-8") as textf:
    ...    _ = print(textf.read())
    ♥%%
     ♥%
      ♥

    """

    max_x = 0
    max_y = 0
    picture = []

    for symb in symbols:
        symbols[symb].sort(key=lambda x: x[0])
        max_x = max(max_x, int(symbols[symb][-1][0]))
        symbols[symb].sort(key=lambda x: x[1])
        max_y = max(max_y, int(symbols[symb][-1][1]))

    for _ in range(max_x + 1):
        picture.append([])
        for _ in range(max_y + 1):
            picture[-1].append(" ")

    for symb in symbols:
        for coord in symbols[symb]:
            picture[coord[0]][coord[1]] = symb

    with open(textfile, "w", encoding="utf-8") as file:
        counter = 1
        rows_count = len(picture)
        for row in picture:
            file.write("".join(row))
            if counter < rows_count:
                file.write("\n")

            counter += 1


if __name__ == "__main__":
    # print(int(tuple(["2", "343"])))
    print(save_pict_to_file(read_file("example2.txt"), "new.txt"))

    # import doctest

    # print(doctest.testmod())
