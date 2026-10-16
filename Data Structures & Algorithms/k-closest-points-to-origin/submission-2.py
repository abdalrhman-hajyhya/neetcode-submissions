class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []

        for point in points:
            distance = -1 * (point[0]**2 + point[1]**2)
            if len(maxHeap) < k:
                heapq.heappush(maxHeap, (distance,point))
            else:
                if maxHeap[0][0] < distance:
                    heapq.heapreplace(maxHeap,(distance,point))
        
        return [point[1] for point in maxHeap]