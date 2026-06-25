class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        def are_intersecting(interval_a, interval_b) -> bool:
            a, b = interval_a
            c, d = interval_b
            return not (a > d or b < c)
        
        result = []
        i = 0

        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
        
        while i < len(intervals) and are_intersecting(intervals[i], newInterval):
            newInterval = [
                min(intervals[i][0], newInterval[0]),
                max(intervals[i][1], newInterval[1]),
            ]
            i += 1
        result.append(newInterval)
        result.extend(intervals[i:])
        return result