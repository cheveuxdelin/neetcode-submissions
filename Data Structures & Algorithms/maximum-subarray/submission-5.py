import itertools

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current = nums[0]
        result = nums[0]

        for num in itertools.islice(nums, 1, None):
            current = max(num, current+num)
            result = max(result, current)
        return result