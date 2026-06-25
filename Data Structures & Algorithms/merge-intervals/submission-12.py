class Solution:
    def are_overlapping(self, interval1, interval2):
        start, end = 0, 1
        return not(interval1[end] < interval2[start] or interval1[start] > interval2[end])
    
    def merge_intervals(self, interval1, interval2):
        return [
            min(interval1[0], interval2[0]),
            max(interval1[1], interval2[1]),
        ]

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = [intervals[0]]
        i = 1
        
        for _, interval in enumerate(intervals, 1):
            if self.are_overlapping(result[-1], interval):
                result[-1] = self.merge_intervals(result[-1], interval)
            else:
                result.append(interval)
        return result