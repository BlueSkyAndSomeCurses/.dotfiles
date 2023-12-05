"""
module with functions to work on notes graphs
"""
import re


def build_graph_from_note(note_path, graph=None):
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

    print(pwd, note, graph)

    with open(note_path, "r", encoding="utf-8") as note_file:
        for node in re.search(r"\[\[.*\]\]", note_file.read()).group(0).split(" "):
            node = node[2:-2]
            if node not in graph[note]:
                graph[note].append(node)
                graph = build_graph_from_note(pwd + node + ".md", graph)

    return graph


if __name__ == "__main__":
    print(build_graph_from_note("./note1.md"))
