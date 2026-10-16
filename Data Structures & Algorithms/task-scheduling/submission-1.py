class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        lettersNum = 26
        frequency = [0] * 26
        for i in range(len(tasks)):
            frequency[ord(tasks[i]) - ord('A')] += 1
        maxHeap = []
        for i in range(len(frequency)):
            if frequency[i]:
                heapq.heappush(maxHeap, -frequency[i])
        queue = deque()
        time = 0
        while maxHeap or queue:
            time += 1
            if maxHeap:
                task = 1 + heapq.heappop(maxHeap)
                if task:
                    queue.append([task, time + n])
            if queue and queue[0][1] <= time:
                heapq.heappush(maxHeap, queue.popleft()[0])
        return time