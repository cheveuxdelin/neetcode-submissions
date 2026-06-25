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
        
        while i < len(intervals):
            while i < len(intervals) and self.are_overlapping(result[-1], intervals[i]):
                result[-1] = self.merge_intervals(result[-1], intervals[i])
                i += 1
            if i < len(intervals):
                result.append(intervals[i])
                i += 1
        return result