"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # heap will represent the current rooms used
        # we dont need to do it real-time, we just can leave it stale
        # because is correctly upper bounding

        intervals.sort(key=lambda x: x.start)
        heap = []

        for interval in intervals:
            # first one or
            # earliest ending meeting hasnt even ended
            if not heap or heap[0] > interval.start:
                # we want to min-heap under the earliest end_time
                heapq.heappush(heap, (interval.end))
            else:
                heapq.heappop(heap)
                heapq.heappush(heap, (interval.end))
        return len(heap)