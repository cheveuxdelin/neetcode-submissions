"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def are_intersecting(self, interval1: Interval, interval2: Interval) -> bool:
        return not(interval1.end <= interval2.start or interval1.start >= interval2.end)
    
    def canAttendMeetings(self, intervals: list[Interval]) -> bool:
        for i in range(len(intervals)-1):
            if self.are_intersecting(intervals[i], intervals[i+1]):
                return False
        return True