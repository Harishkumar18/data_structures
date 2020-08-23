"""
find the largest item association

https://leetcode.com/discuss/interview-question/782606/
"""

from collections import defaultdict


class graph:
    """class for creating graphs"""

    def __init__(self):
        self.graph = defaultdict(list)
        self.children = set()

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.children.add(v)


# the association between list of items
item_association = [['item1', 'item2'], ['item4', 'item5'], ['item3', 'item4']]

# creation of graph
g = graph()
for i in range(len(item_association)):
    g.add_edge(item_association[i][0], item_association[i][1])

# output of the above g statement
# graph defaultdict(<class 'list'>, {'item1': ['item2']})
# children {'item2'}
# graph defaultdict(<class 'list'>, {'item1': ['item2'], 'item4': ['item5']})
# children {'item5', 'item2'}
# graph defaultdict(<class 'list'>, {'item1': ['item2'], 'item4': ['item5'], 'item3': ['item4']})
# children {'item4', 'item5', 'item2'}


# Performing depth-first search to get the combined items in a particular group
def dfs(graph, key, visited, inter):
    visited.add(key)
    inter.append(key)
    for neighbor in graph[key]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, inter)


# Final list that contains resulted output
result = []
# visited set to keep track of visited nodes so that we won't visit the node again
visited = set()

for key in list(g.graph):
    # Intermediate list which gives the items belong to single group
    intermediate_list = []
    if key not in visited:
        if key not in g.children:
            dfs(g.graph, key, visited, intermediate_list)

    if not result:
        result = intermediate_list
    else:
        if len(intermediate_list) > len(result):
            result = intermediate_list
        elif len(intermediate_list) == len(result):
            if sorted(intermediate_list)[0] < sorted(result)[0]:
                result = intermediate_list

print(result)

