class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []
        for i in range(len(stones)):
            maxHeap.append(stones[i] * -1)
        
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            stoneOne = heapq.heappop(maxHeap) * -1
            stoneTwo = heapq.heappop(maxHeap) * - 1
            if stoneOne != stoneTwo:
                heapq.heappush(maxHeap,abs(stoneTwo - stoneOne) * -1)
            else:
                continue
        
        return maxHeap[0] * -1 if maxHeap else 0
            