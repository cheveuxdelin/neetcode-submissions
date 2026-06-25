import functools

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # dp(amount, i) = number of ways you can form amount adding/substracting nums[i:]
        @functools.cache
        def dp(amount, i):
            if i == len(nums):
                return amount == 0
            elif i < len(nums):
                # substract current
                substracting = dp(amount - nums[i], i+1)
                # add current
                adding = dp(amount + nums[i], i+1)
                return substracting + adding
            else:
                return 0
        
        return dp(target, 0)
