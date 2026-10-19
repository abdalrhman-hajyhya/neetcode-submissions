class Solution:
    def rob(self, nums: List[int]) -> int:
        

        def robOne(nums):
            rob1, rob2 = 0, 0
            for n in nums:
                currentMax = max(rob1 + n, rob2)
                rob1 = rob2
                rob2 = currentMax
            return rob2
        
        return max(nums[0],robOne(nums[1:]), robOne(nums[:-1]))