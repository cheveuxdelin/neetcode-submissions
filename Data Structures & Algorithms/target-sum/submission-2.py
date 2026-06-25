# target can be negative
# nums length > 1
# all numbers positive
# need to choose add or substract

from functools import cache

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        @cache
        def f(i, current):
            if i == len(nums):
                return int(current == target)
            elif i < len(nums):
                return f(i+1, current+nums[i]) + f(i+1, current-nums[i])
            return 0
        return f(0, 0)