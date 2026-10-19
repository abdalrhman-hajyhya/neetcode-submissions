class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        DP = [-1] * n
        DP[n - 1] = nums[n - 1]
        DP[n - 2] = max(nums[n - 2], nums[n - 1])

        for i in range(n - 3, -1, -1):
            DP[i] = max(nums[i] + DP[i + 2], DP[i + 1])

        return DP[0] 