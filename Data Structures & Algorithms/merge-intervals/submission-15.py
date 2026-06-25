class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        start = 0
        end = 1

        def are_overlapping(interval1, interval2):
            return not(interval1[start] > interval2[end] or interval1[end] < interval2[start])
        
        def merge_intervals(interval1, interval2):
            return [
                min(interval1[start], interval2[start]),
                max(interval1[end], interval2[end])
            ]
        
        result = []

        for interval in intervals:
            if not result or not are_overlapping(result[-1], interval):
                result.append(interval)
            else:
                result[-1] = merge_intervals(result[-1], interval)
        return result