class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current = 0
        total = nums[0]
        for num in nums:
            current = max(current+num, num)
            total = max(total, current)
        return total