import functools

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @functools.cache
        def f(i, current):
            if i == len(nums):
                return current == target
            else:
                substracting = f(i+1, current-nums[i])
                adding = f(i+1, current+nums[i])
                return substracting + adding
        return f(0, 0)