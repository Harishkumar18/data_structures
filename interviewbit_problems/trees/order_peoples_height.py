"""
"Order of People Heights

You are given the following :

A positive number N
Heights : A list of heights of N persons standing in a queue
Infronts : A list of numbers corresponding to each person (P) that gives the number of persons who are taller than P and standing in front of P
You need to return list of actual order of persons’s height"
"""

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def order(self, heights, infronts):
        if not heights and not infronts:
            return []
        combined_list, result = [], []
        for i in range(len(heights)):
            combined_list.append([heights[i], infronts[i]])
        combined_list.sort(key=lambda a:-a[0])
        for each in combined_list:
            result.insert(each[1], each[0])
        return result