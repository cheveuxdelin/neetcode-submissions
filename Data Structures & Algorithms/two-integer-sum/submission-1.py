class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for index, num in enumerate(nums):
            other_number = target-num
            if other_number in d:
                return [d[other_number], index]
            d[num] = index