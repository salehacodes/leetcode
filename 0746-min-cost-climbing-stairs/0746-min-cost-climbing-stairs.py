class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        prev2 = cost[0]
        prev1 = cost[1]
        for i in range(2, len(cost)):
            current = min(prev1, prev2) + cost[i]
            prev2 = prev1
            prev1 = current
        return min(prev1, prev2)