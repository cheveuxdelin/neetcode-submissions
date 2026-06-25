import functools

class Solution:
    def rob(self, nums: List[int]) -> int:
        @functools.cache
        def helper(i):
            if i < 0:
                return 0

            return max(nums[i] + helper(i-2), helper(i-1))

        
        return helper(len(nums)-1)