class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        n = len(candidates)
        def dfs(index, current, total):
            if total == target:
                res.append(current.copy())
                return
            if index >= n or total > target:
                return
            
            current.append(candidates[index])
            dfs(index + 1, current, total + candidates[index])
            
            current.pop()
            while index + 1 < n and candidates[index] == candidates[index + 1]:
                index += 1
            dfs(index + 1, current, total)
        dfs(0, [], 0)
        return res