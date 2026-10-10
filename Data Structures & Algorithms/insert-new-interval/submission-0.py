
class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        intervals.append(newInterval)
        intervals.sort()
        mergedInt = []
        curr = intervals[0]
        for l in intervals[1:]:
            last = curr[1]
            if last >= l[0]:
                curr[1] = max(last, l[1])
            else:
                mergedInt.append(curr)
                curr = l
        mergedInt.append(curr)
        return mergedInt