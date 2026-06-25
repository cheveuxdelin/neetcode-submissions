class Solution:
    def are_overlapping(self, interval1: list[int], interval2: list[int]) -> bool:
        start, end = 0, 1
        return not (interval1[end] < interval2[start] or interval1[start] > interval2[end])

    def merge_intervals(self, interval1: list[int], interval2: list[int]) -> list[int]:
        return [
            min(interval1[0], interval2[0]),
            max(interval1[1], interval2[1])
        ]

    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        result = []
        i = 0

        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        while i < len(intervals) and self.are_overlapping(intervals[i], newInterval):
            newInterval = self.merge_intervals(intervals[i], newInterval)
            i += 1

        result.append(newInterval)

        while i < len(intervals):
            result.append(intervals[i])
            i += 1

        return result
