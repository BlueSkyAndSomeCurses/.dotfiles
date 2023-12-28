"""
member1: <Valihurskyi Anton>
member2: <Mariia Sirska>
"""
from typing import List, Dict
from copy import deepcopy


def read_csv(file_name: str) -> Dict[int, List[int]]:
    """
    read graph represented as matrix in .csv file and return it
    as dictionary where each key represents a vertex, while the value
    represent the list of matrices adjacent to the key
    :rtype: dict(key=int, value=list(int))
    :param file_name: string
    :return: graph

    >>> read_csv("graph.csv")
    {0: [2, 5, 7], 1: [2, 6, 7], 2: [0, 1, 4, 5, 6, 7], 3: [6, 7], 4: [2, 5, 7], 5: [0, 2, 4, 7], 6: [1, 2, 3, 7], 7: [0, 1, 2, 3, 4, 5, 6]}
    """
    graph = {}

    with open(file_name, "r", encoding="utf-8") as file:
        ver = 0
        for line in file:
            for i, vertex in enumerate(line.strip().split(",")):
                if vertex == "1":
                    if ver in graph:
                        graph[ver].append(int(i))
                    else:
                        graph[ver] = [int(i)]
            ver += 1

    return graph


def bfs(graph: Dict[int, List[int]]) -> List[int]:
    """
    perform bfs on the graph and store its result
    in the list of vertices(integers that represent vertices)
    :rtype: list(int)
    :param graph: dict(key=int, value=list(int))
    :return: bfs-result

    >>> bfs({0: [2, 5, 7], 1: [2, 6, 7], 2: [0, 1, 4, 5, 6, 7], 3: [6, 7], 4: [2, 5, 7], 5: [0, 2, 4, 7], 6: [1, 2, 3, 7], 7: [0, 1, 2, 3, 4, 5, 6]})
    [0, 2, 5, 7, 1, 4, 6, 3]
    """
    # Your code goes here(delete "pass" keyword)
    lst = sorted([[i, graph[i]] for i in graph])
    res = []
    for p in lst:
        if p[0] not in res:
            res.append(p[0])
            res.extend(i for i in p[1])
            for t in res[1:]:
                res.extend(a for a in lst[t][1] if a not in res)
    return res


def dfs(graph: Dict[int, List[int]]) -> List[int]:
    """
    perform dfs on the graph and store its result
    in the list of vertices(integers that represent vertices)
    :rtype: list(int)
    :param graph:  dict(key=int, value=list(int))
    :return: dfs-result
    >>> dfs({0: [2, 5, 7], 1: [2, 6, 7], 2: [0, 1, 4, 5, 6, 7], 3: [6, 7], 4: [2, 5, 7], 5: [0, 2, 4, 7], 6: [1, 2, 3, 7], 7: [0, 1, 2, 3, 4, 5, 6]})
    [0, 2, 1, 6, 3, 7, 4, 5]
    """

    graph = deepcopy(graph)
    stack = [list(graph.keys())[0]]
    dfs_verts = [stack[0]]

    while stack:
        if graph[stack[-1]]:
            if graph[stack[-1]][0] not in dfs_verts:
                stack.append(graph[stack[-1]].pop(0))
                dfs_verts.append(stack[-1])
            else:
                graph[stack[-1]].pop(0)
        else:
            stack.pop()

    return dfs_verts


def calc_pow(graph: Dict[int, List[int]]) -> Dict[int, int]:
    """
    calculate power of every vertex of your graph(i.e. number adjacent edges)
    :rtype: dict(key=int, value=int)
    :param graph: dict(key=int, value=list(int))
    :return: vertices and their powers

    >>> calc_pow({1:[2,3], 2:[1, 3], 3: [], 4: [1]})
    {1: 2, 2: 2, 3: 0, 4: 1}
    """
    # Your code goes here(delete "pass" keyword)
    return {k: len(graph[k]) + graph[k].count(k) for k in graph}


def find_path(n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    """
    here is another way of representing a graph:
    edges - is a list of edges of a graph,
    where each edge is also a list of two integers,
    which represent 2 adjacent vertices
    find if there is a way from the source vertex to the destination one
    :rtype: bool
    :param n: int
    :param edges: list(list(int))
    :param source: int
    :param destination: int
    :return:

    >>> find_path(9, [[1, 2], [3, 4], [5, 6], [7, 8], [2, 4], [3, 5], [4, 5]], 1, 5)
    True
    >>> find_path(9, [[1, 2], [3, 4], [5, 6], [7, 8], [2, 2], [3, 5], [4, 5]], 1, 5)
    False
    """

    visited = set([source])
    queue = [source]

    while queue:
        vert = queue.pop(0)
        verts_to_check = [v for u, v in edges if u == vert]
        for v in verts_to_check:
            if v == destination:
                return True
            if v not in visited:
                visited.add(v)
                queue.append(v)

    return False


if __name__ == "__main__":
    import doctest

    print(doctest.testmod())
