"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

# minimum number of rooms equals max number of parallel meetings
# let's break it into events happening within a timeline,
# and capture the space in time where there are most rooms being used

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        events = []
        result = 0
        current_rooms = 0

        for interval in intervals:
            events.append((interval.start, 1))
            events.append((interval.end, -1))
        events.sort()
        
        for _, delta in events:
            current_rooms += delta
            result = max(result, current_rooms)
        return result