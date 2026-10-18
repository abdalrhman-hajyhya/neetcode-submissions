import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        # Build the graph using 1-indexing to match the problem description
        graphMap = defaultdict(list)
        for u, v, weight in times:
            graphMap[u].append((v, weight))
        
        # Use float('inf') for unreached nodes
        distances = {i: float('inf') for i in range(1, n + 1)}
        distances[k] = 0
        
        # Min-heap must store (weight, node)
        minHeap = [(0, k)]
        
        while minHeap:
            weight, node = heapq.heappop(minHeap)
            
            if weight > distances[node]:
                continue
                
            for nei, edgeWeight in graphMap[node]:
                newWeight = weight + edgeWeight
                if newWeight < distances[nei]:
                    distances[nei] = newWeight
                    heapq.heappush(minHeap, (newWeight, nei))
                    
        # Extract the maximum value from the dictionary
        maxDistance = max(distances.values())
        
        # If any node is still unreachable, return -1
        return maxDistance if maxDistance != float('inf') else -1