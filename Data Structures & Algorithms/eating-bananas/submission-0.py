class Solution:
    def timeToFinish(self, piles: List[int], k: int):
        totalTime = 0
        for i in range(len(piles)):
            if piles[i] == 0:
                continue
            totalTime += math.ceil(piles[i]/k)
        return totalTime

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) > h:
            return -1
        
        best = max(piles)
        left = 1
        right = max(piles)
        
        while left <= right:
            mid = (right + left) // 2
            
            if self.timeToFinish(piles,mid) > h:
                left = mid + 1
            else:
                best = min(best, mid)
                right = mid - 1
        
        return best