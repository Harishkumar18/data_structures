class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        tank = gap = start = 0
        for i in range(len(gas)):
            tank += gas[i]
            if tank >= cost[i]:
                print("count", i)
                tank -= cost[i]
            else:
                gap += cost[i] - tank
                start = i + 1
                tank = 0
        if start == len(gas) or tank < gap: return -1
        return start

s1 = Solution()
gas = [2,3,4]
cost = [3,4,3]
print("ans",s1.canCompleteCircuit(gas, cost))