class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex] = set()

    def get_neighbors(self, vertex_id):
        """
        Return all neighbors of the given vertex
        """
        return self.vertices[vertex_id]

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist.")

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

arr = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
#(parent, child)
def earliest_ancestor(ancestors, starting_node):
    g = Graph()
    for ancestor in ancestors:
        if ancestor[0] not in g.vertices:
            g.add_vertex(ancestor[0])
        if ancestor[1] not in g.vertices:
            g.add_vertex(ancestor[1])
        g.add_edge(ancestor[1], ancestor[0])

    q = Queue()
    q.enqueue([starting_node])
    visited = set()
    paths_list = []

    temp_length = 0
    temp_list = []

    while q.size() > 0:
        path = q.dequeue()
        v = path[-1]
        # print("V>>>", v)
        if v not in visited:
            visited.add(v)
            for next_v in g.vertices[v]:
                path_copy = path.copy()
                path_copy.append(next_v)
                q.enqueue(path_copy)
                # print('NEXT', g.vertices[next_v])
                if len(g.vertices[next_v]) == 0:
                    paths_list.append(path_copy)

    if len(paths_list) > 0:
        for i in paths_list:
            if len(i) > temp_length:
                temp_list = i
        return temp_list[-1]
    return -1

#return smallest ancestor, if multiple
earliest_ancestor(arr, 1)

#  10
#  /
# 1   2   4  11
#  \ /   / \ /
#   3   5   8
#    \ / \   \
#     6   7   9

    # maxList = max(paths_list, key = len)