"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = {}
        ends = {}

        max_meeting_time = 0

        for interval in intervals:
            starts[interval.start] = starts.get(interval.start, 0) + 1
            ends[interval.end] = ends.get(interval.end, 0) + 1
            max_meeting_time = max(max_meeting_time, interval.end)

        max_concurrent_meetings = 0
        current = 0
        for i in range(max_meeting_time):
            current += starts.get(i, 0)
            current -= ends.get(i, 0)
            max_concurrent_meetings = max(max_concurrent_meetings, current)
        
        return max_concurrent_meetings

        