class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        countMap = {}

        res ,left = 0, 0
        for right in range(len(s)):
            countMap[s[right]] = 1 + countMap.get(s[right], 0)

            while (right - left + 1) - max(countMap.values()) > k:
                countMap[s[left]] -= 1
                left += 1
            
            res = max(res, right - left + 1)
        return res