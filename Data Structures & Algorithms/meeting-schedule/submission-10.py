"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import itertools

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        last_end = -1

        for current_interval in intervals:
            if current_interval.start < last_end:
                return False
            last_end = current_interval.end
        return True