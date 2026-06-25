class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        
        def merge_intervals(int1, int2):
            return [
                min(int1[0],int2[0]),
                max(int1[1],int2[1]),
            ]
        
        def are_overlapping(int1, int2):
            a, b = int1
            c, d = int2
            return not(a > d or b < c)
        
        result = [intervals[0]]

        for i in range(1, len(intervals)):
            if are_overlapping(result[-1], intervals[i]):
                result[-1] = merge_intervals(result[-1], intervals[i])
            else:
                result.append(intervals[i])
        return result