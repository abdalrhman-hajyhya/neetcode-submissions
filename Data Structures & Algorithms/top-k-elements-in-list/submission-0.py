class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashTable = {}
        for num in nums:
            if num not in hashTable:
                hashTable[num] = 0
            hashTable[num] +=1
        
        freq = [[] for i in range(len(nums) + 1)]

        for key in hashTable:
            freq[hashTable[key]].append(key)
        
        ans = []
        for i in range(len(freq) - 1, 0,-1):
            for num in freq[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans
