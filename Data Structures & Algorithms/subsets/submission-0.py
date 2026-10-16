class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def getSubSets(startIndex ,subSet):
            res.append(list(subSet))
            for i in range(startIndex,len(nums)):
                subSet.append(nums[i])
                getSubSets(i + 1,subSet)
                subSet.pop()
        
        getSubSets(0,[])
        return res