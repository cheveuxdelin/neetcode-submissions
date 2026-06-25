class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        result = 0
        previous_end = intervals[0][1]

        for start, end in islice(intervals, 1, None):
            if start >= previous_end:
                previous_end = end
            else:
                result += 1
                previous_end = min(previous_end, end)
        return result