class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        step1, step2 = 0, 0
        for i in range(2, len(cost) + 1):
            currentCost = min(step1 + cost[i -1], step2 + cost[i - 2])

            step2 = step1 
            step1 = currentCost
        return step1
