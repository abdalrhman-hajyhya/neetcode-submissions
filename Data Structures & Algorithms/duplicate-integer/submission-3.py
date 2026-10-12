class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numbersTable = set()
        for num in nums: 
            if num in numbersTable:
                return True
            numbersTable.add(num)
        return False