class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        
        hashMap = {}
        left = 0
        maxDiff = 1
        for right in range(len(s)):

            if s[right] in hashMap:
                left = max(hashMap.get(s[right]) + 1, left)
            hashMap[s[right]] = right
            maxDiff = max(maxDiff, right - left + 1)
        return maxDiff
        