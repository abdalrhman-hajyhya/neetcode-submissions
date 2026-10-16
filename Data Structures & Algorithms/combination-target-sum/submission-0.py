class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backTrack(startIndex ,arr):
            if sum(arr) == target:
                res.append(list(arr))
                return
            for i in range(startIndex ,len(nums)):
                count = 0
                while sum(arr) + nums[i] <= target:
                    count += 1
                    arr.append(nums[i])
                    backTrack(i + 1,arr)
                while count > 0:
                    arr.pop()
                    count -= 1
        backTrack(0 ,[])
        return res