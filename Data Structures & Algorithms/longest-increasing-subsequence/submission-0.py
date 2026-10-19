class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        DP = [1] * len(nums) 
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    DP[i] = max(DP[i], 1 + DP[j])
        return max(DP)