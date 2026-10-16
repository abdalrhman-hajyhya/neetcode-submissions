class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        visited = set()
        def dfs(current, length):
            if length == n:
                res.append(current.copy())
                return
            for i in range(n):
                if i not in visited:
                    current.append(nums[i])
                    visited.add(i)
                    dfs(current, length + 1)
                    current.pop()
                    visited.remove(i)
        dfs([], 0)
        return res