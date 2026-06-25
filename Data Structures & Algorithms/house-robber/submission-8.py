import functools

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        a = nums[0]
        b = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            a, b = b, max(nums[i]+a, b)
        return b