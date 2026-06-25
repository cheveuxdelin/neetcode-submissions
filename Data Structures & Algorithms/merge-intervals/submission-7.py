class Solution:
    def overlaps(self, arr1, arr2):
        a, b = arr1
        c, d = arr2
        return not (b < c or a > d)
    
    def merge_intervals(self, arr1, arr2):
        return [
            min(arr1[0], arr2[0]),
            max(arr1[1], arr2[1]),
        ]

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        current = intervals[0]
        result = []

        for i in range(1, len(intervals)):
            other = intervals[i]

            if self.overlaps(current, other):
                current = self.merge_intervals(current, other)
            else:
                result.append(current)
                current = other
        result.append(current)
        return result
            
