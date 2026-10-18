class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i:i[0])
        index, res = 0, []
        n = len(intervals)
        while index < n:
            newInterval = intervals[index]
            while index + 1 < n and newInterval[1] >= intervals[index+1][0]:
                newInterval[1] = max(newInterval[1], intervals[index+1][1])
                index += 1
            res.append(newInterval)
            index += 1
        return res
