import functools

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # dp(amount, i) = number of ways you can form amount adding/substracting nums[i:]
        @functools.cache
        def dp(amount, i):
            if i == len(nums):
                return amount == 0
            else:
                return dp(amount-nums[i], i+1) + dp(amount+nums[i], i+1) 
        return dp(target, 0)
