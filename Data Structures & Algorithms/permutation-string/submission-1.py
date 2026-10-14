class Solution:
    def compareHists(self, hist1, hist2):
        for key in hist1:
            if hist1.get(key, 0) != hist2.get(key, 0):
                return False
        return True
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        histS1 = {}
        for i in range(len(s1)):
            histS1[s1[i]] = 1 + histS1.get(s1[i], 0)
        
        left = 0
        histS2 = {}
        for right in range(len(s2)):

            if (right - left + 1) > len(s1):
                histS2[s2[left]] -=1
                left +=1
            histS2[s2[right]] = 1 + histS2.get(s2[right], 0)

            if self.compareHists(histS1, histS2):
                return True

        
        return False