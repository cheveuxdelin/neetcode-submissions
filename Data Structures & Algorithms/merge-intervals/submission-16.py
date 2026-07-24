import itertools

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # need to sort, likely
        # inclusive counts as intersection

        intervals.sort()
        result = [intervals[0]]

        for current_interval in itertools.islice(intervals, 1, None):
            if result[-1][1] >= current_interval[0]:
                result[-1] = [
                    min(result[-1][0], current_interval[0]),
                    max(result[-1][1], current_interval[1]),
                ]
            else:
                result.append(current_interval)
        return result