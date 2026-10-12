class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashTable = {}
        for string in strs:
            hist = [0] * 26
            for letter in string:
                hist[ord(letter) - ord("a")] += 1
            
            key = tuple(hist)
            if key not in hashTable:
                hashTable[key] = []
            hashTable[key].append(string)

        ans = []
        for value in hashTable.values():
            ans.append(value)
        return ans