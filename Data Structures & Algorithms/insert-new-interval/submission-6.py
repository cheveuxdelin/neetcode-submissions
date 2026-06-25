class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start = 0
        end = 1

        def merge_intervals(interval1, interval2):
            return [
                min(interval1[start], interval2[start]),
                max(interval1[end], interval2[end]),
            ]
        
        result = []
        current_index = 0

        while current_index < len(intervals) and intervals[current_index][end] < newInterval[start]:
            result.append(intervals[current_index])
            current_index += 1
        
        result.append(newInterval)

        while current_index < len(intervals) and result[-1][end] >= intervals[current_index][start]:
            result[-1] = merge_intervals(result[-1], intervals[current_index])
            current_index += 1
        
        result.extend(intervals[current_index:])
        
        return result