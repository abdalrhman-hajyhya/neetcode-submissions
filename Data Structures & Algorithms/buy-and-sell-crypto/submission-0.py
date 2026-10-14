class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        
        left = 0
        maxDiff = float('-inf')

        for index in range(1,len(prices)):

            if prices[index] - prices[left] <= 0:
                left = index
            maxDiff = max(maxDiff, prices[index] - prices[left])
        
        return maxDiff