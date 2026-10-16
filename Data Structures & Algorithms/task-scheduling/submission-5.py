class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks).values()
        maxFreq = max(counts)
        numOfMaxFeq = sum(1 for c in counts if c == maxFreq)
        return max(len(tasks),(maxFreq - 1)*(n+1) + numOfMaxFeq)