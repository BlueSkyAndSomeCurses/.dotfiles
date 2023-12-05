from copy import deepcopy
from itertools import combinations


def read_file(file):
    matrix = []
    with open(file, "r", encoding="utf-8") as csv_table:
        for line in csv_table:
            matrix.append([])
            line = line.strip()
            for numb in line:
                matrix[-1].append(numb)
        for line in matrix:
            while len(line) != len(matrix):
                line.insert(0, "0")
    return matrix


def write_R(matr, file):
    with open(file, "w", encoding="utf-8") as new_file:
        vidnoshenia = []
        for i, lst in enumerate(matr):
            for j, el in enumerate(lst):
                if el == "1":
                    vidnoshenia.append("(" + str(i) + ", " + str(j) + ")")
        vidnoshenia = ",".join(vidnoshenia)
        new_file.write(vidnoshenia)


def write_matr(matr, file):
    with open(file, "w", encoding="utf-8") as new_file:
        for row in matr:
            new_file.write(" ".join(row) + "\n")


def refl_lock(matrix):
    for ind in range(len(matrix)):
        matrix[ind][ind] = "1"

    return matrix


def sym_lock(matrix):
    for row in range(len(matrix)):
        for ind, el in enumerate(matrix[row]):
            if el == "1":
                # try:
                matrix[ind][row] = "1"
                # except IndexError:
                #     print(ind)
    return matrix


def warshall(matrix):
    for line in range(len(matrix)):
        for ind, row in enumerate(matrix):
            if matrix[ind][line] == "1":
                for el in range(len(matrix)):
                    if matrix[ind][el] == "1" or matrix[line][el] == "1":
                        matrix[ind][el] = "1"
    return matrix


def classes_break(matrix):
    classes_eq = []
    for el in range(len(matrix)):
        classes_eq.append([el])
        for i in range(len(matrix)):
            if matrix[el][i] == "1" and i not in classes_eq[el]:
                classes_eq[el].append(i)
        for i in range(len(matrix)):
            if matrix[i][el] == "1" and i not in classes_eq[el]:
                classes_eq[el].append(i)

    return classes_eq


def istranz(rel):
    return deepcopy(rel) == warshall(rel)


def count_tranz(set_):
    set_ = sorted(set_)
    n = len(set_)
    counter = 0
    relation = []
    for i in set_:
        for j in set_:
            relation.append((i, j))

    for numb in range(len(relation) + 1):
        for sub_rel in combinations(relation, numb):
            # print(sub_rel)
            matrix = []
            for _ in range(n):
                matrix.append(["0"] * n)

            for pair in sub_rel:
                matrix[set_.index(pair[0])][set_.index(pair[1])] = "1"

            if istranz(matrix):
                counter += 1

    return counter


if __name__ == "__main__":
    matrix = [
        ["1", "0", "0", "1", "0"],
        ["0", "0", "1", "0", "1"],
        ["1", "1", "1", "0", "1"],
        ["1", "1", "0", "1", "1"],
        ["1", "0", "0", "0", "1"],
    ]

    write_matr(matrix, "beg_matrix.csv")
    write_R(matrix, "beg_relation.csv")

    write_matr(refl_lock(deepcopy(matrix)), "refl_lock.csv")
    write_matr(sym_lock(deepcopy(matrix)), "sym_lock.csv")
    write_matr(warshall(deepcopy(matrix)), "warshall.csv")
    print(classes_break(deepcopy(matrix)))
    print(istranz(deepcopy(matrix)))
    print(istranz(warshall(deepcopy(matrix))))
    print(count_tranz({1, 2, 3}))
