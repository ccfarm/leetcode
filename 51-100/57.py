# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if len(intervals) == 0 or newInterval.start < intervals[0]:
            intervals.append(newInterval)
        l = 0
        r = len(intervals) - 1
        while l <= r:
            m = (l + r) // 2
            if intervals[m].start <= newInterval.start and (m == len(intervals) - 1 or intervals[m + 1].start > newInterval.start):
                break
            else:
                if intervals[m].start < newInterval.start:
                    l = m + 1
                else:
                    r = m - 1
        intervals.insert(m, newInterval)
        i = 0
        while i < len(intervals) - 1:
            if intervals[i].end >= intervals[i + 1].start:
                intervals[i].end = max(intervals[i].end, intervals[i + 1].end)
                del intervals[i + 1]
            else:
                i += 1
        return intervals
