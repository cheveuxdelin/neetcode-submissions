from functools import cache

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        target, remainder = divmod(total_sum, 2)

        if remainder:
            return False
        
        @cache
        def f(i, current):
            if current == target:
                return True
            elif i < len(nums) and current < target:
                # skip or take
                return f(i+1, current) or f(i+1, current+nums[i])
            else:
                return False
        return f(0, 0)