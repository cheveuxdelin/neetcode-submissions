"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        current_rooms_needed = 0
        max_rooms_needed = 0
        events = []

        for interval in intervals:
            events.append((interval.end, -1))
            events.append((interval.start, 1))
        events.sort()

        for event in events:
            current_rooms_needed += event[1]
            max_rooms_needed = max(max_rooms_needed, current_rooms_needed)
        return max_rooms_needed
