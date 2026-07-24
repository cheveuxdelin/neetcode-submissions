class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # already sorted
        # inclusive overlap
        # we need to find the first interval that interval_start > newInterval_end
        # then, at that position p, we will want to insert the new new at p-1, merging with everything its overlapping
        # binary search

        # second thought!!:
        # since its already going to be O(N),
        # just append each one and merge them
        # no need for fancy things
        # easier code

        result = []
        i = 0

        # interval[i] finishes before newInterval starts
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
        
        # we get the new interval
        result.append(newInterval)

        # we merge whatever we need
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            result[-1] = [
                min(result[-1][0],intervals[i][0]),
                max(result[-1][1],intervals[i][1]),
            ]
            i += 1
        
        # we get the rest
        while i < len(intervals):
            result.append(intervals[i])
            i += 1
        return result

