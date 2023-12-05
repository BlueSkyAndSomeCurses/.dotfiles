res = 0


def find_num(line):
    for i, symb in enumerate(line):
        if not symb.isdigit():
            return i


with open("testinput.txt", "r", encoding="utf-8") as file:
    engine = [line.strip() for line in file]


def check_digits(start, stop, row):
    if start > 0 and engine[row][start - 1] != ".":
        return True
    if stop < len(engine[0]) - 1 and engine[row][stop + 1] != ".":
        return True

    if row > 0:
        if (
            start > 0
            and engine[row - 1][start - 1] != "."
            and not engine[row - 1][start - 1].isdigit()
        ):
            return True
        if (
            stop < len(engine[0]) - 1
            and engine[row - 1][stop + 1] != "."
            and not engine[row - 1][stop + 1].isdigit()
        ):
            return True
        for i in range(start, stop + 1):
            if not engine[row - 1][i].isdigit() and engine[row - 1][i] != ".":
                return True

    if row < len(engine) - 1:
        if (
            start > 0
            and engine[row + 1][start - 1] != "."
            and not engine[row + 1][start - 1].isdigit()
        ):
            return True
        if (
            stop < len(engine[0]) - 1
            and engine[row + 1][stop + 1] != "."
            and not engine[row + 1][stop + 1].isdigit()
        ):
            return True
        for i in range(start, stop + 1):
            if not engine[row + 1][i].isdigit() and engine[row + 1][i] != ".":
                return True


for i, line in enumerate(engine):
    start = 0
    stop = -1
    numb = -1
    for j, symb in enumerate(line):
        if stop > -1:
            stop -= 1
            continue
        if symb.isdigit():
            start = j
            stop = j + find_num(line[j:])
            numb = int(line[start:stop])
            if check_digits(start, stop - 1, i):
                print(numb)
                res += numb
print(res)
