class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [((point[0])**2 + (point[1])**2,point) for point in points]
        heapq.heapify(distances)
        ans = []
        while k > 0:
            ans.append(heapq.heappop(distances)[1])
            k -=1
        return ans