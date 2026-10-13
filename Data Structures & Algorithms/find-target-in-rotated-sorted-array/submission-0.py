from typing import List

class Solution:
    def binarySearch(self, nums: List[int], left: int, right: int, target: int) -> int:
        while left <= right:
            mid = (right + left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return -1

    def minIndex(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (right + left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return left

    def search(self, nums: List[int], target: int) -> int:
        minIndex = self.minIndex(nums)
    
        if minIndex == 0:
            return self.binarySearch(nums, 0, len(nums) - 1, target)
        right_search = self.binarySearch(nums, minIndex, len(nums) - 1, target)
        
        if right_search != -1:
            return right_search
        else:
            return self.binarySearch(nums, 0, minIndex - 1, target)