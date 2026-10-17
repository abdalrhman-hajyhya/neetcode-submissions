class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()
        def dfs(index, arrToNow):
            if index >= n:
                res.append(list(arrToNow))
                return
            
            arrToNow.append(nums[index])
            dfs(index + 1,arrToNow)
            
            arrToNow.pop()
            while index + 1 < n and nums[index] == nums[index + 1]:
                index += 1
            dfs(index + 1, arrToNow)

        dfs(0, [])
        return res