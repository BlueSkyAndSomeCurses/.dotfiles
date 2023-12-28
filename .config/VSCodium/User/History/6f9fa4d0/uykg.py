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
    """
    # Your code goes here(delete "pass" keyword)
    pass


def dfs(graph: Dict[int, List[int]]) -> List[int]:
    """
    perform dfs on the graph and store its result
    in the list of vertices(integers that represent vertices)
    :rtype: list(int)
    :param graph:  dict(key=int, value=list(int))
    :return: dfs-result
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
    """
    # Your code goes here(delete "pass" keyword)
    pass


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
    """

    vertices = set()
    in_path = set()
    for edge in edges:
        set.add(edge[0])
        set.add(edge[1])
    print(vertices)
    queue = [source]
    
    while len(queue) != len(vertices):
        


if __name__ == "__main__":
    graph = read_csv("graph.csv")
    print(graph)
    print(dfs(graph))
