class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        DP = [False] * (len(s) + 1)
        DP[len(s)] = True
        for i in range(len(s) - 1, -1 , -1):
            for word in wordDict:
                if (i + len(word)) <= len(s) and s[i:i + len(word)] == word:
                    DP[i] = DP[i + len(word)]
                if DP[i]:
                    break
        return DP[0]