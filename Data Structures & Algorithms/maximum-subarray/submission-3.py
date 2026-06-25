class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current = nums[0]
        result = nums[0]

        for num in islice(nums, 1, None):
            current = max(current+num, num)
            result = max(result, current)
        return result