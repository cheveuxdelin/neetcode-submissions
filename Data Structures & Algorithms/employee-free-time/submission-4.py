"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""
class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        start = 0
        end = 1

        def are_overlapping(interval1, interval2):
            return not(interval1.start >= interval2.end or interval1.end <= interval2.start)

        # first i acknlowledge that translating the schedules into the intervals of free time
        # might be a great step
        # then we can find the common intervals within all these list of schedules??

        # nevermind.
        # we merge them all into a single array.
        # we merge all these intervals. the result would represent common busy time between them all
        # gaps between these would just be what we are looking for
        all_intervals = []
        heap = [(intervals[0].start, i, 0) for i, intervals in enumerate(schedule) if intervals]
        heapq.heapify(heap)

        # O(N*logK) instead of O(N*logN)
        while heap:
            _, schedule_index, interval_index = heapq.heappop(heap)
            all_intervals.append(schedule[schedule_index][interval_index])
            if (next_index := interval_index + 1) < len(schedule[schedule_index]):
                heapq.heappush(heap, (schedule[schedule_index][next_index].start, schedule_index, next_index))
        
        # now that they are all flattened, let's begin merging them
        merged_intervals = []
        for interval in all_intervals:
            if not merged_intervals or not are_overlapping(merged_intervals[-1], interval):
                merged_intervals.append(interval)
            else:
                merged_intervals[-1].start = min(merged_intervals[-1].start, interval.start)
                merged_intervals[-1].end = max(merged_intervals[-1].end, interval.end)
        
        # now that they are super duper merged, we find the gaps
        # we compare the current start with the last end
        # compute the gap and make sure its of min width 1
        result = []
        if merged_intervals:
            last_end = merged_intervals[0].end

            for interval in merged_intervals[1:]:
                if interval.start > last_end:
                    result.append(Interval(last_end, interval.start))
                last_end = interval.end
        return result
        
