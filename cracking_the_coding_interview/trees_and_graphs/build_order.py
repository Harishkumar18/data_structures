#TODO: Need to fix the code
"""You are given a list of projects and a list of dependencies (which is a list of pairs of
projects, where the second project is dependent on the first project). All of a project's dependencies
must be built before the project is. Find a build order that will allow the projects to be built. If there
is no valid build order, return an error. """

from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.v = vertices

    def addEdge(self, u , v):
        self.graph[u].append(v)

    def topological_sort_util(self, v, visited, stack):
        visited[v] = True
        for vertex in self.graph[v]:
            if not visited[vertex]:
                self.topological_sort_util(vertex, visited, stack)
        stack.insert(0, v)

    def topological_sort(self):
        visited = [False]*self.v
        stack = []
        for i in range(self.v):
            if not visited[i]:
                self.topological_sort_util(i, visited, stack)

        print(stack)


vertices = 6
g = Graph(vertices)
g.addEdge("a", "d")
g.addEdge("f", "b")
g.addEdge("b","d")
g.addEdge("f", "a")
g.addEdge("d", "c")
print(g.graph)
g.topological_sort()