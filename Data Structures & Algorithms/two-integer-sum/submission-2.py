class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashTable = {}
        for i in range(len(nums)):
            tmp = target - nums[i]
            if tmp in hashTable:
                return [hashTable[tmp], i]
            hashTable[nums[i]] = i
