"""
https://www.programiz.com/dsa/graph-adjacency-matrix

adjacency matrix
"""


class Graph:
    def __init__(self, size):
        self.size = size
        self.graph_matrix = [[0 for _ in range(size)] for _ in range(size)]

    def add_edge(self, u, v):
        self.graph_matrix[u][v] = 1
        self.graph_matrix[v][u] = 1

    def __len__(self):
        return self.size

    def print_matrix(self):
        return self.graph_matrix



g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
print(g.print_matrix())