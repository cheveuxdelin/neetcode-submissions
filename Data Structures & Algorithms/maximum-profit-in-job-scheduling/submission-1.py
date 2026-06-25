import functools

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = list(zip(startTime, endTime, profit))
        jobs.sort()

        @functools.cache
        def helper(i: int) -> int:
            if i == len(jobs):
                return 0
            else:
                best = -sys.maxsize
                # skip
                best = max(best, helper(i+1))

                # take
                next_i = i
                while next_i < len(jobs) and jobs[next_i][0] < jobs[i][1]:
                    next_i += 1

                if next_i > i:
                    best = max(best, jobs[i][2] + helper(next_i))
                return best
        
        result = helper(0)
        if result == sys.maxsize:
            return 0
        else:
            return result