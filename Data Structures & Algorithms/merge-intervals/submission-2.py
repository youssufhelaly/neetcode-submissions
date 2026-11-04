class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()
        curr = intervals[0]

        for interval in intervals[1:]:
            if interval[0] <= curr[1]:
                curr[1] = max(interval[1], curr[1])
            else:
                res.append(curr)
                curr = interval
        res.append(curr)
        return res