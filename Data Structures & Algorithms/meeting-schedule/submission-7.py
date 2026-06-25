"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        def are_overlapping(interval1, interval2):
            return not(interval1.start >= interval2.end or interval1.end <= interval2.start)

        intervals.sort(key= lambda x: x.start)

        for i in range(len(intervals)-1):
            if are_overlapping(intervals[i], intervals[i+1]):
                return False
        return True