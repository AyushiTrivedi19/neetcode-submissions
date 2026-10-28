class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        newInterval = intervals[0]
        res = []
        res.append(newInterval)

        for interval in intervals[1:]:
            if newInterval[1] < interval[0]:
                res.append(interval)
                newInterval = interval
            elif newInterval[0] > interval[1]:
                break
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
        return res