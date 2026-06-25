"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        heap = []

        def are_overlapping(interval1, interval2):
            start = 0
            end = 1
            return not(interval.start >= interval2.end and interval1.end <= interval2.start)
        def merge_intervals(interval1, interval2):
            return Interval(
                min(interval1.start, interval2.start),
                max(interval1.end, interval2.end),
            )


        for employee_index, employee in enumerate(schedule):
            first_interval = employee[0]
            heap.append((first_interval.start, employee_index, 0, first_interval))
        heapq.heapify(heap)

        result = []
        previous_end = None

        while heap:
            start, employee_index, interval_index, interval = heapq.heappop(heap)

            if previous_end is not None and start > previous_end:
                result.append(Interval(previous_end, start))
            
            # update prev_end to the furthest end so far
            previous_end = max(previous_end, interval.end) if previous_end is not None else interval.end
            
            if interval_index < len(schedule[employee_index])-1:
                next_interval = schedule[employee_index][interval_index + 1]
                heapq.heappush(heap, (next_interval.start, employee_index, interval_index + 1, next_interval))
        return result



