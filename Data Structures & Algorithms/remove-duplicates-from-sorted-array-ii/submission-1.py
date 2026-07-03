import itertools

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 2

        for num in itertools.islice(nums, 2, None):
            if num != nums[i-2]:
                nums[i] = num
                i += 1
        return i
