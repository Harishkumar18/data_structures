"""
You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. Return the destination city, that is, the city without any path outgoing to another city.

It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.



Example 1:

Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
Output: "Sao Paulo"
Explanation: Starting at "London" city you will reach "Sao Paulo" city which is the destination city. Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".
"""
from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        """
        Key Idea
        Smart way: Add destination cities into a set and remove source cities from set.

        Why smart way works
        You want to find a city which will not go anywhere, so that city would never come into source cities i.e. paths[i][0] for all i.
        Every other city will certainly appear once in source paths[i][0] for all i.

        Hence, if you add all paths[i][1] into a set and remove paths[i][0] for all i's, it will eventually have just one value.

        Complexity Analysis
        If there are n paths, there would be at most n insertions into the set. and simmilarly n removals.
        Hence space required would O(n).
        Each insertion/removal would take constant time, so time complexity O(n).
        """
        return (set(path[1] for path in paths) - set(path[0] for path in paths)).pop()

    def destCity2(self, paths: List[List[str]]) -> str:
        """destination city should not be in source"""
        hTable = {}
        cities = []

        for path in paths:
            hTable[path[0]] = path[1]
            cities.append(path[0])
            cities.append(path[1])

        for city in cities:
            if city not in hTable.keys():
                return city