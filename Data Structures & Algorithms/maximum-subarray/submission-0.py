class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentMax = nums[0]
        currentSum = 0
        for n in nums:
            if currentSum < 0:
                currentSum = 0
            currentSum += n
            
            if currentSum > currentMax:
                currentMax = currentSum
        return currentMax