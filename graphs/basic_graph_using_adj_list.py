"""
Reference: https://medium.com/youstart-labs/implement-graphs-in-python-like-a-pro-63bc220b45a0

Building graph using adjacency list
"""


from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        """add edges to the graph"""
        self.graph[u].append(v)

    def show_edges(self):
        """Printing all the edges with ots relation of the graph"""
        for element in self.graph:
            print(element, self.graph[element])

    def find_path(self, start, end, path=[]):
        """find the path between any given nodes"""
        path = path+[start]
        if start == end:
            return path
        for node in self.graph[start]:
            if node not in path:
                newpath = self.find_path(node, end, path)
                if newpath:
                    return newpath
        return None

    def find_shortest_path(self, start, end, path=[]):
        """find the path between any given nodes"""
        path = path+[start]
        if start == end:
            return path
        shortest_path = []
        for node in self.graph[start]:
            if node not in path:
                newpath = self.find_path(node, end, path)
                if not shortest_path or len(shortest_path) > len(newpath):
                    shortest_path = newpath
        return shortest_path if shortest_path else None

    def find_all_path(self, start, end, path=[]):
        """find all the paths between given nodes"""
        path = path+[start]
        if start == end:
            return path
        paths = []
        for node in self.graph[start]:
            if node not in path:
                newpaths = self.find_path(node, end, path)
                paths.append(newpaths)
        return paths


if __name__ == "__main__":
    g = Graph()
    g.add_edge("1", "2")
    g.add_edge("1", "3")
    g.add_edge("2", "1")
    g.add_edge("2", "3")
    g.add_edge("3", "4")
    g.add_edge("4", "3")
    g.add_edge("3", "1")
    g.add_edge("3", "2")
    # g.show_edges()
    # print(g.find_path("2", "4"))
    # print(g.find_shortest_path("2", "4"))
    print(g.find_all_path("2", "4"))