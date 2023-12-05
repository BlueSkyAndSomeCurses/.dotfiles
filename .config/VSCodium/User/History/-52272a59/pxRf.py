"""
module with functions to work on notes graphs
"""
import re


def build_graph_from_note(note_path: str, graph=None) -> dict:
    """
    Functoin takes a path to a note and returns a dictionary
    with all links to other notes in this note, and all notes which directs to given note.
    """

    if not graph:
        graph = {}

    note = re.search(r"/.*\.md$", note_path).group(0)[1:-3]
    pwd = note_path[: note_path.rfind("/") + 1]

    if note not in graph:
        graph[note] = []

    try:
        with open(note_path, "r", encoding="utf-8") as note_file:
            for line in note_file:
                match = re.search(r"\[\[.*\]\]", line)
                if match:
                    for node in match.group(0).split(" "):
                        node = node[2:-2]
                        if node not in graph[note]:
                            graph[note].append(node)
                            graph = build_graph_from_note(pwd + node + ".md", graph)
    except FileNotFoundError:
        return graph

    return graph


def convert_to_dot(graph: dict):
    """
    Converts dictionary to graph
    """

    with open("graph.dot", "w", encoding="utf-8") as graph_dot:
        graph_dot.write("digraph {\n")
        for key, value in graph.items():
            for node in value:
                graph_dot.write(f"{key} -> {node}\n")

        graph_dot.write("}\n")


if __name__ == "__main__":
    convert_to_dot(build_graph_from_note("./note1.md"))
    print(build_graph_from_note("./note1.md"))
